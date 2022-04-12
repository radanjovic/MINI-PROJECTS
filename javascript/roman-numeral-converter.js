function convertToRoman(num) {
 let dec = num;
 let roman = '';
 let dict = {
   M:1000,
   CM:900,
   D:500,
   CD:400,
   C:100,
   XC:90,
   L:50,
   XL:40,
   X:10,
   IX:9,
   V:5,
   IV:4,
   I:1
}

for (let i in dict) {
   while ( dec >= dict[i] ) {
      roman += i;
      dec -= dict[i];
    }
 }
 return roman;
}

convertToRoman(36);

/* Roman Numeral Converter
Convert the given number into a roman numeral.

All roman numerals answers should be provided in upper-case. */