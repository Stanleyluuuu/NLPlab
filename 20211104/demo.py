import pandas as pd
import pdb
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
import gensim
import random
from sklearn.model_selection import train_test_split
import numpy as np
from tensorflow.keras import layers

def loadData(path):
    ngram, _class = [], []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip("\n").split("\t")
            ngram.append(line[0])
            _class.append(int(line[1]))

    return pd.DataFrame({"phrase":ngram,"class":_class})

def generate_embemdding(x):
    embedding_matrix = []
    for row in x:
        a = np.mean([w2v_model[e] for e in row])
        embedding_matrix.append(a)

    return np.array(embedding_matrix)

def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(600, activation='relu', input_shape=(5,)),
    # keras.layers.Dropout(0.5),
    # keras.layers.Dense(400),
    # keras.layers.Dropout(0.5),
    # keras.layers.Dense(200),
    # keras.layers.Dropout(0.5),
    keras.layers.Dense(2)
  ])

  model.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=[tf.metrics.SparseCategoricalAccuracy()])

  return model
# generate_embemdding()
train = loadData("./data/train.tsv")
print(train.head())
test = loadData("./data/test.tsv")    
print(test.head())

pdb.set_trace()


# good, bad = {}, {}
# for index, row in train.iterrows():
#     if row["class"] == 1: good[row["phrase"]] = row["class"]
#     else: bad[row["phrase"]] = row["class"]
# good, bad = list(good.items()), list(bad.items())
# random.shuffle(bad)
# good.extend(bad[:len(good)])
# random.shuffle(good)
# train = pd.DataFrame(good, columns=["phrase", "class"])
# w2v_model = gensim.models.KeyedVectors.load_word2vec_format("./data/GoogleNews-vectors-negative300.bin", binary=True)
# w2v_model["language"]
# pdb.set_trace()
# tok = Tokenizer()
# tok.fit_on_texts(pd.concat([train, test],ignore_index=True).astype(str)['phrase'])
# vocab_size = len(tok.word_index) + 1

# train_encoded_phrase = tok.texts_to_sequences(train['phrase'])
# test_encoded_phrase = tok.texts_to_sequences(test['phrase'])

# max_ngram = 5
# X_train = pad_sequences(train_encoded_phrase, maxlen=max_ngram, padding='post')
# X_test = pad_sequences(test_encoded_phrase, maxlen=max_ngram, padding='post')
# print(X_train[:5])

# y_train = to_categorical(train['class'])
# y_test = to_categorical(test['class'])
# print(y_train[:5])

# X_train, X_val, y_train, y_val = train_test_split(X_train,y_train,test_size=0.20,random_state=42)

# X_train_emb = generate_embemdding(X_train)
# X_val_emb = generate_embemdding(X_val)

# # model = create_model()
# # model = tf.keras.layers.LSTM(10)
# model = keras.Sequential()
# model.add(layers.Embedding(input_dim=300, output_dim=64))
# model.add(layers.LSTM(128))
# model.add(layers.Dense(2))
# model.compile(optimizer='adam',
#                 loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
#                 metrics=[tf.metrics.SparseCategoricalAccuracy()])

# model.fit(X_train, y_train, batch_size=200, epochs=50, validation_data=(X_val,y_val))
# accuracy = model.evaluate(X_test,y_test)
# print(accuracy[1])
# pdb.set_trace()