print('Bem-vindo ao Pet Shop do Gabriel Peixoto de Campos\n')   # mostra a mensagem de boas-vindas



def cachorro_peso():
    while True:
        try:
            peso = float(input('Entre com o peso do cachorro: '))   # recebe o peso do cachorro

            if (peso < 3): base = 40   # se o peso for menor que 3kg o preço base vai ser 40 reais
            elif (peso >= 3 and peso < 10): base = 50   # se o peso for maior igual a 3kg ou menor que 10kg o preço base vai ser 50 reais
            elif (peso >= 10 and peso < 30): base = 60   # se o peso for maior igual a 10kg ou menor que 30kg o preço base vai ser 60 reais
            elif (peso >= 30 and peso < 50): base = 70   # se o peso for maior igual a 30kg ou menor que 50kg o preço base vai ser 70 reais
            else:
                # se o peso for maior que 50kg exibir a mensagem abaixo
                print('\nNão aceitamos cachorros tão grandes.')
                print('Por favor entre com o peso do cachorr90o novamente.\n')
                continue

        except ValueError:   # caso o peso recebido for uma letra, mostrar a mensagem de erro abaixo, e depois perguntar o peso novamente
            print('\nVocê digitou um valor não numérico!')
            print('Por favor entre com o peso do cachoro novamente.\n')
            continue

        else:
            return base   # retorna o valor base



def cachorro_pelo():
    while True:
        try:
            print('\nEntre com o pelo do cachorro')
            print('c - Pelo Curto')
            print('m - Pelo Médio')
            print('l - Pelo Longo')
            pelo = input('>')

            if(pelo == 'c' or pelo == 'm' or pelo == 'l'):   # verifica se o valor informado é válido
                if(pelo == 'c'): mult = 1   # se o pelo for curto (c), o multiplicador sera 1
                elif(pelo == 'm'): mult = 1.5   # se o pelo for médio (m), o multiplicador sera 1.5
                else: mult = 2   # se o pelo for longo (l), o multiplicador sera 2
            else:   # se o dado for inválido, exibir a mensagem abaixo e entrar com o pelo do cachorro novamente
                print('\ndigite uma opção correta.')
                print('Por favor tente novamente')
                continue

        except:   # caso de algum outro erro exibir a mensagem abaixo (erro genérico)
            print('Erro')
            continue

        else:
            return mult   # retornar o valor mult (multiplicador), o valor sera armazenado em uma váriavel na parte do main
            break



def cachorro_extra():
    totalExtra = 0   # inicia a variável com 0
    extra = 0

    while True:
        try:
            print('\nDeseja adicionar mais algum serviço?')
            print('1 - Corte de Unhas - R$10,00')
            print('2 - Escovar Dentes - R$12,00')
            print('3 - Limpeza de Orelhas - R$15,00')
            print('0 - Não desejo mais nada')
            op = int(input('>'))

            if(op >= 0 and op <= 3):   # verifica se o valor informado é válido
                if(op == 1): extra = 10   # se a opção for 1, o valor extra será 10 reais
                elif(op == 2): extra = 12   # se a opção for 2, o valor extra será 12 reais
                elif(op == 3): extra = 15   # se a opção for 3, o valor extra será 15 reais

            else:   # se o valor informado não for 0, 1, 2 ou 3 será exibido a mensagem abaixo e tentar adicionar o serviço novamente
                print('\ndigite uma opção correta.')
                print('Por favor tente novamente')
                continue

        except ValueError:   # caso a opção recebida for uma letra, mostrar a mensagem de erro abaixo, e depois perguntar novamente
            print('\nVocê digitou um valor não numérico!')
            print('Por favor entre com o peso do cachoro novamente.\n')
            continue

        else:
            if(op == 0):
                return totalExtra  # retorna o valor extra total
                break

            else:
                totalExtra = totalExtra + extra  # calcula o total do valor extra
                continue



peso = cachorro_peso()   # recebe o valor base conforme o peso do cachorro
pelo = cachorro_pelo()   # recebe o multiplicador com base no pelo do cachorro
extra = cachorro_extra()   # recebe o valor extra total

total = peso * pelo + extra   # calcula o total


print('\nTotal a pagar R${} (peso: {} * pelo: {} + adicional(is): {}'.format(total, peso, pelo, extra))