import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="lakshmi",
	passwd="password",
	database="trust_model"
)
mycursor=mydb.cursor()
mycursor.execute("create table Trust(SL_NO INT AUTO_INCREMENT PRIMARY KEY,PRODUCT varchar(20),AMAZON_GOOD float,AMAZON_BAD float,FLIPKART_GOOD float,FLIPKART_BAD float,EBAY_GOOD float,EBAY_BAD float)")
