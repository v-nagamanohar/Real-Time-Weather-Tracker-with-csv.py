import os
import csv
from datetime import datetime
import requests

 
FILE_NAME = 'weather_logs.csv'

API_key = "bfcde4e99cdb7b1f9d1b8b3b39e30ee0"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME,'w',newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Date','City','Temperature','Condition'])

def log_weather():
    city = input("Enter your city name: ").strip().lower()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME,'r',newline="",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == date and row['City'].lower() == city.lower():
                print("Entry for this city and date exists")
                return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
        response = requests.get(url) # The Response will be in string
        data = response.json() # converting the string into json

        if response.status_code != 200:
            print(f"API Error ")
            return
        temp = data['main']['temp']
        condition = data['weather'][0]['main']
        with open(FILE_NAME,'a',newline="",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([date,city.title(),temp,condition])
            print(f"Logged: {temp} {condition} in  {city.title()} on {date}")
    except Exception as e:
        print("Failed to make API call")

def view_logs():
    with open(FILE_NAME,'r',encoding="utf-8") as file:
        reader = list(csv.reader(file))
        if len(reader) <= 1:
            print("No Data Avaliable")
            return
        for row in reader[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")


def main():
    while True:
        print("Real time weather logger")
        print("1. Add weather logger")
        print("2. View weather logger")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                log_weather()
            case "2":
                view_logs()
            case "3":
                print("Exiting the weather app")
                break
            case _:
                print("Invalid option")




if __name__== "__main__":
    main()





