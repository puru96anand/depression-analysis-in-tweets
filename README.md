# An Analysis of Depression Detection in Tweets

This is a project created by Puru Anand (purua@uci.edu), Radhika Sharma (radhiks3@uci.edu) and Ritu Jha (jhar2@uci.edu) as a part of their course requirement at UC Irvine. Course CS271P - Introduction to Artificial Intelligence.

## Details/Explanations about the files
The [make_dataset](make_dataset.py) Python file creates the [final_dataset](final_dataset.csv) CSV file uisng the [Sentiment140](https://www.kaggle.com/kazanova/sentiment140) dataset CSV file. It is named '1m_tweets.csv' in the Python file.

The different Jupyter notebooks perform different tasks as per their names.
If trying to execute any notebook on its own, you would have to add a folder to your Google Drive called 'CS271P_Project' containing the [final_dataset](final_dataset.csv) file and a folder called glove, in which these unzipped [GloVe word embeddings](https://nlp.stanford.edu/data/glove.6B.zip) are present.

You can modify the [LSTM notebook](CS271P_LSTM.ipynb) in your own playground as per your own need, for example a different loss function, activation function, optimizer etc.

## References/Acknowledgements
Ali H. El-Kassas: [Getting started with text data](https://www.kaggle.com/ali01lulu/getting-started-with-text-data)

Arun Pandian R: NLP Beginner - [Text Classification using LSTM](https://www.kaggle.com/arunrk7/nlp-beginner-text-classification-using-lstm)

Diveesh Singh & Aileen Wang: [Detecting Depression Through Tweets](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184/reports/6879557.pdf)

Hien Nguyen: [WIP: Detect early depression through tweets](https://www.kaggle.com/yonebayashi/wip-detect-early-depression-through-tweets)

<!-- ## References/Acknowledgements -->
Diveesh Singh & Aileen Wang: [Detecting Depression Through Tweets](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184/reports/6879557.pdf)

Mandar Deshpande, Vignesh Rao: [Depression detection using emotion artificial intelligence](https://ieeexplore.ieee.org/abstract/document/8389299/)

Ahmed Husseini Orabi, Prasadith Buddhitha, Mahmoud Husseini Orabi, Diana Inkpen: [Deep Learning for Depression Detection of Twitter Users](https://www.aclweb.org/anthology/W18-0609.pdf)

I. Rish: [An empirical study of the naive Bayes classifier](https://www.cc.gatech.edu/~isbell/reading/papers/Rish.pdf)

Wright R.E.: [Logistic Regression](https://psycnet.apa.org/record/1995-97110-007)

Hochreiter Sepp, Schmidhuber Jürgen: [Long Short-term Memory](https://www.researchgate.net/publication/13853244_Long_Short-term_Memory)
