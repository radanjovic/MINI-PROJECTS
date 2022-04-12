// Function that updates record collection
const recordCollection = {
    2548: {
      albumTitle: 'Slippery When Wet',
      artist: 'Bon Jovi',
      tracks: ['Let It Rock', 'You Give Love a Bad Name']
    },
    2468: {
      albumTitle: '1999',
      artist: 'Prince',
      tracks: ['1999', 'Little Red Corvette']
    },
    1245: {
      artist: 'Robert Palmer',
      tracks: []
    },
    5439: {
      albumTitle: 'ABBA Gold'
    }
};

function updateRecords(records, id, prop, value) {
    if (prop !== 'tracks' && value !== '') {
      records[id][prop] = value;
    } else if (prop === 'tracks') {
      if (!records[id].hasOwnProperty(prop)) {
        records[id][prop] = [value];
      }
      if (value !== '') {
        records[id][prop].push(value);
      }
    }
    if (value === '') {
      delete records[id][prop];
    }
    return records;
}
  
updateRecords(recordCollection, 5439, 'artist', 'ABBA');

/*
Function always returns the entire record collection object.

If prop isn't tracks and value isn't an empty string, update or set that album's 
prop to value.

If prop is tracks but the album doesn't have a tracks property, create an empty 
array and add value to it.

If prop is tracks and value isn't an empty string, add value to the end of the 
album's existing tracks array.

If value is an empty string, delete the given prop property from the album.
*/