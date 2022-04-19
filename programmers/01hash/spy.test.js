function solution(clothes) {
  var obj = {};

  for (var i = 0; i < clothes.length; i++) {
    const category = clothes[i][1];

    if (obj[category]) {
      obj[category] += 1;
    } else {
      obj[category] = 1;
    }
  }

  var answer = 1;

  for (var x in obj) {
    answer = answer * (obj[x] + 1);
  }

  return answer - 1;
}

test("spy", () => {
  const clothes1 = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
  ];
  const clothes2 = [
    ["crow_mask", "face"],
    ["blue_sunglasses", "face"],
    ["smoky_makeup", "face"],
  ];
  const clothes3 = [
    ["a", "1"],
    ["b", "2"],
    ["c", "3"],
  ];
  const clothes4 = [
    ["1", "a"],
    ["2", "a"],
    ["3", "b"],
    ["4", "b"],
    ["5", "c"],
    ["6", "c"],
    ["7", "d"],
    ["8", "d"],
  ];

  expect(solution(clothes1)).toBe(5);
  expect(solution(clothes2)).toBe(3);
  expect(solution(clothes3)).toBe(7);
  expect(solution(clothes4)).toBe(80);
});
