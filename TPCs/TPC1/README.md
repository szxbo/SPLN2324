---
Título: TPC1
Data: 20 de fevereiro de 2024
Autor: Robert Szabo
UC: SPLN
---

# Script que conta o número de palavras num texto

## Resumo

A script calcula a frequência de palavras num texto, escrevendo o resultado, para o ficheiro output.txt, sendo este composto por uma lista de palavras desse texto com o respetivo número de ocorrências
Contém duas flags:

Mostrar as 20 palavras mais comuns
``` 
-m 20
```
Ordenar alfabeticamente
```    
-n 
```

## Estrutura do Projeto
```
.
├── README.md
├── output.txt
├── wordfreq.py
└── data
    └── Camilo-Amor_de_Perdicao.md
```

## Dependências
Para correr a script, é necessário ter o **python3** instalado.

```sh
sudo apt install python3
```
E a biblioteca **jjcli** 
```sh
pip install jjcli
```

## Instruções de execução
Para executar a script, deve-se correr o seguinte comando:
```sh
python3 wordfreq.py -m 20 data/Camilo-Amor_de_Perdicao.md
```

### Resultado
```
4216 : ,
2465 : .
1835 : a
1723 : que
1657 : de
1387 : o
1320 : e
698 : não
673 : do
642 : da
464 : se
441 : com
424 : para
363 : Simão
346 : em
345 : ao
336 : ;
326 : os
325 : as
322 : ?
```
