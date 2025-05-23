from validator import validar_dados

def test_dados_validos():
  dados = {
    "nome": "Nickolas",
    "email": "nickolas@email.com",
    "idade": 22
  }
  resultado, erro = validar_dados(dados)
  assert resultado == True
  assert erro == ""

def test_falta_email():
    dados = {
        "nome": "Nickolas",
        "idade": 22
    }
    resultado, erro = validar_dados(dados)
    assert resultado == False
    assert "email" in erro.lower()

def test_nome_vazio():
    dados = {
        "nome": "   ",
        "email": "teste@email.com",
        "idade": 25
    }
    resultado, erro = validar_dados(dados)
    assert resultado == False
    assert "nome" in erro.lower()

def test_email_invalido():
    dados = {
        "nome": "João",
        "email": "joaoemail.com",  # Falta @
        "idade": 30
    }
    resultado, erro = validar_dados(dados)
    assert resultado == False
    assert "email" in erro.lower()

def test_idade_invalida():
    dados = {
        "nome": "Maria",
        "email": "maria@email.com",
        "idade": 15
    }
    resultado, erro = validar_dados(dados)
    assert resultado == False
    assert "idade" in erro.lower()