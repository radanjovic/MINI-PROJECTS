import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get money(cash)
    db_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    money = float(db_cash[0]["cash"])
    # Get portfolio
    portfolio = db.execute("SELECT * FROM total WHERE user_id = ?", session["user_id"])

    total = money

    # With a little help from others - we figured out that we should
    # at this point update our portfolio var to add current price and
    # total sum.
    for i in portfolio:
        price = lookup(i["symbol"])["price"]
        total_price = i["shares"] * price
        i.update({"price": price, "total": total_price})
        total = total + total_price

    return render_template("index.html", portfolio=portfolio, money=money, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # POST
    if request.method == "POST":
        # First, pass the symbol to lookup and save shares in a var (if possible)
        data = lookup(request.form.get("symbol"))
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("number of shares not a positive integer")

        # check to see if the symbol is right - we know that the lookup will
        # return None if the symbol is invalid.
        if data == None:
            return apology("invalid symbol")

        # check if shares is a positiv int
        if shares < 0:
            return apology("number of shares not a positive integer")
        # Check cash user has and if it's enough
        db_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        money = float(db_cash[0]["cash"])
        if money < (shares * data["price"]):
            return apology("not enough cash")
        new_money = money - (shares * data["price"])

        # Get info about current portfolio from total
        db_total = db.execute("SELECT * FROM total WHERE user_id = ?", session["user_id"])

        # In every case - we update cash and history
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_money, session["user_id"])
        db.execute("INSERT INTO history (user_id, symbol, shares, action, price, time) VALUES (?, ?, ?, 'bought', ?, datetime('now'))",
                    session["user_id"], data["symbol"], shares, data["price"])

        # If user has no prev. portfolio - insert this purchase
        if not db_total:
            db.execute("INSERT INTO total (user_id, symbol, name, shares) VALUES (?, ?, ?, ?)",
                        session["user_id"], data["symbol"], data["name"], shares)
        # But if user has prev. portfolio, we check if the selected stock was prev. purchased
        # and if yes - update the number of shares and redirect user to index.
        else:
            for i in db_total:
                if data["name"] == i["name"]:
                    db.execute("UPDATE total SET shares = ? WHERE user_id = ? AND name = ?",
                                (i["shares"] + shares), session["user_id"], data["name"])
                    return redirect("/")
            # If the user has prev. portfolio but not the current stock - insert it
            db.execute("INSERT INTO total (user_id, symbol, name, shares) VALUES (?, ?, ?, ?)",
                        session["user_id"], data["symbol"], data["name"], shares)

        return redirect("/")

    # GET
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Passing our prev. created sqltable history with all the info we need
    history = db.execute("SELECT * FROM history WHERE user_id = ? ORDER BY time", session["user_id"])

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # POST
    if request.method == "POST":
        # First, pass the symbol to lookup and save it in a var
        data = lookup(request.form.get("symbol"))

        # check to see if the symbol is right - we know that the lookup will
        # return None if the symbol is invalid.
        if data == None:
            return apology("invalid symbol")

        # if the symbol is right - show the quote for that symbol.
        return render_template("quoted.html", data=data)

    # GET
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # POST
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username")
        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide password")
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password must match")

        # Storing username and pass in variables
        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)

        # Checking if username is in the database - if not inserting it
        if not db.execute("SELECT * FROM users WHERE username = ?", username):
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, password)
        else:
            return apology("username already exists")

        # Getting the user_id to save it in the session and redirect user to main page
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]
        return redirect("/")

    # GET
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # POST
    if request.method == "POST":
        # Open total and find symbol
        db_total = db.execute("SELECT * FROM total WHERE user_id = ?", session["user_id"])
        symbol = request.form.get("symbol")

        # Saving number of shares
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("number of shares not a positive integer")

        if not symbol:
            return apology("enter symbol")

        # lookup for price and symb
        data = lookup(symbol)

        # Finding out total number of shares
        for i in db_total:
            if symbol == i["symbol"]:
                total_shares = i["shares"]

        # bad cases
        if not db_total or data == None or shares < 1 or shares > total_shares:
            return apology("You don't have enough shares")

        # setting up vars for updating tables
        price = data["price"]
        db_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        money = float(db_cash[0]["cash"])
        cost = price * shares
        new_money = money + cost
        new_shares = total_shares - shares

        # in any case - we want to update users cash and history
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_money, session["user_id"])
        db.execute("INSERT INTO history (user_id, symbol, shares, action, price, time) VALUES (?, ?, ?, 'sold', ?, datetime('now'))",
                    session["user_id"], data["symbol"], shares, data["price"])

        # deleting a entirely if user sells all shares
        if shares == total_shares:
            db.execute("DELETE FROM total WHERE user_id = ? and symbol = ?", session["user_id"], symbol)
        # if not - updating number of shares
        else:
            db.execute("UPDATE total SET shares = ? WHERE user_id = ? and symbol = ?", new_shares, session["user_id"], symbol)

        return redirect("/")

    # GET
    else:
        symbols = db.execute("SELECT symbol FROM total WHERE user_id = ?", session["user_id"])
        return render_template("sell.html", symbols=symbols)


# Adding personal touch - allowing users to change their passwords.
@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    # POST
    if request.method == "POST":
        # Saving new data to vars
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        new_confirmation = request.form.get("new_confirmation")

        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        # Checking old password
        if not old_password or len(rows) != 1 or not check_password_hash(rows[0]["hash"], old_password):
            return apology("enter a valid old password")

        # Cheking if new password and match are identical
        if new_password != new_confirmation:
            return apology("new password must match")

        # Updating our table with new password and redirecting to index
        new_password_hash = generate_password_hash(new_password, method='pbkdf2:sha256', salt_length=8)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_password_hash, session["user_id"])
        return redirect("/")

    # GET
    else:
        return render_template("profile.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
