import numpy as np
import pandas as pd
from pandas_datareader import data as wb

#o Beta mostra até que ponto a mudança no preço de um ativo está relacionado ao desempenho global do mercado.
#ele e usualmente calculado nos ultimos 5 anos...

tickers = ["PG", "^GSPC"]
data = pd.DataFrame()
for t in tickers:
    data[t] = wb.DataReader(t, data_source="yahoo", start="2016-03-24", end="2021-03-24")["Adj Close"]
#primeiro e saber a convariançia entre PG e o S&P500 e em segundo e a variancia do S&P500
sec_returns = np.log(data / data.shift(1))

#criando matriz de covariancia entre PG e o mercado S&P500.

cov = sec_returns.cov() * 250
cov

#usando o comando iloc para obter a covariancia entre pg e o mercado mas em float.
cov_with_market = cov.iloc[0,1]
cov_with_market

#agora vamos achar a variancia do mercado anualizada
market_var = sec_returns["^GSPC"].var() * 250
market_var

#para o Beta da PG iremos atribuir o coeficiente da divisão da covariancia obtido pela variancia do mercado
PG_BETA = cov_with_market / market_var
PG_BETA
#o valor é a cima de 0 porém e abaixo de 1 que caracteriza a ação defensiva # ver o word da aula.
#quando o mercado sobe o valor da ação nao vai disparar
#porém em tempos de crise você perderá menos dinheiro.

#Calculate the expected return of PG (CAPM)
#Rpg=ativo livre de risco + Beta da PG  (Rm-RF)> Prêmio de risco
#pegando a taxa dos 10y temos 2,52% e por ultimo temos q usar o prêmio de risco podendo ser 5% com base nos dados academicos
PG_er = 0.025 + PG_BETA * 0.05
PG_er

#Indice de sharpe olhar no word => sharpe = Rpg - Rj / Desvio padrão do PG
Sharpe = (PG_er - 0.025) / (sec_returns["PG"].std() * 250 ** 0.5)
Sharpe
#podemos usar esse indice quando quiser comparar diferente ações e portfolio de ações.
