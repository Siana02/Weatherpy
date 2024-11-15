
# Weather App

This is a simple weather app built using Django and JavaScript that allows users to input a city name and get the current weather information, such as temperature, description, sunrise, and sunset times. The app fetches real-time weather data from the OpenWeather API.

## Features

- **City-based weather search**: Users can enter the name of a city to get the current weather information.
- **AJAX-based interaction**: The app uses AJAX (JavaScript `fetch`) to send requests and display the results dynamically without reloading the page.
- **Modern design**: The app features a simple, responsive design with a visually appealing background and form.

## Prerequisites

Before running the app, ensure you have the following installed:

- **Python 3.x**: Python is required for running Django.
- **Django**: Web framework used for building the application.
- **Requests**: Python package for making HTTP requests.
- **OpenWeather API Key**: You'll need to sign up for a free API key from [OpenWeather](https://openweathermap.org/) to fetch weather data.

## Setup and Installation

Follow these steps to set up the app on your local machine.

### 1. Clone the repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app

2. Create a virtual environment

Create a virtual environment to isolate your project dependencies:

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies

Install the required Python dependencies:

pip install -r requirements.txt

Ensure requests and django are included in the requirements.txt file.

4. Configure the OpenWeather API Key

In settings.py, add your OpenWeather API key:


OPENWEATHER_API_KEY = 'your-api-key-here'

5. Run the Development Server

Now you are ready to run the app. Start the Django development server:

python manage.py runserver

6. View the app in your browser

Go to http://127.0.0.1:8000/ in your browser to see the weather app in action.

Directory Structure

Here’s an overview of the key files and directories in the project:

weather-app/
│
├── weather/                  # Django app for weather-related views and templates
│   ├── static/               # Static files (e.g., CSS, JS)
│   ├── templates/            # HTML templates
│   │   └── weather/
│   │       └── index.html    # Main page of the weather app
│   ├── views.py              # Contains views for rendering the home page and fetching weather data
│   └── urls.py               # URL routing for weather app
│
├── weather-app/              # Main project directory
│   ├── settings.py           # Django settings
│   ├── urls.py               # Project-level URL routing
│   └── wsgi.py               # WSGI entry point for deployment
├── requirements.txt          # Python dependencies (Django, requests, etc.)
└── manage.py                 # Django management script for running the app

Key Files

weather/views.py: This file contains the views for rendering the home page and handling requests to fetch weather data from the OpenWeather API.

weather/templates/weather/index.html: The main template for displaying the weather form and results.

weather/urls.py: URL routing specific to the weather app, mapping the views to their respective URLs.

weather-app/urls.py: Project-level URL configuration.

requirements.txt: List of Python dependencies required for the project.

---

License

This project is licensed under the MIT License - see the LICENSE file for details.



