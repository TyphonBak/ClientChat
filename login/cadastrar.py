import requests as req

def novo():
    nome = input('Digite seu nome para cadastro: ')
    try:
        resposta = req.post('http://localhost:6000/usr', json={'nome': nome})
        dados = resposta.json()
        if resposta.status_code == 201:
            print('Cadastro realizado com Sucesso!')
            print(f'Seu id é {dados.get("id")}')
            print(f'Seu segredo é {dados.get("segredo")}')
            return {'id':dados.get("id"), 'segredo': dados.get("segredo")}
        else:
            print(dados)
            return None
    except:
        print('Erro: 404, Servidor fora do ar.')
        print('Tente mais tarde novamente.')