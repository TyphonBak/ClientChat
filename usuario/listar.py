import requests as req
def lista_usuarios():            
    try:
        resposta = req.get(f'http://localhost:6000/usr').json()
        if len(resposta['usr']):
            print('--------Lista de Usuários--------')
            for user in resposta["usr"]:
                print (f"ID: {user['id']} Nome: {user['nome']}" )
            print ("-=-=-=-=-=-=-= Fim da lista de usuários -=-=-=-=-=-=-=")
        else:
            print ("-=-=-=-=-=-=-= Não há usuários -=-=-=-=-=-=-=")
                
    except Exception as e:
        print(e)
        print('Erro: 404, Servidor fora do ar.')
        print('Tente mais tarde novamente.')
