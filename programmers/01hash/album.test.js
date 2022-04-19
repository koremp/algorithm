function solution(genres, plays) {
  genres = genres.map((genre, idx) => {
    return {
      genre: genre,
      idx,
      play: plays[idx],
    };
  });

  var genreTotalCount = [];

  for (var i = 0; i < genres.length; i++) {
    var genre = genreTotalCount.find((item) => item.genre === genres[i].genre);

    if (!genre) {
      genreTotalCount.push({
        genre: genres[i].genre,
        total: genres[i].play,
      });
    } else {
      genre.total += genres[i].play;
    }
  }

  genreTotalCount.sort((a, b) => b.total - a.total);

  var answer = [];

  for (var i = 0; i < genreTotalCount.length; i++) {
    var genre = genreTotalCount[i].genre;

    var curGenre = [];

    genres.map((song) => {
      if (song.genre === genre) {
        curGenre.push(song);
      }
    });

    curGenre.sort((a, b) => b.play - a.play);

    answer.push(curGenre[0].idx);

    if (curGenre.length > 1) {
      answer.push(curGenre[1].idx);
    }
  }

  return answer;
}

test("album", () => {
  expect(
    solution(
      ["classic", "pop", "classic", "classic", "pop"],
      [500, 600, 150, 800, 2500]
    )
  ).toStrictEqual([4, 1, 3, 0]);
});
