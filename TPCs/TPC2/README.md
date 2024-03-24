---
Título: TPC2
Data: 28 de fevereiro de 2024
Autor: Robert Szabo
UC: SPLN
---

# Script que conta o número de palavras num texto

## Resumo

A script calcula a frequência de palavras num texto, apresentando o resultado no terminal, sendo este composto por uma lista de palavras desse texto com o respetivo número de ocorrências.
Contém duas flags:

Mostrar as 20 palavras mais comuns
``` 
-m 20
```
Ordenar alfabeticamente
```    
-n 
```

Capitalização preferencial
```
-c
```

Remove as palavras com frequência inferior a 2x a esperada
```
-f
```

## Estrutura do Projeto
```
.
├── README.md
├── pyproject.toml
├── dist
│   ├── wordfreq-0.1.0-py3-none-any.whl
│   └── wordfreq-0.1.0.tar.gz
├── data
│   ├── Camilo-Amor_de_Perdicao.md
│   └── formas.totalpt_utf8.txt
└── word_freq
    └── __init__.py
```

## Dependências
Para correr a script, é necessário ter o **python3** instalado.

```sh
sudo apt install python3
```
E configurar o projeto usando o comando:
```sh
flit build && flit install
```

## Instruções de execução
Para executar a script, deve-se correr o seguinte comando:
```sh
wfreq -f -c -m 20  data/Camilo-Amor_de_Perdicao.md
```

### Resultado
```
—   1427
Simão   363
;   335
?   322
eu   306
!   291
lhe   265
sua   248
seu   245
me   240
disse   240
...   238
Teresa   235
pai   213
Não   205
ela   200
ele   184
Mariana   167
minha   165
meu   144
```