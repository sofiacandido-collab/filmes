import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Gráfico no Streamlit")

st.write("Este site analisa uma lista de filmes gerada por uma IA (ChatGPT) e analisa a representatividade feminina nas IAs")

df = pd.read_csv("filmes.csv")

st.subheader("Tabela de Dados")
st.dataframe(df)

contagem = df["Gênero Diretor"].value_counts()

st.subheader("Diretores Femininos x Masculinos")


fig, ax = plt.subplots()

ax.bar(contagem.index, contagem.values)


ax.set_xlabel("Gênero")
ax.set_ylabel("Quantidade")
ax.set_title("Quantidade de Diretores por Gênero")


st.pyplot(fig)

st.write("Assim, podemos perceber que as inteligencias artificias possuem um viés, ainda, muito 'homem centrado'")
