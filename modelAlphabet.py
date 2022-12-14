import h5py
import keras
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, model_from_json

try:

    with h5py.File("modelAlphabet.h5",'r') as f:
        print("fileAlreadyDownloaded")
        pass

except Exception as e:
    X = np.load("X.npz")
    y = np.load("y.npz")

    X = X["arr_0"]
    y = y["arr_0"]
    print(X)
    X_trn, X_tst, y_trn, y_tst = train_test_split(X, y, test_size=0.2, random_state=42)
    print(X_trn)

    X_valid, X_train = X_trn[:20], X_trn[20:]
    y_valid, y_train = y_trn[:20], y_trn[20:]



    model = keras.models.Sequential()
    model.add(keras.layers.Flatten(input_shape=[21,2]))
    model.add(keras.layers.Dense(37, activation="sigmoid"))
    model.add(keras.layers.Dense(27, activation="sigmoid"))
    model.add(keras.layers.Dense(23, activation="softmax"))



    model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd" ,metrics=["accuracy"])


    history = model.fit(X_trn, y_trn, epochs=300,validation_data=(X_valid, y_valid))


    print(model.evaluate(X_tst, y_tst))


    model_json = model.to_json()
    with open("modelAlphabet.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("modelAlphabet.h5")
    print("Saved model to disk")


# load json and create model

json_file = open('modelAlphabet.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("modelAlphabet.h5")
print("Loaded model from disk")

# predictionss1 = loaded_model.predict(x1)
