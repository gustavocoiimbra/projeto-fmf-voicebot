import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from keras.models import Sequential
from nltk.corpus import stopwords
from keras.layers import Dense, Activation, Dropout
import random
import tensorflow as tf

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
lemmatizer = WordNetLemmatizer()

# Abrir arquivo json
data_file = open('data_music.json').read()
intents = json.loads(data_file)

words = []
documents = []
classes = []
ignore_words = ['!', '?', '...', '"', ',', '``', "'", "''", "(", ")"]

for musica in intents:
    title = nltk.word_tokenize(musica['title'])
    title = [word for word in title if word.isalnum()]
    musica['title'] = ''.join(title).lower()

for musica in intents:
    for letras in musica['liryc']:
        # take each word and tokenize it
        w = nltk.word_tokenize(letras)
        w = [word for word in w if word.isalnum() and word not in stopwords.words('english')]
        words.extend(w)

        # adding documents
        documents.append((w, musica['title']))

        # adding classes to our class list
        if musica['title'] not in classes:
            classes.append(musica['title'])

lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(w.lower())
         for w in words if w not in ignore_words]

words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "unique lemmatized words", words)

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# initializing training data
training = []
output_empty = [0] * len(classes)
for doc in documents:
    # initializing bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # lemmatize each word - create base word, in attempt to represent related words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # create our bag of words array with 1, if word match found in current pattern
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training, dtype=object)
# create train and test lists. X - patterns, Y - intents
train_x = list(training[:, 0])
train_y = list(training[:, 1])
print("Training data created")

# Create model - 3 layers. First layer 128 neurons, second layer
# 64 neurons and 3rd output layer contains number of neurons
# equal to number of intents to predict output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5)

model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# fitting and saving the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=400, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)

print("model created")
