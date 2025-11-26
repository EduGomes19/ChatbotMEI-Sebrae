# 🤖 ChatbotMEI-Sebrae: Assistente Virtual Fiscal (IR/MEI)

<div style="background:#e8f2ff;border-left:6px solid #2b7be4;padding:12px;border-radius:6px;margin:8px 0">
	<strong style="color:#0b3a66">Projeto de Estágio — Aplicação com Inteligência Artificial<br></strong>
	<div style="color:#0b3a66;margin-top:6px">Chatbot para consultas sobre Imposto de Renda (IRPF) e Microempreendedor Individual (MEI). Interface web com Flask e componente de NLP para classificação de intenções.<br></div>
</div>

📋 Sobre o Projeto

- O **ChatbotMEI-Sebrae** foi desenvolvido para auxiliar usuários com dúvidas fiscais recorrentes, oferecendo respostas rápidas e links para fontes oficiais. O sistema opera em duas frentes:

- **Base de Conhecimento Local:** modelo de Machine Learning (Naive Bayes) treinado em um dataset local para identificar intenções e retornar respostas rápidas.
- **Busca Externa (Google Custom Search):** quando necessário, o bot realiza buscas para complementar respostas com links atualizados.

---

## 🚀 Principais Tecnologias

- **Python 3.11+**
- **Flask** (backend web)
- **Scikit-learn** (MultinomialNB, CountVectorizer)
- **Pandas** (manipulação de dados)
- **Google Custom Search JSON API** (opcional para busca externa)
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

---

## 📂 Estrutura do Projeto

```
Chatbot-Emotech/
├─ ChatbotEmotech.py      # Aplicação Flask + lógica de IA
├─ perguntas.csv          # Dataset de treino (frases e categorias)
├─ respostas.json         # Base de conhecimento (textos e links oficiais)
├─ templates/
│  └─ index.html          # Interface do chatbot
└─ ReadMe.md              # Documentação
```

## ⚙️ Pré-requisitos

- Python 3.11 ou superior
- Recomendo criar um virtualenv antes de instalar dependências

## Instalação (PowerShell)

```powershell
# criar e ativar virtualenv (Windows PowerShell)
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# instalar dependências
pip install -r requirements.txt
# ou manualmente:
pip install flask pandas scikit-learn google-api-python-client
```

> Observação: se não existir `requirements.txt`, você pode criar um com as bibliotecas acima.

## Configuração de API (opcional)

Para usar a busca externa do Google, defina as chaves em variáveis de ambiente ou no arquivo de configuração:

- `GOOGLE_API_KEY` = sua chave
- `GOOGLE_CSE_CX` = seu ID de mecanismo de busca

Exemplo (PowerShell):

```powershell
$env:GOOGLE_API_KEY = 'SUA_CHAVE'
$env:GOOGLE_CSE_CX = 'SEU_CSE_ID'
```

## Executando a aplicação

```powershell
# rodar a aplicação Flask (arquivo principal)
python ChatbotEmotech.py
```

Abra o navegador em `http://127.0.0.1:5000/` (ou o endereço exibido no terminal).

---

## 🧠 Como funciona a IA (resumo)

1. O sistema carrega `perguntas.csv` no início.
2. Frases são vetorizadas com `CountVectorizer` (Bag of Words).
3. O modelo `MultinomialNB` é treinado com as categorias do dataset.
4. Ao receber uma mensagem do usuário, o texto é vetorizado e o modelo prevê a categoria.
5. A resposta correspondente é obtida a partir de `respostas.json` (com links oficiais quando aplicável).

---

## ✅ Testes rápidos e verificação

- Abra a interface web e envie perguntas; verifique se respostas e links aparecem.
- Use o DevTools do navegador para testar comportamento responsivo (mobile/desktop).

## 👥 Autoria

Desenvolvido por: Grupo 1

Instituição: FMU - Faculdades Metropolitanas Unidas

Disciplina: Estágio Supervisionado — Ano: 2025