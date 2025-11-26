from flask import Flask, render_template, request, jsonify
import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from googleapiclient.discovery import build # Biblioteca do Google

app = Flask(__name__)

# --- CONFIGURAÇÕES ---
GOOGLE_API_KEY = 'AIzaSyA8sDN7jWn0sHCLtchr7thnYLp81l9eIm4'  
GOOGLE_CSE_CX = '523992075c2e64540'

# --- 1. CARREGAMENTO E TREINAMENTO (Executa uma vez ao iniciar) ---
try:
    # Carrega dados (ajuste o caminho se necessário, mas idealmente deixe na mesma pasta)
    dados = pd.read_csv("perguntas.csv")
    
    # Treinamento
    frases = dados["frase"].astype(str).tolist()
    categorias = dados["categoria"].astype(str).tolist()
    
    vetorizador = CountVectorizer()
    X = vetorizador.fit_transform(frases)
    
    modelo = MultinomialNB()
    modelo.fit(X, categorias)
    print("Modelo treinado com sucesso!")

    # Carrega respostas
    with open("respostas.json", "r", encoding="utf-8") as f:
        respostas_db = json.load(f)
    print("Respostas carregadas!")

except Exception as e:
    print(f"Erro ao carregar arquivos: {e}")

# --- FUNÇÃO DE BUSCA NO GOOGLE (ETAPAS 6 e 7) ---
def buscar_no_google(termo):
    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        # Faz a busca
        res = service.cse().list(q=termo, cx=GOOGLE_CSE_CX, num=2).execute()
        
        resultados = []
        if 'items' in res:
            for item in res['items']:
                resultados.append({'titulo': item['title'], 'link': item['link']})
        return resultados
    except Exception as e:
        print(f"Erro na API do Google: {e}")
        return []

# --- ROTAS DO FLASK (ETAPA 8) ---

@app.route('/')
def index():
    # Renderiza a página HTML (vamos criar esse arquivo logo abaixo)
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    mensagem_usuario = request.form['msg']
    
    if not mensagem_usuario:
        return jsonify({'resposta': 'Por favor, digite algo.'})

    # 1. Predição da IA
    vetor_pergunta = vetorizador.transform([mensagem_usuario])
    categoria_prevista = modelo.predict(vetor_pergunta)[0]
    
    # 2. Busca resposta no JSON local
    resp_data = respostas_db.get(categoria_prevista, None)
    
    resposta_final = ""
    links_uteis = []

    if resp_data:
        resposta_final = resp_data.get("texto", "")
        links_uteis = resp_data.get("links", [])
    else:
        resposta_final = "Desculpe, não encontrei uma resposta específica na minha base."

    # 3. Integração com Google (Opcional: busca se não tiver links ou para complementar)
    # Aqui vamos buscar no Google para enriquecer a resposta com +2 links externos
    resultados_google = buscar_no_google(f"Receita Federal {mensagem_usuario}")
    
    # Formata a resposta para o frontend
    return jsonify({
        'resposta': resposta_final,
        'links_locais': links_uteis,
        'links_google': resultados_google,
        'categoria_detectada': categoria_prevista
    })

if __name__ == "__main__":
    app.run(debug=True)