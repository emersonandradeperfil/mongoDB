import pandas as pd
import matplotlib.pyplot as plt

from consultas import dados

# dataframe
df = pd.DataFrame(dados)

#mostrar dataframe
print(df)

#gráfico
df.plot(
    x="NOME",
    y="NUMERO_NOTAS",
    kind="bar"
)

plt.show()