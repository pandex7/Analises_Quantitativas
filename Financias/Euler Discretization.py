import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb
from scipy.stats import norm 
import matplotlib.pyplot as plt 

ticker = "PG"
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source="yahoo", start="2007-01-1", end="2017-3-21")["Adj Close"]

#vamos calcular o preço de um opção de compra so q mais sofisticada do q a anterior.
log_returns = np.log(1 + data.pct_change())

r = 0.025

stdev = log_returns.std() * 250 ** 0.5
stdev

type(stdev)

stdev = stdev.values
stdev

T = 1.0
t_intervals = 250
delta_t = T / t_intervals #agora podemos criar um valor fixo de intervalo de tempo o delta.
iterations = 10000

Z = np.random.standard_normal((t_intervals + 1, iterations))
S = np.zeros_like(Z)
S0 = data.iloc[-1]
S[0] = S0

#vamos fazer um loop de 1 para o numero de intervalo de tempo + 1 e vamos clicar um matriz completa de preços de ações
#com a dimensão de intervalo de tempo + 1 para o numero de interacões mas precisamente 250 + 1 q e 251 e teremos 
#10k de interações por isso a dimensão dessa matriz e 251 por 10 mil.

for t in range(1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])
S

#portanto para plotar apenas 10 interações pode usar um truque do matplotlib depois de especificarmos q gostariamos de plotar
#o S poderiamos adicionar o operador index onde designamos todos os 251 intervalos de tempo que deve ser plotados
#digitando : antes da , e depois q nao estamos dispostos a ver todos os 10k potencial resultados podemos limitar o grafico
#mostrando somente os 10 primeiros que geramos digitando :10 

S.shape

plt.figure(figsize=(10, 6))
plt.plot(S[:, :10]);
plt.show()

#como e calculado o payoff de uma opção de compra "CALL" ?? durante um determinado período de tempo vc exercera seu direito
#de comprar a opção se o preço da ação - preço de exercicio for um número positivo. e vc n exercera seu direito
#se a diferença for negativa. # olhar o word.

p = np.maximum(S[-1] - 100, 0)
p

p.shape

#a formula para descontar a média do payoff está descrita na formula olhar o WORD
#corresponde ao desconto exponencial com o componente matematico multiplicado pela soma dos payoff computador
#divido pelo numero de interações q escolhemos

C = np.exp(-r * T) * np.sum(p) / iterations
C

#é importante ver se esse numero difere daquele q obtivemos da formula de Black Scholes anteriormente o BSM.
#os valores não é assim tão diferentes essa é a prova q a escolha de metodo de calculo pode levar a pequena mas
#importante diferença no resultado 