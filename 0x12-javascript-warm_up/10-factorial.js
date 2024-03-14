#!/usr/bin/node

const a = Number(process.argv[2]);

function factorial (a) {
  if (isNaN(a) || a === 1 || a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}

console.log(factorial(a));
