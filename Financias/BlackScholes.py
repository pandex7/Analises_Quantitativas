import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm

#vamos calcular o preço de um opção de compra "CALL"
#vamos criar função que nos permitira calcular os valores do d1 e d2 q precisamos para a formula do black-Scholes
#os parametros q nos precisamos são S - Preço da ação / K - preço do exercício / r - Taxa livre de risco
#stdev - Desvio padrão /  T - intervalo de tempo (anos)
#olha no Word para ajudar com a formula se precisar.

def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

def d2(S, K, r, stdev, T):
    return (np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

#para usar a formula precisamos da distruicao normal cumulativa (CDF) mostra como os dados se acumulam no tempo
#ele nunca pode ser a baixo de 0 e a cima de 1
#a partir dos dados / OLHAR O WORD

norm.cdf(0)
norm.cdf(0.25)
norm.cdf(0.75)
norm.cdf(9)

#agora usa a funcao de black scholes #olhar o word para entender os parametros(argumentos)
def BSM(S, K, r, stdev, T):
    return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))

#agora vamos aplicar para a ação do PG.
ticker = ["PG"]
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source="yahoo", start="2007-1-1", end="2017-3-21")["Adj Close"]

#agora o iloc ira trazer o preço do valor atual -1 lembra?
S = data.iloc[-1]
S
#vamos estrair o desvio padrão os profissionais usam as formula para interpolações para calcular esse valor
#no nosso caso iremos usar como aproximação o desvio padrão do retorno logaritmo dessa ação

log_returns = np.log(1 + data.pct_change())
stdev = log_returns.std() * 250 ** 0.5
stdev

#agora podemos calcular o preço de uma opção de compra "CALL"
r = 0.025
K = 110.0
T = 1

#vamos usar o taxa livre de risco entre 0.025 = r = rendimento dos titulos de 10 americanos. e o preço do exercicio e 110
# e o tempo e 1 ano.
#achando o d1 e d2 e o preço de opção de compra(BSM)
d1(S, K, r, stdev, T)
d2(S, K, r, stdev, T)
BSM(S, K, r, stdev, T)

#sera q e possivel ter um preço de opção muito mais baixo do q do preço das ações? concerteza
#o valor da opção depende de inumeros parametro tais como o preço de exercicio, o tempo para o vencimento
#e a volatilidade, não e diretamente proporcional ao preço do ativo 