#!/usr/bin/node
// searches the second biggest integer in the list of arguments
const args = process.argv.slice(2);
const nums = args.map(Number).filter(num => !isNaN(num));
nums.sort((a, b) => b - a);
if (nums.length <= 1) {
  console.log(0);
} else {
  console.log(nums[1]);
}
