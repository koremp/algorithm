function solution(participant, completion) {
  completion.forEach(element => {
    if (participant.indexOf(element) !== -1) {
      participant.splice(participant.indexOf(element), 1);
    }
  });

  return participant[0];
}

test('marathon', () => {
  expect(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki'])).toBe('leo');
  expect(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola'])).toBe('vinko');
  expect(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav'])).toBe('mislav');
})
