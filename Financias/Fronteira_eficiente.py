import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt



assets =["PG", "^GSPC"]
pf_data = pd.DataFrame()
for t in assets:
    pf_data[t] = wb.DataReader(t, data_source="yahoo", start="2010-01-01")["Adj Close"]
pf_data.tail()

#normalizar os graficos "PADRÃO"
(pf_data / pf_data.iloc[0] * 100).plot(figsize = (10,5))
plt.show()

#para obtermos uma fronteira eficiente desses 2 ativos precisamos do retornos logaritmos, da sua media anual e sua =>
#covariancia anualizada e as matrizes de correlação
log_returns = np.log(pf_data / pf_data.shift(1))
log_returns.mean() * 250
log_returns.cov() * 250
log_returns.corr()

#vamos obter uma otimizacao do portfloio criando uma variavel para contar o numero de ativos na carteira
#para que ela possa responder uma mudança no numero de ativos que compoem a carteira
num_assets = len(assets)
num_assets

#temos que criar 2 pesos aleatorios
arr = np.random.random(2)
arr
#somar os dois valores da celular para ver o resultado
arr[0] + arr[1]
#temos q rodar o random muitas vezes para conseguir achar um valor que some 1 para resolver isso vamos usar =>
#depois disso e incrementar a sessão de loops o sum para entender a sintaxe /= verificar na aula word.
#lembre-se weights e uma matriz q significa q a 2 linha do codigo nos transformamos os valores da nossa matriz
#W1/W1+W2 + W2/W1+w2 = W1+W2/W1+W2 = ficando igual a 1 olhando o word para entender.
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
weights[0] + weights[1]
#portanto lembre-se dessa cedula de preferencia o weights /= np.sum(weights) isso permite obter 2 pesos
#gerados aleatoriamente cuja soma sera igual a 1

#Expected Portfolio Return : retorno esperado de um portfolio 
#a formula e dada pela soma do produtos da média dos retorno logaritmos anualizados pelos respectivos preços
np.sum(weights * log_returns.mean()) * 250
#Expected Portfolio Variance
np.dot(weights.T, np.dot(log_returns.cov()* 250, weights))
#Expected Portfolio Volatility
np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()* 250, weights))) #passamos por essas 3 celulas pq precisamos =>
#da formula para o retorno e a volatilidade na simulacao de portfolio de minima varianca

#vamos criar um grafico onde 1000 simulações de minima varianca serão plotadas NOTA :>
#Nos não estamos considerando 1000 investimentos diferentes e =>
#SIM estamos considerando 1000 combinações diferentes dos mesmos ativos ! #olhar o word se quiser.
#a logica e o seguinte iremos fazer 2 portfolio e verificar qual o melhor 1%PG, 99%GSPC \e/ 99%PG, 1%GSPC 

#tende entender o raciocio que explica o fluxo das operações relacionadas, dissemos q o nosso objetivo e criar =>
#um grafico q mostra o retorno HIPOTETICO da carteira vs a volatilidade portanto precisaremos de dois objetos
#portanto precisaremos de 2 objetos para armazenar esses dados, assim o retornos do portfolio começa com uma lista vazia
#e pretendemos preenchê-la com retornos esperados aleatoriamente faremos a mesma coisa para a volatilidade
#precisaremos escrever um loop que sera repetido 1000 vezes. no corpo do loop vamos gerar aleatoriamente dois pesos
#onde a soma vai ser igual a 1 / precisamos de 2 pesos pq tem 2 ativos no portfolio se for mais tera mais pesos...
#depois disso a proxima celula e a chave do negocio "appende" que adicionara na nosta lista pfolio_returns cada valor
#de retorno do portfolio gerado aleatoriamente e essa operação sera repetida para cada passagem do loop ate que nossa lista
#pfolio_returns acumule 1000 observaçoes

pfolio_returns = []
pfolio_volatilities = []
for x in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250 )
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
pfolio_returns, pfolio_volatilities #vamos ver como ficou o retorno e vol do nosso portfolio.

#essas lista são dificieis de manipular o 3 segredo e como converter essas lista em array usando numpy.
#lembre-se quando for plotar a fronteira eficiente usar esse grande passo

pfolio_returns = []
pfolio_volatilities = []
for X in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

pfolio_returns, pfolio_volatilities

#trabalho pesado ja foi agora vamos completar o exercicio e ver o resultado do nosso trabalho
#1 vamos criar um objeto de dataframe contendo 2 colunas uma para o retornos e outra para vol
#vamos chamar esse objeto de portfolios seus dados vao ser composto por um dicionario com as chaves sendo Return e Volatility

portfolios = pd.DataFrame({"Return": pfolio_returns, "Volatility": pfolio_volatilities})
portfolios.head()
portfolios.tail()

#Parte final do exercicio agora vem a sintaxe do matplotlib a partir do DataFrame do portfolios vamos plotar um grafico
#com eixo X respondendo Volatility e Y = returns o grafico q queremos e dispersão "Scatter" e tbm e ajustar o tamanho
#do grafico 10, 6 / um grafico profissional tem rotulos signficativos para X e Y
portfolios.plot(x="Volatility", y="Return", kind="scatter", figsize=(10, 6));
plt.xlabel("Expected Volatility")
plt.ylabel("Expected Return")
plt.show()

