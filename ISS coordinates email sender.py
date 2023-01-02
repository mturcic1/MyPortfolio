import requests
from datetime import datetime
from email.message import EmailMessage
import ssl
import smtplib
from time import sleep


def check_coordinates(coordinates):
    if 50 < coordinates[0] < 60 and 7 < coordinates[1] < 17:
        return True

def check_time():
    if sunset < current_hour and current_hour > sunrise:
        return True



timer = True
while timer:
    sleep(60)
    # ISS coordinates
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()

    latitude = float(response_iss.json()["iss_position"]["latitude"])
    longitude = float(response_iss.json()["iss_position"]["longitude"])

    coordinates_iss = (latitude, longitude)

    # Sunset/sunrise times
    parameters = {"lat": 55.676098,
                  "lng": 12.568337,
                  "formatted": 0,
                  }

    response = requests.get("https://api.sunrise-sunset.org/json", parameters)
    response.raise_for_status()
    sunset_data = response.json()
    sunrise_info = (sunset_data["results"]["sunrise"]).split("T")
    sunset_info = (sunset_data["results"]["sunset"]).split("T")

    sunrise_time = sunrise_info[1].split(":")
    sunset_time = sunset_info[1].split(":")
    time = datetime.now()

    sunrise = int(sunrise_time[0])
    sunset = int(sunset_time[0])
    current_hour = time.hour


    # Email sending
    if check_coordinates(coordinates_iss) and check_time():
        my_email = "insert_your email here"
        email_password = "your email password"
        receiving_email = "enter receiving email here"
        subject = "ISS position"
        body = "ISS is above your location"
        em = EmailMessage()

        em["From"] = my_email
        em["To"] = receiving_email
        em["Subject"] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(my_email, email_password)
            smtp.sendmail(my_email, receiving_email, em.as_string())
        print("Email sent")

    else:
        print("Email not sent")
