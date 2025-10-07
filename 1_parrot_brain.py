import numpy as np
from collections import Counter
from utils import getPoems, getWords


if __name__ == "__main__":

    poems = getPoems()

    words = getWords(poems)

    d = Counter(words)
    l = len(words)

    probabilities = [count/l for count in d.values()]
    words = list(d.keys())

    rng = np.random.default_rng()
    words = rng.choice(words, size=100, p=probabilities)

    with open("poem.txt", "w", encoding="utf8") as text_file:
        line_break = np.random.randint(8, 11)
        counter = 1
        for word in words:
            text_file.write(word + " ")
            if counter == line_break:
                text_file.write("\n")
                counter = 1
                line_break = np.random.randint(8, 11)
            counter+=1