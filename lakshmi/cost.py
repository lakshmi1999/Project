from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome(executable_path="/home/ubuntu/Downloads/chromedriver")
driver.get("https://www.flipkart.com/microsoft-xbox-one-wireless-controller-bluetooth-gamepad/product-reviews/itmff8u3mz3yysf4?pid=ACCE7AV9TZHHAESC&lid=LSTACCE7AV9TZHHAESCQKSNCL&marketplace=FLIPKART&page=1")

content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
cost=soup.find('div',attrs={'class':'_1vC4OE'}).text
print(cost)
