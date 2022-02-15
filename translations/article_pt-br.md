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
