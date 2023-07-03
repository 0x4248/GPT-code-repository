# Weather Forecasting using Machine Learning
import requests
from sklearn.linear_model import LinearRegression

def get_weather_data(location, date):
    """Fetches historical weather data for a given location and date."""
    url = f"https://api.weatherapi.com/v1/history.json?key=YOUR_API_KEY&q={location}&dt={date}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["forecast"]["forecastday"][0]["hour"]
    else:
        print("Error fetching weather data.")
        return None

def train_model(data):
    """Trains a linear regression model on the historical weather data."""
    X = [[hour["temp_c"], hour["humidity"]] for hour in data]
    y = [hour["condition"]["code"] for hour in data]
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_weather(model, temperature, humidity):
    """Uses a machine learning model to predict the weather conditions."""
    code = int(round(model.predict([[temperature, humidity]])[0]))
    if code == 1000:
        return "Sunny"
    elif code >= 1003 and code <= 1063:
        return "Partly Cloudy"
    elif code >= 1066 and code <= 1195:
        return "Cloudy"
    elif code >= 1197 and code <= 1299:
        return "Rainy"
    elif code >= 1300 and code <= 1326:
        return "Snowy"
    else:
        return "Unknown"

def main():
    """Prompts the user for a location and date, and predicts the weather conditions."""
    location = input("Enter location (city, state/country): ")
    date = input("Enter date (YYYY-MM-DD): ")
    weather_data = get_weather_data(location, date)
    if weather_data:
        model = train_model(weather_data)
        temperature = float(input("Enter temperature in Celsius: "))
        humidity = int(input("Enter humidity (0-100): "))
        conditions = predict_weather(model, temperature, humidity)
        print(f"Predicted weather conditions for {location} on {date}: {conditions}")

if __name__ == "__main__":
    main()
