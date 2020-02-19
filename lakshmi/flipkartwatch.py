
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome(executable_path="/home/ubuntu/Downloads/chromedriver")
names=[]
reviews=[]
ratings=[]
driver.get("https://www.flipkart.com/casio-d011-a-158wa-1q-digital-watch-men-women/product-reviews/itmf3zhdga85ghju?pid=WATDJ5YXGFUP5RNG&lid=LSTWATDJ5YXGFUP5RNG3Q3EEO&marketplace=FLIPKART&page=1")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'_1PBCrt'}):
	name=a.find('p', attrs={'class':'_3LYOAd _3sxSiS _2675cp'}).text
	review=a.find('div',attrs={'class':''}).text
	rating=a.find('div',attrs={'class':'hGSR34'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.flipkart.com/casio-d011-a-158wa-1q-digital-watch-men-women/product-reviews/itmf3zhdga85ghju?pid=WATDJ5YXGFUP5RNG&lid=LSTWATDJ5YXGFUP5RNG3Q3EEO&marketplace=FLIPKART&page=2")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'_1PBCrt'}):
	name=a.find('p', attrs={'class':'_3LYOAd _3sxSiS _2675cp'}).text
	review=a.find('div',attrs={'class':''}).text
	rating=a.find('div',attrs={'class':'hGSR34'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.flipkart.com/casio-d011-a-158wa-1q-digital-watch-men-women/product-reviews/itmf3zhdga85ghju?pid=WATDJ5YXGFUP5RNG&lid=LSTWATDJ5YXGFUP5RNG3Q3EEO&marketplace=FLIPKART&page=3")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'_1PBCrt'}):
	name=a.find('p', attrs={'class':'_3LYOAd _3sxSiS _2675cp'}).text
	review=a.find('div',attrs={'class':''}).text
	rating=a.find('div',attrs={'class':'hGSR34'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.flipkart.com/casio-d011-a-158wa-1q-digital-watch-men-women/product-reviews/itmf3zhdga85ghju?pid=WATDJ5YXGFUP5RNG&lid=LSTWATDJ5YXGFUP5RNG3Q3EEO&marketplace=FLIPKART&page=4")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'_1PBCrt'}):
	name=a.find('p', attrs={'class':'_3LYOAd _3sxSiS _2675cp'}).text
	review=a.find('div',attrs={'class':''}).text
	rating=a.find('div',attrs={'class':'hGSR34'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.flipkart.com/casio-d011-a-158wa-1q-digital-watch-men-women/product-reviews/itmf3zhdga85ghju?pid=WATDJ5YXGFUP5RNG&lid=LSTWATDJ5YXGFUP5RNG3Q3EEO&marketplace=FLIPKART&page=5")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'_1PBCrt'}):
	name=a.find('p', attrs={'class':'_3LYOAd _3sxSiS _2675cp'}).text
	review=a.find('div',attrs={'class':''}).text
	rating=a.find('div',attrs={'class':'hGSR34'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.flipkart.com/casio-d011-a-158wa-1q-digital-watch-men-women/product-reviews/itmf3zhdga85ghju?pid=WATDJ5YXGFUP5RNG&lid=LSTWATDJ5YXGFUP5RNG3Q3EEO&marketplace=FLIPKART&page=6")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'_1PBCrt'}):
	name=a.find('p', attrs={'class':'_3LYOAd _3sxSiS _2675cp'}).text
	review=a.find('div',attrs={'class':''}).text
	rating=a.find('div',attrs={'class':'hGSR34'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.flipkart.com/casio-d011-a-158wa-1q-digital-watch-men-women/product-reviews/itmf3zhdga85ghju?pid=WATDJ5YXGFUP5RNG&lid=LSTWATDJ5YXGFUP5RNG3Q3EEO&marketplace=FLIPKART&page=7")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'_1PBCrt'}):
	name=a.find('p', attrs={'class':'_3LYOAd _3sxSiS _2675cp'}).text
	review=a.find('div',attrs={'class':''}).text
	rating=a.find('div',attrs={'class':'hGSR34'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.flipkart.com/casio-d011-a-158wa-1q-digital-watch-men-women/product-reviews/itmf3zhdga85ghju?pid=WATDJ5YXGFUP5RNG&lid=LSTWATDJ5YXGFUP5RNG3Q3EEO&marketplace=FLIPKART&page=8")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'_1PBCrt'}):
	name=a.find('p', attrs={'class':'_3LYOAd _3sxSiS _2675cp'}).text
	review=a.find('div',attrs={'class':''}).text
	rating=a.find('div',attrs={'class':'hGSR34'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.flipkart.com/casio-d011-a-158wa-1q-digital-watch-men-women/product-reviews/itmf3zhdga85ghju?pid=WATDJ5YXGFUP5RNG&lid=LSTWATDJ5YXGFUP5RNG3Q3EEO&marketplace=FLIPKART&page=9")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'_1PBCrt'}):
	name=a.find('p', attrs={'class':'_3LYOAd _3sxSiS _2675cp'}).text
	review=a.find('div',attrs={'class':''}).text
	rating=a.find('div',attrs={'class':'hGSR34'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.flipkart.com/casio-d011-a-158wa-1q-digital-watch-men-women/product-reviews/itmf3zhdga85ghju?pid=WATDJ5YXGFUP5RNG&lid=LSTWATDJ5YXGFUP5RNG3Q3EEO&marketplace=FLIPKART&page=10")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'_1PBCrt'}):
	name=a.find('p', attrs={'class':'_3LYOAd _3sxSiS _2675cp'}).text
	review=a.find('div',attrs={'class':''}).text
	rating=a.find('div',attrs={'class':'hGSR34'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
cost=soup.find('div',attrs={'class':'_1vC4OE'}).text
cost=cost.replace("₹","")
cost=cost.replace(",","")

df = pd.DataFrame({'Name':names,'Review':reviews,'Ratings':ratings,'Cost(₹)':float(cost)})
df.to_csv("flipkartwatch.csv", index=False, encoding='utf-8')
reviews_df = pd.read_csv("flipkartwatch.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["Reviews"] = reviews_df["Review"].apply(lambda x: x.replace("READ MORE", " "))
reviews_df["Good/Bad"] = reviews_df["Ratings"].apply(lambda x: 0 if x < 3 else 1)
reviews_df = reviews_df[["Names","Reviews", "Good/Bad"]]
print(reviews_df)
print(reviews_df["Good/Bad"].value_counts(normalize = True))
reviews_df.head()
