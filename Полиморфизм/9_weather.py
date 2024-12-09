import argparse
import requests
from weather_service import WeatherService


def main(city_name):
    # BEGIN
    weather_app = WeatherService(requests)
    data = weather_app.look_up(city_name)
    message = f"Temperature in {data['name']}: {data['temperature']}C"
    return message
    # END


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type=str, required=True)
    args = parser.parse_args()
    print(main(args.city))
