from login.cadastrar import novo as cadastrar
from login.entrar import logar
from mensagem.nova import nova_mensagem
from mensagem.listar import lista_mensagens
from usuario.listar import lista_usuarios

print('------------------------------------------')
print('|      Bem vindo ao Chat Batutinhas      |')
print('------------------------------------------')
sessao = None
while True:
    opcao = input('Digite uma opção: Entrar(1), Cadastrar(2), Listar Usuarios(3), Sair(0) \n')
    if opcao == '1':
        sessao = logar()
        if sessao:
            break
    elif opcao == '2':
        sessao = cadastrar()
        if sessao:
            break
    elif opcao == '3':
        lista_usuarios()
    elif opcao == '0':
        break
if sessao:
    print('-------Menu-------')
    while True:
        opcao = input('Enviar Mensagem(1), Listar Usuarios(2), Listar Mensagens(3), Sair(0) \n >_ ')
        if opcao == '1':
            nova_mensagem(sessao)
        elif opcao == '2':
            lista_usuarios()
        elif opcao == '3':
            lista_mensagens(sessao)
        elif opcao == '0':
            break
print('------------------------------------------')
print('|   Chat Encerrado. Tenha um bom dia.    |')
print('------------------------------------------')
