import requests as req

def logar():
    while True:
        while True:
            try:
                id_usuario = int(input('Digite seu id: '))
                break
            except:
                print('Digite um numero inteiro!')
        segredo = input('Digite seu segredo: ')
        try:
            resposta = req.get(f'http://localhost:6000/usr/{id_usuario}',json={"segredo": segredo})
            if resposta.status_code == 200:
                print(f'\nBem vindo ao chat {resposta.json()["nome"]}!!!\n')
                return {'id': id_usuario, 'segredo': segredo}
            else:
                print('\nId e/ou senha inválido(s)!\n')
                return None
        except Exception as e:
            print(e)
            print('Erro: 404, Servidor fora do ar.')
            print('Tente mais tarde novamente.')
            break
