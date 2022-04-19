// https://programmers.co.kr/learn/courses/30/lessons/64061

function calc(items, answer) {
  let ans = answer;

  for (let i = 0; i < items.length - 1; i += 1) {
    if (items[i] === items[i + 1]) {
      ans += 2;
      items.splice(i, 2);
      ans = calc(items, ans);
    }
  }

  return ans;
}

function solution(board, moves) {
  const items = new Array(board.length);

  for (let i = 0; i < board.length; i += 1) {
    items[i] = [];
    for (let j = board[i].length - 1; j >= 0; j -= 1) {
      if (board[j][i] !== 0) {
        items[i].push(board[j][i]);
      }
    }
  }

  const a = [];

  for (let i = 0; i < moves.length; i += 1) {
    const item = items[moves[i] - 1].pop();
    if (item !== undefined) {
      a.push(item);
    }
  }

  return calc(a, 0);
}

test('crane', () => {
  expect(solution([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
  ], [1, 5, 3, 5, 1, 2, 1, 4])).toBe(4);
});
