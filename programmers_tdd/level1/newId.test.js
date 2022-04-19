// https://programmers.co.kr/learn/courses/30/lessons/72410

function solution(newId) {
  // 1
  let answer = newId.toLowerCase();

  // 2
  answer = answer.replace(/[^a-z0-9-_.]/g, '');

  // 3
  while (answer.indexOf('..') >= 0) {
    answer = answer.replace('...', '.');
    answer = answer.replace('..', '.');
  }

  // 4
  if (answer[0] === '.') {
    answer = answer.slice(1);
  }

  if (answer[answer.length - 1] === '.') {
    answer = answer.slice(0, answer.length - 1);
  }

  // 5
  if (answer === '') {
    answer = 'a';
  }

  // 6
  if (answer.length > 15) {
    answer = answer.slice(0, 15);
  }

  while (answer[answer.length - 1] === '.') {
    answer = answer.slice(0, answer.length - 1);
  }

  // 7
  if (answer.length < 3) {
    if (answer.length === 1) {
      answer = answer.concat('', answer[0]);
      answer = answer.concat('', answer[0]);
      return answer;
    }

    if (answer.length === 2) {
      answer = answer.concat('', answer[1]);
      return answer;
    }
  }

  return answer;
}

test('newId', () => {
  expect(solution('...!@BaT#*..y.abcdefghijklm')).toBe('bat.y.abcdefghi');
  expect(solution('z-+.^.')).toBe('z--');
  expect(solution('=.=')).toBe('aaa');
  expect(solution('123_.def')).toBe('123_.def');
  expect(solution('abcdefghijklmn.p')).toBe('abcdefghijklmn');
  expect(solution('z')).toBe('zzz');
  expect(solution('ab')).toBe('abb');
});
