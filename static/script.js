const $flavorInput = $("#flavor");
const $sizeInput = $("#size");
const $ratingInput = $("#rating");
const $imageInput = $("#image");

$("form").on("submit", async function (evt) {
    evt.preventDefault();

    const searchTerm = $searchInput.val();
    $searchInput.val("");

    const response = await axios.get("http://api.giphy.com/v1/gifs/search", {
        params: {
            q: searchTerm,
            api_key: "MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym"
        }
    });
    addGif(response.data);
});


$("form").on("submit", async function (evt) {
    evt.preventDefault();

    const flavor = $flavorInput.val();
    const size = $sizeInput.val();
    const rating = $ratingInput.val();
    const image = $imageInput.val();

    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
    flavor,
    rating,
    size,
    image
  });

  let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
  $("#cupcakes-list").append(newCupcake);
  $("#new-cupcake-form").trigger("reset");

});