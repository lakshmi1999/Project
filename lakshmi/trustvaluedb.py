import pandas as pd
import mysql.connector

reviews_df = pd.read_csv("amazonlaptop.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["Ratings"].apply(lambda x:'1' if x >='2.5' else '0')
lamazon_good=reviews_df["Good/Bad"].value_counts(normalize=True)[0]
lamazon_bad=reviews_df["Good/Bad"].value_counts(normalize=True)[1]

reviews_df = pd.read_csv("amazonphone.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x:'1' if x >='2.5' else '0')
pamazon_good=reviews_df["Good/Bad"].value_counts(normalize=True)[0]
pamazon_bad=reviews_df["Good/Bad"].value_counts(normalize=True)[1]

reviews_df = pd.read_csv("amazonwatch.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x:'1' if x >='2.5' else '0')
wamazon_good=reviews_df["Good/Bad"].value_counts(normalize=True)[0]
wamazon_bad=reviews_df["Good/Bad"].value_counts(normalize=True)[1]

reviews_df = pd.read_csv("amazontablet.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x:'1' if x >='2.5' else '0')
tamazon_good=reviews_df["Good/Bad"].value_counts(normalize=True)[0]
tamazon_bad=reviews_df["Good/Bad"].value_counts(normalize=True)[1]

reviews_df = pd.read_csv("amazonjoystick.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x:'1' if x >='2.5' else '0')
jamazon_good=reviews_df["Good/Bad"].value_counts(normalize=True)[0]
jamazon_bad=reviews_df["Good/Bad"].value_counts(normalize=True)[1]



reviews_df = pd.read_csv("flipkartlaptop.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["Good/Bad"] = reviews_df["Ratings"].apply(lambda x:'1' if x >=2.5 else '0')
lflipkart_good=reviews_df["Good/Bad"].value_counts(normalize = True)[0]
lflipkart_bad=reviews_df["Good/Bad"].value_counts(normalize = True)[1]

reviews_df = pd.read_csv("flipkartphone.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["Good/Bad"] = reviews_df["Ratings"].apply(lambda x:'1' if x >=2.5 else '0')
pflipkart_good=reviews_df["Good/Bad"].value_counts(normalize=True)[0]
pflipkart_bad=reviews_df["Good/Bad"].value_counts(normalize=True)[1]

reviews_df = pd.read_csv("flipkartjoystick.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["Good/Bad"] = reviews_df["Ratings"].apply(lambda x:'1' if x >=2.5 else '0')
jflipkart_good=reviews_df["Good/Bad"].value_counts(normalize=True)[0]
jflipkart_bad=reviews_df["Good/Bad"].value_counts(normalize=True)[1]

reviews_df = pd.read_csv("flipkarttablet.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["Good/Bad"] = reviews_df["Ratings"].apply(lambda x:'1' if x >=2.5 else '0')
tflipkart_good=reviews_df["Good/Bad"].value_counts(normalize=True)[0]
tflipkart_bad=reviews_df["Good/Bad"].value_counts(normalize=True)[1]

reviews_df = pd.read_csv("flipkartwatch.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["Good/Bad"] = reviews_df["Ratings"].apply(lambda x:'1' if x >=2.5 else '0')
wflipkart_good=reviews_df["Good/Bad"].value_counts(normalize=True)[0]
wflipkart_bad=reviews_df["Good/Bad"].value_counts(normalize=True)[1]



reviews_df = pd.read_csv("ebaylaptop.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x: 0 if x >= '2.5' else 1)
lebay_good=reviews_df["Good/Bad"].value_counts(normalize = True)[0]
lebay_bad=reviews_df["Good/Bad"].value_counts(normalize = True)[1]

reviews_df = pd.read_csv("ebayphone.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x: 0 if x >= '2.5' else 1)
pebay_good=reviews_df["Good/Bad"].value_counts(normalize = True)[0]
pebay_bad=reviews_df["Good/Bad"].value_counts(normalize = True)[1]

reviews_df = pd.read_csv("ebaywatch.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x: 0 if x >= '2.5' else 1)
webay_good=reviews_df["Good/Bad"].value_counts(normalize = True)[0]
webay_bad=reviews_df["Good/Bad"].value_counts(normalize = True)[1]

reviews_df = pd.read_csv("ebaytablet.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x: 0 if x >= '2.5' else 1)
tebay_good=reviews_df["Good/Bad"].value_counts(normalize = True)[0]
if tebay_good==1:
	tebay_bad=0
else:
	tebay_bad=reviews_df["Good/Bad"].value_counts(normalize = True)[1]

reviews_df = pd.read_csv("ebayjoystick.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x: 0 if x >= '2.5' else 1)
jebay_good=reviews_df["Good/Bad"].value_counts(normalize = True)[0]
jebay_bad=reviews_df["Good/Bad"].value_counts(normalize = True)[1]


mydb=mysql.connector.connect(
	host="localhost",
	user="lakshmi",
	passwd="password",
	database="trust_model"
)
mycursor=mydb.cursor()
sql="Insert into Trust(PRODUCT,AMAZON_GOOD,AMAZON_BAD,FLIPKART_GOOD,FLIPKART_BAD,EBAY_GOOD,EBAY_BAD)values(%s,%s,%s,%s,%s,%s,%s)"
val=[('LAPTOP',str(lamazon_good),str(lamazon_bad),str(lflipkart_good),str(lflipkart_bad),str(lebay_good),str(lebay_bad)),        	       	    ('PHONE',str(pamazon_good),str(pamazon_bad),str(pflipkart_good),str(pflipkart_bad),str(pebay_good),str(pebay_bad)),
     ('WATCH',str(wamazon_good),str(wamazon_bad),str(wflipkart_good),str(wflipkart_bad),str(webay_good),str(webay_bad)),
     ('TABLET',str(tamazon_good),str(tamazon_bad),str(tflipkart_good),str(tflipkart_bad),str(tebay_good),str(tebay_bad)),
     ('JOYSTICK',str(jamazon_good),str(jamazon_bad),str(jflipkart_good),str(jflipkart_bad),str(jebay_good),str(jebay_bad))]
mycursor.executemany(sql,val)
mydb.commit()
