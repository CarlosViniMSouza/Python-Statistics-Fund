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

Nas estatísticas, a **população** é um conjunto de todos os elementos ou itens nos quais você está interessado. As populações geralmente são vastas, o que as torna inadequadas para coletar e analisar dados. É por isso que os estatísticos geralmente tentam tirar algumas conclusões sobre uma população escolhendo e examinando um subconjunto representativo dessa população.

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
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

print(x_list)
# Output: [8.0, 1, 2.5, 4, 28.0]

print(x_with_nan)
# Output: [8.0, 1, 2.5, nan, 4, 28.0]
```

Agora você tem as listas `x_list` e `x_with_nan`. Eles são quase os mesmos, com a diferença de que x_with_nan contém um valor nan. É importante entender o comportamento das rotinas de estatísticas do Python quando elas se deparam com um [valor não numérico (nan)](https://en.wikipedia.org/wiki/NaN). Na ciência de dados, os valores ausentes são comuns e você geralmente os substitui por `nan`.

> **Nota**: Como você obtém um valor nan?
> 
> Em Python, você pode usar qualquer um dos seguintes:
> 
>   ° float('nan')
>   ° math.nan
>   ° np.nan
> 
> Você pode usar todas essas funções de forma intercambiável:
> 
> ```python
> math.isnan(np.nan), np.isnan(math.nan)
> # output: (True, True)
> 
> math.isnan(y_with_nan[3]), np.isnan(y_with_nan[3])
> # output: (True, True)
> ```
> 
> Você pode ver que as funções são todas equivalentes. No entanto, lembre-se de que comparar dois valores `nan` para igualdade retorna `False`. Em outras palavras, `math.nan == math.nan` é `False`!

Agora, crie objetos np.ndarray e pd.Series que correspondam a x e x_with_nan:

```python
y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
y
# Output: array([ 8. ,  1. ,  2.5, 4. , 28. ])

print(y_with_nan)
# Output: array([ 8. ,  1. ,  2.5,  nan,  4. , 28. ])

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

print(z_with_nan)
"""
Output: 

0     8.0
1     1.0
2     2.5
3     NaN
4     4.0
5    28.0
dtype: float64
"""
```

Agora você tem dois arrays NumPy (y e y_with_nan) e dois Pandas Series (`z e z_with_nan`). Todos estes são sequências 1D de valores.

> **NOTA**: embora você use [listas](https://realpython.com/python-lists-tuples/) ao longo deste tutorial, lembre-se de que, na maioria dos casos, você pode usar [tuplas](https://realpython.com/python-lists-tuples/) da mesma maneira.

Você pode opcionalmente especificar um rótulo para cada valor em `z e z_with_nan`.

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

No entanto, se houver valores nan entre seus dados, `statistics.mean()` e `statistics.fmean()` retornará nan como saída:

```python
mean = statistics.mean(x_with_nan)
print(mean)
# output: nan

mean = statistics.fmean(x_with_nan)
print(mean)
# output: nan
```

Este resultado é consistente com o comportamento de sum(), porque sum(x_with_nan) também retorna `nan`.

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

A função `mean()` e o método `.mean()` de NumPy retornam o mesmo resultado que `statistics.mean()`. Este também é o caso quando há valores nan entre seus dados:

```python
print(np.mean(y_with_nan))
# output: nan

print(y_with_nan.mean())
# output: nan
```

Muitas vezes, você não precisa obter um valor `nan` como resultado. Se você preferir ignorar os valores `nan`, então você pode usar [`np.nanmean()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanmean.html):

```python
print(np.nanmean(y_with_nan))
# output: 8.7
```

`nanmean()` simplesmente ignora todos os valores `nan`. Ele retorna o mesmo valor que `mean()` se você o aplicasse ao conjunto de dados sem os valores `nan`.

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

Você pode implementar a média ponderada em Python puro combinando `sum()` com [range()](https://realpython.com/courses/python-range-function/) ou [zip()](https://realpython.com/python-zip-function/):

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

No entanto, tenha cuidado se seu conjunto de dados contiver valores `nan`:

```python
w = np.array([0.1, 0.2, 0.3, 0.0, 0.2, 0.1])
print((w * y_with_nan).sum() / w.sum())
# output: nan

print(np.average(y_with_nan, weights=w))
# output: nan

print(np.average(z_with_nan, weights=w))
# output: nan
```
Nesse caso, `average()` retorna `nan`, que é consistente com `np.mean()`.

## Média Harmônica:

A **média harmônica** é a recíproca da média das recíprocas de todos os itens no conjunto de dados: 𝑛 / Σᵢ(1/𝑥ᵢ), onde 𝑖 = 1, 2, …, 𝑛 e 𝑛 é o número de itens no conjunto de dados 𝑥. Uma variante da implementação Python pura da média harmônica é esta:

```python
h_mean = len(x) / sum(1 / item for item in x)
print(h_mean)
# output: 2.7613412228796843
```

O exemplo acima mostra uma implementação de `statistics.harmonic_mean()`. Se você tiver um valor `nan` em um conjunto de dados, ele retornará `nan`. Se houver pelo menos um 0, ele retornará 0. Se você fornecer pelo menos um número negativo, receberá [statistics.StatisticsError](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError):

```python
statistics.harmonic_mean(x_with_nan)
# output: nan

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

Novamente, esta é uma implementação bastante simples. No entanto, se seu conjunto de dados contiver nan, 0, um número negativo ou qualquer coisa menos números [positivos](https://realpython.com/python-numbers/), você receberá um [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)!

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

Se você passar dados com valores nan, então `statistics.geometric_mean()` se comportará como a maioria das funções semelhantes e retornará `nan`:

```python
g_mean = statistics.geometric_mean(x_with_nan)
print(g_mean)
# output: nan
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

Se você tiver valores nan em um conjunto de dados, `gmean()` retornará nan. Se houver pelo menos um 0, ele retornará 0.0 e dará um aviso. Se você fornecer pelo menos um número negativo, receberá nan e o aviso.

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

`statistics.mode()` e `statistics.multimode()` tratam valores nan como valores regulares e podem retornar nan como o valor modal:

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

## Medidas de Variabilidade

As medidas de tendência central não são suficientes para descrever os dados. Você também precisará das **medidas de variabilidade** que quantificam a dispersão dos pontos de dados. Nesta seção, você aprenderá como identificar e calcular as seguintes medidas de variabilidade:

° Variação
° Desvio padrão
° Distorção
° Percentis
° Gamas

### Variação

A **variância da amostra** quantifica a dispersão dos dados. Mostra numericamente a que distância os pontos de dados estão da média. Você pode expressar a variância amostral do conjunto de dados 𝑥 com elementos 𝑛 matematicamente como 𝑠² = Σᵢ(𝑥ᵢ − média(𝑥))² / (𝑛 − 1), onde 𝑖 = 1, 2, …, 𝑛 e média(𝑥) é a média amostral de 𝑥. Se você quiser entender mais profundamente por que você divide a soma com 𝑛 − 1 em vez de 𝑛, então você pode se aprofundar na [correção de Bessel](https://en.wikipedia.org/wiki/Bessel%27s_correction).

A figura a seguir mostra por que é importante considerar a variação ao descrever conjuntos de dados:

![img1](https://files.realpython.com/media/py-stats-06.2cafb41d561e.png)

Há dois conjuntos de dados nesta figura:

1. **Pontos verdes**: este conjunto de dados tem uma variância menor ou uma diferença média menor em relação à média. Ele também tem um intervalo menor ou uma diferença menor entre o maior e o menor item.
2. **Pontos brancos**: este conjunto de dados tem uma variância maior ou uma diferença média maior em relação à média. Ele também tem um alcance maior ou uma diferença maior entre o maior e o menor item.

Observe que esses dois conjuntos de dados têm a mesma média e mediana, embora pareçam diferir significativamente. Nem a média nem a mediana podem descrever essa diferença. É por isso que você precisa das medidas de variabilidade.

Veja como você pode calcular a variação da amostra com Python puro:

```python
n = len(x)
mean = sum(x) / n
var = sum((item - mean) ** 2 for item in x) / (n - 1)
print(var)
# output: 123.19999999999999
```

Essa abordagem é suficiente e calcula bem a variância da amostra. No entanto, a solução mais curta e elegante é chamar a função existente [statistics.variance()](https://docs.python.org/3/library/statistics.html#statistics.variance):

```python
var = statistics.variance(x)
print(var)
# output: 123.2
```

Você obteve o mesmo resultado para a variância acima. `variance()` pode evitar calcular a média se você fornecer a média explicitamente como o segundo argumento: `statistics.variance(x, mean_)`.

Se você tiver valores nan entre seus dados, `statistics.variance()` retornará `nan`:

```python
print(statistics.variance(x_with_nan))
# output: nan
```

É muito importante especificar o parâmetro ddof=1. É assim que você define os [graus de liberdade delta](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)) para 1. Este parâmetro permite o cálculo adequado de 𝑠², com (𝑛 − 1) no denominador em vez de 𝑛.

Se você tiver valores nan no conjunto de dados, `np.var()` e `.var()` retornarão `nan`:

```python
print(np.var(y_with_nan, ddof=1))
# output: nan

print(y_with_nan.var(ddof=1))
# output: nan
```

Isso é consistente com np.mean() e np.average(). Se você quiser pular os valores nan, então você deve usar np.nanvar():

```python
print(np.nanvar(y_with_nan, ddof=1))
# output: 123.19999999999999
```

`np.nanvar()` ignora valores `nan`. Ele também precisa que você especifique `ddof=1`.

Você calcula a **variação da população** de forma semelhante à variação da amostra. No entanto, você deve usar 𝑛 no denominador em vez de 𝑛 − 1: Σᵢ(𝑥ᵢ − mean(𝑥))² / 𝑛. Neste caso, 𝑛 é o número de itens em toda a população. Você pode obter a variação da população semelhante à variação da amostra, com as seguintes diferenças:

° `Substituir` (n - 1) com n na implementação Python pura.
° `Use` [statistics.pvariance()](https://docs.python.org/3/library/statistics.html#statistics.pvariance) em vez de `statistics.variance()`.
° `Especifique` o parâmetro ddof=0 se você usar NumPy ou Pandas. No NumPy, você pode omitir ddof porque seu valor padrão é 0.

Observe que você deve sempre estar ciente se está trabalhando com uma amostra ou com toda a população sempre que estiver calculando a variância!

### Desvio padrão

O **desvio padrão da amostra** é outra medida de dispersão de dados. Está ligado à variância da amostra, pois o desvio padrão, 𝑠, é a raiz quadrada positiva da variância da amostra. O desvio padrão geralmente é mais conveniente do que a variância porque tem a mesma unidade dos pontos de dados. Depois de obter a variação, você pode calcular o desvio padrão com Python puro:

```python
std = var ** 0.5
print(std)
# output: 11.099549540409285
```

Embora esta solução funcione, você também pode usar [statistics.stdev()](https://docs.python.org/3/library/statistics.html#statistics.stdev):

```python
std = statistics.stdev(x)
print(std)
# output: 11.099549540409287
```

Claro, o resultado é o mesmo de antes. Assim como `variance()`, `stdev()` não calcula a média se você a fornecer explicitamente como o segundo argumento: `statistics.stdev(x, mean_)`.

Você pode obter o desvio padrão com o NumPy quase da mesma maneira. Você pode usar a função std() e o método correspondente .std() para calcular o desvio padrão. Se houver valores nan no conjunto de dados, eles retornarão nan. Para ignorar valores nan, você deve usar np.nanstd(). Você usa std(), .std(), e nanstd() do NumPy como você usaria var(), .var() e nanvar():

```python
print(np.std(y, ddof=1))
# output: 11.099549540409285

print(y.std(ddof=1))
# output: 11.099549540409285

print(np.std(y_with_nan, ddof=1))
# output: nan

print(y_with_nan.std(ddof=1))
# output: nan

print(np.nanstd(y_with_nan, ddof=1))
# output: 11.099549540409285
```

Não se esqueça de definir os graus de liberdade delta para 1!

Os objetos `pd.Series` também possuem o método .std() que pula nan por padrão:

```python
print(z.std(ddof=1))
# output: 11.099549540409285

print(z_with_nan.std(ddof=1))
# output: 11.099549540409285
```

O parâmetro `ddof` é padronizado como 1, então você pode omiti-lo. Novamente, se você quiser tratar os valores `nan` de maneira diferente, aplique o parâmetro `skipna`.

O `desvio padrão da população` refere-se a toda a população. É a raiz quadrada positiva da variância da população. Você pode calculá-lo assim como o desvio padrão da amostra,
com as seguintes diferenças:

° **Encontre** a raiz quadrada da variância da população na implementação do Python puro.
° **Use** [statistics.pstdev()](https://docs.python.org/3/library/statistics.html#statistics.pstdev) em vez de `statistics.stdev()`.
° **Especifique** o parâmetro `ddof=0` se você usar NumPy ou Pandas. No NumPy, você pode omitir `ddof` porque seu valor padrão é 0.

### Distorção

A assimetria da amostra mede a assimetria de uma amostra de dados.

Existem várias definições matemáticas de assimetria. Uma expressão comum para calcular a assimetria do conjunto de dados 𝑥 com elementos 𝑛 é (𝑛² / ((𝑛 − 1)(𝑛 − 2))) (Σᵢ(𝑥ᵢ − mean(𝑥))³ / (𝑛𝑠³)). Uma expressão mais simples é Σᵢ(𝑥ᵢ − média(𝑥))³ 𝑛 / ((𝑛 − 1)(𝑛 − 2)𝑠³), onde 𝑖 = 1, 2, …, 𝑛 e média(𝑥) é a média amostral de 𝑥. A assimetria definida assim é chamada de **coeficiente de momento padronizado de Fisher-Pearson ajustado**.

A figura anterior mostrou dois conjuntos de dados bastante simétricos. Em outras palavras, seus pontos tinham distâncias semelhantes da média. Em contraste, a imagem a seguir ilustra dois conjuntos assimétricos:

![img1](https://files.realpython.com/media/py-stats-07.92abf9f362b0.png)

O primeiro conjunto é representado pelos pontos verdes e o segundo pelos brancos. Normalmente, **valores de assimetria negativos** indicam que há uma cauda dominante no lado esquerdo, que você pode ver com o primeiro conjunto. Os **valores de assimetria positivos** correspondem a uma cauda mais longa ou mais gorda no lado direito, que você pode ver no segundo conjunto. Se a assimetria estiver próxima de 0 (por exemplo, entre -0,5 e 0,5), o conjunto de dados será considerado bastante simétrico.

Depois de calcular o tamanho do seu conjunto de dados n, a média da amostra `mean_` e o desvio padrão std_, você pode obter a assimetria da amostra com Python puro:

```python
x = [8.0, 1, 2.5, 4, 28.0]
n = len(x)

mean = sum(x) / n
var = sum((item - mean)**2 for item in x) / (n - 1)
std = var ** 0.5
skew = (sum((item - mean)**3 for item in x) * n / ((n - 1) * (n - 2) * std ** 3))

print(skew)
# output: 1.9470432273905929
```

A assimetria é positiva, então x tem uma cauda do lado direito.

Você também pode calcular a assimetria da amostra com [scipy.stats.skew()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skew.html)

```python
y, y_with_nan = np.array(x), np.array(x_with_nan)

print(scipy.stats.skew(y, bias=False))
# output: 1.9470432273905927

print(scipy.stats.skew(y_with_nan, bias=False))
# output: nan
```

O resultado obtido é o mesmo da implementação Python pura. O `viés` do parâmetro é definido como `Falso` para habilitar as correções para viés estatístico. O parâmetro opcional `nan_policy` pode assumir os valores `'propagate', 'raise'` ou `'omit'`. Ele permite que você controle como lidará com os valores `nan`.

Os objetos da `série` Pandas têm o método [.skew()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.skew.html) que também retorna a assimetria de um conjunto de dados:

```python
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)

print(z.skew())
# output: 1.9470432273905924

print(z_with_nan.skew())
# output: 1.9470432273905924
```

Como outros métodos, `.skew()` ignora os valores `nan` por padrão, devido ao valor padrão do parâmetro opcional `skipna`.

### Percentis

O **percentil 𝑝 da amostra** é o elemento no conjunto de dados tal que 𝑝% dos elementos no conjunto de dados são menores ou iguais a esse valor. Além disso, (100 − 𝑝)% dos elementos são maiores ou iguais a esse valor. Se houver dois desses elementos no conjunto de dados, o percentil 𝑝 da amostra é sua média aritmética. Cada conjunto de dados tem três **quartis**, que são os percentis que dividem o conjunto de dados em quatro partes:

> ° **O primeiro quartil** é o percentil 25 da amostra. Ele divide aproximadamente 25% dos menores itens do restante do conjunto de dados.
> 
> ° **O segundo quartil** é o percentil 50 da amostra ou a mediana. Aproximadamente 25% dos itens situam-se entre o primeiro e o segundo quartis e outros 25% entre o segundo e o terceiro quartis.
> 
> ° **O terceiro quartil** é o percentil 75 da amostra. Ele divide aproximadamente 25% dos maiores itens do restante do conjunto de dados.

Cada parte tem aproximadamente o mesmo número de itens. Se você quiser dividir seus dados em vários intervalos, você pode usar [statistics.quantiles()](https://docs.python.org/3/library/statistics.html#statistics.quantiles):

```python
x = [-5.0, -1.1, 0.1, 2.0, 8.0, 12.8, 21.0, 25.8, 41.0]

print(statistics.quantiles(x, n=2))
# output: [8.0]

print(statistics.quantiles(x, n=4, method="inclusive"))
# output: [0.1, 8.0, 21.0]
```

Neste exemplo, 8.0 é a mediana de x, enquanto 0.1 e 21.0 são os percentis 25 e 75 da amostra, respectivamente. O parâmetro n define o número de percentis de igual probabilidade resultantes e o método determina como calculá-los.

Você também pode usar [np.percentile()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.percentile.html) para determinar qualquer percentil de amostra em seu conjunto de dados. Por exemplo, é assim que você pode encontrar os percentis 5 e 95:

```python
y = np.array(x)

print(np.percentile(y, 5))
# output: -3.44

print(np.percentile(y, 95))
# output: 34.919999999999995
```

`percentile()` recebe vários argumentos. Você precisa fornecer o conjunto de dados como o primeiro argumento e o valor do percentil como o segundo. O conjunto de dados pode estar na forma de uma matriz NumPy, lista, tupla ou estrutura de dados semelhante. O percentil pode ser um número entre 0 e 100 como no exemplo acima, mas também pode ser uma sequência de números:

```python
print(np.percentile(y, [25, 50, 75]))
# output: array([0.1, 8. , 21. ])

print(np.median(y))
# output: 8.0
```

Este código calcula os percentis 25, 50 e 75 de uma só vez. Se o valor do percentil for uma sequência, percentile() retornará uma matriz NumPy com os resultados. A primeira instrução retorna a matriz de quartis. A segunda instrução retorna a mediana, para que você possa confirmar que é igual ao percentil 50, que é 8.0 .

Se você quiser ignorar os valores nan, use [np.nanpercentile()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanpercentile.html) em vez disso:

```python
y_with_nan = np.insert(y, 2, np.nan)

print(y_with_nan)
# output: array([-5. , -1.1,  nan,  0.1,  2. ,  8. , 12.8, 21. , 25.8, 41. ])

print(np.nanpercentile(y_with_nan, [25, 20, 75]))
# output: array([ 0.1,  8. , 21. ])
```

É assim que você pode evitar valores nan.

O NumPy também oferece funcionalidades muito semelhantes em [quantile()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.quantile.html) e [nanquantile()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanquantile.html). Se você os usar, precisará fornecer os valores de quantil como números entre 0 e 1 em vez de percentis:

```python
print(np.quantile(y, 0.05))
# output: -3.44

print(np.percentile(y, 0.95))
# output: 34.919999999999995

print(np.quantile(y, [0.25, 0.5, 0.75]))
# output: array([0.1, 8. , 21. ])

print(np.nanquantile(y_with_nan, [0.25, 0.5, 0.75]))
```

Os resultados são os mesmos dos exemplos anteriores, mas aqui seus argumentos estão entre 0 e 1. Em outras palavras, você passou 0,05 em vez de 5 e 0,95 em vez de 95.

Os objetos `pd.Series` possuem o método [.quantile()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.quantile.html):

```python
z, z_with_nan = pd.Series(y), pd.Series(y_with_nan)

print(z.quantile(0.05))
# output: -3.44

print(z.quantile(0.95))
# output: 34.919999999999995

print(z.quantile([0.25, 0.5, 0.75]))
# output:
# 0.25     0.1
# 0.50     8.0
# 0.75    21.0
# dtype: float64

print(z_with_nan.quantile([0.25, 0.5, 0.75]))
# output:
# 0.25     0.1
# 0.50     8.0
# 0.75    21.0
# dtype: float64
```

`.quantile()` também precisa que você forneça o valor do quantil como argumento. Esse valor pode ser um número entre 0 e 1 ou uma sequência de números. No primeiro caso, `.quantile()` retorna um escalar. No segundo caso, retorna uma nova `Série` contendo os resultados.

### Gamas

O **intervalo de dados** é a diferença entre o elemento máximo e mínimo no conjunto de dados. Você pode obtê-lo com a função [np.ptp()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ptp.html):

```python
print(np.ptp(y))
# output: 46.0

print(np.ptp(z))
# output: 46.0

print(np.ptp(y_with_nan))
# output: nan

print(np.ptp(z_with_nan))
# output: 46.0
```

Esta função retorna nan se houver valores nan em sua matriz NumPy. Se você usar um objeto `Pandas Series`, ele retornará um número.

Como alternativa, você pode usar funções e métodos internos do Python, NumPy ou Pandas para calcular os máximos e mínimos de sequências:

> ° [.max()](https://docs.python.org/3/library/functions.html#max) e [.min()](https://docs.python.org/3/library/functions.html#min) da biblioteca padrão do Python
> 
> ° [.amax()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.amax.html) e [.amin()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.amin.html) do NumPy
> 
> ° [.nanmax()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanmax.html) e [.nanmin()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanmin.html) do NumPy para ignorar os valores nan
> 
> ° [.max()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.max.html) e [.min()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.min.html) do NumPy
> 
> ° [.max()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.max.html) e [.min()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.min.html) do Pandas para ignorar os valores nan por padrão

Aqui estão alguns exemplos de como você usaria essas rotinas:

```python
print(np.amax(y) - np.amin(y))
# output: 46.0

print(np.nanmax(y_with_nan) - np.nanmin(y_with_nan))
# output: 46.0

print(y.max() - y.min())
# output: 46.0

print(z.max() - z.min())
# output: 46.0

print(z_with_nan.max() - z_with_nan.min())
# output: 46.0
```

É assim que você obtém o intervalo de dados.

## Resumo das Estatísticas Descritivas

SciPy e Pandas oferecem rotinas úteis para obter estatísticas descritivas rapidamente com uma única função ou chamada de método. Você pode usar [scipy.stats.describe()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.describe.html) assim:

Você precisa fornecer o conjunto de dados como o primeiro argumento. O argumento pode ser uma matriz NumPy, lista, tupla ou estrutura de dados semelhante. Você pode omitir `ddof=1`, pois é o padrão e só importa quando você está calculando a variação. Você pode passar `bias=False` para forçar a correção da assimetria e [curtose](https://en.wikipedia.org/wiki/Kurtosis) para viés estatístico.

> **Nota**: O parâmetro opcional `nan_policy` pode assumir os valores `'propagate'` (padrão), `'raise'` (um erro) ou `'omit'`. Este parâmetro permite controlar o que está acontecendo quando há valores `nan`.

`describe()` retorna um objeto que contém as seguintes estatísticas descritivas:

> ° **nobs**: the number of observations or elements in your dataset
> 
> ° **minmax**: the tuple with the minimum and maximum values of your dataset
> 
> ° **mean**: the mean of your dataset
> 
> ° **variance**: the variance of your dataset
> 
> ° **skewness**: the skewness of your dataset
> 
> ° **kurtosis**: the kurtosis of your dataset

Você pode acessar valores específicos com notação de ponto:

```python
print(result.nobs())
# output: 9

print(result.minmax[0])
# output: -5.0

print(result.minmax[1])
# output: 41.0

print(result.mean)
# output: 11.622222222222222

print(result.variance)
# output: 228.75194444444446

print(result.skewness)
# output: 0.9249043136685094

print(result.kurtosis)
# output: 0.14770623629658886
```

Com o SciPy, você está a apenas uma chamada de função de um resumo de estatísticas descritivas para seu conjunto de dados.

Pandas tem funcionalidade semelhante, se não melhor. `Objetos de série` têm o método [.describe()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.describe.html):

```python
result = z.describe()

print(result)
"""
output:

count     9.000000
mean     11.622222
std      15.124548
min      -5.000000
25%       0.100000
50%       8.000000
75%      21.000000
max      41.000000
dtype: float64
"""
```

Ele retorna uma nova série que contém o seguinte:

> ° **contagem**: o número de elementos em seu conjunto de dados
> 
> ° **mean**: a média do seu conjunto de dados
> 
> ° **std**: o desvio padrão do seu conjunto de dados
> 
> ° **min e max**: os valores mínimo e máximo do seu conjunto de dados
> 
> ° **25%, 50% e 75%**: os quartis do seu conjunto de dados

## Medidas de correlação entre pares de dados

Muitas vezes, você precisará examinar a relação entre os elementos correspondentes de duas variáveis em um conjunto de dados. Digamos que existam duas variáveis, 𝑥 e 𝑦, com um número igual de elementos, 𝑛. Deixe 𝑥₁ de 𝑥 corresponder a 𝑦₁ de 𝑦, 𝑥₂ de 𝑥 a 𝑦₂ de 𝑦 e assim por diante.
Você pode então dizer que existem 𝑛 pares de elementos correspondentes: (𝑥₁, 𝑦₁), (𝑥₂, 𝑦₂), e assim por diante.

Você verá as seguintes **medidas de correlação** entre pares de dados:

> ° **Correlação Positiva** existe quando valores maiores de 𝑥 correspondem a valores maiores de 𝑦 e vice-versa.
> ° Existe **Correlação Negativa** quando valores maiores de 𝑥 correspondem a valores menores de 𝑦 e vice-versa.
> ° **Fraca ou nenhuma Correlação** existe se não houver tal relação aparente.

A figura a seguir mostra exemplos de correlação negativa, fraca e positiva:

![img1](https://files.realpython.com/media/py-stats-08.5a1e9f3e3aa4.png)

O gráfico à esquerda com os pontos vermelhos mostra correlação negativa. O gráfico no meio com os pontos verdes mostra correlação fraca. Por fim, o gráfico à direita com os pontos azuis mostra correlação positiva.

> **Nota**: Há uma coisa importante que você deve sempre ter em mente ao trabalhar com correlação entre um par de variáveis, e é que a **correlação não é uma medida ou indicador de causalidade**, mas apenas de associação!

As duas estatísticas que medem a correlação entre conjuntos de dados são a **covariância** e o **coeficiente de correlação**. Vamos definir alguns dados para trabalhar com essas medidas. Você criará duas listas Python e as usará para obter matrizes NumPy correspondentes e séries Pandas:

```python
x = list(range(-10, 11))
y = [0, 2, 2, 2, 2, 3, 3, 6, 7, 4, 7, 6, 6, 9, 4, 5, 5, 10, 11, 12, 14]
x1, y1 = np.array(x), np.array(y)
x2, y2 = pd.Series(x1), pd.Series(y1)
```

Agora que você tem as duas variáveis, pode começar a explorar a relação entre elas.