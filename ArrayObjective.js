/*
  The Array truly is a beatiful thing.
  For this mini assignment we're going to have you go through some of the commonly used array methods.
  There are methods built onto the Array prototype 
  so here is a refernce of where you can learn more about them.
  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
  Array Methods you should use to complete these assignemnts:
  .pop(), .push(), .splice(), .slice(), .shift(), .unshift(), .map() .filter(),
*/



/* 
  Problem 1: Justice League
  Remove the side kick 'Robin' from the front of this List.
  Add a super hero `Green Lantern` to the end of this List.
  Add a super hero `Superman` to the front of this List.
  Your final array should look like this:
  [ 'Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern' ]
  [ "Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern" ]
*/

const justiceLeague = ['Robin', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman'];
justiceLeague.shift();
justiceLeague.push('Green Lantern');
justiceLeague.unshift('Superman');

//console.log(justiceLeague)
/* 
  Problem 2: Middle Earth
  In our list of Characters from Middle Earth remove sauraman. He's a traitor.
*/
//  ['Frodo', 'Samwise', 'Gandalf', 'Sauraman', 'Treebeard']
//  ["Frodo", "Samwise", "Gandalf", "Treebeard"]


const middleEarth = ['Frodo', 'Samwise', 'Gandalf', 'Sauraman', 'Treebeard'];
middleEarth.splice(3, 1)

//console.log(middleEarth);
/* 
  Problem 3: Numbers
  map over this array, and return a new array of the numbers in it, multiplied by 10
*/

const numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10];

function timesTen(num){
  return "I love you times" + num * 10;
};

console.log(numbers.map(timesTen));

/* 
  Problem 4: Filter Friends
  Here you're going to create two new arrays. 
  One called femaleFriends (a list of all friends filtered where gender === 'F')
  One called maleFriends (a list of all friends filtered where gender === 'M')
*/

const friends = [
  { name: 'Monica', gender: 'F' },
  { name: 'Chandler', gender: 'M' },
  { name: 'Ross', gender: 'M' },
  { name: 'Phoebe', gender: 'F' },
  { name: 'Joey', gender: 'M' },
  { name: 'Rachel', gender: 'F' }
];

const femaleFriends = friends.filter(element => element.gender === 'F').map(element => element.name); // finish this


const male = friends.filter(
  function (element){
    return element.gender === 'M'
  }); // finish this
let newmale = male.map(function (element){
  return element.name;
})





console.log(femaleFriends);
console.log(newmale);
