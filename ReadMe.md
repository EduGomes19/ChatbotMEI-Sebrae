# 🤖 Chatbot-Emotech: Assistente Virtual Fiscal (IR/MEI)

> **Projeto de Estágio - Desenvolvimento de Aplicação com Inteligência Artificial**

Este projeto implementa um **chatbot inteligente** focado em responder dúvidas sobre **Imposto de Renda (IRPF)** e **Microempreendedor Individual (MEI)**. O sistema utiliza **Processamento de Linguagem Natural (NLP)** para classificação de intenções e integra uma interface web moderna via **Flask**.

---

## 📋 Sobre o Projeto

O **Chatbot-Emotech** foi desenvolvido para auxiliar usuários com dúvidas fiscais recorrentes, oferecendo respostas rápidas e direcionando para canais oficiais. O sistema opera em dois níveis:
1.  **Base de Conhecimento Local:** Utiliza um modelo de Machine Learning (**Naive Bayes**) treinado com um dataset personalizado para identificar a intenção do usuário e fornecer respostas curtas e precisas.
2.  **Busca Externa (Google API):** Caso a resposta precise de complemento, o bot realiza uma busca em tempo real utilizando a API do Google para fornecer links atualizados.

---

## 🚀 Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias e bibliotecas:

* **Linguagem:** [Python 3.11+](https://www.python.org/)
* **Web Framework:** [Flask](https://flask.palletsprojects.com/)
* **Machine Learning:** [Scikit-learn](https://scikit-learn.org/) (MultinomialNB, CountVectorizer)
* **Manipulação de Dados:** [Pandas](https://pandas.pydata.org/)
* **Integração API:** [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/overview)
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

---

## 📂 Estrutura do Projeto

A organização dos arquivos segue o padrão MVC simplificado para Flask:

```text
Chatbot-Emotech/
│
├── chatbot_estagio.py    # Código principal (Aplicação Flask + Treinamento da IA)
├── perguntas.csv         # Dataset de treino (Frases e Categorias)
├── respostas.json        # Base de conhecimento (Textos e Links Oficiais)
├── templates/
│   └── index.html        # Interface gráfica do usuário (Chat Widget)
└── README.md             # Documentação do projeto