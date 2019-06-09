## Rotina automatizada de testes na API
# Expõe os métodos CRUD a situações de sucesso e falha

import os

print("\nTeste: Buscar ID 3")
os.system('python TESTE.py TestAPI.test_get_3')
# Resultado esperado: sucesso

print("\nTeste: Deletar ID 3")
os.system('python TESTE.py TestAPI.test_delete_3')
# Resultado esperado: sucesso

print("\nTeste: Buscar ID 3")
os.system("python TESTE.py TestAPI.test_get_3")
# Resultado esperado: falha, pois o ID foi deletado

print("\nTeste: Modificar ID 3")
os.system('python TESTE.py TestAPI.test_put_3')
# Resultado esperado: falha, pois o ID foi deletado

print("\nTeste: Deletar ID 4")
os.system('python TESTE.py TestAPI.test_delete_4')
# Resultado esperado: falha, pois o ID ainda não existe

print("\nTeste: Inserir ID 4")
os.system('python TESTE.py TestAPI.test_post_4')
# Resultado esperado: sucesso

print("\nTeste: Modificar ID 4")
os.system('python TESTE.py TestAPI.test_put_4')
# Resultado esperado: sucesso

print("\nTeste: Deletar ID 4")
os.system('python TESTE.py TestAPI.test_delete_4')
# Resultado esperado: sucesso

print("\nTeste: Inserir ID 4")
os.system('python TESTE.py TestAPI.test_post_5')
# Resultado esperado: falha, pois é passado um texto ao invés de número no atributo "qtd"
