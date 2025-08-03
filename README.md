WeatherBot
Description:

WeatherBot is a Python-based command-line application that displays the current weather for any city in the world. It uses the free OpenWeatherMap API to fetch live weather data based on a user-provided city name. The program then extracts the temperature in both Celsius and Fahrenheit, along with a short weather description like "clear sky" or "rain".

The user runs the program from the command line and passes the city name as an argument, for example: python project.py Berlin

The program checks whether the city name has been provided. If not, it exits with an appropriate message. If the city name is provided, the program sends a request to the OpenWeatherMap API and processes the response. It then prints a message such as: Current temperature in Berlin is 24°C (75°F). Current weather: clear sky

If the city is not found or the API returns an error, the program displays an error message and exits gracefully.
Files Included

    project.py: This is the main Python file. It contains:
        main(): Handles input, calls the helper functions, and prints the result.
        get_weather(city): Fetches weather data using the OpenWeatherMap API.
        get_temperature(weather): Extracts the temperature and converts it.
        get_weather_type(weather): Extracts a short weather description.
        kelvin_to_celcius() and kelvin_to_fahrenheit(): Convert temperature values.

    test_project.py: This file contains automated tests using the pytest framework. It checks the accuracy of the temperature conversion functions and the correct parsing of weather description from a sample JSON object.

Technologies Used

    Python
    requests library for HTTP requests
    OpenWeatherMap API
    pytest for testing

Design Decisions

The application uses the sys module to handle command-line arguments and exits cleanly if no city is provided. All logic related to the weather API and data processing is separated into functions to make the code easy to read, reuse, and test. API responses are checked for validity using the HTTP status code. To enhance user experience, the output includes both Celsius and Fahrenheit.

Testing was a key part of the development. I wrote simple unit tests for all helper functions, including temperature conversion and weather description extraction. The program is modular and can be extended in the future, for example by adding forecasts or integrating location-based queries using coordinates or IP lookup.

I chose to keep the project focused, concise, and beginner-friendly. All external dependencies are limited to the well-known requests and pytest libraries.
Installation and Usage

To use this program, follow these steps:

    Ensure that Python is installed on your system.
    Install the required library:
    Run the program in your terminal: python project.py
    To run the test suite: pytest test_project.py

Summary
WeatherBot is a simple but functional Python project that demonstrates how to work with APIs, parse JSON data, handle command-line input, and write clean, testable code. While the idea itself is relatively straightforward, the implementation required structured thinking, modular design, and real-world API interaction. Compared to CS50 problem sets, this project involved more independent problem-solving, integration of external data sources, and testing. It serves as a complete, end-to-end software project and marks a significant step in my learning journey.
