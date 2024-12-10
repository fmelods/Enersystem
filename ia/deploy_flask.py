from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Carregar o modelo e o escalonador
model_filename = 'regression_model.pkl'
scaler_filename = 'scaler.pkl'
cluster_filename = 'cluster_model.pkl'

with open(model_filename, 'rb') as file:
    model = pickle.load(file)

with open(scaler_filename, 'rb') as file:
    scaler = pickle.load(file)
    
with open(cluster_filename, 'rb') as file:
    cluster = pickle.load(file)

@app.route('/')
def home():
    return "Bem-vindo!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Transformar o dicionário em um DataFrame
    nova_amostra_df = pd.DataFrame.from_dict(data, orient='index').transpose()
    
    # Escalonar a amostra
    nova_amostra_scaled = scaler.transform(nova_amostra_df)
    
    # Fazer a previsão
    prediction = cluster.predict(nova_amostra_scaled)
    
    # Converter para um tipo Python nativo
    prediction_name = int(prediction[0])
    
    return jsonify({'prediction': prediction_name})


@app.route('/regress', methods=['POST'])
def regress():
    data = request.get_json(force=True)
    
    # Transformar o dicionário em um DataFrame
    nova_amostra_df = pd.DataFrame.from_dict(data, orient='index').transpose()
    
    # Escalonar a amostra
    # nova_amostra_scaled = scaler.transform(nova_amostra_df)
    
    # Fazer a previsão
    regression = model.predict(nova_amostra_df)  # Verifique se o método é 'predict'
    
    # Converter para um tipo Python nativo
    regression_name = float(regression[0])
    
    return jsonify({'regression': regression_name})

if __name__ == '__main__':
    app.run(debug=True)
    

