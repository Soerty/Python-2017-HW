#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import json




class Word(object):
    def __init__(self, **values):
        vars(self).update(values)




def get_wordform(**values):
    return values['text']



def get_frequency_parsing(*analysis):
    return len(*analysis)



def get_the_most_frequent_lemma(*lemms):
    freq_dict = {}
    lemma, freq = None, 0

    for i in lemms[0]:
        freq_dict[i] = temp = freq_dict.get(i, 0)+1
        if temp > freq:
            lemma, freq = i, temp

    return lemma



def get_most_freq_part_of_speech(*values):
    return get_the_most_frequent_lemma(*values)



if __name__ == '__main__':
    words = []

    with open('python_mystem.json') as file:
        for line in file:
            line = json.loads(line.replace('\n', ''))

            if 'analysis' in line:
                analysis = line['analysis']
                lemms = [i['lex'] for i in analysis]
                speechs = [i['gr'].replace('=', ',').split(',')[0] for i in analysis]

                words.append(Word(
                    wordform = get_wordform(**line),
                    freq_parsing = get_frequency_parsing(analysis),
                    most_freq_lemma = get_the_most_frequent_lemma(lemms),
                    most_freq_part_of_speech = get_most_freq_part_of_speech(speechs)
                ))
    
    for word in words:
        print (word.__dict__)