import os
import requests
from datetime import date
from dotenv import load_dotenv

class Omie:
    def __init__(self, empresa):
        
        self.AlterarPrecoItem = OmieAlterarPrecoItem(empresa)
        self.AlterarProduto = OmieAlterarProduto(empresa)
        self.ConsultarCliente = OmieConsultarCliente(empresa)
        self.ConsultarPedido = OmieConsultarPedido(empresa)
        self.ConsultarVendedor = OmieConsultarVendedor(empresa)
        self.ListarCenarios = OmieListarCenarios(empresa)
        self.ListarClientes = OmieListarClientes(empresa)
        self.ListarContasPagar = OmieListarContasPagar(empresa)
        self.ListarContasReceber = OmieListarContasReceber(empresa)
        self.ListarAnexo = OmieListarAnexo(empresa)
        self.ListarImpostosCenario = OmieListarImpostosCenario(empresa)
        self.ListarLocaisEstoque = OmieListarLocaisEstoque(empresa)
        self.ListarPedidos = OmieListarPedidos(empresa)
        self.ListarPosEstoque = OmieListarPosEstoque(empresa)
        self.ListarProdutos = OmieListarProdutos(empresa)
        self.ListarTabelaItens = OmieListarTabelaItens(empresa)
        self.ListarTabelasPreco = OmieListarTabelasPreco(empresa)
        self.ListarVendedores = OmieListarVendedores(empresa)
        self.ObterAnexo = OmieObterAnexo(empresa)

class OmieAlterarPrecoItem:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/tabelaprecos/"
        self.call = "AlterarPrecoItem"
        self.nCodTabPreco = 0
        self.nCodProd = 0
        self.nValorTabela = 0

    def executar(self, console = True):
        return OmieApi().executar(self, self.empresa, console = console) 

class OmieAlterarProduto:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/produtos/"
        self.call = "AlterarProduto"
        self.codigo_produto = 0

    def executar(self, console = True):
        return OmieApi().executar(self, self.empresa, console = console) 

class OmieConsultarCliente:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/clientes/"
        self.call = "ConsultarCliente"
        self.codigo_cliente_omie = 0
        self.codigo_cliente_integracao = ""

    def executar(self):
        return OmieApi().executar(self, self.empresa) 

class OmieConsultarPedido:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/pedido/"
        self.call = "ConsultarPedido"
        self.codigo_pedido = 0

    def executar(self):
        return OmieApi().executar(self, self.empresa)

class OmieConsultarVendedor:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/vendedores/"
        self.call = "ConsultarVendedor"
        self.codigo = 0
        self.codInt = ""

    def executar(self):
        return OmieApi().executar(self, self.empresa)  
    
class OmieListarAnexo:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/anexo/"
        self.call = "ListarAnexo"
        self.nPagina = 1
        self.nRegPorPagina = 500
        self.nId = 0
        self.cTabela = ""

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console)

class OmieListarCenarios:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/cenarios/"
        self.call = 'ListarCenarios'
        self.nPagina = 1
        self.nRegPorPagina = 20

    def executar(self):
        return OmieApi().executar(self, self.empresa) 

class OmieListarClientes:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/clientes/"
        self.call = 'ListarClientes'
        self.pagina = 1
        self.registros_por_pagina = 50

    def executar(self):
        return OmieApi().executar(self, self.empresa) 

    def todos(self):
        nome_lista_omie = "clientes_cadastro"
        self.registros_por_pagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            registros = self.executar()[nome_lista_omie]
            for registro in registros:
                lista.append(registro)
        return lista
    
class OmieListarContasPagar:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "financas/contapagar/"
        self.call = "ListarContasPagar"
        self.pagina = 1
        self.registros_por_pagina = 20

    def executar(self):
        return OmieApi().executar(self, self.empresa) 
    
    def todos(self):
        nome_lista_omie = "conta_pagar_cadastro"
        self.registros_por_pagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            registros = self.executar()[nome_lista_omie]
            for registro in registros:
                lista.append(registro)
        return lista
    
class OmieListarContasReceber:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "financas/contareceber/"
        self.call = "ListarContasReceber"
        self.pagina = 1
        self.registros_por_pagina = 20
        self.apenas_importado_api = "N"

    def executar(self):
        return OmieApi().executar(self, self.empresa) 
    
    def todos(self):
        nome_lista_omie = "conta_receber_cadastro"
        self.registros_por_pagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            registros = self.executar()[nome_lista_omie]
            for registro in registros:
                lista.append(registro)
        return lista

class OmieListarImpostosCenario:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/cenarios/"
        self.call = 'ListarImpostosCenario'
        self.consumo_final = "N"
        self.codigo_produto = 0       

    def executar(self):
        self.codigo_cliente_omie = OmieApi(self.empresa).cliente_imposto()
        self.codigo_cenario = OmieApi(self.empresa).cenario_imposto()
        return OmieApi().executar(self, self.empresa)

class OmieListarLocaisEstoque:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "estoque/local/"
        self.call = 'ListarLocaisEstoque'
        self.nPagina = 1
        self.nRegPorPagina = 20

    def executar(self):
        return OmieApi().executar(self, self.empresa) 
    
class OmieListarPedidos:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/pedido/"
        self.call = "ListarPedidos"
        self.pagina = 1
        self.registros_por_pagina = 100
        self.apenas_importados_api = "N"

    def executar(self, console = False): 
        return OmieApi().executar(self, self.empresa, console = console)
    
    def todos(self, console = False):
        nome_lista_omie = "pedido_venda_produto"
        self.registros_por_pagina = 500
        consulta = self.executar(console = console)
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            lista_pagina = self.executar(console = console)[nome_lista_omie]
            for ind in lista_pagina:
                lista.append(ind)
        return lista

class OmieListarPosEstoque:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "estoque/consulta/"
        self.call = 'ListarPosEstoque'
        self.nPagina = 1
        self.nRegPorPagina = 20
        self.dDataPosicao = date.today().strftime("%d/%m/%Y")
        self.cExibeTodos = "N"
        self.codigo_local_estoque = OmieApi(empresa).local_de_estoque()

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console) 

    def todos(self, console = False):
        nome_lista_omie = "produtos"
        self.nRegPorPagina = 500
        consulta = self.executar(console = console)
        total_de_paginas = consulta['nTotPaginas']
        lista = consulta[nome_lista_omie]
        while self.nPagina < total_de_paginas:
            self.nPagina += 1
            produtos = self.executar()[nome_lista_omie]
            for produto in produtos:
                lista.append(produto)
        return lista

class OmieListarProdutos:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/produtos/"
        self.call = 'ListarProdutos'
        self.pagina = 1
        self.registros_por_pagina = 50
        self.apenas_importado_api = 'N'
        self.filtrar_apenas_omiepdv = 'N'

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console)

    def todos(self, console = False):
        nome_lista_omie = "produto_servico_cadastro"
        self.registros_por_pagina = 500
        consulta = self.executar(console = console)
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            produtos = self.executar(console = console)[nome_lista_omie]
            for produto in produtos:
                lista.append(produto)
        return lista

class OmieListarTabelaItens:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/tabelaprecos/"
        self.call = 'ListarTabelaItens'
        self.nPagina = 1
        self.nRegPorPagina = 20
        self.nCodTabPreco = 0

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console) 

    def todos(self, console = False):
        nome_lista_omie = "listaTabelaPreco"
        self.nRegPorPagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['nTotPaginas']
        lista = consulta[nome_lista_omie]['itensTabela']
        while self.nPagina < total_de_paginas:
            self.nPagina += 1
            busca = self.executar(console = console)
            produtos = busca[nome_lista_omie]['itensTabela']
            for produto in produtos:
                lista.append(produto)
        return lista

class OmieListarTabelasPreco:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/tabelaprecos/"
        self.call = 'ListarTabelasPreco'
        self.nPagina = 1
        self.nRegPorPagina = 20

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console) 
    
class OmieListarVendedores:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/vendedores/"
        self.call = "ListarVendedores"
        self.pagina = "1"
        self.registros_por_pagina = 100
        self.apenas_importado_api = "N"

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console) 
    
class OmieObterAnexo:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/anexo/"
        self.call = "ObterAnexo"
        self.cCodIntAnexo = "",
        self.cTabela = "",
        self.nId = 0,
        self.nIdAnexo = 0,
        self.cNomeArquivo = ""

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console) 

class OmieApi:
    def __init__(self, empresa = ""):
        self.caminho = ""
        self.call = ""
        load_dotenv()
        self.empresa = empresa

    def executar(self, metodo, empresa, console = False):

        self.empresa = empresa

        metodo_json = self.__converter_json(metodo)

        parametros = metodo_json.copy()
        parametros.pop('caminho')
        parametros.pop('call')
        parametros.pop('empresa')

        json_data = {}
        json_data['app_key'] = self.key()
        json_data['app_secret'] = self.secret()
        json_data['call'] = metodo_json['call']
        json_data['param'] = [parametros]
        response = requests.post('https://app.omie.com.br/api/v1/' + metodo_json['caminho'], json=json_data)
        if console == True: print(response.json())
        return response.json()

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

    def key(self): return os.getenv(self.empresa + '_KEY')
    def secret(self): return os.getenv(self.empresa + '_SECRET')
    def cliente_imposto(self): return os.getenv(self.empresa + '_CLIENTE_IMPOSTO')
    def cenario_imposto(self): return os.getenv(self.empresa + '_CENARIO_IMPOSTO')
    def local_de_estoque(self): return os.getenv(self.empresa + '_LOCAL_DE_ESTOQUE')