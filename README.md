# CyberPy_bot

Cyberbullying and spamming have reached all-time highs, thanks to the emergence of social media and the Covid-19 epidemic. We can tackle this phenomenon by developing technologies that automatically detect potentially damaging messages and dissect hateful tendencies. 

CyberPy is a Discord chatbot that can be considered a potential solution designed for handling this malicious content.

The brains of this chatbot are sequence-to-sequence (seq2seq) models. The goal of a seq2seq model is to take a variable-length sequence as an input, and return a variable-length sequence as an output using a fixed-sized model. One RNN acts as an encoder, which encodes a variable length input sequence to a fixed-length context vector, and another one is decoder which takes an input word and the context vector, and returns a guess for the next word in the sequence and a hidden state to use in the next iteration. Both encoder and decoder are based on LSTM architecture.

![image](https://user-images.githubusercontent.com/92053176/168848628-e2c6bf60-2435-4337-b540-4edd486d78fd.png)
Image source: https://github.com/Arturus/kaggle-web-traffic/blob/master/images/encoder-decoder.png

**Chatbot API**

The main features of chatbot are:

- It filters all messages that are incoming and detects the malicious ones, classifing them into cyberbullying or spamming ones;
- It detects the type of cyberbullying: age, ethnicity, gender, religion, not cyberbullying;
- It warns the user who sent a cyberbullying message through an interactive interface: 

![image](https://user-images.githubusercontent.com/92053176/168857535-af80c14e-d243-4c5d-a7f3-47a596da6645.png)


- It automatically deletes the spam messages.
- It counts the number of damaging messages and reports to the admins (through a private channel) the user(s) who has exceeded the number of malicious messages.

![image](https://user-images.githubusercontent.com/92053176/168858665-eb7a5d85-64f1-4802-a03c-4cf80311fb4b.png)


