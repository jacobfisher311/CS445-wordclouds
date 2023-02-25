import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import multidict as multidict

df = pd.read_csv("TweetsElonMusk.csv")
df.head()
# Converting tweets into lists by split()
df['new_text'] = df['tweet'].apply(lambda x: x.split() )
# Removing first element of all lists,which compose of tweet words
df['new_text'] = df['new_text'].apply(lambda x: x[1:])
# Converting back to string
df['last'] = df['new_text'].apply(lambda x: " ".join(str(y) for y in x))
stopwords = set(STOPWORDS)
# Converting to a big string
text = ' '.join(df['last'])

# Remove words that contain characters outside of the alphabet
text = re.sub(r'[^a-z A-Z]', ' ', text)

# Remove words smaller than 3 characters
text= re.sub(r'\b\w{1,3}\b', ' ', text)

fullTermsDict = multidict.MultiDict()
tmpDict = {}

# Making dict for counting frequencies
for text in text.split(" "):
    if re.match("with|that|http|them|than|which", text):
        continue
    val = tmpDict.get(text, 0)
    tmpDict[text.lower()] = val + 1
for key in tmpDict:
    fullTermsDict.add(key, tmpDict[key])

# Variable to hold the number of words on the word cloud
# 100, 150, 200, 250
button_val = 250

wc = WordCloud(background_color="white", max_words=button_val,
               stopwords=stopwords)
# Generate word cloud
wc.generate_from_frequencies(fullTermsDict)

# Show word cloud
print(wc)
plt.rcParams["figure.figsize"] = (15, 10)
fig = plt.figure(1)
plt.imshow(wc)
plt.title('Word cloud - Elon Musk\'s tweets',pad=10)
plt.axis('off')
plt.show()