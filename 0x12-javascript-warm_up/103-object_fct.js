#!/usr/bin/node
// adding a new function incr that increments the integer value
function incr () {
  this.value++;
}
const myObject = {
	  type: 'object',
	  value: 12
};
console.log(myObject);
myObject.incr = incr;
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
