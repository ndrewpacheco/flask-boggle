const GAME_LENGTH = 10000;
const $startGame = $("#start-game");
const $form = $("#guess-form");
const $response = $("#response");
const $score = $("#score");

// initial setup
let score = 0;
let gamesPlayed = 0;
$form.hide();

$startGame.click(() => {
  score = 0;
  $score.text(score);
  $startGame.hide();
  $form.show();

  setTimeout(() => {
    $startGame.show();
    $form.hide();
    gamesPlayed += 1;
    axios.post("/games-played", { games_played: gamesPlayed });
  }, GAME_LENGTH);
});

async function sendWord(e) {
  e.preventDefault();

  const guess = e.target[0].value;

  axios
    .post("/check-word", { guess: guess })
    .then(function (response) {
      console.log(response);

      $response.text(response.data["result"]);

      if (response.data["result"] === "ok") score += 1;
      $score.text(score);
    })
    .catch(function (error) {
      console.log(error);
    });

  e.target[0].value = "";
}

$form.on("submit", sendWord);
