

import json

def fetch_weather_data_from_json(file_path):
    try:
        with open(file_path, "r") as json_file:
            weather_data = json.load(json_file)
            return weather_data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in the file: {file_path}")
    except Exception as e:
        print(f"Error occurred while reading the JSON file: {e}")
    return None

if __name__ == "__main__":
    file_path = "/content/drive/MyDrive/weather.json"
    weather = fetch_weather_data_from_json(file_path)

    if weather:
        print("Current Weather Data:")
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Conditions: {weather['conditions']}")
    else:
        print("Failed to fetch weather data from the JSON file.")



from google.colab import drive
drive.mount('/content/drive')

