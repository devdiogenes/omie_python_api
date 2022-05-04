from config import *

class OmieListarProdutos:

    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/produtos/"
        self.call = 'ListarProdutos'
        self.pagina = 1
        self.registros_por_pagina = 50
        self.apenas_importado_api = 'N'
        self.filtrar_apenas_omiepdv = 'N'

    def executar(self):
        return OmieApi().executar(self, self.empresa)

    def todos(self):
        self.registros_por_pagina = 100
        consulta = self.executar()
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta['produto_servico_cadastro']
        while self.pagina < total_de_paginas:
            self.pagina += 1
            produtos = self.executar()['produto_servico_cadastro']
            for produto in produtos:
                lista.append(produto)

        return lista