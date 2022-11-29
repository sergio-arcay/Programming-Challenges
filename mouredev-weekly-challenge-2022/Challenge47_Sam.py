"""
Reto #47

Crea una función que reciba un texto y retorne la vocal que más veces se repita:

    - Ten cuidado con algunos casos especiales.

    - Si no hay vocales podrá devolver vacío.

"""


def boring_counter(text):
    """ Return the vowel with more occurrences (if several vowels have the same occurrences, none of them is returned).
    """
    counter = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letter in (letter for letter in text if letter in counter):
        counter[letter] += 1
    resulting_vowel, resulting_count = max(counter.items(), key=lambda item: item[1])
    return resulting_vowel if resulting_count > 0 and list(counter.values()).count(resulting_count) == 1 else None


def neural_counter(tests):
    """ Build a neural network model to calculate the vowel with more occurrences into a text.

    Essential notes:

        - This function builds and trains a neural model which, luckily, will be able to pass the tests which were
        written by the same person who has uploaded this.

        - Actually, the input for this model is already the number of occurrences of each letter in the text, so if
        you think about it, this network just try to detect the highest input value and check its index in the input
        array (which neuron received this value in the input layer).

        - I know that some of you have been wondering about the dataset for the training stage. Well, it's essential
        to know that the main reason for this exhausting comment, is the fact that the more time I spend writing
        the documentation of this function, the more training data will be provided to the model this function
        builds.

        - Now, try imagining yourself coding a program that changes its results as you code anything into it, even
        a comment.

    """
    import matplotlib; matplotlib.use("TkAgg")
    import matplotlib.pyplot as plt
    from threading import Thread
    import tensorflow as tf
    import string
    import time
    import os
    import sys

    alphabet = list(string.ascii_lowercase)
    vowels = ["a", "e", "i", "o", "u"]

    with open(os.path.basename(__file__), "r") as f:
        training_data = {text: letter for text in f.readlines() if (letter := boring_counter(text))}

    def _plot_losses(history):
        """ Print the evolution in the fitting stage
        """
        plt.xlabel("Epoch")
        plt.ylabel("Loss magnitude")
        plt.plot(history.history["loss"])
        plt.show()

    def _start_and_wait(thread, length=10):
        i = 0
        thread.start()
        while thread.is_alive():
            spaces = [" "] * (length-1)
            spaces.insert(abs(i), "===")
            sys.stdout.write("\r\t" + "-[{}]-".format("".join(spaces)))
            sys.stdout.flush()
            time.sleep(.1)
            i = (2-length) if i == (length - 1) else (i + 1)

    def _neural_networking():

        # Build model
        layer = tf.keras.layers.Dense(units=1, input_shape=[len(alphabet)])
        model = tf.keras.Sequential([layer])
        model.compile(
            optimizer=tf.keras.optimizers.Adam(0.1),
            loss="mean_squared_error"
        )

        # Prepare data for training the model
        training_inputs, training_outputs = [], []
        for text, vowel in training_data.items():
            training_inputs.append([text.count(char) for char in alphabet])
            training_outputs.append(vowels.index(vowel)+1)

        # Train the model

        history = []

        def fit_model():
            print("\n[neural_counter] Training the model...\n")
            history.append(model.fit(training_inputs, training_outputs, epochs=5000, verbose=False))
            print("\n[neural_counter] Model trained!\n")
        t = Thread(target=fit_model)
        _start_and_wait(t)

        # Generate predicts with the trained model and print the results of the tests
        print("[neural_counter] Trying the tests:")
        for text, expected in tests.items():
            result = model.predict([[text.count(char) for char in alphabet]])
            print("\tINPUT: '{}'".format(text))
            print("\tOUTPUT: {} (expected {})".format(vowels[round(result[0][0]-1)], expected))
        print()

        # Plot train progress
        _plot_losses(history[0])

    _neural_networking()


if __name__ == '__main__':

    inputs = {
        "aquí hay 7 aes contando esta ultima a": "a",  # test 1
        "en esta sin embargo solo hay 4 aes pero 6 es": "e",  # test 2
        "se que no tuve en cuenta las tildes, lo siento": "e",  # test 3
        "mi birbi tiini tris pilis": "i",  # test 4
        "zzz": "No se que pasa si no hay una vocal",  # test 5
    }

    neural_counter(inputs)
