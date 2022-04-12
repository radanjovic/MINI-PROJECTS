// Functions that recreate the effects of the MAP and FILTER functions from JS

// The global array
const s = [23, 65, 98, 5];

// myMap
Array.prototype.myMap = function(callback) {
    const newArray = [];
    for (let i = 0; i < this.length; i++) {
      newArray.push(callback(this[i]));
    }
    return newArray;
  };

// myFilter
Array.prototype.myFilter = function(callback) {
  const newArray = [];
  for (let i = 0; i < this.length; i++) {
    if (callback(this[i])) {
      newArray.push(this[i]);
    }
  }
  return newArray;
};

// myReplace
function myReplace(str, before, after) {
  if (before[0] === before[0].toUpperCase()) {
    let newAfter = `${after[0].toUpperCase()}${after.slice(1)}`
    return str.replace(before, newAfter);
  } else {
    return str.replace(before, after.toLowerCase());
  }
}

myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped");

const new_s = s.myFilter(function(item) {
  return item % 2 === 1;
});

const new_s2 = s.myMap(function(item) {
    return item * 2;
});