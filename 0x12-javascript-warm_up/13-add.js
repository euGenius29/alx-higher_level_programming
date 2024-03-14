#!/usr/bin/node

exports.add = function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
    process.exit(0);
  } else {
    return (a + b);
  }
};
