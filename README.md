# 🌦 Real-Time Weather Logger

A Python script that fetches real-time weather data for any city using the [OpenWeatherMap API](https://openweathermap.org/api), logs it to a CSV file, and allows users to view past weather records.

---

## 🚀 Features

- Fetches current temperature and weather condition for a city
- Logs data with date, city, temperature, and condition
- Prevents duplicate entries for the same city on the same date
- Saves logs in `weather_logs.csv`
- View all past logged weather data

---

## 🧠 Concepts Used

- File handling (`open`, `csv.reader`, `csv.writer`)
- API calls with `requests`
- JSON parsing
- Date handling with `datetime`
- Error handling using `try-except`
- Pattern matching (`match-case`)

---

## 📦 Requirements

- Python 3.10+  
- Install dependencies:
  ```bash
  pip install requests
  ```

---

## 🔑 API Key Setup

This script uses [OpenWeatherMap API](https://openweathermap.org/api).

1. Sign up at OpenWeatherMap and get a free API key.
2. Replace the `API_key` variable in the script:
   ```python
   API_key = "YOUR_API_KEY_HERE"
   ```

---

## 📊 CSV File Structure

`weather_logs.csv` will store:
```
Date,City,Temperature,Condition
2025-08-11,London,25.3,Clear
2025-08-11,New York,29.0,Clouds
```

---

## 💡 How to Use

1. Save script as `weather_logger.py`
2. Run:
   ```bash
   python weather_logger.py
   ```
3. Choose:
   - `1` → Add weather log  
   - `2` → View weather logs  
   - `3` → Exit

---

## 📋 Example Output

```
Real time weather logger
1. Add weather logger
2. View weather logger
3. Exit
Choose an option: 1
Enter your city name: London
Logged: 25.3 Clear in London on 2025-08-11
```

