import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import multidict as multidict

plt.rcdefaults("TweetsElonMusk.csv")
fig, ax = plt.subplots()
bar_colors = ['tab:red', 'tab:blue']


df = pd.read_csv("")
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

# Sorting the dictionary from largest value to smallest
temp = dict(sorted(fullTermsDict.items(), key=lambda item: item[1], reverse=True))

def top10():
    first10 = dict({k: temp[k] for k in list(temp)[1:11]})

    words = list(first10.keys())
    values = list(first10.values())

    plt.barh(range(len(first10)), values, tick_label=words, color=bar_colors)
    ax.set_title('Top Ten Words Used')
    ax.set_xlabel('Use Frequency')
    ax.set_ylabel('Word')
    ax.invert_yaxis()
    plt.show()

def top30():
    first30 = dict({k: temp[k] for k in list(temp)[1:31]})

    words = list(first30.keys())
    values = list(first30.values())

    plt.barh(range(len(first30)), values, tick_label=words, color=bar_colors)
    ax.set_title('Top Thirty Words Used')
    ax.set_xlabel('Use Frequency')
    ax.set_ylabel('Word')
    ax.invert_yaxis()
    plt.show()

def top50():
    first50 = dict({k: temp[k] for k in list(temp)[1:51]})

    words = list(first50.keys())
    values = list(first50.values())

    plt.barh(range(len(first50)), values, tick_label=words, color=bar_colors)
    ax.set_title('Top Fifty Words Used')
    ax.set_xlabel('Use Frequency')
    ax.set_ylabel('Word')
    ax.invert_yaxis()
    plt.show()


#top10()
top30()
#top50()
