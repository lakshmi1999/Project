import pandas as pd
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
if tamazon_good==1:
	tamazon_bad=0
else:
	tamazon_bad=reviews_df["Good/Bad"].value_counts(normalize = True)[1]


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

my_dict = { 'PRODUCT': ["LAPTOP","PHONE","WATCH","TABLET","JOYSTICK"],
	    'AMAZON_GOOD' : [lamazon_good,pamazon_good,wamazon_good,tamazon_good,jamazon_good],
            'AMAZON_BAD' : [lamazon_bad,pamazon_bad,wamazon_bad,tamazon_bad,jamazon_bad],
            'FLIPKART_GOOD': [lflipkart_good,pflipkart_good,wflipkart_good,tflipkart_good,jflipkart_good],
	    'FLIPKART_BAD' : [lflipkart_bad,pflipkart_bad,wflipkart_bad,tflipkart_bad,jflipkart_bad],
            'EBAY_GOOD': [lebay_good,pebay_good,webay_good,tebay_good,jebay_good],
		'EBAY_BAD': [lebay_bad,pebay_bad,webay_bad,tebay_bad,jebay_bad]
	  }
	   
df = pd.DataFrame(my_dict)
df.to_csv("trustvalue.csv", index=False, encoding='utf-8')
reviews_df.head()

