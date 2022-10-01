# This program is to catch the real time currency exchange rate from CAD to CNY
# And e-mail the result to "wangzhao0424@icloud.com"

# import the necessary packages
from http import server
import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.message import EmailMessage
import ssl
import datetime


# get the URL of the current exchange rate
urlGoogle = 'https://www.google.com/search?q=CAD+price+CNY&rlz=1C1GCEU_enCA982CA982&sxsrf=ALiCzsahM3Hc910ndydGe_3Xb_KukNiI6A%3A1664328916018&ei=1KQzY8Qo1Iam1A_9yqGIAg&ved=0ahUKEwjE4s-urLb6AhVUg4kEHX1lCCEQ4dUDCA4&uact=5&oq=CAD+price+CNY&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQyBQgAEKIEOgoIABBHENYEELADOgcIABCwAxBDOg0IABDkAhDWBBCwAxgBOhIILhDHARDRAxDIAxCwAxBDGAI6BAgjECc6BQgAEIAEOggIABCABBCLAzoICAAQywEQiwM6BQgAEMsBOgsIABCABBCxAxCDAToJCCMQJxBGEIICOgoILhDHARDRAxAnOgoIABCxAxCDARBDOgQIABBDOhEILhCABBCxAxCDARDHARDRAzoQCC4QsQMQgwEQxwEQ0QMQQzoHCCMQ6gIQJzoNCC4QxwEQ0QMQ6gIQJzoHCAAQQxCLAzoQCC4QsQMQxwEQrwEQQxCLAzoGCAAQHhAHOgoILhDHARCvARANOgcIABCxAxANOgQIABANOgUILhCABDoICAAQHhAHEAo6CwguEIAEEMcBEK8BOgsIABCxAxCDARCRAjoFCAAQkQJKBAhBGABKBAhGGAFQjwVYhWZg52doBXABeACAAc0BiAHdIZIBBjAuMjYuMZgBAKABAbABCsgBE7gBAsABAdoBBggBEAEYCdoBBggCEAEYCA&sclient=gws-wiz'

# make a request to the website
# HTML = requests.get(url)
HTML = requests.get(urlGoogle)


# parse the HTML from our request
soup = BeautifulSoup(HTML.text, 'html.parser')

# print the result
# print(soup.prettify())


# <div class="BNeawe iBp4i AP7Wnd">

# Create a function to get the price of the CNY
# Create a function to get the price of the CNY
def get_CNY(coin):
    url = 'https://www.google.com/search?q=CAD+price+CNY&rlz=1C1GCEU_enCA982CA982&sxsrf=ALiCzsahM3Hc910ndydGe_3Xb_KukNiI6A%3A1664328916018&ei=1KQzY8Qo1Iam1A_9yqGIAg&ved=0ahUKEwjE4s-urLb6AhVUg4kEHX1lCCEQ4dUDCA4&uact=5&oq=CAD+price+CNY&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQyBQgAEKIEOgoIABBHENYEELADOgcIABCwAxBDOg0IABDkAhDWBBCwAxgBOhIILhDHARDRAxDIAxCwAxBDGAI6BAgjECc6BQgAEIAEOggIABCABBCLAzoICAAQywEQiwM6BQgAEMsBOgsIABCABBCxAxCDAToJCCMQJxBGEIICOgoILhDHARDRAxAnOgoIABCxAxCDARBDOgQIABBDOhEILhCABBCxAxCDARDHARDRAzoQCC4QsQMQgwEQxwEQ0QMQQzoHCCMQ6gIQJzoNCC4QxwEQ0QMQ6gIQJzoHCAAQQxCLAzoQCC4QsQMQxwEQrwEQQxCLAzoGCAAQHhAHOgoILhDHARCvARANOgcIABCxAxANOgQIABANOgUILhCABDoICAAQHhAHEAo6CwguEIAEEMcBEK8BOgsIABCxAxCDARCRAjoFCAAQkQJKBAhBGABKBAhGGAFQjwVYhWZg52doBXABeACAAc0BiAHdIZIBBjAuMjYuMZgBAKABAbABCsgBE7gBAsABAdoBBggBEAEYCdoBBggCEAEYCA&sclient=gws-wiz'
    HTML = requests.get(url)
    soup = BeautifulSoup(HTML.text, 'html.parser')

    # Find the current price
    text = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find(
        'div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # return the text
    return text


# Get the price of the CNY
price = get_CNY('Chinese Yuan')

# print the price
# print(price)

# Create a function to consistently show the price of the CNY when it changes


def main():
    last_price = -1
    # Create a loop to continuously show the price
    while True:
        # Choose the CNY that i want to get the price for
        CNY = 'Chinese Yuan'
        # get the price of the CNY
        price = get_CNY(CNY)
        # print(price)

        # store current date to date variable in yyyy-mm-dd format
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        # store current time to t variable in hh:mm:ss format
        t = datetime.datetime.now().strftime("%H:%M:%S")

        
    # add the price to the end of the "./priceHistory.txt" file
        with open('./priceHistory.txt', 'a') as f:
            f.write(date + ' ' + t + ' ' + price + '\n')
        time.sleep(300)

    # devide the first 4 charactors and the Chinese Yuan and conver to float
    # priceFloat = float(price[:4])

    # send_email()
    # Check if the price changed
    # if price != last_price:
    # if priceFloat <= 5.20:
    #     print(price)
    #     # add the price to the end of the "./priceHistory.txt" file
    #     with open('./priceHistory.txt', 'a') as f:
    #         # add date and time each time date type yyyy-mm-dd
    #         f.write(str(datetime.date.today()) + " ")
    #         f.write(price + ''+'\n')

    # send_email()
    # time.sleep(10)


# sender email
sender_email = "wangzhao724@gmail.com"
# receiver email
receiver_email = "wangzhao0424@icloud.com"
# password
password = "jkwsutqgdfyceuur"
# subject
subject = "CNY Price CHANGED"
# message
message = "The price of the CNY is "+price


# def send_email():

#     em = EmailMessage()
#     em['From'] = sender_email
#     em['To'] = receiver_email
#     em['Subject'] = subject
#     em.set_content(message)

#     context = ssl.create_default_context()

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(sender_email, password)
#         smtp.sendmail(sender_email, receiver_email, em.as_string())
#         print("Email has been sent to ", receiver_email)


# Run the main function
main()
