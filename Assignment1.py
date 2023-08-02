import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "b6907d289e10d714a6e88b30761fae22"

def get_weather_data(location):
    url = f"{API_BASE_URL}?q={location}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error retrieving weather data.")
        return None

def get_weather_for_date(weather_data, date):
    for forecast in weather_data["list"]:
        if forecast["dt_txt"].startswith(date):
            return forecast["main"]["temp"]
    return None

def get_wind_speed_for_date(weather_data, date):
    for forecast in weather_data["list"]:
        if forecast["dt_txt"].startswith(date):
            return forecast["wind"]["speed"]
    return None

def get_pressure_for_date(weather_data, date):
    for forecast in weather_data["list"]:
        if forecast["dt_txt"].startswith(date):
            return forecast["main"]["pressure"]
    return None

def main():
    location = input("Enter the location (e.g., London,us): ")
    weather_data = get_weather_data(location)

    if weather_data:
        while True:
            print("\nMenu:")
            print("1. Get weather")
            print("2. Get Wind Speed")
            print("3. Get Pressure")
            print("0. Exit")

            option = input("Enter your choice: ")

            if option == "1":
                date = input("Enter the date (YYYY-MM-DD): ")
                temperature = get_weather_for_date(weather_data, date)
                if temperature:
                    print(f"Temperature on {date}: {temperature}°C")
                else:
                    print("Data not found for the given date.")

            elif option == "2":
                date = input("Enter the date (YYYY-MM-DD): ")
                wind_speed = get_wind_speed_for_date(weather_data, date)
                if wind_speed:
                    print(f"Wind speed on {date}: {wind_speed} m/s")
                else:
                    print("Data not found for the given date.")

            elif option == "3":
                date = input("Enter the date (YYYY-MM-DD): ")
                pressure = get_pressure_for_date(weather_data, date)
                if pressure:
                    print(f"Pressure on {date}: {pressure} hPa")
                else:
                    print("Data not found for the given date.")

            elif option == "0":
                print("Exiting the program.")
                break

            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()