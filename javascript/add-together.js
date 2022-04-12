// Function that sums two arguments together. If only one argument is provided, 
// then returns a function that expects one argument and returns the sum (curried func).
// If neither of args is valid, returns undefined
function addTogether() {
    let args = [];
    for (let i in arguments) {
      if (typeof(arguments[i]) !== 'number') {
        return undefined;
      }
      args.push(arguments[i]);
    }
    if (args.length === 2) {
      return args[0] + args[1];
    } else {
      return function(num) {
        if (typeof(num) !== 'number') {
          return undefined;
        }
        return args[0] + num;
      }
    }
}
addTogether(2,3);