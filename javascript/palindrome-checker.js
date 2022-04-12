function palindrome(str) {
  let regex = /[a-z0-9]+/ig;
  let newStr = str.match(regex);
  newStr = newStr.join('').toLowerCase();
  let reverseStr = '';
  for (let i = (newStr.length - 1); i>=0; i--) {
    reverseStr += newStr[i];
  }
  if (newStr === reverseStr) {
    return true;
  }
  return false;
}

palindrome("A man, a plan, a canal. Panama");

/*Palindrome Checker
Return true if the given string is a palindrome. Otherwise, return false.

A palindrome is a word or sentence that's spelled the same way both forward and backward, 
ignoring punctuation, case, and spacing.

Remove all non-alphanumeric characters (punctuation, spaces and symbols) and turn 
everything into the same case (lower or upper case) in order to check for palindromes.

*/