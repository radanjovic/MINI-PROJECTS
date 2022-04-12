// Function that takes array as input (which contains average altitude), and which
// returns new array with calculated orbital period for the given space body
function orbitalPeriod(arr) {
    const GM = 398600.4418;
    const earthRadius = 6367.4447;
    let newArr = [];
    for (let i in arr) {
      let newObj = {};
      newObj.name = arr[i]['name'];
      newObj.orbitalPeriod = Math.round(2*Math.PI*Math.sqrt((Math.pow((arr[i]['avgAlt']+earthRadius),3))/GM));
      newArr.push(newObj);
    }
    return newArr;
  }
  
  orbitalPeriod([{name : "sputnik", avgAlt : 35873.5553}]);
  
  /*Map the Debris
  
  The values should be rounded to the nearest whole number. The body being orbited 
  is Earth.
  
  The radius of the earth is 6367.4447 kilometers, and the GM value of earth is 
  398600.4418 km3s-2. */
  