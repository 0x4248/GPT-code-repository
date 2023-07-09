import requests
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Fetch weather data from API
def fetch_weather_data(api_key, location):
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=5"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

# Extract required information from weather data
def extract_information(weather_data):
    current_condition = weather_data['current']['condition']['text']
    forecast_days = weather_data['forecast']['forecastday']
    temperatures = [day['day']['avgtemp_c'] for day in forecast_days]
    dates = [datetime.strptime(day['date'], '%Y-%m-%d').strftime('%b %d') for day in forecast_days]
    return current_condition, temperatures, dates

# Display current weather condition
def display_current_condition(current_condition):
    print(f"Current Weather Condition: {current_condition}\n")

# Display forecast for the next few days
def display_forecast(temperatures, dates):
    print("Forecast:")
    for i in range(len(temperatures)):
        print(f"{dates[i]}: {temperatures[i]}°C")

# Plot temperature trends
def plot_temperature_trends(temperatures, dates):
    plt.figure(figsize=(8, 5))
    plt.plot(dates, temperatures, marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trends')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Calculate statistical summaries
def calculate_statistics(temperatures):
    avg_temp = np.mean(temperatures)
    max_temp = np.max(temperatures)
    min_temp = np.min(temperatures)
    return avg_temp, max_temp, min_temp

# Display statistical summaries
def display_statistics(avg_temp, max_temp, min_temp):
    print(f"\nAverage Temperature: {avg_temp:.2f}°C")
    print(f"Maximum Temperature: {max_temp}°C")
    print(f"Minimum Temperature: {min_temp}°C")

# Main function
def main():
    api_key = "YOUR_API_KEY"
    location = "New York"
    weather_data = fetch_weather_data(api_key, location)
    if weather_data:
        current_condition, temperatures, dates = extract_information(weather_data)
        display_current_condition(current_condition)
        display_forecast(temperatures, dates)
        plot_temperature_trends(temperatures, dates)
        avg_temp, max_temp, min_temp = calculate_statistics(temperatures)
        display_statistics(avg_temp, max_temp, min_temp)

# Entry point
if __name__ == "__main__":
    main()
