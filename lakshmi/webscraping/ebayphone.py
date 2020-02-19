from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome(executable_path="/home/ubuntu/Downloads/chromedriver")
names=[]
reviews=[]
ratings=[]
driver.get("https://www.ebay.com/urw/Samsung-Galaxy-S9-SM-G960-64GB-Midnight-Black-Unlocked-/product-reviews/243315735?pgn=1")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'ebay-review-section'}):
	name=a.find('a',href=True,attrs={'class':'review-item-author'}).text
	review=a.find('h3',attrs={'itemprop':'name'}).text
	val=a.find('div', attrs={'class':'ebay-star-rating'})
	rating=val.get("title")
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.ebay.com/urw/Samsung-Galaxy-S9-SM-G960-64GB-Midnight-Black-Unlocked-/product-reviews/243315735?pgn=2")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'ebay-review-section'}):
	name=a.find('a',href=True,attrs={'class':'review-item-author'}).text
	review=a.find('h3',attrs={'itemprop':'name'}).text
	val=a.find('div', attrs={'class':'ebay-star-rating'})
	rating=val.get("title")
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.ebay.com/urw/Samsung-Galaxy-S9-SM-G960-64GB-Midnight-Black-Unlocked-/product-reviews/243315735?pgn=3")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'ebay-review-section'}):
	name=a.find('a',href=True,attrs={'class':'review-item-author'}).text
	review=a.find('h3',attrs={'itemprop':'name'}).text
	val=a.find('div', attrs={'class':'ebay-star-rating'})
	rating=val.get("title")
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.ebay.com/urw/Samsung-Galaxy-S9-SM-G960-64GB-Midnight-Black-Unlocked-/product-reviews/243315735?pgn=4")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'ebay-review-section'}):
	name=a.find('a',href=True,attrs={'class':'review-item-author'}).text
	review=a.find('h3',attrs={'itemprop':'name'}).text
	val=a.find('div', attrs={'class':'ebay-star-rating'})
	rating=val.get("title")
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.ebay.com/urw/Samsung-Galaxy-S9-SM-G960-64GB-Midnight-Black-Unlocked-/product-reviews/243315735?pgn=5")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'ebay-review-section'}):
	name=a.find('a',href=True,attrs={'class':'review-item-author'}).text
	review=a.find('h3',attrs={'itemprop':'name'}).text
	val=a.find('div', attrs={'class':'ebay-star-rating'})
	rating=val.get("title")
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.ebay.com/urw/Samsung-Galaxy-S9-SM-G960-64GB-Midnight-Black-Unlocked-/product-reviews/243315735?pgn=6")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'ebay-review-section'}):
	name=a.find('a',href=True,attrs={'class':'review-item-author'}).text
	review=a.find('h3',attrs={'itemprop':'name'}).text
	val=a.find('div', attrs={'class':'ebay-star-rating'})
	rating=val.get("title")
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.ebay.com/urw/Samsung-Galaxy-S9-SM-G960-64GB-Midnight-Black-Unlocked-/product-reviews/243315735?pgn=7")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'ebay-review-section'}):
	name=a.find('a',href=True,attrs={'class':'review-item-author'}).text
	review=a.find('h3',attrs={'itemprop':'name'}).text
	val=a.find('div', attrs={'class':'ebay-star-rating'})
	rating=val.get("title")
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.ebay.com/urw/Samsung-Galaxy-S9-SM-G960-64GB-Midnight-Black-Unlocked-/product-reviews/243315735?pgn=8")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'ebay-review-section'}):
	name=a.find('a',href=True,attrs={'class':'review-item-author'}).text
	review=a.find('h3',attrs={'itemprop':'name'}).text
	val=a.find('div', attrs={'class':'ebay-star-rating'})
	rating=val.get("title")
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.ebay.com/urw/Samsung-Galaxy-S9-SM-G960-64GB-Midnight-Black-Unlocked-/product-reviews/243315735?pgn=9")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'ebay-review-section'}):
	name=a.find('a',href=True,attrs={'class':'review-item-author'}).text
	review=a.find('h3',attrs={'itemprop':'name'}).text
	val=a.find('div', attrs={'class':'ebay-star-rating'})
	rating=val.get("title")
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.ebay.com/urw/Samsung-Galaxy-S9-SM-G960-64GB-Midnight-Black-Unlocked-/product-reviews/243315735?pgn=10")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'ebay-review-section'}):
	name=a.find('a',href=True,attrs={'class':'review-item-author'}).text
	review=a.find('h3',attrs={'itemprop':'name'}).text
	val=a.find('div', attrs={'class':'ebay-star-rating'})
	rating=val.get("title")
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.ebay.com/p/243315735")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")

cost=soup.find('div',attrs={'class':'price'}).text
cost=cost.replace("INR","")
cost=cost.replace(",","")

df = pd.DataFrame({'Name':names,'Ratings':ratings,'Review':reviews,'Cost(₹)':float(cost)})
df.to_csv("ebayphone.csv", index=False, encoding='utf-8')
reviews_df = pd.read_csv("ebayphone.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x: 0 if x < '3' else 1)
reviews_df = reviews_df[["Names","Review", "Good/Bad"]]
print(reviews_df)
print(reviews_df["Good/Bad"].value_counts(normalize = True))
reviews_df.head()

