# 🌦️ Weather Dashboard

A Python-based real-time weather dashboard that uses the **OpenWeather API** to fetch and display current weather information for any city.

## 📌 About the Project

This project was created to practice working with **APIs, JSON data, Python functions, environment variables, and Git/GitHub**.

The application takes a city name from the user, sends a request to the OpenWeather API, receives the weather data, and displays the information in a simple terminal-based dashboard.

## ✨ Features

* 🌍 Search weather for any city
* 🌡️ Display current temperature
* 🤗 Display "feels like" temperature
* 💧 Display humidity
* 🌬️ Display wind speed
* 📊 Display atmospheric pressure
* ☁️ Display current weather condition
* 🔄 Search for multiple cities without restarting the program
* ❌ Handles invalid city names
* 🔐 Keeps the API key outside the source code using `.env`

## 🛠️ Technologies Used

* **Python**
* **Requests** — for making HTTP requests
* **python-dotenv** — for loading environment variables
* **OpenWeather API** — for real-time weather data
* **Git & GitHub** — for version control and project hosting

## 📂 Project Structure

```text
weather-dashboard/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

> `.env` is used locally to store the API key and is intentionally excluded from GitHub.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd weather-dashboard
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

## 🔑 API Setup

This project uses the OpenWeather API.

Create an account on OpenWeather and generate an API key.

Then create a `.env` file in the project folder:

```text
API_KEY=your_api_key_here
```

**Do not share your API key or upload the `.env` file to GitHub.**

The `.gitignore` file already prevents `.env` from being uploaded.

## ▶️ Run the Project

Run:

```bash
python main.py
```

Then enter a city name:

```text
Enter a city name: Pune
```

To stop the program:

```text
Enter a city name: exit
```

## 📊 Example Output

```text
=========================
Weather Dashboard
=========================

Temperature: 28 °C
Feels Like: 30 °C
Humidity: 70 %
Pressure: 1008 hPa
Wind Speed: 3.5 m/s
Condition: scattered clouds
=========================
```

## 🧠 What I Learned

Through this project, I practiced:

* Making API requests using `requests`
* Understanding API endpoints
* Sending query parameters
* Working with HTTP status codes
* Converting API JSON responses into Python dictionaries
* Accessing nested dictionary data
* Creating and using Python functions
* Using environment variables
* Protecting API keys with `.env` and `.gitignore`
* Managing dependencies with `requirements.txt`
* Using Git and GitHub for version control

## 🔮 Future Improvements

Some improvements I plan to add:

* 🖥️ Create a graphical user interface
* 🎨 Improve the dashboard design
* 📅 Add weather forecast information
* 🌅 Add sunrise and sunset times
* 🌧️ Add more detailed weather information
* 📍 Add location-based weather
* 📈 Add weather charts
* 🗺️ Add map integration

## 👨‍💻 Author

**Atharva**

This project was built as a learning project to improve my Python, API, and Git/GitHub skills.
