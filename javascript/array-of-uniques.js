// Function that takes multiple arrguments (which are arrays),
// creates a new array from every element of each of them (without)
// duplications, and returns that new array, sorted not in the num
// order, but order of appearance..
function uniteUnique(arr) {
    let args = [];
    // Get all the arguments
    for (let i = 0; i < arguments.length; i++) {
      args.push(arguments[i]);
    }
    let newArr = [];
    args.forEach(i => {
      i.forEach( j => {
        if (!newArr.includes(j)) {
          newArr.push(j);
        }
      });
    });
    return newArr;
}
uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);