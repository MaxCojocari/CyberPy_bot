# CyberPy Bot ©

Cyberbullying and spamming have reached all-time highs, thanks to the emergence of social media and the Covid-19 epidemic. We can tackle this phenomenon by developing technologies that automatically detect potentially damaging messages and dissect hateful tendencies. 

CyberPy is a Discord chatbot that can be considered a potential solution designed for handling this malicious content.

The brains of this chatbot are sequence-to-sequence (seq2seq) models. The goal of a seq2seq model is to take a variable-length sequence as an input, and return a variable-length sequence as an output using a fixed-sized model. One RNN acts as an encoder, which encodes a variable length input sequence to a fixed-length context vector, and another one is decoder which takes an input word and the context vector, and returns a guess for the next word in the sequence and a hidden state to use in the next iteration. Both encoder and decoder are based on LSTM architecture.

![image](https://user-images.githubusercontent.com/92053176/168848628-e2c6bf60-2435-4337-b540-4edd486d78fd.png)

Image source: https://github.com/Arturus/kaggle-web-traffic/blob/master/images/encoder-decoder.png

## Chatbot API

The main features of chatbot are:

- It filters all messages that are incoming and detects the malicious ones, classifing them into cyberbullying or spamming;
- It detects the type of cyberbullying;
- It warns the user who sent a cyberbullying message through an interactive interface: 

![image](https://user-images.githubusercontent.com/92053176/168859501-5d116187-8e50-4607-9fea-0091bd9771a2.png)

- It automatically deletes the spam messages;
- It counts the number of damaging messages and reports to the admins (through a private channel) the user(s) who has exceeded the number of malicious messages;
- It can provide a natural conversation with the user.

## Installation and usage

The project is structured into 3 directories: ```training```, ```models``` and ```app```.

The ```training``` directory contains Google Colab notebooks used for training seq2seq models.

The ```models``` directory includes the following pre-trained models:

- ```cyberbullying_lstm.pt``` pipeline that classifies cyberbullying messages in five classes: **age**, **ethnicity**, **gender**, **religion**, **not cyberbullying**;
- ```spam_lstm.pt``` pipeline that classifies every message in two classes: **spam**, **not spam**;

The cluster of pipelines ```chatbot_checkpoint.tar``` for natural conversation issues is missing here due to its huge size, but it can be generated 
in this way:

1. Copy ```chatbot.ipynb``` and in the last cell change the path 'drive/MyDrive/NLPC2022' to your local path, which should look like '.../models';

![image](https://user-images.githubusercontent.com/92053176/169882027-8e000088-b9a9-448f-a3f9-b8e599ea3d3f.png)

2. Run the notebook using Google Colab or Jupyter Notebook and make sure that all cells were run.

The ```app``` directory includes these modules:

- ```launch.ipynb``` the notebook used for application launching;
- ```app.py``` the main script that glues all of the magic from the other modules.


To run this project, you first should install the following dependencies by running the following command:

```
$ pip install -r requirements.txt
```

In order to be able to use chatbot in the Discord environment, you should create an account for it and invite in whichever server(s) you want. A detailed [guide](https://discordpy.readthedocs.io/en/stable/discord.html) can help you! While creating the account, make a copy of the generated token and keep it in secret.

Next, in the ```app``` folder create a .env file and insert the bot's token in this format:

```
TOKEN=(paste your token here)
```

In order to start the chatbot, run ```launch.ipynb```, copy the output URL which should look like "http://9e7b-35-199-179-209.ngrok.io" and paste into URL variable in ```main.py```. Finally, start ```main.py``` in ```app``` directory, by running this command in your terminal:

```
python main.py
```

## Datasets

The data used when training the **nlp** models:

- [Spam Text Message Classification](https://www.kaggle.com/datasets/team-ai/spam-text-message-classification)
- [Cyberbullying Classification](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)
- [Cornell Movie Dialogs Corpus](http://www.cs.cornell.edu/~cristian/data/cornell_movie_dialogs_corpus.zip)
