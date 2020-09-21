#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing neccessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import warnings
warnings.filterwarnings('ignore')


# In[3]:


#tensorflow is used to train the model
import csv
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# In[4]:


get_ipython().system(u'pip install tweet-preprocessor')


# In[5]:


#importing dataset
file='/home/nbuser/library/train.csv'

tweet_df = pd.read_csv(file)


# In[6]:


tweet_df.columns=['sentiment','text','null']


# In[7]:


tweet_df=tweet_df.drop(['null'],axis=1)


# In[8]:


tweet_df.head()


# In[9]:


#removal of stopwords
sentences = []
labels = []
stopwords = [ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]
print(len(stopwords))


# In[10]:


with open("laptop.csv", 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        print(row)
        labels.append(row[0])
        sentence = row[1]
        for word in stopwords:
            token = " " + word + " "
            sentence = sentence.replace(token, " ")
        sentences.append(sentence)


# In[11]:


tweet_df.columns=['sentiment','text']


# In[12]:


tweet_df.head()


# In[13]:


tweet_list = tweet_df['text'].tolist()


# In[14]:


tweet_list[:5]


# In[15]:


import preprocessor as p
from preprocessor import clean
import re #to remove backslash and all
def normalize_text(text):
    p.set_options(p.OPT.URL, p.OPT.EMOJI,p.OPT.SMILEY, p.OPT.NUMBER, p.OPT.MENTION, p.OPT.HASHTAG, p.OPT.RESERVED)
    text=p.clean(str(text))
    text=text.lower()
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(pic\.twitter\.com/[^\s]+))','', text)
    text = re.sub('@[^\s]+','', text)
    text = re.sub('#([^\s]+)', '', text)
    #text = re.sub(r'[^\w]', ' ', text)
    text = re.sub('[:;>?<=*+()&,\-#!$%\{˜|\}\[^_\\@\]1234567890’‘]',' ', text)
    text = re.sub('[\d]','', text)
    text = text.replace(".", '')
    text = text.replace("amp", '')
    text = text.replace("'", '')
    text = text.replace("`", '')
    text = text.replace("'s", '')
    text = text.replace("/", ' ')
    text = text.replace("\"", ' ')
    text = text.replace("\\", '')
    re.sub(' +', ' ', text)
    text=text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    #normalize some utf8 encoding
    text = text.replace("\x9d",'').replace("\x8c",'')
    text = text.replace("\xa0",'')
    text = text.replace("\x9d\x92", '').replace("\x9a\xaa\xf0\x9f\x94\xb5", '').replace("\xf0\x9f\x91\x8d\x87\xba\xf0\x9f\x87\xb8", '').replace("\x9f",'').replace("\x91\x8d",'')
    text = text.replace("\xf0\x9f\x87\xba\xf0\x9f\x87\xb8",'').replace("\xf0",'').replace('\xf0x9f','').replace("\x9f\x91\x8d",'').replace("\x87\xba\x87\xb8",'')
    text = text.replace("\xe2\x80\x94",'').replace("\x9d\xa4",'').replace("\x96\x91",'').replace("\xe1\x91\xac\xc9\x8c\xce\x90\xc8\xbb\xef\xbb\x89\xd4\xbc\xef\xbb\x89\xc5\xa0\xc5\xa0\xc2\xb8",'')
    text = text.replace("\xe2\x80\x99s", "").replace("\xe2\x80\x98", '').replace("\xe2\x80\x99", '').replace("\xe2\x80\x9c", "").replace("\xe2\x80\x9d", "")
    text = text.replace("\xe2\x82\xac", "").replace("\xc2\xa3", "").replace("\xc2\xa0", "").replace("\xc2\xab", "").replace("\xf0\x9f\x94\xb4", "").replace("\xf0\x9f\x87\xba\xf0\x9f\x87\xb8\xf0\x9f", "")
    text =  re.sub(r"\b[a-z]\b", "", text)
    text=re.sub( '\s+', ' ', text).strip()
    
    text=re.sub(r'\.+', ".", text)
    text=re.sub(r'\.\.+', ' ', text).replace('.', '')
    # Replace multiple dots with space
    text = re.sub('\.\.+', ' ', text) 
    # Remove single dots
    text = re.sub('\.', '', text)
    text = re.sub(r'\.{2,}', ' ', text)
    text = re.sub(r'\.{1}', '', text)
    
    return text


# In[16]:


clean_tweet=[]
for tweet in tweet_list:
    norm_sent=normalize_text(tweet)
    clean_tweet.append(norm_sent)


# In[17]:


clean_tweet[:5]


# In[18]:


tweet_df['text'] = clean_tweet


# In[19]:


tweet_df.head()


# In[20]:


import csv
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# In[21]:


tweet_df.head()


# In[22]:


tokenizer = Tokenizer(nb_words=2500, lower=True,split=' ')
tokenizer.fit_on_texts(tweet_df['text'].values)
X = tokenizer.texts_to_sequences(tweet_df['text'].values)
X = pad_sequences(X)


# In[23]:


X


# In[24]:


print(tokenizer.word_index) 


# In[25]:


X.shape[1]


# In[26]:


from keras import optimizers
embed_dim = 128
lstm_out = 100
batch_size = 32

# the model will take as input an integer matrix of size (batch,input_length).
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(2500, embed_dim,input_length =1393), # 2500 is the vocabulary size >1393
    tf.keras.layers.LSTM(lstm_out),
    tf.keras.layers.Dense(6, activation='sigmoid'), # 6 is the unit which is the dim of the output space
    
])

model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model.summary())


# In[27]:


from sklearn.model_selection import train_test_split
Y = pd.get_dummies(tweet_df['sentiment']).values
X_train, X_valid, Y_train, Y_valid = train_test_split(X,Y, test_size = 0.20, random_state = 36)
model.fit(X_train, Y_train, batch_size =batch_size, nb_epoch = 1,  verbose = 10)


# In[28]:


score,acc = model.evaluate(X_valid,Y_valid,verbose=5,batch_size=batch_size)
print("Score : %.2f" %(score))
print("Validation Accuracy : %.2f" %(acc))


# In[29]:


num_epochs = 5
history = model.fit(X_train, Y_train, epochs=num_epochs, validation_data=(X_valid,Y_valid), verbose=2)


# In[36]:


import matplotlib.pyplot as plt

def plot_graphs(history, string):
  plt.plot(history.history[string])
  plt.plot(history.history['val_'+string])
  plt.xlabel("Epochs")
  plt.ylabel(string)
  plt.legend([string, 'val_'+string])
  plt.show()
  
plot_graphs(history, "accuracy")
plot_graphs(history, "loss")


# In[31]:


#import test dataset
test=pd.read_csv('/home/nbuser/library/test_set.csv')


# In[32]:


test.head()


# In[33]:


test=test.drop(['label'],axis=1)


# In[34]:


test.head()


# In[40]:


test=test.astype(str)


# In[42]:


tokenizer = Tokenizer(nb_words=2500,lower='true',split=' ')
tokenizer.fit_on_texts(test['sentence'].values)
Xe = tokenizer.texts_to_sequences(test['sentence'].values)


# In[43]:


Xe = pad_sequences(Xe)


# In[44]:


Xe


# In[47]:



from keras import preprocessing
Xe = preprocessing.sequence.pad_sequences(Xe, maxlen=1393)
print(Xe.shape)


# In[48]:


preds=model.predict_classes(Xe,verbose=0)


# In[49]:


preds


# In[50]:


list=preds.tolist()


# In[51]:


import pandas as pd
from pandas import DataFrame
df = DataFrame(list,columns=['ratings'])


# In[52]:


df.head()
df.to_csv('/home/nbuser/library/testans.csv')


# In[ ]:
