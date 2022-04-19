function solution(phone_book) {
  for(var i = 0; i < phone_book.length; i++) {
    for(var j = 0; j < phone_book.length; j++) {
      if(i === j) {
        continue;
      }
      if(phone_book[i].indexOf(phone_book[j]) !== 0) {
        continue;
      }
      return false;
    }
  }

  return true;
}

test('phone', () => {
  expect(solution(['119', '97674223', '1195524421']	)).toBe(false);
  expect(solution(['123','456','789'])).toBe(true);
  expect(solution(['12','123','1235','567','88'])).toBe(false);
})