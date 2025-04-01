# https://brickset.com/article/52664/api-version-3-documentation
# 

import requests

API_KEY = '3-tgev-1qP3-cdGjH'
USER_HASH = '4vduPL67GP'
BASE_URL = 'https://brickset.com/api/v3.asmx/'
QUERY = '4098-1'

def search_sets(api_key, user_hash, query):
    """Busca conjuntos de LEGO pelo nome."""
    data = {
        "apiKey": api_key,
        "userHash": user_hash,
        "params": 
        {
            "setNumber": query
        }
    }

    response = requests.post(f"{BASE_URL}getSets", json=data)  # Enviar via POST
    print("Status Code:", response.status_code)
    print("Resposta Bruta:", response.text)

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("Erro ao decodificar JSON. Resposta pode estar vazia ou malformada.")
        return None

# Testar a busca por "Star Wars"
sets = search_sets(API_KEY, USER_HASH, QUERY)

if sets and sets.get('status') == 'success':
    print(f"✅ {len(sets.get('sets', []))} sets encontrados!")
    for s in sets.get('sets', [])[:5]:  # Exibir os primeiros 5 sets
        print(f"- {s['name']} ({s['setID']})")
else:
    print("❌ Erro ao buscar conjuntos:", sets)



import requests

API_KEY = '3-tgev-1qP3-cdGjH'
USERNAME = 
PASSWORD = 
BASE_URL = 'https://brickset.com/api/v3.asmx/'

def check_api_key(api_key):
    """Verifica se a chave de API é válida."""
    # response = requests.post(f"{BASE_URL}checkKey", json={'apiKey': api_key})
    response = requests.get(f"{BASE_URL}checkKey?apiKey={api_key}")
    print("Status Code:", response.status_code)  # Verifica o status HTTP
    print("Resposta Bruta:", response.text)  # Verifica o conteúdo da resposta
    
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("Erro ao decodificar JSON. Resposta pode estar vazia ou malformada.")
        return None

key_status = check_api_key(API_KEY)
if key_status.get('status') == 'success':
    print("Chave de API válida.")
else:
    print("Chave de API inválida.")
    exit()




import requests
import hashlib

API_KEY = '3-tgev-1qP3-cdGjH'
USERNAME = 
PASSWORD = 
BASE_URL = 'https://brickset.com/api/v3.asmx/'

def hash_password(password):
    """Converte a senha para MD5 (a API do Brickset exige isso)."""
    return hashlib.md5(password.encode()).hexdigest()

def login(api_key, username, password):
    """Realiza login e retorna o userHash."""
    # password_hash = hash_password(password)  # Convertendo a senha para MD5
    response = requests.get(f"{BASE_URL}login?apiKey={api_key}&username={username}&password={password}")
    
    print("Status Code:", response.status_code)
    print("Resposta Bruta:", response.text)

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("Erro ao decodificar JSON. Resposta pode estar vazia ou malformada.")
        return None

# Testar o login
login_response = login(API_KEY, USERNAME, PASSWORD)

if login_response and login_response.get('status') == 'success':
    print("✅ Login bem-sucedido! User Hash:", login_response.get('hash'))
else:
    print("❌ Erro no login:", login_response)




# final para testes

import requests

USERNAME = 'Fabricks'
PASSWORD = 'K0nt@_Brickset'
API_KEY = '3-tgev-1qP3-cdGjH'
USER_HASH = '4vduPL67GP'
BASE_URL = 'https://brickset.com/api/v3.asmx/'
QUERY = '4100-1'

def search_sets(api_key, user_hash, query):
    """Busca conjuntos de LEGO pelo número do set."""
    data = {
        "apiKey": api_key,
        "userHash": user_hash,
        "params": '{"setNumber": "' + query + '"}'  # Formatar JSON como string
    }

    response = requests.post(f"{BASE_URL}getSets", data=data)

    print("Status Code:", response.status_code)
    print("Resposta Bruta:", response.text)

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("Erro ao decodificar JSON. Resposta pode estar vazia ou malformada.")
        return None

# Testar a busca pelo set "4100-1"
sets = search_sets(API_KEY, USER_HASH, QUERY)

if sets and sets.get('status') == 'success':
    print(f"✅ {len(sets.get('sets', []))} sets encontrados!")
    for s in sets.get('sets', [])[:5]:  # Exibir os primeiros 5 sets
        print(f"- {s['name']} ({s['setID']})")
else:
    print("❌ Erro ao buscar conjuntos:", sets)
