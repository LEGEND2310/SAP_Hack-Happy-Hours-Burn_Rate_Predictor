# Personality Prediction API

This is a deep learning model that predicts a person's personality using Natural Language Processing.
It utilizes posts made by the individual.

## The Dataset

The data was collected from Kaggle. It can be found [here](https://www.kaggle.com/datasnaek/mbti-type).

## Running in localhost

To run this model some python packages are required which can be installed using the given requirements.txt file by entering the following command in the terminal:

```
pip install -r requirements.txt
```

To run the flask file as local host use the command
```
python app.py
```

## Architecture

The architecture uses Tensorflow and Keras library.
First layer trains the custom word embeddings based on the tokenizer and converted to sequences.
The model has 3 Gate Recurrent Units(GRUs). This was used over Bidirectional LSTM considering the size of the dataset.
It is then flattened followed by 3 hidden layers and a final output layer.

![model0](https://user-images.githubusercontent.com/47575172/115267890-524df700-a157-11eb-955e-42ab985bf5e1.png)

