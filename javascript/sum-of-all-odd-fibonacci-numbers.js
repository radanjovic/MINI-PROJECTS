// Function that takes some positiv integer as num, and returns the sum
// of all odd fibonacci numbers that are less than or equal to num
function sumFibs(num) {
    let prev = 0;
    let next = 1;
    let sum = 0;
    do {
      if (next % 2 !== 0) {
        sum += next;
      }
      next+=prev;
      prev=next-prev;
    } while (next<=num);
    return sum;
}
sumFibs(4);