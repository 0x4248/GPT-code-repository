const apiKey = "YOUR_API_KEY_HERE";

function getWeatherData(city) {
  // Call the OpenWeatherMap API to retrieve weather data for the specified city
  fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
    .then(response => response.json())
    .then(data => {
      // Extract the relevant weather data from the API response
      const temperature = data.main.temp;
      const description = data.weather[0].description;
      const windSpeed = data.wind.speed;
      const humidity = data.main.humidity;

      // Update the HTML to display the weather data
      document.getElementById("temperature").innerText = `${temperature} °C`;
      document.getElementById("description").innerText = description;
      document.getElementById("wind-speed").innerText = `${windSpeed} m/s`;
      document.getElementById("humidity").innerText = `${humidity} %`;
    })
    .catch(error => {
      // Display an error message if the API call fails
      console.error("Error retrieving weather data:", error);
      alert("Error retrieving weather data. Please try again later.");
    });
}

// Add an event listener to the search button to retrieve weather data when clicked
document.getElementById("search-button").addEventListener("click", () => {
  const city = document.getElementById("city-input").value;
  getWeatherData(city);
});
