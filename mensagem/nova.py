import requests as req

def nova_mensagem(sessao):
    print('--------Nova Mensagem--------')
    while True:
        try:
            destinatario = int(input('Para: '))
            break
        except:
            print('Digite um numero inteiro!')

    texto = input('Mensagem: ')

    try:
        resposta = req.post('http://localhost:6000/msg', json={"de": sessao.get('id'),"para": destinatario,"segredo": sessao.get('segredo'),"texto": texto}).json()
        if isinstance(resposta, dict):
            print('Mensagem enviada com Sucesso! \n')
            print(f'Id da mensagem: {resposta["id"]}')
            print(f'Data/Hora da mensagem: {resposta["datahora"]}')
    except:
        print('Erro: 404, Servidor fora do ar.')
        print('Tente mais tarde novamente.')
    