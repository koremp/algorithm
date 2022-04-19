function solution(answers) {
  var one = [1, 2, 3, 4, 5];
  var two = [2, 1, 2, 3, 2, 4, 2, 5];
  var three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  var scores = [0, 0, 0]

  for (var i = 0; i < answers.length; i++) {
    if (one[i % 5] === answers[i]) {
      scores[0]++;
    }
    if (two[i % 8] === answers[i]) {
      scores[1]++;
    }
    if (three[i % 10] === answers[i]) {
      scores[2]++;
    }
  }

  const max = Math.max(...scores);

  var answer = [];
  scores.map((score, idx) => {
    if (score === max)
      answer.push(idx + 1);
  })

  return answer;
}

test('test', () => {
  expect(solution([1, 2, 3, 4, 5])).toStrictEqual([1]);
  expect(solution([1, 3, 2, 4, 2])).toStrictEqual([1, 2, 3]);
})