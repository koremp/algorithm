// https://programmers.co.kr/learn/courses/30/lessons/68644

function solution(numbers) {
  const answer = [];

  for (let i = 0; i < numbers.length; i += 1) {
    for (let j = i + 1; j < numbers.length; j += 1) {
      const num = numbers[i] + numbers[j];
      if (!answer.includes(num)) {
        answer.push(num);
      }
    }
  }

  return answer.sort((a, b) => a - b);
}

test('Add two', () => {
  expect(solution([2, 1, 3, 4, 1])).toStrictEqual([2, 3, 4, 5, 6, 7]);
  expect(solution([5, 0, 2, 7])).toStrictEqual([2, 5, 7, 9, 12]);
});
