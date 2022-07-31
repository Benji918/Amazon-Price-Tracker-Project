import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

BUY_PRICE = 1000
MY_EMAIL = 'name@gmail.com'
PWD = 'YOUR PWD'
URL = 'https://www.amazon.com/ASUS-ROG-Zephyrus-Gaming-Laptop/dp/B09MMHSXSH/ref=sr_1_5?crid=2BPJ7PHL2EEG5&keywords' \
      '=asus%2Brog%2Bzephyrus&qid=1659300456&sprefix=asus%2Brog%2B%2Caps%2C426&sr=8-5&th=1 '
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 "
                  "Safari/537.36 "
}
response = requests.get(url=URL, headers=headers)
web_data = response.text
soup = BeautifulSoup(web_data, 'lxml')
price_tag = soup.find(name='span', class_='a-price-whole')
price_as_text = price_tag.getText().strip('.')
price_as_float = float(price_as_text.replace(',', ''))
product_name = soup.find(id='productTitle').text
# print(type(price_as_float))
if price_as_float <= BUY_PRICE:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # Secure the connection
        connection.starttls()
        # login the user
        connection.login(user=MY_EMAIL, password=PWD)
        # send email
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f'Subject:Amazon Price drop alert!!!.\n\nYour desired product {product_name} price has dropped to ${price_as_text}\n{URL} '
            .encode("utf-8")
        )

