//console.info("funzica");

/*
function A() {}
A.prototype.run = function () {};
function B() {}
B.prototype = new A();
B.prototype.constructor = B;

function A() {}
A.prototype.run = function () {};
function tmp() {}
tmp.prototype = A.prototype;
function B() {}
B.prototype = new (tmp)();
B.prototype.constructor = B;

function A() {}
A.prototype.run = function () {};
tmp = function () {}
tmp.prototype = A.prototype;
function B() {}
B.prototype = new (tmp)();
B.prototype.constructor = B;
*/
/*
function inherit(o) {
  f = function () {}; // Dummy constructor
  f.prototype = o; 
  return new (f)(); 
}
function A() {}
A.prototype.run = function () {};
function B() {}
B.prototype = inherit(A.prototype);
B.prototype.constructor = B;
*/
/*

function inherit(B, A) {
  f = function () {}; // Dummy constructor
  f.prototype = A.prototype; 
  B.prototype = new (f)(); 
  B.prototype.constructor = B;
}
function A() {}
A.prototype.run = function () {};
function B() {}
inherit(B, A);

b = new B()
console.log(b.run)
console.log(b instanceof A)

console.log(f)

function fun(a, b, c, d) {
	return [a, b, c, d] //a+b+c+d 
}
console.log("dentro")
console.log(fun(1, 2, 3, 4))
console.log("dentro")
console.log(fun(1, ...[2, 3], 4))


a = [1,2]
a.toString() // => 1,2
a.constructor.prototype.toString = function(){ return this[0] + ':' + ('0' + this[1]).slice(-2) }
a.toString() // => 1:02

var SubArray = function() {                                           
    var a = new Array(... arguments) // spread arguments object
    Object.setPrototypeOf(a, SubArray.prototype) // redirection A
    return a // now instanceof SubArray
}
// o
function SubArray() {                                           
    var a = new Array(... arguments) // spread arguments object
    Object.setPrototypeOf(a, SubArray.prototype) // redirection A (a.__proto__ == SubArray.prototype)
    return a // now instanceof SubArray
}
SubArray.prototype.constructor = SubArray
SubArray.prototype.toString = function () { return this[0] + ':' + ('0' + this[1]).slice(-2) }
Object.setPrototypeOf(SubArray.prototype, Array.prototype); // redirection B (SubArray.prototype.__proto__ ==  Array.prototype)
new SubArray(1, 2).toString() // => '1:02'
delete SubArray.prototype.toString
new SubArray(1, 2).toString() // => '1,2'


class TArray extends Array {
	constructor () { super(... arguments) }
	toString() { return this[0] + ':' + ('0' + this[1]).slice(-2) }	
}
*/

/*
var str = "from datetime import time as hm\
def sm(s, m): return [s, m]\
\
giorni = {'c':['dow', 1, 1, 0, 1, 1, 0, 1], 'b':['even'], 'a':['every', 1]\
orari = {'c':[hm(10,30)], 'b':[hm(9,30)], 'a':[hm(9,30), hm(11,30)]}\
durate = {'c':[sm(9,1), sm(1,5)], 'b':[sm(4,2), sm(3,5)], 'a':[sm(2,4), sm(1,6)]}"
	
console.log(str.slice(str.indexOf('giorni')))
*/

//String.fromCharCode(my_string.charCodeAt(my_string.length - 1) + 1)

var p=[]; for (i=0; i<=11; i+=1) p.push(String.fromCharCode(97+i)); console.log(p) 