// Function that counts cards, in a game called Blackjack
let count = 0;
function countCards(card) {
  switch(card) {
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
      count++;
      break;
    case 7:
    case 8:
    case 9:
      break;
    case 10:
    case 'J':
    case 'Q':
    case 'K':
    case 'A':
      count--;
      break;
  }
  if (count > 0) {
    return (count + ' Bet');
  } else {
    return (count + ' Hold')
  }
}
countCards(2); countCards(3); countCards(7); countCards('K'); countCards('A');

/*
In the casino game Blackjack, a player can gain an advantage over the house by 
keeping track of the relative number of high and low cards remaining in the deck. 
This is called Card Counting.

Having more high cards remaining in the deck favors the player. Each card is assigned 
a value according to the table below. When the count is positive, the player should 
bet high. When the count is zero or negative, the player should bet low.

Count Change	    Cards
    +1	        2, 3, 4, 5, 6
    0	        7, 8, 9
    -1	        10, 'J', 'Q', 'K', 'A' 
*/
