from omie import *


exemplo = Omie("EmpresaTeste")

exemplo.ListarClientes.registros_por_pagina = 2

exec = exemplo.ListarClientes.executar()

print(exec)