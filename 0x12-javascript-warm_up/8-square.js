#!/usr/bin/node

let i;
let j;

if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (i = 0; i < Number(process.argv[2]); i++) {
    let line = '';
    for (j = 0; j < Number(process.argv[2]); j++) {
      line += 'X';
    }
    console.log(line);
  }
}
