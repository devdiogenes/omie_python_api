import sys
import os
import requests
from dotenv import load_dotenv

class OmieApi:
    def __init__(self):
        self.caminho = ""
        self.call = ""

    def executar(self, metodo, empresa):

        self.__obter_empresa(empresa)

        metodo_json = self.__converter_json(metodo)

        parametros = metodo_json.copy()
        parametros.pop('caminho')
        parametros.pop('call')
        parametros.pop('empresa')

        json_data = {}
        json_data['app_key'] = self.__key
        json_data['app_secret'] = self.__secret
        json_data['call'] = metodo_json['call']
        json_data['param'] = [parametros]
        
        response = requests.post('https://app.omie.com.br/api/v1/' + metodo_json['caminho'], json=json_data)
        return response.json()

    def __obter_empresa(self, numero_empresa):
        load_dotenv()

        self.__key = os.getenv(str(numero_empresa) + '_KEY')
        self.__secret = os.getenv(str(numero_empresa) + '_SECRET')

    def __converter_json(self, metodo):

        antigo = metodo.__dict__
        classe = metodo.__class__.__name__
        novo = {}

        for atributo in antigo:
            valor = antigo[atributo]
            atributo = atributo.replace("_" + classe + "__", "")
            atributo = atributo.replace("_" + classe + "_", "")
            atributo = atributo.replace("_" + classe, "") 
            novo[atributo] = valor     

        return novo
