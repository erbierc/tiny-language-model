import kagglehub
import pandas as pd
import string
from multiprocessing import Pool
import os

def cleanUp(poem):
    poem = poem.lower()
    poem = poem.strip()
    poem = poem.replace("\r\n", "")
    poem = poem.translate(str.maketrans('', '', string.punctuation + "“”‘’—"))
    poem = poem.split()
    return poem

def getPoems():
    path = kagglehub.dataset_download("tgdivy/poetry-foundation-poems")

    df = pd.read_csv(path + "/PoetryFoundationData.csv", encoding='utf8')
    poems_col = df.Poem
    return poems_col

def getWords(poems):
    pool = Pool(os.cpu_count())
    results = pool.map(cleanUp, poems)
    pool.close()
    pool.join()

    words = []
    for arr in results:
        words.extend(arr)

    return words