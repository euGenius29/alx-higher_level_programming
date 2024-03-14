#!/usr/bin/node

const arr = [];
let i;

for (i = 0; i < process.argv.length - 2; i++) {
  arr[i] = Number(process.argv[i + 2]);
  if (isNaN(arr[i])) {
    console.log('0');
    process.exit(0);
  }
}
if (arr.length < 2) {
  console.log('0');
} else {
  let maxNum = -Infinity;
  let nextMax = -Infinity;

  for (i = 1; i < arr.length; i++) {
    if (arr[i] > maxNum) {
      nextMax = maxNum;
      maxNum = arr[i];
    } else if (arr[i] > nextMax && arr[i] < maxNum) {
      nextMax = arr[i];
    }
  }
  if (nextMax === -Infinity) {
    console.log('0');
  } else {
    console.log(nextMax);
  }
}
