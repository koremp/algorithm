function isPrime(num) {
  if (num < 2) {
    return false;
  }
  for (var i = 2; i < Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false
    }
  }
  return true;
}

function generateNums(arr, str) {
  if (arr.length > 0) {
    for (var i = 0; i < arr.length; i++) {
      const temp = [...arr];
      temp.slice(i, 1);
      generateNums(temp, str + arr[i]);
    }
  }

  if (str.length > 0) {
    isPrime(str)
  }
}

function solution(numbers) {
  var answer = 0;
  var primes = [];

  var nums = numbers.split('').map((num) => { return parseInt(num, 10) }).sort();



  return answer;
}

test('prime', () => {
  expect(solution('17')).toBe(3);
  expect(solution('011')).toBe(2);
})