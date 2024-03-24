#!/usr/bin/env python3

# Documentação que fica guardada na variável __doc__
'''
NAME
   word_freq - Calculates word frequency in a text

SYNOPSIS
   word_freq [options] input_files
   options: 
        -m 20 : Show 20 most common
        -n : Order alfabetically
        -c : Capitalization by reference
        -f : Remove words with frequency lower than 2x the expected

DESCRIPTION
    This program reads a text from a file or from the standard input and prints the frequency of each word in the text. 
    A word is a sequence of characters separated by spaces. It is case-insensitive. 
    The words are printed in descending order of frequency. 
    When two words have the same frequency, they are printed in alphabetical order.
    The program also has an option to capitalize the words by reference.

FILES
    https://linguateca.pt/acesso/tokens/formas.totalpt.txt -- reference ocurrences table
'''


from jjcli import * 
from collections import Counter # Dicionario chave - nº ocorrencias (multi-set)
import re

__version__ = "0.1.0"


def tokeniza(texto):
    palavras = re.findall(r"\w+(?:\-\w+)?",texto)
    pontuacao = re.findall(r"[;,.:!?_—]+",texto)
    print(f"Tem {len(palavras)} palavras e {len(pontuacao)} sinais")
    return palavras + pontuacao


def imprime(lista, opt):
    if opt == 'm':
        for palavra, n_ocorr in lista:
            print(f"{palavra}   {n_ocorr}")
    elif opt == 'n':
        for palavra, n_ocorr in lista:
            print(f"{n_ocorr}   {palavra}")
    
    
def capital_pref(ocorr):
    for palavra, n1 in ocorr.items():
        if 'A' <= palavra[0] <= 'Z':
            n2 = 0
            if palavra[0].isupper():
                palavra_mod = palavra.lower()
                if palavra_mod in ocorr:
                    n2 = ocorr[palavra_mod]
            else:
                palavra_mod = palavra[0].upper() + palavra[1:]
                if palavra_mod in ocorr:
                    n2 = ocorr[palavra_mod]

            if n1 > n2:
                ocorr[palavra] += n2
                ocorr[palavra_mod] = 0
            else:
                ocorr[palavra_mod] += n1
                ocorr[palavra] = 0

    ocorr = {key: value for key, value in ocorr.items() if value != 0}
    return ocorr


def main():
    # "-m" recebe um argumento logo leva ":", ao contrário de "-n"
    cl=clfilter("f:cnm:", doc=__doc__)     ## option values in cl.opt dictionary

    for txt in cl.text():     ## process one file at the time
        lista_palavras = tokeniza(txt)
        ocorr = Counter(lista_palavras)
        
        # se "-c" estiver presente, capitalizar as palavras
        if "-c" in cl.opt:
            lista_palavras.sort()
            ocorr = capital_pref(Counter(lista_palavras))
            imprime(ocorr.items(), 'n')
            
        # se "-f" estiver presente, eliminar palavras com frequência inferior a 2x a esperada
        if "-f" in cl.opt:
            eliminar = []
            
            with open("data/formas.totalpt_utf8.txt") as f:
                frequenciesRatio = {}
                totalFreq = 0
                
                # ler o ficheiro e por as frequências no dicionário
                for line in f.readlines():
                    frequency,word = line.split("\t")
                    totalFreq += int(frequency)
                    frequenciesRatio[word[:-1]] = int(frequency)

            # normalizar as frequências (frequência/total de palavras no texto)
            for word,frequency in frequenciesRatio.items():
                frequenciesRatio[word] = frequency/totalFreq
                    
            # total de palavras no texto
            total_frequency = sum(ocorr.values())
            # iterar sobre as palavras e verificar a frequência
            for elem,n in ocorr.items():
                if elem in frequenciesRatio:
                    ratio = (n/total_frequency)/frequenciesRatio[elem]
                    # ratio < 2 -> a palavra aparece menos de 2x do que o esperado
                    if ratio<2:
                        # se a palavra estiver no dicionário de frequências, adicionar à lista de eliminação
                        if elem in frequenciesRatio:
                            eliminar.append(elem)
            # remover as palavras da lista de eliminação
            for elem in eliminar:
                ocorr.pop(elem)

        # se "-n" estiver presente, ordenar alfabeticamente
        if "-n" in cl.opt:
            lista_palavras.sort()
            ocorr = Counter(lista_palavras)
            imprime(ocorr.items(), 'n')
                
        # se "-m" estiver presente, mostrar as "m" palavras mais comuns
        if "-m" in cl.opt:
            imprime(ocorr.most_common(int(cl.opt.get("-m"))), 'm')
            
        # se "-m" não estiver presente, mostrar todas as palavras
        else:
            imprime(ocorr.items(), 'm')