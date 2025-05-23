import re

def validar_dados(dados):
  """
  Valida os campos 'nome', 'email' e 'idade' em um dicionário.
  Retorna (True, '') se estiver tudo certo, senão (False, 'mensagem de erro')
  """

  campos_esperados = ['nome','email','idade']
  for campo in campos_esperados:
    if campo not in dados:
      return False, f"Campo obrigatório ausente: {campo}"
    
  nome = dados.get('nome')
  if not isinstance(nome, str) or nome.strip() == "":
    return False, "Nome inválido"
  
  email = dados.get('email')
  regex_email = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
  if not re.match(regex_email, email):
    return False, "Email inválido"
  
  idade = dados.get('idade')
  if not isinstance(idade, int) or idade < 18:
    return False, "Idade deve ser um número inteiro maior ou igual a 18"
  
  return True, ""
