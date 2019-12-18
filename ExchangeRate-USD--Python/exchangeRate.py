import requests
import json
import smtplib
import time

def exchange_rate():
    url = "https://api.exchangeratesapi.io/latest"
    r = requests.get(url)
    data = r.json() #convert the value to json
    return  data['rates']['USD']

def send_email():
    import smtplib  # SMTP is required to connect to the mail server and to send an e-mail.

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect a mail server and send it(587 is a port).
    server.starttls()

    server.login("username", "password")
    server.sendmail("sender@gmail.com", "receiver@gmail.com","The USD currency is {}".format(exchange_rate()))

    server.quit()

while True:
    print(exchange_rate())
    if (exchange_rate() >= 1.50):
        send_email()
    time.sleep(600)
