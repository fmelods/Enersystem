import requests
import json

def make_prediction(data):
    url = 'http://127.0.0.1:5000/predict'
    headers = {'Content-type': 'application/json'}
    
    # Enviar a solicitação POST com os dados da nova amostra
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        result = response.json()
        prediction = result['prediction']
        print(f"Previsão para a nova amostra: {prediction}")
    else:
        print("Erro ao fazer a previsão.")


def make_regression(data):
    url = 'http://127.0.0.1:5000/regress'
    headers = {'Content-type': 'application/json'}
    
    #Enviar a solicitação POST com os dados da nova amostra
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    #Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        result = response.json()
        regression = result['regression']
        print(f"Previsão para a nova amostra: {regression}")
    else:
        print("Erro ao fazer a previsão.")

if __name__ == '__main__':
    # Dados da nova amostra
    nova_amostra = {
        "renewables_share_energy": "0.053",
        "fossil_share_energy": "99.947",
        "carbon_intensity_elec": "508.162"
    }
    
    nova_amostra12 = {
        "renewables_share_energy": "0.480"
    }			
    # Fazer a previsão usando o cliente
    make_prediction(nova_amostra)
    make_regression(nova_amostra12)