# Weather Forecast Web Application - 3977

**Language**: `JavaScript`

**Lines of code**: `31`

## Description

This program is a weather forecast web application that uses the OpenWeatherMap API to retrieve and display the current weather conditions for a specified location. The user can input the location and the program will display the current temperature, weather description, wind speed, and humidity.

In this example, the program uses the fetch function to call the OpenWeatherMap API and retrieve weather data for the specified city. The relevant weather data is extracted from the API response and displayed on the HTML page. The program also includes error handling in case the API call fails. The user can input the desired location using a search bar and the weather data will be updated when the search button is clicked. This program demonstrates the use of JavaScript to create a web application that interacts with an API and updates the HTML page dynamically.

## Code

``` JavaScript
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

```

## Prompt

```
Make me a program in JavaScript that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```