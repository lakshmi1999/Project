import pandas as pd
print("FLIPKART")
df = pd.read_csv('flipkartlaptop.csv')
lflipkarttrust=(df['Ratings'] ==1).sum()+((df['Ratings'] ==2).sum()*2)+((df['Ratings'] ==3).sum()*3)+((df['Ratings'] ==4).sum()*4)+((df['Ratings'] ==5).sum()*5)
lflipkarttrust=lflipkarttrust/len(df['Ratings'])
lflipkarttrust=round((lflipkarttrust/5)*100,2)
clflipkart=df.iloc[1,3]
print(lflipkarttrust)

df = pd.read_csv('flipkartphone.csv')
pflipkarttrust=(df['Ratings'] ==1).sum()+((df['Ratings'] ==2).sum()*2)+((df['Ratings'] ==3).sum()*3)+((df['Ratings'] ==4).sum()*4)+((df['Ratings'] ==5).sum()*5)
pflipkarttrust=pflipkarttrust/len(df['Ratings'])
pflipkarttrust=round((pflipkarttrust/5)*100,2)
cpflipkart=df.iloc[1,3]

print(pflipkarttrust)

df = pd.read_csv('flipkartwatch.csv')
wflipkarttrust=(df['Ratings'] ==1).sum()+((df['Ratings'] ==2).sum()*2)+((df['Ratings'] ==3).sum()*3)+((df['Ratings'] ==4).sum()*4)+((df['Ratings'] ==5).sum()*5)
wflipkarttrust=wflipkarttrust/len(df['Ratings'])
wflipkarttrust=round((wflipkarttrust/5)*100,2)
cwflipkart=df.iloc[1,3]
print(wflipkarttrust)

df = pd.read_csv('flipkarttablet.csv')
tflipkarttrust=(df['Ratings'] ==1).sum()+((df['Ratings'] ==2).sum()*2)+((df['Ratings'] ==3).sum()*3)+((df['Ratings'] ==4).sum()*4)+((df['Ratings'] ==5).sum()*5)
tflipkarttrust=tflipkarttrust/len(df['Ratings'])
tflipkarttrust=round((tflipkarttrust/5)*100,2)
ctflipkart=df.iloc[1,3]
print(tflipkarttrust)

df = pd.read_csv('flipkartjoystick.csv')
jflipkarttrust=(df['Ratings'] ==1).sum()+((df['Ratings'] ==2).sum()*2)+((df['Ratings'] ==3).sum()*3)+((df['Ratings'] ==4).sum()*4)+((df['Ratings'] ==5).sum()*5)
jflipkarttrust=jflipkarttrust/len(df['Ratings'])
jflipkarttrust=round((jflipkarttrust/5)*100,2)
cjflipkart=df.iloc[1,3]
print(jflipkarttrust)

print("AMAZON")
df= pd.read_csv('amazonlaptop.csv')
df["Ratings"] =df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
lamazontrust=(df["Ratings"].astype(float) ==1).sum()+((df['Ratings'].astype(float) ==2).sum()*2)+((df['Ratings'].astype(float) ==3).sum()*3)+((df['Ratings'].astype(float) ==4).sum()*4)+((df['Ratings'].astype(float) ==5).sum()*5)
lamazontrust=lamazontrust/len(df['Ratings'])
lamazontrust=round((lamazontrust/5)*100,2)
clamazon=df.iloc[1,3]
print(lamazontrust)


df= pd.read_csv('amazonphone.csv')
df["Ratings"] =df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
pamazontrust=(df["Ratings"].astype(float) ==1).sum()+((df['Ratings'].astype(float) ==2).sum()*2)+((df['Ratings'].astype(float) ==3).sum()*3)+((df['Ratings'].astype(float) ==4).sum()*4)+((df['Ratings'].astype(float) ==5).sum()*5)
pamazontrust=pamazontrust/len(df['Ratings'])
pamazontrust=round((pamazontrust/5)*100,2)
cpamazon=df.iloc[1,3]
print(pamazontrust)

df= pd.read_csv('amazonwatch.csv')
df["Ratings"] =df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
wamazontrust=(df["Ratings"].astype(float) ==1).sum()+((df['Ratings'].astype(float) ==2).sum()*2)+((df['Ratings'].astype(float) ==3).sum()*3)+((df['Ratings'].astype(float) ==4).sum()*4)+((df['Ratings'].astype(float) ==5).sum()*5)
wamazontrust=wamazontrust/len(df['Ratings'])
wamazontrust=round((wamazontrust/5)*100,2)
cwamazon=df.iloc[1,3]
print(wamazontrust)

df= pd.read_csv('amazontablet.csv')
df["Ratings"] =df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
tamazontrust=(df["Ratings"].astype(float) ==1).sum()+((df['Ratings'].astype(float) ==2).sum()*2)+((df['Ratings'].astype(float) ==3).sum()*3)+((df['Ratings'].astype(float) ==4).sum()*4)+((df['Ratings'].astype(float) ==5).sum()*5)
tamazontrust=tamazontrust/len(df['Ratings'])
tamazontrust=round((tamazontrust/5)*100,2)
ctamazon=df.iloc[1,3]
print(tamazontrust)

df= pd.read_csv('amazonjoystick.csv')
df["Ratings"] =df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
jamazontrust=(df["Ratings"].astype(float) ==1).sum()+((df['Ratings'].astype(float) ==2).sum()*2)+((df['Ratings'].astype(float) ==3).sum()*3)+((df['Ratings'].astype(float) ==4).sum()*4)+((df['Ratings'].astype(float) ==5).sum()*5)
jamazontrust=jamazontrust/len(df['Ratings'])
jamazontrust=round((jamazontrust/5)*100,2)
cjamazon=df.iloc[1,3]
print(jamazontrust)

print("EBAY")
df = pd.read_csv('ebaylaptop.csv')
df["Ratings"] =df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
lebaytrust=(df['Ratings'].astype(float) ==1).sum()+((df['Ratings'].astype(float) ==2).sum()*2)+((df['Ratings'].astype(float) ==3).sum()*3)+((df['Ratings'].astype(float) ==4).sum()*4)+((df['Ratings'].astype(float) ==5).sum()*5)
lebaytrust=lebaytrust/len(df['Ratings'])
lebaytrust=round((lebaytrust/5)*100,2)
clebay=df.iloc[1,3]
print(lebaytrust)


df = pd.read_csv('ebayphone.csv')
df["Ratings"] =df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
pebaytrust=(df['Ratings'].astype(float) ==1).sum()+((df['Ratings'].astype(float) ==2).sum()*2)+((df['Ratings'].astype(float) ==3).sum()*3)+((df['Ratings'].astype(float) ==4).sum()*4)+((df['Ratings'].astype(float) ==5).sum()*5)
pebaytrust=pebaytrust/len(df['Ratings'])
pebaytrust=round((pebaytrust/5)*100,2)
cpebay=df.iloc[1,3]
print(pebaytrust)


df = pd.read_csv('ebaywatch.csv')
df["Ratings"] =df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
webaytrust=(df['Ratings'].astype(float) ==1).sum()+((df['Ratings'].astype(float) ==2).sum()*2)+((df['Ratings'].astype(float) ==3).sum()*3)+((df['Ratings'].astype(float) ==4).sum()*4)+((df['Ratings'].astype(float) ==5).sum()*5)
webaytrust=webaytrust/len(df['Ratings'])
webaytrust=round((webaytrust/5)*100,2)
cwebay=df.iloc[1,3]
print(webaytrust)

df = pd.read_csv('ebaytablet.csv')
df["Ratings"] =df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
tebaytrust=(df['Ratings'].astype(float) ==1).sum()+((df['Ratings'].astype(float) ==2).sum()*2)+((df['Ratings'].astype(float) ==3).sum()*3)+((df['Ratings'].astype(float) ==4).sum()*4)+((df['Ratings'].astype(float) ==5).sum()*5)
tebaytrust=tebaytrust/len(df['Ratings'])
tebaytrust=round((tebaytrust/5)*100,2)
ctebay=df.iloc[1,3]
print(tebaytrust)

df = pd.read_csv('ebayjoystick.csv')
df["Ratings"] =df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
jebaytrust=(df['Ratings'].astype(float) ==1).sum()+((df['Ratings'].astype(float) ==2).sum()*2)+((df['Ratings'].astype(float) ==3).sum()*3)+((df['Ratings'].astype(float) ==4).sum()*4)+((df['Ratings'].astype(float) ==5).sum()*5)
jebaytrust=jebaytrust/len(df['Ratings'])
jebaytrust=round((jebaytrust/5)*100,2)
cjebay=df.iloc[1,3]
print(jebaytrust)
my_dict = { 'PROVIDER': ["AMAZON","FLIPKART","EBAY"],
	    'LAPTOP' : [lamazontrust,lflipkarttrust,lebaytrust],
            'PHONE' : [pamazontrust,pflipkarttrust,pebaytrust],
            'WATCH': [lamazontrust,lflipkarttrust,lebaytrust],
	    'TABLET' : [tamazontrust,tflipkarttrust,tebaytrust],
            'JOYSTICK': [jamazontrust,jflipkarttrust,jebaytrust]
	  }
	   
df = pd.DataFrame(my_dict)
df.to_csv("trustvalue.csv", index=False, encoding='utf-8')

my_dict1={'PROVIDER':["AMAZON","FLIPKART","EBAY"],
	  'LAPTOP':[clamazon,clflipkart,clebay],
	  'PHONE':[cpamazon,cpflipkart,cpebay],
	  'WATCH':[cwamazon,cwflipkart,cwebay],
	  'TABLET':[ctamazon,ctflipkart,ctebay],
	  'JOYSTICK':[cjamazon,cjflipkart,cjebay]
	}
df1=pd.DataFrame(my_dict1)
df1.to_csv("costvalue.csv", index=False, encoding='utf-8')
df.head()
