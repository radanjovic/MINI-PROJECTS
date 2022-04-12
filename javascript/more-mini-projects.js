

////////////// JS MINI-PROJECTS /////////////////////



// Function that turns input string into url slugs
function urlSlug(title) {
    return title.toLowerCase().trim().split(/\s+/).join('-');
}
urlSlug("A Mind Needs Books Like A Sword Needs A Whetstone");



// Function that takes 2 inputs (arr - nested array) and elem - element that may or may
// not be present on one or more nested arr arrays. It returns filtered version of arr
// such that any array nested within arr containing elem is removed
function filteredArray(arr, elem) {
    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
      if (arr[i].indexOf(elem) === -1) {
        newArr.push(arr[i]);
      }
    }
    return newArr;
}
console.log(filteredArray([[3, 2, 3], [1, 6, 3], [3, 13, 26], [19, 3, 9]], 3));



// Function that returns an English translated sentence of the passed binary string.
function binaryAgent(str) {
    let arr = str.split(' ');
    let newArr = [];
    for (let i in arr) {
      newArr.push(String.fromCharCode(parseInt(arr[i], 2)));
    }
    let newStr = newArr.join('');
    return newStr;
}
binaryAgent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111");



// Function that confirms the ending of a string - without endsWITH !
function confirmEnding(str, target) {
    const strlen = str.length;
    const tgtlen = target.length;
    for (let i = 0; i < tgtlen; i++) {
      if (str[strlen-tgtlen+i] !== target[i]) {
          return false;
      }
    }
    return true;
}
confirmEnding("Bastian", "n");



// Function that compares 2 arrays and returns new array with any items found
// in one of the two given arrays, but not items found in both
function diffArray(arr1, arr2) {
    const newArr = arr1.concat(arr2);
    const result= [];
    for (let n in newArr) {
      if ((arr1.includes(newArr[n]) && !arr2.includes(newArr[n])) || (arr2.includes(newArr[n]) && !arr1.includes(newArr[n]))) {
        result.push(newArr[n]);
      }
    }
    return result;
}
diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);



// Function that takes string of DNA elements, takes each, finds it's pair, and
// returns 2D array of DNA pairs (dna pairs are AT and CG)
function pairElement(str) {
    let arr = str.split('');
    let result = [];
    arr.forEach(i => {
      switch(i) {
        case 'A':
          result.push(['A', 'T']);
          break;
        case 'T':
          result.push(['T', 'A']);
          break;
        case 'C':
          result.push(['C', 'G']);
          break;
        case 'G':
          result.push(['G', 'C']);
          break;
      }
    });
    return result;
}
pairElement("GCG");



// Function that takes array and another function as inputs, iterates through array
// and removes each element, up until the input function returns true, when current
// element is passed through it
function dropElements(arr, func) {
    while (arr.length > 0 && !func(arr[0])) {
      arr.shift();
    }
    return arr;
}
dropElements([1, 2, 3, 7, 4], function(n) {return n < 3; });



// Function that takes collection (array of objects) and predicament as its inputs and
// returns true if that predicament in that collection is truthy, else returns false
function truthCheck(collection, pre) {
    for (let i in collection) {
      if (!collection[i][pre]) {
        return false;
      }
    }
    return true;
}

truthCheck([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy", "sex": "male"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex");



// Function that returns the factorial of the provided integer.
function factorialize(num) {
    let result = 1;
    if (num === 0 || num === 1) {
      return 1;
    }
    for (let i = 1; i <= num; i++) {
      result *= i;
    }
    return result;
}
factorialize(5);



// Function that takes array and another function as inputs, loops through array and 
// returns element if the provided function is truthy on it, else returns undefined
function findElement(arr, func) {
    for (let i = 0; i < arr.length; i++) {
      if (func(arr[i])) {
        return arr[i];
      }
    }
    return undefined;
}
findElement([1, 2, 3, 4], num => num % 2 === 0);



// Function that finds the longest word in a string
function findLongestWordLength(str) {
    let longest = 0;
    let longestWord;
    let arr = str.split(' ');
    for (let i = 0; i<arr.length; i++) {
        if (arr[i].length > longest) {
            longest = arr[i].length;
            longestWord = arr[i];
        }
    }
    return longestWord.length;
}
findLongestWordLength("The quick brown fox jumped over the lazy dog");



// Function that finds missing letter, if one, else returns undefined
function fearNotLetter(str) {
    for (let i = 0; i<str.length; i++) {
      if (str.charCodeAt(i+1) === undefined) {
        return undefined;
      }
      if ((str.charCodeAt(i+1) - str.charCodeAt(i)) === 2) {
        return String.fromCharCode(str.charCodeAt(i) + 1);
      }
    }
}
fearNotLetter("abce");



// Function that takes string as input and returns pig-latin string of that word
function translatePigLatin(str) {
    let regex = /[aeiou]/;
    if (regex.test(str[0])) {
      return `${str}way`;
    } else {
      let consRegex = /[^aeiou]+/;
      let firstPart = str.match(consRegex);
      let newStr = str.slice(firstPart[0].length);
      return `${newStr}${firstPart}ay`;
    }
}
translatePigLatin("consonant");
translatePigLatin("glove");
  
  /*Pig Latin
  Pig Latin is a way of altering English Words. The rules are as follows:
  
  - If a word begins with a consonant, take the first consonant or consonant cluster,
   move it to the end of the word, and add ay to it.
  
  - If a word begins with a vowel, just add way at the end.

*/



// Function that looks for name and property in contacts list
const contacts = [
    {
      firstName: "Akira",
      lastName: "Laine",
      number: "0543236543",
      likes: ["Pizza", "Coding", "Brownie Points"],
    },
    {
      firstName: "Harry",
      lastName: "Potter",
      number: "0994372684",
      likes: ["Hogwarts", "Magic", "Hagrid"],
    },
    {
      firstName: "Sherlock",
      lastName: "Holmes",
      number: "0487345643",
      likes: ["Intriguing Cases", "Violin"],
    },
    {
      firstName: "Kristian",
      lastName: "Vos",
      number: "unknown",
      likes: ["JavaScript", "Gaming", "Foxes"],
    },
  ];
  
  function lookUpProfile(name, prop) {
    for (let i = 0; i < contacts.length; i++) {
      if (contacts[i]['firstName'] === name ) {
        return contacts[i][prop] || "No such property"
      } 
    }
    return "No such contact";
}
lookUpProfile("Akira", "likes");



// Function that returns array of numbers between starting and ending number 
// (which gets by input), using recursion!
function rangeOfNumbers(startNum, endNum) {
  if (startNum === endNum) {
    return [startNum];
  } else {
    const arr = rangeOfNumbers(startNum +1, endNum);
    arr.unshift(startNum);
    return arr;
  }
};
rangeOfNumbers(12,18);



// Function that takes array of nested arrays, finds the largest number in each,
// and returns an array with only those largest numbers 
function largestOfFour(arr) {
  let newArr = [];
  for (let i = 0; i < arr.length; i++) {
    let largest = arr[i][0];
    for (let j = 0; j < arr[i].length; j++) {
      if (arr[i][j] > largest) {
        largest = arr[i][j];
      }
    }
    newArr.push(largest);
  }
  return newArr;
}
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);



// Function that gets array as first argument, and one or more of other arguments 
// afterwards, and returns new array from elements whose value is not the same
// as the value of the other arguments
function destroyer(arr) {
  let args = [];
  for (let i = 1; i < arguments.length; i++) {
    args.push(arguments[i]);
  }
  const newArr = arr.filter(n => !args.includes(n));
  return newArr;
}
destroyer([1, 2, 3, 1, 2, 3], 2, 3);



// Function that returns spinal cased string
function spinalCase(str) {
  let regex = /\s+|_+/g;
  let newStr = str.replace(/([a-z])([A-Z])/g, "$1 $2").replace(regex, "-").toLowerCase();
  console.log(newStr);
  return newStr;
}
spinalCase('This Is Spinal Tap');



// Function that takes array with multiple nested arrays and flattens them
function steamrollArray(arr) {
  let newArr = [];
  for (let i in arr) {
    if (!Array.isArray(arr[i])) {
      newArr.push(arr[i]);
    } else {
      newArr.push(...steamrollArray(arr[i]));
    }
  }
  return newArr;
}
steamrollArray([1, [2], [3, [[4]]]]);



// Function that returns true if the string in the first element of the inputed
// array contains all of the letters of the string in the second element of the 
// array
function mutation(arr) {
  let word1 = arr[0].toLowerCase().split('');
  let word2 = arr[1].toLowerCase().split('');
  for (let i = 0; i < word2.length; i++) {
    if (word1.indexOf(word2[i]) === -1) {
      return false;
    }
  }
  return true;
}
mutation(["hello", "hey"]);



// FUnction that takes array of two numbers and returns sum of those two  numbers
// along with the sum of all numbers between them (not presuming that the smaller
// number will be first)
function sumAll(arr) {
  let a;
  let b;
  if (arr[0] < arr[1]) {
    a = arr[0];
    b = arr[1];
  } else {
    a = arr[1];
    b = arr[0];
  }
  let sum = 0;
  while (a <= b) {
    sum+=a;
    a++;
  }
  return sum;
}
sumAll([11, 4]);



// Function that takes string and an integer as num, and truncates that sting
// up to that number
function truncateString(str, num) {
  let len = str.length;
  if (len > num) {
    let newStr = '';
    for (let i = 0; i < num; i++) {
      newStr += str[i];
    }
    return newStr + '...';
  } else {
    return str;
  }
}
truncateString("A-tisket a-tasket A green and yellow basket", 8);



// Function that title-cases a sentence
function titleCase(str) {
  let arr = str.split(' ');
  let newStr = '';
  for (let i = 0; i < arr.length; i++) {
      if (i === (arr.length-1)) {
          newStr += (arr[i].charAt(0).toUpperCase() + arr[i].slice(1).toLowerCase());
      } else {
          newStr += (arr[i].charAt(0).toUpperCase() + arr[i].slice(1).toLowerCase()) + ' ';
      }
  }
  return newStr;
}
titleCase("I'm a little tea pot");



