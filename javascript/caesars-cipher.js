// Caesars cipher using rot13, assuming all the letters are UpperCase
function rot13(str) {
    let reversed = '';
    for (let i = 0; i<str.length; i++) {
      let ascii = str.charCodeAt(i);
      if (ascii < 65 || ascii > 90) {
        reversed += str[i];
      } else {
        let newLetterAscii = (((ascii - 65) +13) % 26) + 65;
        reversed += String.fromCharCode(newLetterAscii);
      }
    }
    return reversed;
  }
  
  rot13("SERR YBIR?");


// Cipher using any user inputed value for key, and strings with both upper
// and lower cases
function cipher(str, num) {
    let reversed = '';
    for (let i = 0; i<str.length; i++) {
      let ascii = str.charCodeAt(i);
      if (ascii >= 97 && ascii <= 122) {
        let newLetterAscii = (((ascii - 97) + num) % 26) + 97;
        reversed += String.fromCharCode(newLetterAscii);
      } else if (ascii >= 65 && ascii <= 90) {
        let newLetterAscii = (((ascii - 65) + num) % 26) + 65;
        reversed += String.fromCharCode(newLetterAscii);
      } else {
        reversed += str[i];
      }
    }
    return reversed;
}



