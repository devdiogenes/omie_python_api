from omie import *

exemplo = Omie(0)

exemplo.ListarProdutos.registros_por_pagina = 1
exemplo.ListarProdutos.apenas_importado_api = "S"

exec = exemplo.ListarProdutos.executar()

print(exec)