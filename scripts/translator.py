import re
import requests
import json
import pandas as pd

class Translator(object):

    def __init__(self, api_token):
        self.api_token = api_token

    
    def translate_words(self, dict_words):
        
        translate_words = []
        for word in dict_words:
            link = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=' + self.api_token + \
                   '&lang=en-ru&text=' + word + '&flags=4'
            error_count = 0
            while True:
                try:
                    response = requests.get(link, timeout=10)
                    translate = json.loads(response.text)
                    break
                except requests.exceptions.ReadTimeout as to_error:
                    error_count += 1
                    print(word + " " + to_error)
                    if error_count == 10:
                        translate = None
                        break
            try:
                word_tr = translate['def'][0]['tr'][0]['text']
            except IndexError:
                word_tr = "none"
            translate_words.append(word_tr)
        return translate_words



if __name__ == '__main__':
    token = "dict.1.1.20181028T224749Z.ff6adfed02abf4c6.c0abbf12efc1c7a63a447bc3d1f999c17aa1baa8"
    df = pd.read_table("../files/words.txt")
    
    translator = Translator(token)
    dict_of_translate_words = translator.translate_words(list(df.iloc[:,0]))
    df["Translate"] = dict_of_translate_words
    df.to_csv("translate_words.csv")

