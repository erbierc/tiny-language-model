import string
import kagglehub
import pandas as pd
import numpy as np
from multiprocessing import Pool
import os

def cleanUp(poem):
    poem = poem.lower()
    poem = poem.strip()
    poem = poem.replace("\r\n", "")
    poem = poem.translate(str.maketrans('', '', string.punctuation + "“”‘’—–"))
    poem = poem.split()
    return poem

if __name__ == "__main__":
    path = kagglehub.dataset_download("tgdivy/poetry-foundation-poems")

    df = pd.read_csv(path + "/PoetryFoundationData.csv", encoding='utf8')
    poems_col = df.Poem
    words = []

    pool = Pool(os.cpu_count())
    results = pool.map(cleanUp, poems_col)
    pool.close()
    pool.join()

    for arr in results:
        words.extend(arr)

    d = {}

    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    l = len(words)

    for word in d:
        d[word] = d[word]/l
        
    words = list(d.keys())
    probabilities = list(d.values())

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