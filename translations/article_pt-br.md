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
