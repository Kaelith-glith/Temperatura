nome = input('Qual seu nome? ')
idade = int(input('Sua idade? '))

if idade < 18:
    print(f'Desculpe, {nome}, mas apenas maiores de idade podem acessar o sistema.')
else:
    print(f'Bem-vindo ao sistema, {nome}!')

    # Parte com loop para temperatura
    def escolhas():
        while True:
            print('\nDigite 1 para verificar temperatura ou 2 para sair.')
            escolha = input('Escolha: ')

            if escolha == '2':
                print('Saindo do sistema... Até mais!')
                break

            elif escolha == '1':
                temp = int(input('Qual a temperatura hoje? '))

                if temp > 25:
                    print(f'Hoje está quente, {nome}!')
                elif temp < 0:
                    print('Hoje está muito frio, véi!')
                elif temp <= 24:
                    print('Hoje está frio!')
                else:
                    print('Hoje está agradável!')
            else:
                print('Opção inválida. Tente novamente.')

    # Só chama a função se a idade for válida
    escolhas()
