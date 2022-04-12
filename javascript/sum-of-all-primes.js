// Function that takes some integer as num and returns sum of all prime
// numbers that are less than or equal to num. Prime numbers are numbers
// divisible only by 1 and themselves
function sumPrimes(num) {
    let startArr = [];
    for (let i = 2; i <= num; i++) {
      startArr.push(i);
    }
    // eliminate non-primes
    let notPrime = [];
    startArr.forEach(i => {
      for (let j = 2; j<i; j++) {
        if (i % j === 0) {
          notPrime.push(i);
          break;
        }
      }
    });
    // filter-out
    let prime = startArr.filter( i => !notPrime.includes(i));
    let sum = 0;
    prime.forEach(i => {
      sum+=i;
    });
    return sum;
}
sumPrimes(2432);