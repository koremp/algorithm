function solution(progresses, speeds) {
  var answer = [];

  const leftDays = progresses.map((progress, idx) => {
    return Math.ceil((100 - progress) / speeds[idx]);
  });

  var date = leftDays[0];
  var deploys = 1;

  for (var i = 1; i < leftDays.length; i++) {
    if (date < leftDays[i]) {
      answer.push(deploys);
      deploys = 1;
      date = leftDays[i];
    } else {
      deploys++;
    }
  }

  answer.push(deploys);

  return answer;
}

test("func", () => {
  expect(solution([93, 30, 55], [1, 30, 5])).toStrictEqual([2, 1]);
  expect(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])).toStrictEqual([
    1,
    3,
    2,
  ]);
});
