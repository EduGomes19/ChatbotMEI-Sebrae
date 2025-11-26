import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1) Carregar dados de treino
dados = pd.read_csv("C:/Users/Eduu/Documents/VSCodeProjects/Python/Chatbot-Emotech/perguntas.csv")

# Seleciona as colunas frase e categoria do DF etransforma tudo em string
frases = dados["frase"].astype(str).tolist() #converte a Serie em um lista
categorias = dados["categoria"].astype(str).tolist()

# 2) Vetorizar e treinar
vetorizador = CountVectorizer()
X = vetorizador.fit_transform(frases)

modelo = MultinomialNB()
modelo.fit(X, categorias)

# 3) Carregar respostas.json
with open("C:/Users/Eduu/Documents/VSCodeProjects/Python/Chatbot-Emotech/respostas.json", "r", encoding="utf-8") as f: #r: modo
    respostas = json.load(f) # Lê o json e transforma em estruturas phyton

# 4) loop do chat
print("RF/SEBRAE Bot: Olá! Como posso ajudar? (digite 'sair' para terminar)")
while True:
    entrada = input("Você: ").strip()
    if entrada.lower() == "sair":
      print("RF/ Bot: Até logo!")
      break
    if not entrada:
      print("RF/SEBRAE Bot: Pode digitar sua dúvida ;)")
      continue

    categoria_prevista = modelo.predict(vetorizador.transform([entrada]))[0]
    resp = respostas.get(categoria_prevista, {"texto": "", "links": []})
    texto = (resp.get("texto") or "").strip()
    links = resp.get("links") or []

    if not texto and not links:
      print("RF/SEBRAE Bot: Desculpe, não entendi. Pode reformular sua pergunta?")
      continue

    if texto:
      print(f"RF/SEBRAE Bot: {texto}")
    if links:
      print("Links oficiais:")
      for url in links:
        print("-", url)