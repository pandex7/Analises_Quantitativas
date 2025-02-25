import numpy as np
import pandas as pd 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 
from scipy.stats import norm

ticker = ["PG"]
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source="yahoo", start="2007-1-1")["Adj Close"]

log_returns = np.log(1 + data.pct_change()) #pct_change é o retorno simples a partir de uma base de dados.

log_returns.tail()

data.plot(figsize=(10,6));
plt.show()

log_returns.plot(figsize= (10, 6))
plt.show()

u = log_returns.mean()
u

var = log_returns.var()
var

#agora vamos usar o Drift melhor aproximação das taxas futuras de retorno de uma ação olhar o WORD
#u = retorno log média - metade de sua variançia

drift = u - (0.5 * var)
drift
#os numeros são pequenos pq nós não vamos anualizar esses dados, esse e o retorno diario q queremos achar. "prever"
#movimento browniado e o r = drift + stdev * e R
#achamos o STDEV agora falta o restante... 
stdev = log_returns.std()
stdev


type(drift)
type(stdev)

np.array(drift) # SE vc usar o object.values vc transfere o objeto para uma array numpy
drift.values 
stdev.values #fornecendo um valor analogo e nos permite obter o desvio padrão.

#segundo componente do movimento browniado e uma variavel aleatoria "Z" correspondente a distância entre a média e os
#eventos, expresso pelo número de desvios padrão,  (utilize norm.pff(scipy)) se o evento tem 95% de chance de ocorrer
norm.ppf(0.95) # então a distancia e a média sera o resultado 1,64% desvio padrão
#para complementar o segundo componente precisamos usar de numero aleatorio usamemores o rand.
X = np.random.rand(10, 2)
X
#vmao incluir esse elemento aleatorio dentro do ppf para saber distancia da média correspondente a cada uma dessa probalibilidade
#geradas automaticamente / o 1 numero da 1 linha corresponde a 1 probabilidade da 1 linha da matriz X e o segundo
#o 2 elemento da 2 probabilidade como mostrado no X
norm.ppf(X)

#o array recem gerado usou as propabilidade geradas pelo rand e as converteu em distancias em relação as médias 0 
#medida pelo numero de desvio padrão essa funcao criou o Z que precisamos.
Z = norm.ppf(np.random.rand(10,2))
Z

#agora vamos criar os retornos diários
#prever o preço das ações para mil dias e perguntaremos para o computador 10 series de previsões futuras do preço da ação
t_intervals = 1000
iterations = 10
#daily_returns sera usado para mostrar o e R 
#para isso precisamo da funcao exp de numpy para elevar a espressão entre ()
#olhar o WORD
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
daily_returns
#obtendo uma matriz de 1000 por 10 com valores do retornos diários/ 10 conjuntos com 1000 preços futuros aleatorios da ações

#agora e criar uma lista de preços. cada preço deve ser igual ao produto do preço observados do dia anteriror
#e o retorno diario simulado portanto uma vez q obtermos o preço do dia T podemos estimar o preço da ação do dia T+1
# / olhar o WORD

#precisamos partir do ultimo numero da nossa base de dados que é o preço atual do mercado.
#usando o iloc precisamo do ultimo numero da tabela [-1]
S0 = data.iloc[-1]
S0

#teremos q usar o numpy zeros_like para obter um array com as mesmas dimensões que um array q ja existe e que nois especificamos
price_list = np.zeros_like(daily_returns) # e o argumento vc adiciona a matriz dos retornos diarios "daily_returns"
price_list
#podemos subtutir esses zeros pelos preços esperados usando o loop
#primeiro precisamos definir a 1 linha 
price_list[0] = S0
price_list

#temnos q criar um loop q começa no dia e termina no dia 1000 nos podemos simplismente escrever para formula o 
#preço esperados da ação no dia St = St-1 * daily_returns observado no dia [t]
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]

price_list

plt.figure(figsize=(10,6))
plt.plot(price_list);
plt.show()