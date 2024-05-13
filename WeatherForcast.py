class WeatherDataFetcher:
    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data.get(city, {})

class WeatherDataParser:
    def parse_weather_data(self, data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class UserInterface:
    def get_user_input(self):
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        return city.lower()

    def get_detailed_forecast_preference(self):
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        return detailed == 'yes'

def main():
    weather_fetcher = WeatherDataFetcher()
    weather_parser = WeatherDataParser()
    ui = UserInterface()

    while True:
        city = ui.get_user_input()
        if city == 'exit':
            break
        detailed = ui.get_detailed_forecast_preference()
        data = weather_fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            if detailed:
                forecast = weather_parser.parse_weather_data(data)
            else:
                forecast = f"Weather in {city}: {data['temperature']} degrees, {data['condition']}"
            print(forecast)

if __name__ == "__main__":
    main()
