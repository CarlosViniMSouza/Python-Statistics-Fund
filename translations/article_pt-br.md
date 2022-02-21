# Entendendo as Estatísticas Descritivas

A **estatística descritiva** trata de descrever e resumir dados. Ele usa duas abordagens principais:

> **A abordagem quantitativa** descreve e resume os dados numericamente.
>
> **A abordagem visual** ilustra dados com gráficos, gráficos, histogramas e outros gráficos.

Você pode aplicar estatísticas descritivas a um ou vários conjuntos de dados ou [variáveis](https://realpython.com/python-variables/). Quando você descreve e resume uma única variável, está realizando uma **análise univariada**. Ao pesquisar relacionamentos estatísticos entre um par de variáveis, você está fazendo uma **análise bivariada**. Similarmente, uma **análise multivariada** está preocupada com múltiplas variáveis ao mesmo tempo.

### Tipos de Medidas:

Neste tutorial, você aprenderá sobre os seguintes tipos de medidas em estatísticas descritivas:

° A **Tendência Central** informa sobre os centros dos dados. Medidas úteis incluem a média, mediana e moda.

° A **Variabilidade** informa sobre a disseminação dos dados. Medidas úteis incluem variância e desvio padrão.

° A **Correlação ou Variabilidade Conjunta** informa sobre a relação entre um par de variáveis em um conjunto de dados. Medidas úteis incluem a covariância e o [coeficiente de correlação](https://realpython.com/numpy-scipy-pandas-correlation-python/).

Você aprenderá a entender e calcular essas medidas com Python.

### População e Amostras:

Nas estatísticas, a **população** é um conjunto de todos os elementos ou itens nos quais você está interessado. As populações geralmente são vastas, o que as torna inadequadas para coletar e analisar dados. É por isso que os estatísticos geralmente tentam tirar algumas conclusões sobre uma população escolhendo e exami`nan`do um subconjunto representativo dessa população.

Esse subconjunto de uma população é chamado de **amostra**. Idealmente, a amostra deve preservar as características estatísticas essenciais da população de forma satisfatória. Dessa maneira, você poderá usar a amostra para obter conclusões sobre a população.

### Outlier(Atípicos):

Um **outlier** é um ponto de dados que difere significativamente da maioria dos dados obtidos de uma amostra ou população. Existem muitas causas possíveis de discrepâncias, mas aqui estão algumas para você começar:

° **Variação natural** nos dados

° **Mudança** no comportamento do sistema observado

° **Erros** na coleta de dados

Erros de coleta de dados são uma causa particularmente proeminente de discrepâncias. Por exemplo, as limitações dos instrumentos ou procedimentos de medição podem significar que os dados corretos simplesmente não podem ser obtidos. Outros erros podem ser causados por erros de cálculo, contaminação de dados, erro humano e muito mais.

Não há uma definição matemática precisa de outliers. Você precisa confiar na experiência, no conhecimento sobre o assunto de interesse e no bom senso para determinar se um ponto de dados é um valor discrepante e como lidar com isso.

## Escolhendo Bibliotecas de Estatísticas Python:

Existem muitas bibliotecas de estatísticas Python para você trabalhar, mas neste tutorial, você aprenderá sobre algumas das mais populares e amplamente usadas:

° A [**statistics**](https://docs.python.org/3/library/statistics.html) do Python são uma biblioteca interna do Python para estatísticas descritivas. Você pode usá-lo se seus conjuntos de dados não forem muito grandes ou se não puder contar com a importação de outras bibliotecas.

° [**NumPy**](https://docs.scipy.org/doc/numpy/user/index.html) é uma biblioteca de terceiros para computação numérica, otimizada para trabalhar com matrizes unidimensionais e multidimensionais. Seu tipo primário é o tipo de array chamado [ndarray](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html). Esta biblioteca contém muitas [rotinas](https://docs.scipy.org/doc/numpy/reference/routines.statistics.html) para análise estatística.

° [**SciPy**](https://www.scipy.org/getting-started.html) é uma biblioteca de terceiros para computação científica baseada em NumPy. Ele oferece funcionalidade adicional em comparação ao NumPy, incluindo [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) para análise estatística.

° [**Pandas**](https://pandas.pydata.org/pandas-docs/stable/) é uma biblioteca de terceiros para computação numérica baseada em NumPy. Ele se destaca no manuseio de dados rotulados unidimensionais (1D) com objetos [Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) e dois dados dimensionais (2D) com objetos [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

° [**Matplotlib**](https://matplotlib.org/) é uma biblioteca de terceiros para visualização de dados. Funciona bem em combinação com NumPy, SciPy e Pandas.

Observe que, em muitos casos, objetos Series e [DataFrame](https://realpython.com/pandas-dataframe/) podem ser usados no lugar de arrays NumPy. Muitas vezes, você pode simplesmente passá-los para uma função estatística NumPy ou [SciPy](https://realpython.com/python-scipy-cluster-optimize/). Além disso, você pode obter os dados não rotulados de um Series ou DataFrame como um objeto np.ndarray chamando [.values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.values.html) ou [.to_numpy()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html).

## Introdução às bibliotecas de estatísticas do Python:

A biblioteca de `estatísticas` embutida do Python possui um número relativamente pequeno das funções estatísticas mais importantes. A [documentação oficial](https://docs.python.org/3/library/statistics.html) é um recurso valioso para encontrar os detalhes. Se você está limitado ao Python puro, a biblioteca de `estatísticas` do Python pode ser a escolha certa.

Um bom lugar para começar a aprender sobre o NumPy é o [Guia do Usuário](https://docs.scipy.org/doc/numpy/user/index.html) oficial, especialmente as seções de [início rápido](https://docs.scipy.org/doc/numpy/user/quickstart.html) e [básico](https://docs.scipy.org/doc/numpy/user/basics.html). A [referência oficial](https://docs.scipy.org/doc/numpy/reference/) pode ajudá-lo a refrescar sua memória em conceitos específicos do NumPy. Enquanto você lê este tutorial, você pode querer verificar a seção de [estatísticas](https://docs.scipy.org/doc/numpy/reference/routines.statistics.html) e a [referência oficial do scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) também.

> **Obs**:
> 
> Para saber mais sobre o NumPy, confira estes recursos:
> 
>   ° [Look Ma, sem For-Loops: programação de matrizes com NumPy](https://realpython.com/numpy-array-programming/)
>   ° [Limpeza de dados Pythonic com Pandas e NumPy](https://realpython.com/python-data-cleaning-numpy-pandas/)
>   ° [NumPy arange(): Como usar np.arange()](https://realpython.com/how-to-use-numpy-arange/)

Se você quiser aprender Pandas, a [página oficial de Introdução](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html) é um excelente lugar para começar. A [introdução às estruturas de dados](https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html) pode ajudá-lo a aprender sobre os tipos de dados fundamentais, `Series` e `DataFrame`. Da mesma forma, o excelente [tutorial introdutório oficial](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html) visa fornecer informações suficientes para começar a usar efetivamente o Pandas na prática.

> **Obs**:
> 
> Para saber mais sobre o Pandas, confira estes recursos:
> 
>   ° [Usando Pandas e Python para explorar seu conjunto de dados](https://realpython.com/pandas-python-explore-dataset/)
>   ° [Pandas DataFrames 101](https://realpython.com/courses/pandas-dataframes-101/)
>   ° [Pandas idiomáticos: truques e recursos que você talvez não conheça](https://realpython.com/courses/idiomatic-pandas-tricks-features-you-may-not-know/)
>   ° [Rápido, flexível, fácil e intuitivo: como acelerar seus projetos de pandas](https://realpython.com/fast-flexible-pandas/)

O `matplotlib` possui um [Guia do Usuário oficial](https://matplotlib.org/users/index.html) abrangente que você pode usar para mergulhar nos detalhes do uso da biblioteca. [Anatomia do Matplotlib](https://github.com/matplotlib/AnatomyOfMatplotlib) é um excelente recurso para iniciantes que desejam começar a trabalhar com o `matplotlib` e suas bibliotecas relacionadas.

> Obs:
> 
> Para saber mais sobre visualização de dados, confira estes recursos:
> 
>   ° [Python Plotando com Matplotlib (Guia)](https://realpython.com/python-matplotlib-guide/)
>   ° [Plotagem de histograma Python: NumPy, Matplotlib, Pandas e Seaborn](https://realpython.com/python-histograms/)
>   ° [Visualização de dados interativa em Python com Bokeh](https://realpython.com/python-data-visualization-bokeh/)
>   ° [Plot com Pandas: Visualização de Dados Python para Iniciantes](https://realpython.com/pandas-plot-python/)

Vamos começar a usar essas bibliotecas de estatísticas do Python!

## Calculando Estatísticas Descritivas:

Comece importando todos os pacotes que você vai precisar:

```python
import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
```

Estes são todos os pacotes que você precisará para cálculos de estatísticas do Python. Normalmente, você não usará o pacote `matemático` integrado do Python, mas será útil neste tutorial. Mais tarde, você importará `matplotlib.pyplot` para visualização de dados.

Vamos criar alguns dados para trabalhar. Você começará com listas Python que contêm alguns dados numéricos arbitrários:

```python
x_list = [8.0, 1, 2.5, 4, 28.0]
x_with_`nan` = [8.0, 1, 2.5, math.`nan`, 4, 28.0]

print(x_list)
# Output: [8.0, 1, 2.5, 4, 28.0]

print(x_with_`nan`)
# Output: [8.0, 1, 2.5, `nan`, 4, 28.0]
```

Agora você tem as listas `x_list` e `x_with_`nan``. Eles são quase os mesmos, com a diferença de que x_with_`nan` contém um valor `nan`. É importante entender o comportamento das rotinas de estatísticas do Python quando elas se deparam com um [valor não numérico (`nan`)](https://en.wikipedia.org/wiki/`NaN`). Na ciência de dados, os valores ausentes são comuns e você geralmente os substitui por ``nan``.

> **Nota**: Como você obtém um valor `nan`?
> 
> Em Python, você pode usar qualquer um dos seguintes:
> 
>   ° float('`nan`')
>   ° math.`nan`
>   ° np.`nan`
> 
> Você pode usar todas essas funções de forma intercambiável:
> 
> ```python
> math.is`nan`(np.`nan`), np.is`nan`(math.`nan`)
> # output: (True, True)
> 
> math.is`nan`(y_with_`nan`[3]), np.is`nan`(y_with_`nan`[3])
> # output: (True, True)
> ```
> 
> Você pode ver que as funções são todas equivalentes. No entanto, lembre-se de que comparar dois valores ``nan`` para igualdade retorna `False`. Em outras palavras, `math.`nan` == math.`nan`` é `False`!

Agora, crie objetos np.ndarray e pd.Series que correspondam a x e x_with_`nan`:

```python
y, y_with_`nan` = np.array(x), np.array(x_with_`nan`)
z, z_with_`nan` = pd.Series(x), pd.Series(x_with_`nan`)
y
# Output: array([ 8. ,  1. ,  2.5, 4. , 28. ])

print(y_with_`nan`)
# Output: array([ 8. ,  1. ,  2.5,  `nan`,  4. , 28. ])

print(z)
"""
Output: 

0     8.0
1     1.0
2     2.5
3     4.0
4    28.0
dtype: float64
"""

print(z_with_`nan`)
"""
Output: 

0     8.0
1     1.0
2     2.5
3     `NaN`
4     4.0
5    28.0
dtype: float64
"""
```

Agora você tem dois arrays NumPy (y e y_with_`nan`) e dois Pandas Series (`z e z_with_`nan``). Todos estes são sequências 1D de valores.

> **NOTA**: embora você use [listas](https://realpython.com/python-lists-tuples/) ao longo deste tutorial, lembre-se de que, na maioria dos casos, você pode usar [tuplas](https://realpython.com/python-lists-tuples/) da mesma maneira.

Você pode opcionalmente especificar um rótulo para cada valor em `z e z_with_`nan``.

### Medidas de tendência central:

As medidas de tendência central mostram os valores centrais ou médios dos conjuntos de dados. Existem várias definições do que é considerado o centro de um conjunto de dados. Neste tutorial, você aprenderá a identificar e calcular essas medidas de tendência central:

>   ° Significar
>   ° Média ponderada
>   ° Média geométrica
>   ° média harmônica
>   ° Mediana
>   ° Modo

° Significar

A **média amostral**, também chamada de **média aritmética amostral** ou simplesmente **média**, é a média aritmética de todos os itens em um conjunto de dados. A média de um conjunto de dados 𝑥 é expressa matematicamente como `Σᵢ𝑥ᵢ/𝑛`, onde `𝑖 = 1, 2, …, 𝑛`. Em outras palavras, é a soma de todos os elementos `𝑥ᵢ` dividido pelo número de itens no conjunto de dados 𝑥.

Esta figura ilustra a média de uma amostra com cinco pontos de dados:

![img1](https://files.realpython.com/media/py-stats-01.3254dbfe6b9a.png)

Os pontos verdes representam os pontos de dados 1, 2,5, 4, 8 e 28. A linha tracejada vermelha é a média, ou (1 + 2,5 + 4 + 8 + 28) / 5 = 8,7.

Você pode calcular a média com Python puro usando [sum()](https://docs.python.org/3/library/functions.html#sum) e [len()](https://docs.python.org/3/library/functions.html#len), sem importar bibliotecas:

```python
import statistics

mean = sum(x_list) / len(x_list)
print(mean)
# output: 8.7
```

Embora isso seja limpo e elegante, você também pode aplicar funções estatísticas internas do Python:

```python
mean = statistics.mean(x_list)
print(mean)
# output: 8.7

mean = statistics.fmean(x_list)
print(mean)
# output: 8.7
```

Você chamou as funções [mean()](https://docs.python.org/3/library/statistics.html#statistics.mean) e [fmean()](https://docs.python.org/3/library/statistics.html#statistics.fmean) da biblioteca de `estatísticas` interna do Python e obteve o mesmo resultado que obteve com o Python puro. `fmean()` é introduzido no [Python 3.8](https://realpython.com/python38-new-features/) como uma alternativa mais rápida para `mean()`. Ele sempre retorna um número de ponto flutuante.

No entanto, se houver valores `nan` entre seus dados, `statistics.mean()` e `statistics.fmean()` retornará `nan` como saída:

```python
mean = statistics.mean(x_with_`nan`)
print(mean)
# output: `nan`

mean = statistics.fmean(x_with_`nan`)
print(mean)
# output: `nan`
```

Este resultado é consistente com o comportamento de sum(), porque sum(x_with_`nan`) também retorna ``nan``.

Se você usar o NumPy, poderá obter a média com [np.mean()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html):

```python
mean = np.mean(y)
print(mean)
# output: 8.7
```

No exemplo acima, mean() é uma função, mas você também pode usar o método correspondente [.mean()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.mean.html):

```python
mean = y.mean()
print(mean)
# output: 8.7
```

A função `mean()` e o método `.mean()` de NumPy retornam o mesmo resultado que `statistics.mean()`. Este também é o caso quando há valores `nan` entre seus dados:

```python
print(np.mean(y_with_`nan`))
# output: `nan`

print(y_with_`nan`.mean())
# output: `nan`
```

Muitas vezes, você não precisa obter um valor ``nan`` como resultado. Se você preferir ignorar os valores ``nan``, então você pode usar [`np.`nan`mean()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.`nan`mean.html):

```python
print(np.`nan`mean(y_with_`nan`))
# output: 8.7
```

``nan`mean()` simplesmente ignora todos os valores ``nan``. Ele retorna o mesmo valor que `mean()` se você o aplicasse ao conjunto de dados sem os valores ``nan``.

## Média Ponderada

A **média ponderada**, também chamada de **média aritmética ponderada** ou **média ponderada**, é uma generalização da média aritmética que permite definir a contribuição relativa de cada ponto de dados para o resultado.

Você define um **peso 𝑤ᵢ** para cada ponto de dados 𝑥ᵢ do conjunto de dados 𝑥, onde 𝑖 = 1, 2, …, 𝑛 e 𝑛 é o número de itens em 𝑥. Em seguida, você multiplica cada ponto de dados pelo peso correspondente, soma todos os produtos e divide a soma obtida pela soma dos pesos: Σᵢ(𝑤ᵢ𝑥ᵢ) / Σᵢ𝑤ᵢ.

> **Nota**: É conveniente (e geralmente o caso) que todos os pesos sejam **não negativos**, 𝑤ᵢ ≥ 0, e que sua soma seja igual a um, ou Σᵢ𝑤ᵢ = 1.

A média ponderada é muito útil quando você precisa da média de um conjunto de dados contendo itens que ocorrem com determinadas frequências relativas. Por exemplo, digamos que você tenha um conjunto no qual 20% de todos os itens sejam iguais a 2, 50% dos itens sejam iguais a 4 e os 30% restantes dos itens sejam iguais a 8. Você pode calcular a média de um conjunto como este:

```python
print(0.2 * 2 + 0.5 * 4 + 0.3 * 8)
# output: 4.8
```

Aqui, você leva em consideração as frequências com os pesos. Com esse método, você não precisa saber o número total de itens.

Você pode implementar a média ponderada em Python puro combi`nan`do `sum()` com [range()](https://realpython.com/courses/python-range-function/) ou [zip()](https://realpython.com/python-zip-function/):

```python
x = [8.0, 1, 2.5, 4, 28.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]

w_mean = sum(w[i] * x[i] for i in range(len(x))) / sum(w)
print(w_mean)

# Other way:
w_mean = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w)
print(w_mean)
```
Novamente, esta é uma implementação limpa e elegante onde você não precisa importar nenhuma biblioteca.

No entanto, se você tiver grandes conjuntos de dados, o NumPy provavelmente fornecerá uma solução melhor. Você pode usar [np.average()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.average.html) para obter a média ponderada de arrays NumPy ou Pandas `Series`:

```python
w, y, z = np.array(w), np.array(x), pd.Series(x)
w_mean = np.average(y, weights=w)
print(w_mean)
# output: 6.95

w_mean = np.average(z, weights=w)
print(w_mean)
# output: 6.95
```
O resultado é o mesmo que no caso da implementação pura do Python. Você também pode usar esse método em listas e tuplas comuns.

Outra solução é usar o produto elementar `w * y` com [np.sum()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html) ou [.sum()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.sum.html):

```python
print((w * y).sum() / w.sum())
# output: 6.95
```

É isso! Você calculou a média ponderada.

No entanto, tenha cuidado se seu conjunto de dados contiver valores ``nan``:

```python
w = np.array([0.1, 0.2, 0.3, 0.0, 0.2, 0.1])
print((w * y_with_`nan`).sum() / w.sum())
# output: `nan`

print(np.average(y_with_`nan`, weights=w))
# output: `nan`

print(np.average(z_with_`nan`, weights=w))
# output: `nan`
```
Nesse caso, `average()` retorna ``nan``, que é consistente com `np.mean()`.

## Média Harmônica:

A **média harmônica** é a recíproca da média das recíprocas de todos os itens no conjunto de dados: 𝑛 / Σᵢ(1/𝑥ᵢ), onde 𝑖 = 1, 2, …, 𝑛 e 𝑛 é o número de itens no conjunto de dados 𝑥. Uma variante da implementação Python pura da média harmônica é esta:

```python
h_mean = len(x) / sum(1 / item for item in x)
print(h_mean)
# output: 2.7613412228796843
```

O exemplo acima mostra uma implementação de `statistics.harmonic_mean()`. Se você tiver um valor ``nan`` em um conjunto de dados, ele retornará ``nan``. Se houver pelo menos um 0, ele retornará 0. Se você fornecer pelo menos um número negativo, receberá [statistics.StatisticsError](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError):

```python
statistics.harmonic_mean(x_with_`nan`)
# output: `nan`

statistics.harmonic_mean([1, 0, 2])
# output: 0

statistics.harmonic_mean([1, 0, -2])
# output: Raises StatisticsError
```

Lembre-se desses três cenários ao usar esse método!

Uma terceira maneira de calcular a média harmônica é usar [scipy.stats.hmean()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hmean.html):

```python
scipy.stats.hmean(y)
# output: 2.7613412228796843

scipy.stats.hmean(z)
# output: 2.7613412228796843
```

Novamente, esta é uma implementação bastante simples. No entanto, se seu conjunto de dados contiver `nan`, 0, um número negativo ou qualquer coisa menos números [positivos](https://realpython.com/python-numbers/), você receberá um [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)!

## Média Geométrica:

A **média geométrica** é a 𝑛-ésima raiz do produto de todos os 𝑛 elementos 𝑥ᵢ em um conjunto de dados 𝑥: ⁿ√(Πᵢ𝑥ᵢ), onde 𝑖 = 1, 2, …, 𝑛. A figura a seguir ilustra as médias aritméticas, harmônicas e geométricas de um conjunto de dados:

![img1](https://files.realpython.com/media/py-stats-02.ec1ca0f9a9ac.png)

Novamente, os pontos verdes representam os pontos de dados 1, 2,5, 4, 8 e 28. A linha tracejada vermelha é a média. A linha tracejada azul é a média harmônica e a linha tracejada amarela é a média geométrica.

Você pode implementar a média geométrica em Python puro assim:

```python
g_mean = 1
for item in x:
  g_mean *= item

g_mean **= 1 / len(x)
print(g_mean)
# output: 4.677885674856041
```

Como você pode ver, o valor da média geométrica, neste caso, difere significativamente dos valores das médias aritmética (8,7) e harmônica (2,76) para o mesmo conjunto de dados x.

O Python 3.8 introduziu [statistics.geometric_mean()](https://docs.python.org/3/library/statistics.html#statistics.geometric_mean), que converte todos os valores em números de ponto flutuante e retorna sua média geométrica:

```python
g_mean = statistics.geometric_mean(x)
print(g_mean)
# output: 4.67788567485604
```

Você obteve o mesmo resultado do exemplo anterior, mas com um erro mínimo de arredondamento.

Se você passar dados com valores `nan`, então `statistics.geometric_mean()` se comportará como a maioria das funções semelhantes e retornará ``nan``:

```python
g_mean = statistics.geometric_mean(x_with_`nan`)
print(g_mean)
# output: `nan`
```

De fato, isso é consistente com o comportamento de `statistics.mean()`, `statistics.fmean()` e `statistics.harmonic_mean()`. Se houver um número zero ou negativo entre seus dados, `statistics.geometric_mean()` aumentará o `statistics.StatisticsError`.

Você também pode obter a média geométrica com `scipy.stats.gmean()`:

```python
print(scipy.stats.gmean(y))
# output: 4.67788567485604
print(scipy.stats.gmean(z))
# output: 4.67788567485604
```

Você obteve o mesmo resultado com a implementação pura do Python.

Se você tiver valores `nan` em um conjunto de dados, `gmean()` retornará `nan`. Se houver pelo menos um 0, ele retornará 0.0 e dará um aviso. Se você fornecer pelo menos um número negativo, receberá `nan` e o aviso.

## Mediana

A **mediana da amostra** é o elemento central de um conjunto de dados classificado. O conjunto de dados pode ser classificado em ordem crescente ou decrescente. Se o número de elementos 𝑛 do conjunto de dados for ímpar, então a mediana é o valor na posição do meio: 0,5(𝑛 + 1). Se 𝑛 for par, então a mediana é a média aritmética dos dois valores no meio, ou seja,
os itens nas posições 0,5𝑛 e 0,5𝑛 + 1.

Por exemplo, se você tiver os pontos de dados 2, 4, 1, 8 e 9, o valor mediano será 4, que está no meio do conjunto de dados classificado (1, 2, 4, 8, 9). Se os pontos de dados são 2, 4, 1 e 8, então a mediana é 3, que é a média dos dois elementos centrais da sequência ordenada (2 e 4). A figura a seguir ilustra isso:

![img1](https://files.realpython.com/media/py-stats-04.f7b39a21dd2d.png)

Os pontos de dados são os pontos verdes e as linhas roxas mostram a mediana para cada conjunto de dados. O valor médio do conjunto de dados superior (1, 2.5, 4, 8 e 28) é 4. Se você remover o valor discrepante 28 do conjunto de dados inferior, a mediana se tornará a média aritmética entre 2.5 e 4, que é 3.25.

A figura abaixo mostra a média e a mediana dos pontos de dados 1, 2.5, 4, 8 e 28:

![img2](https://files.realpython.com/media/py-stats-03.33356e86aa97.png)

Novamente, a média é a linha tracejada vermelha, enquanto a mediana é a linha roxa.

A principal diferença entre o comportamento da média e da mediana está relacionada aos **outliers** ou **extremos** do conjunto de dados. A média é fortemente afetada por outliers, mas a mediana depende apenas de outliers ligeiramente ou nada. Considere a figura a seguir:

![img3](https://files.realpython.com/media/py-stats-05.b5c3dba0cd5f.png)

O conjunto de dados superior novamente tem os itens 1, 2.5, 4, 8 e 28. Sua média é 8.7 e a mediana é 5, como você viu anteriormente. O conjunto de dados inferior mostra o que está acontecendo quando você move o ponto mais à direita com o valor 28:

> ° **Se você aumentar seu valor (movê-lo para a direita)**, a média aumentará, mas o valor mediano nunca mudará.
> 
> ° **Se você diminuir seu valor (movê-lo para a esquerda)**, a média cairá, mas a mediana permanecerá a mesma até que o valor do ponto móvel seja maior ou igual a 4.

Você pode comparar a média e a mediana como uma maneira de detectar discrepâncias e assimetria em seus dados. Se o valor médio ou o valor mediano é mais útil para você depende do contexto do seu problema específico.

Aqui está uma das muitas implementações Python puras possíveis da mediana:

```python 
n = len(x)
if n % 2:
    median = sorted(x)[round(0.5 * (n - 1))]
else:
    x_ord, index = sorted(x), round(0.5 * n)
    median = 0.5 * (x_ord[index - 1] + x_ord[index])

print(median)
# output: 4
```

Duas etapas mais importantes dessa implementação são as seguintes:

1. **Classificando** os elementos do conjunto de dados
2. **Encontrando** o(s) elemento(s) intermediário(s) no conjunto de dados classificado

Você pode obter a mediana com [statistics.median()](https://docs.python.org/3/library/statistics.html#statistics.median):

```python
median = statistics.median(x)
print(median)
# output: 4

median = statistics.median(x[:-1])
print(median)
# output: 3.25
```

A versão ordenada de `x` é `[1, 2.5, 4, 8.0, 28.0]`, então o elemento no meio é 4. A versão ordenada de x[:-1], que é x sem o último item 28.0, é `[1 , 2.5, 4, 8.0]`. Agora, existem dois elementos do meio, 2.5 e 4. Sua média é 3.25.

[median_low()](https://docs.python.org/3/library/statistics.html#statistics.median_low) e [median_high()](https://docs.python.org/3/library/statistics.html#statistics.median_high) são mais duas funções relacionadas à mediana na biblioteca de estatísticas do Python. Eles sempre retornam um elemento do conjunto de dados:

> ° **Se o número de elementos for ímpar**, então há um único valor médio, então essas funções se comportam como `median()`.
> 
> ° **Se o número de elementos for par**, então existem dois valores médios. Nesse caso, `median_low()` retorna o valor médio mais baixo e `median_high()` o valor médio mais alto.

Você pode usar essas funções da mesma forma que usaria median():

```python
statistics.median_low(x[:-1])
# output: 2.5

statistics.median_low(x[:-1])
# output: 4
```

Os objetos da `série Pandas` têm o método [.median()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.median.html) que ignora os valores nan por padrão:

```python
print(z.median())
# output: 4.0

print(z_with_nan.median())
# output: 4.0
```

O comportamento de `.median()` é consistente com `.mean()` em Pandas. Você pode alterar esse comportamento com o parâmetro opcional `skipna`.

## Moda

O **modo de amostra** é o valor no conjunto de dados que ocorre com mais frequência. Se não houver um único valor desse tipo, o conjunto será **multimodal**, pois possui vários valores modais. Por exemplo, no conjunto que contém os pontos 2, 3, 2, 8 e 12, o número 2 é a moda porque ocorre duas vezes, ao contrário dos demais itens que ocorrem apenas uma vez.

É assim que você pode obter o modo com Python puro:

```python
sample = [2, 3, 2, 8, 12]

sample2 = [12, 15, 12, 15, 21, 15, 12]

mode = max((sample.count(item), item) for item in set(sample))[1]
print(mode)
# output: 2
```

Você usa `sample.count()` para obter o número de ocorrências de cada item em sample. O item com o número máximo de ocorrências é a moda. Observe que você não precisa usar `set(sample)`. Em vez disso, você pode substituí-lo por apenas u e iterar em toda a lista.

> **Nota:** `set(sample)` retorna um [conjunto](https://realpython.com/python-sets/) Python com todos os itens exclusivos em sample. Você pode usar esse truque para otimizar o trabalho com dados maiores, especialmente quando espera ver muitas duplicatas.

Você pode obter o modo com [statistics.mode()](https://docs.python.org/3/library/statistics.html#statistics.mode) e [statistics.multimode()](https://docs.python.org/3/library/statistics.html#statistics.multimode):

```python
mode = statistics.mode(sample)
print(mode)
# output:

mode = statistics.multimode(sample)
print(mode)
# output: [2]
```

Você deve prestar atenção especial a esse cenário e ter cuidado ao escolher entre essas duas funções.

`statistics.mode()` e `statistics.multimode()` tratam valores `nan` como valores regulares e podem retornar `nan` como o valor modal:

```python
statistics.mode([2, math.nan, 2])
# output: 2

statistics.multimode([2, math.nan, 2])
# output: [2]

statistics.mode([2, math.nan, 0, math.nan, 5])
# output: nan

statistics.multimode([2, math.nan, 0, math.nan, 5])
# output: [nan]
```

> **Nota**: `statistics.multimode()` é introduzido no [Python 3.8](https://realpython.com/courses/cool-new-features-python-38/).

Os objetos Pandas Series têm o método .mode() que trata bem os valores multimodais e ignora os valores nan por padrão:

```python
u, v, w = pd.Series(sample), pd.Series(sample2), pd.Series([2, 2, math.nan])

print(u.mode())
# output:
# 0    2
# dtype: int64

print(v.mode())
# output:
# 0    12
# 1    15
# dtype: int64

print(w.mode())
# output:
# 0    2.0
# dtype: float64
```

Como você pode ver, `.mode()` retorna um novo `pd.Series` que contém todos os valores modais. Se você quiser que `.mode()` leve em consideração os valores nan, então apenas passe o argumento opcional `dropna=False`.
