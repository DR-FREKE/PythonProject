let arr = [1, 2, 3]

let it = arr[Symbol.iterator]();
it.next();
console.log(it.next().value);