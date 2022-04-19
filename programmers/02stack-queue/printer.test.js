function solution(priorities, location) {
  var target_idx = location;
  var answer = 1;
  var first = -1;

  while (priorities.length > 0) {
    first = priorities.shift();

    if (priorities.some((val, idx) => val > first)) {
      priorities.push(first);
    }
    else {
      if (target_idx === 0) {
        break;
      }
      else {
        answer++;
      }
    }

    if (target_idx === 0) {
      target_idx = priorities.length - 1;
    }
    else {
      target_idx--;
    }
  }


  return answer;
}

test("printer", () => {
  expect(solution([2, 1, 3, 2], 2)).toBe(1);
  expect(solution([1, 1, 9, 1, 1, 1], 0)).toBe(5);
});
