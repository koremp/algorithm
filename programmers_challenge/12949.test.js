function solution(arr1, arr2) {
  return Array(arr1.length).fill()
    .map((r, i) => Array(arr2[0].length).fill()
      .map((v, j) => arr1[i].reduce((a, c, k) => a + c * arr2[k][j], 0)))
}

test('input arr1 and arr2 in solution funciton should be answer', () => {
  const arr = [
    {
      arr1: [[1, 4], [3, 2], [4, 1]],
      arr2: [[3, 3], [3, 3]],
      answer: [[15, 15], [15, 15], [15, 15]],
    },
    {
      arr1: [[2, 3, 2], [4, 2, 4], [3, 1, 4]],
      arr2: [[5, 4, 3], [2, 4, 1], [3, 1, 1]],
      answer: [[22, 22, 11], [36, 28, 18], [29, 20, 14]],
    }]

  arr.forEach(({ arr1, arr2, answer }) => {
    expect(solution(arr1, arr2)).toMatchObject(answer)
  })
})
