#!/usr/bin/node
// computes and prints a factorial
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
// prints the factorial
const arg = parseInt(process.argv[2]);
if (!isNaN(arg)) {
  console.log(factorial(arg));
} else {
  console.log(1);
}
