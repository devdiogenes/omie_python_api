# omie_python_api
Uma maneira fácil de comunicar-se com a API da Omie, utilizando Python.

## Configuração inicial

### Primeiramente, crie um arquivo .env contendo os seguintes dados: 

*EmpresaTeste_KEY = '38333295000'*

*EmpresaTeste_SECRET = 'fed2163e2e8dccb53ff914ce9e2f1258'*

#### Essas são as credenciais da API teste da Omie. Para adicionar suas empresas, utilize o mesmo padrão, mudando apenas o nome inicial no nome da variável e as informações. 
### Exemplo:

*MinhaEmpresa_KEY = "APP_KEY da sua primeira empresa"*

*MinhaEmpresa_SECRET = "APP_SECRET da sua primeira empresa"*

*MinhaOutraEmpresa_KEY = "APP_KEY da sua segunda empresa"*

*MinhaOutraEmpresa_SECRET = "APP_SECRET da sua segunda empresa"*

### Após, instale as bibliotecas necessárias, rodando dentro dessa pasta o comando:

*pip install -r requirements.txt*

### E então, você pode usar o arquivo *exemplo.py* para entender como essa biblioteca funciona, e se basear.

## Métodos já configurados: 

*ListarCenarios - executar()

*ListarClientes - executar(), todos()

*ListarProdutos - executar(), todos()