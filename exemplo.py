from omie import *


exemplo = Omie("EmpresaTeste")

exemplo.ListarCenarios.nRegPorPagina = 20

exec = exemplo.ListarCenarios.executar()

print(exec)