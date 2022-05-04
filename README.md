# omie_python_api
Uma maneira fácil de comunicar-se com a API da Omie, utilizando Python.

## Configuração inicial

Primeiramente, crie um arquivo .env contendo os seguintes dados: 

*0_KEY = '38333295000'*

*0_SECRET = 'fed2163e2e8dccb53ff914ce9e2f1258'*

Essas são as credenciais da API teste da Omie. Para adicionar suas empresas, utilize o mesmo padrão, mudando apenas o numero inicial no nome da variável e as informações. Exemplo:

*1_KEY = "APP_KEY da sua primeira empresa"*

*1_SECRET = "APP_SECRET da sua primeira empresa"*

*2_KEY = "APP_KEY da sua segunda empresa"*

*2_SECRET = "APP_SECRET da sua segunda empresa"*

Após, instale as bibliotecas necessárias, rodando dentro dessa pasta o comando:

*pip install -r requirements.txt*

E então, você pode usar o arquivo *exemplo.py* para entender como essa biblioteca funciona, e se basear.

## Métodos já configurados: 

*ListarProdutos