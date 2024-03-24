#!/usr/bin/python3
# __doc__ é a primeira string num documento python, neste caso da linha 2 a 13
'''
NAME
    wordfreq - Calculates word frequency in a text

SYNOPSIS
    wordfreq [options] input_files
    options:
        -m 20 : Show 20 most common words
        -n : Order alphabeticaly

DESCRIPTION
    This program reads a text from a file or from the standard input and prints the frequency of each word in the text. 
    A word is a sequence of characters separated by spaces. It is case-insensitive. 
    The words are printed in descending order of frequency. 
    When two words have the same frequency, they are printed in alphabetical order. 
    
    The program accepts the following options:
        -n : orders the words alphabetically
        -m : shows only the m most common words
        
    If the option -m is not given, all the words are printed. If the input file is not given, the program reads from the standard input.
    The output is a list of words followed by the respective frequency, one word per line.

EXAMPLES
    wordfreq text.txt
    wordfreq -n text.txt
    wordfreq -m 20 text.txt
    wordfreq -m 20 -n text.txt
    wordfreq < text.txt
    wordfreq -n < text.txt
    wordfreq -m 20 < text.txt
    wordfreq -m 20 -n < text.txt
'''


from jjcli import *
from collections import Counter # Dicionario chave - nº ocorrencias (multi-set)
import re


cl = clfilter("nm:", doc=__doc__)


def tokenize(texto):
    palavras = re.findall(r'\w+(?:-\w+)?|[\;\,\.\:\!\?\_\-]+',texto)
    # (?: ...) agrupa mas não captura
    print("O texto tem " + str(len(palavras))+ " palavras.")
    return palavras


for txt in cl.text():
    lista_palavras = tokenize(txt)
    ocorr = Counter(lista_palavras)
    listCounter = list(ocorr.items())
    flag=False
    
    if "-n" in cl.opt:
        listCounter.sort()
    else:
        flag=True
        listCounter.sort(key = lambda a: -a[1])
        
    if "-m" in cl.opt:
        with open("output.txt","w") as f:
            for word,frequency in listCounter[:int(cl.opt.get("-m"))]:
                if flag:
                    f.write(f"{frequency} : {word}\n")
                else:
                    f.write(f"{word} : {frequency}\n")
    else:
        with open("output.txt","w") as f:
            for word,frequency in listCounter:
                if flag:
                    f.write(f"{frequency} : {word}\n")
                else:
                    f.write(f"{word} : {frequency}\n")

'''
ADICIONAR AO PATH:
```bash
chmod 755 word_freq.py
cp word_freq.py /home/[user]/.local/bin/word_freq
```
'''

        
