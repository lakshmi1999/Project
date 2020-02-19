from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome(executable_path="/home/ubuntu/Downloads/chromedriver")
names=[]
reviews=[]
ratings=[]
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Midnight-Black/product-reviews/B07CSDCJG8/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Midnight-Black/product-reviews/B07CSDCJG8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Midnight-Black/product-reviews/B07CSDCJG8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=3")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Midnight-Black/product-reviews/B07CSDCJG8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=4")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Midnight-Black/product-reviews/B07CSDCJG8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=5")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Midnight-Black/product-reviews/B07CSDCJG8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=6")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Midnight-Black/product-reviews/B07CSDCJG8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=7")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Midnight-Black/product-reviews/B07CSDCJG8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=8")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Midnight-Black/product-reviews/B07CSDCJG8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=9")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Midnight-Black/product-reviews/B07CSDCJG8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=10")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Samsung-Galaxy-Midnight-Storage-Offers/dp/B07CSDCJG8/ref=pd_sbs_107_t_1/261-9075635-6483860?_encoding=UTF8&pd_rd_i=B07CSDCJG8&pd_rd_r=4e94dc4e-62cc-4b5e-8881-4c65f71e3919&pd_rd_w=tjbFf&pd_rd_wg=eS1WT&pf_rd_p=21bbdc4d-873b-48c5-a88a-70e643377944&pf_rd_r=ER13EEM6H0TX5DWEF7F3&psc=1&refRID=ER13EEM6H0TX5DWEF7F3")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
cost=soup.find('span',attrs={'class':'a-color-price'}).text
cost=cost.replace("₹","")
cost=cost.replace(",","")

df = pd.DataFrame({'Name':names,'Ratings':ratings,'Review':reviews,'Cost(₹)':float(cost)})
df.to_csv("amazonphone.csv", index=False, encoding='utf-8')
reviews_df = pd.read_csv("amazonphone.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x: 0 if x < '3' else 1)
reviews_df = reviews_df[["Names","Review", "Good/Bad"]]
print(reviews_df)
print(reviews_df["Good/Bad"].value_counts(normalize = True))
reviews_df.head()

