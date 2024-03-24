---
Título: TPC5
Data: 15 de março de 2024
Autor: Robert Szabo
UC: SPLN
---


## Resumo
O código carrega o modelo de processamento de linguagem natural "pt_core_news_lg" do spacy e realiza o processamento de um texto em português. 

De seguida, são mapeadas as diferentes partes do discurso e é gerada uma tabela em Markdown com as palavras, os seus tipos e lemas respetivos. 


## Dependências
Para correr a script, é necessário ter o **python3** instalado.

```sh
sudo apt install python3
```
A bibliteca **spacy**:
```sh
pip install spacy
```
E o pacote **pt_core_news_lg** do spacy:
```sh
python -m spacy download pt_core_news_lg
```
## Instruções de execução
Para executar a script, deve-se correr o seguinte comando:
```sh
python3 parseTexto.py > resultado.md
```

### Resultado
Para a frase "O Roberto e a Roberta foram passear a Viana do Castelo e deixaram a porta aberta. A gata deles, a Alberta, fugiu."

| Palavra | Tipo | Lema |
|----|--------|----|
| O | determinante | o |
| Roberto  | nome próprio | Roberto  |
| e | conjunção coordenativa | e |
| a | determinante | o |
| Roberta  | nome próprio | Roberta  |
| foram | auxiliar | ir |
| passear | verbo | passear |
| a | determinante | o |
| Viana do Castelo  | nome próprio | Viana do Castelo  |
| e | conjunção coordenativa | e |
| deixaram | verbo | deixar |
| a | determinante | o |
| porta | nome | porta |
| aberta | verbo | abrir |
| A | determinante | o |
| gata | nome | gata |
| deles | pronome | de eles |
| a | determinante | o |
| Alberta | nome próprio | Alberta |
| fugiu | verbo | fugir |