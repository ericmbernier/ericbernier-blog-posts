/*
Allow ENTER button to submit the user's Pokemon name
*/
var input = document.getElementById("pokemonName");
input.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("catchEmButton").click();
  }
});

/*
This function is called when the user clicks the submit, or "Catch 'Em" button.
*/
function catchPokemon(pokemonName) {
  // Handle an empty Pokemon name
  if (pokemonName === null || pokemonName === "") {
    $("#pokemonSprite").addClass("d-none");
    $("#warningLabel").removeClass("d-none");
    $("#warningLabel").text("Please enter a Pokemon name.");
    return;
  }

  // Hide the warning label and add our spinning Pokeball
  $("#warningLabel").addClass("d-none");
  $("#pokemonSprite").removeClass("d-none");
  $("#pokemonSprite").attr("src", "/static/images/pokeball.gif");

  // Make a call to our pokemon GET endpoint and then call the getPokemonSprite function below
  fetch(`/pokemon/${pokemonName}`, {
    method: "GET",
  })
    .then((response) => response.json())
    .then((pokemonTask) => getPokemonSprite(pokemonTask.taskId, pokemonName));
}

/*
This function retrieves the sprite once it has been downloaded
It polls our Flask App, looking for a SUCCESS or FAILURE status on 
the Celery task that is responsible for retrieving the Pokemon sprite
*/
function getPokemonSprite(taskId, pokemonName) {
  // Get the latest Celery status from our Flask app
  fetch(`/celery/task/status/${taskId}`, {
    method: "GET",
  })
    .then((response) => response.json())
    .then((res) => {
      const taskState = res.taskState;
      if (taskState === "SUCCESS") {
        // Display the sprite upon success
        $("#pokemonSprite").removeClass("d-none");
        $("#pokemonSprite").attr("src", `/static/pokemon/${pokemonName}.png`);
        $("#warningLabel").addClass("d-none");

        return false;
      } else if (taskState === "FAILURE") {
        // Display a warning if we fail to retrieve a sprite
        $("#pokemonSprite").addClass("d-none");
        $("#warningLabel").removeClass("d-none");
        $("#warningLabel").text("Pokemon was not caught! (Invalid Pokemon name)");

        return false;
      }

      // Keep trying once per second until we get a SUCCESS or FAILURE Celery status
      setTimeout(function () {
        getPokemonSprite(taskId, pokemonName);
      }, 1000);
    })
    .catch((err) => console.log(err));
}
