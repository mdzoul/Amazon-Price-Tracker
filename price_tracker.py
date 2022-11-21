import requests
import smtplib
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Acer-Laptop-i7-1260P-Graphics-SF514-56T-797T/dp/B09TCH74C1/ref=sr_1_1?crid=1ZPPMTINEO3P5&keywords=acer+swift+5&qid=1669049704&s=electronics&sprefix=acer+swift+%2Celectronics-intl-ship%2C284&sr=1-1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)
website = response.text

soup = BeautifulSoup(website, "html5lib")
# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen").text
price_without_curr = price.split("$")[1].replace(",", "")
price_as_float = float(price_without_curr)
# print(price_as_float)

product = soup.find(name="span", id="productTitle").text.strip()
# print(product)

EMAIL = "zoulaimi@hotmail.com"
PASSWORD = "Oe92*Mr5wWLi$7"
SMTP_SERVER = {
    "gmail": "smtp.gmail.com",
    "yahoo": "smtp.mail.yahoo.com",
    "hotmail": "smtp-mail.outlook.com",
}


def send_email():
    """Set up to send email to user"""
    with smtplib.SMTP(f"{SMTP_SERVER['hotmail']}") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="melisasuhaila.s@gmail.com",
            msg="Subject:Amazon Price Alert!\n\n"
                f"{product} is now only {price}!\n"
                f"{url}"
        )


if price_as_float < 1500:
    send_email()
