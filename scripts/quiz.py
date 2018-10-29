import pandas as pd
import numpy  as np
import os

df = pd.read_csv("../files/translate_words.csv")
df = df[["Words","Translate"]]

clear = lambda: os.system('clear')

def quiz(df):
    rs = set()
    r = np.random.randint(df.shape[0])
    str_quiz = ""
    str_answers = ""
    for _ in range(10):
        while r in rs:
            r = np.random.randint(df.shape[0])
        rs.add(r)
        str_quiz += df["Words"].iloc[r] + "\n"
        l = len(df["Words"].iloc[r])
        if   l < 4:
            tab = "\t\t\t\t"
        elif l < 8:
            tab = "\t\t\t"
        else :
            tab = "\t\t"

        str_answers += df["Words"].iloc[r] + tab + df["Translate"].iloc[r] + "\n"
    print (str_quiz)
    input("Для ответов нажите enter")
    clear()
    print (str_answers)

if __name__ == '__main__':
    quiz(df)
