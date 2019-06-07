## Rotina automatizada de testes na API
# Expõe os métodos CRUD a situações de sucesso e falha

import os

print("\nTeste: Buscar ID 3")
os.system('python test.py TestAPIMethods.test_get_3')
# Resultado esperado: sucesso

print("\nTeste: Deletar ID 3")
os.system('python test.py TestAPIMethods.test_delete_3')
# Resultado esperado: sucesso

print("\nTeste: Buscar ID 3")
os.system("python test.py TestAPIMethods.test_get_3")
# Resultado esperado: falha, pois o ID foi deletado

print("\nTeste: Modificar ID 3")
os.system('python test.py TestAPIMethods.test_put_3')
# Resultado esperado: falha, pois o ID foi deletado

print("\nTeste: Deletar ID 7")
os.system('python test.py TestAPIMethods.test_delete_7')
# Resultado esperado: falha, pois o ID ainda não existe

print("\nTeste: Inserir ID 7")
os.system('python test.py TestAPIMethods.test_post_7')
# Resultado esperado: sucesso

print("\nTeste: Modificar ID 7")
os.system('python test.py TestAPIMethods.test_put_7')
# Resultado esperado: sucesso

print("\nTeste: Deletar ID 7")
os.system('python test.py TestAPIMethods.test_delete_7')
# Resultado esperado: sucesso

print("\nTeste: Inserir ID 7")
os.system('python test.py TestAPIMethods.test_post_7')
# Resultado esperado: falha, pois é passado um texto ao invés de número no atributo "preço"
