// Function that finds smallest common multiple for two provided numbers 
// (which are provided in an array, and which are not necessarily in num
// order)
function smallestCommons(arr) {
    let start;
    let end;
    if (arr[0] < arr[1]) {
      start = arr[0];
      end = arr[1];
    } else {
      start = arr[1];
      end = arr[0];
    }
    let newArr = [];
    for (let i = start; i <= end; i++) {
      newArr.push(i);
    }
    let potentialResult = end + end;
    let result = 0;
    do {
      let match = 0;
      newArr.forEach(i => {
        if (potentialResult % i === 0) {
          match++;
        }
      });
      if (match === newArr.length) {
        result = potentialResult;
      } else {
        potentialResult+=end;
      }
    } while(result === 0);
    return result;
}
smallestCommons([23, 18]);