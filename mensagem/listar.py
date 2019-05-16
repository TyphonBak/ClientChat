import requests as req
def lista_mensagens(sessao):  
    print('--------Gostaria de filtrar?--------')
    while True:
        resposta = input('Sim(1), Não(2)\n >_ ')
        if resposta == '1':
            while True:
                try:
                    id_inicial = int(input('Digite um numero inteiro positivo (caso menor ou igual a zero anulara o filtro inicial).\nDe: '))
                    id_final = int(input('Digite um numero inteiro maior que o inicial (caso for menor ou igual anulara o filtro final).\nAté: '))
                    break
                except:
                    print('Digite um numero inteiro!')
            if id_inicial or id_final:
                query_comp = ''
                query_comp += f'&inicio={id_inicial}' if id_inicial >0 else ''
                query_comp += f'&fim={id_final}' if id_final>id_inicial else ''
                break
        elif resposta == '2':
            query_comp = ''
            break            
        else:
            print('Digite uma opção valida')            

    try:
        resposta = req.get(f'http://localhost:6000/msg/{sessao["id"]}?segredo={sessao["segredo"]}{query_comp}').json()
        if isinstance(resposta, dict):
            if len(resposta['mensagens'])>0:
                print ("-=-=-=-=-=-=-= Lista de Mensagens -=-=-=-=-=-=-=")  
                for mensagem in resposta["mensagens"]:
                    print (f"\nDe: {mensagem['de']} Data Hora: {mensagem['datahora']}" )
                    print (f"Texto: {mensagem['texto']}")
                    print('-'*30)
                print ("\n-=-=-=-=-=-=-= Fim da lista de mensagem -=-=-=-=-=-=-=\n")    
            else:
                print('\n-=-=-=-=-=-=-= Não há mensagens para você -=-=-=-=-=-=-=\n')

    except Exception as e:
        print(e)
        print('Erro: 404, Servidor fora do ar.')
        print('Tente mais tarde novamente.')
