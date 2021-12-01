import pandas as pd 
from re import search

# May need to change the below location
df = pd.read_csv('1m_tweets.csv', encoding="utf-8")

depressed_tweets = []
happy_tweets = []

sad_words = ['depress', 'sadden', 'upset', 'bother', 'dishearten', 'anxiety']
happy_words = ['love', 'happy', 'glad', 'lol', 'thank', 'beautiful', 'good', 'great']

for index, row in df.iterrows():
    if row['target'] == 0:
        if any(word in row['text'] for word in sad_words):
            depressed_tweets.append('"' + row['text'] + '","1"\n')

num_sad = len(depressed_tweets);

for index, row in df.iterrows():
    if row['target'] == 4:
        if any(word in row['text'] for word in happy_words):
            happy_tweets.append('"' + row['text'] + '","0"\n')
            num_sad = num_sad - 1
        if num_sad == 0:
            break

print(len(depressed_tweets))
print(len(happy_tweets))

# May need to change the below location
file = open('final_dataset.csv', 'w')
file.write('text,label\n')
file.writelines(depressed_tweets)
file.writelines(happy_tweets)
file.close()
