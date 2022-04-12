# A program that computes the approximate grade level needed to comprehend
# some text, in accordance to the Coleman-Liau formula

from cs50 import get_string


# creating main function
def main():

    # geting text from user
    text = get_string("Text: ")

    # calling other functions and passing their values to
    # new variables
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # calculating grade
    grade = index(letters, words, sentences)

    # printing the right grade
    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


# counting the letters in text
def count_letters(text):
    letters1 = 0
    for i in range(len(text)):
        if text[i] >= 'a' and text[i] <= 'z':
            letters1 += 1
        if text[i] >= 'A' and text[i] <= 'Z':
            letters1 += 1
    return letters1


# counting words in text
def count_words(text):
    words1 = 1
    for i in range(len(text)):
        if text[i] == " ":
            words1 += 1
    return words1


# counting sentences in text
def count_sentences(text):
    sentences1 = 0
    for i in range(len(text)):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            sentences1 += 1
    return sentences1


# calculating grade
def index(letters, words, sentences):
    l = letters / words * 100
    s = sentences / words * 100

    i = round(0.0588 * l - 0.296 * s - 15.8)
    grade = int(i)

    return grade


# calling main function
main()