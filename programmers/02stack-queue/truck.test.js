function solution(bridge_length, weight, truck_weights) {
  const firstTruck = truck_weights.shift();

  var bridge = new Array(bridge_length - 1).fill(0);

  bridge.push(firstTruck);

  var bridgeWeight = firstTruck;

  var answer = 1;

  while (bridgeWeight) {
    bridgeWeight -= bridge.shift();

    const nextTruck = truck_weights[0];

    if (bridgeWeight + nextTruck <= weight) {
      bridge.push(nextTruck);

      truck_weights.shift();
      bridgeWeight += nextTruck;
    } else {
      bridge.push(0);
    }

    answer++;
  }

  return answer;
}

test("truck", () => {
  expect(solution(2, 10, [7, 4, 5, 6])).toBe(8);
  expect(solution(100, 10, [10])).toBe(101);
  expect(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])).toBe(
    110
  );
});
