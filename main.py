import pandas as pd
import matplotlib.pyplot as plt

# Carregar o CSV do IBGE (certifique-se que o arquivo está na mesma pasta do script)
df = pd.read_csv("pof_aquisicao_alimentar.csv")

# Estatísticas descritivas
print("\n📊 Estatísticas descritivas:")
print(df.describe())

# Top 3 mais consumidos
top3 = df.nlargest(3, "Consumo_per_capita_kg_ano")
print("\n🥇 Top 3 grupos mais consumidos:")
print(top3[["Grupo_Alimentar", "Consumo_per_capita_kg_ano"]])

# Bottom 3 menos consumidos
bottom3 = df.nsmallest(3, "Consumo_per_capita_kg_ano")
print("\n🥉 3 grupos menos consumidos:")
print(bottom3[["Grupo_Alimentar", "Consumo_per_capita_kg_ano"]])

# Gráfico de barras
plt.figure(figsize=(10,6))
plt.bar(df["Grupo_Alimentar"], df["Consumo_per_capita_kg_ano"], color="skyblue")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Consumo per capita (kg/ano)")
plt.title("Consumo alimentar per capita anual - IBGE POF 2017-2018")
plt.tight_layout()
plt.show()

# Gráfico de pizza
plt.figure(figsize=(8,8))
plt.pie(df["Consumo_per_capita_kg_ano"],
        labels=df["Grupo_Alimentar"],
        autopct='%1.1f%%',
        startangle=140)
plt.title("Distribuição do consumo alimentar per capita - IBGE POF 2017-2018")
plt.show()
