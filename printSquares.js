/**
 * Write a program that prints the squares of the first 32 natural numbers.
 * The output will be in the format: "n × n = n^2", where n is the natural number.
 * Example output:
 * 1 × 1 = 1
 * 2 × 2 = 4
 * 3 × 3 = 9
 * ...
 * 32 × 32 = 1024
*/
(new Array(32)).fill(0, 0, 32).map((_, index) => ++index).forEach(num => console.log(`${num} \u00D7 ${num} = ${num * num}`));