import requests
import pandas as pd

def get_data(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(endpoint, timeout=10)
        
        if response.status_code == 200: # 200 é o status code para sucesso
            return response.json()
        else: # se o status code não for 200, retorna None pois é um erro
            print(f"Erro ao buscar CEP {cep}: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError as e:
        print(f"Erro de conexão para CEP {cep}: {e}")
        return None
    except requests.exceptions.Timeout as e:
        print(f"Timeout para CEP {cep}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição para CEP {cep}: {e}")
        return None




users_path = "01-bronze-raw/users.csv"
users_df = pd.read_csv(users_path)

cep_lists = users_df["cep"].tolist() 

cep_info_list = []

for cep in cep_lists:
    cep_clean = cep.replace("-", "")
    cep_info = get_data(cep_clean)
    print(cep_info)
    # se contem a chave "erro" no dicionario, pula para o próximo cep
    if "erro" in cep_info:
        continue
    cep_info_list.append(cep_info)

cep_info_df = pd.DataFrame(cep_info_list)

cep_info_df.to_csv("01-bronze-raw/cep_info.csv", index=False)












