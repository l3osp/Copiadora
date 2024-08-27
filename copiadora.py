def escolha_servico(): # Função que faz o usuário escolher um serviço
    
    while True: # Inicio do laço de repetição
        # Primeiro menu
        print('Bem-vindo a copiadora do Leonardo Pinheiro')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servico = input('>>').lower()
        try: # Try para tratativa de erros
            # ifs para validar o input do usuário
            if servico == 'dig':
                return 1.1
            elif servico == 'ico':
                return 1
            elif servico == 'ipb':
                return 0.4
            elif servico == 'fot':
                return  0.2
            else:
                print('Escolha inválida, entre com o tipo do serviço novamente')   
        
        except:
            print('Erro: Por favor, digite entre os serviços: dig, ico, ipb e fot')

def num_paginas(): # Função que calcula o desconto conforme a quantidade de páginas
    
    while True: # Inicio do laço de repetição

        global numero # Variavel que recebe o input do usuário

        try: # Try para tratativa de erros
            # ifs aplicar o desconto conforme a quantidade de páginas
            if numero >= 1  and numero < 20:
                return numero
            elif numero >= 20 and numero < 200:
                return numero * 0.85
            elif numero >= 200 and numero < 2000:
                return numero * 0.80
            elif numero >= 2000 and numero < 20000:
                return numero * 75
            else:
                print('Não aceitamos este número de páginas. Por favor, entre com o número de páginas entre 1 e 19.999')
                numero = int(input('Entre com o número de páginas: '))

        except:
            print('Erro: Tente novamente')

def servico_extra(): # Função que faz o usuário escolher ou não um serviço extra
    while True: # Inicio do laõ de repetição
        # Segundo menu
        print('Deseja adicionar algum serviço?')
        print('1 - Encadernação Simples - R$ 15.00')
        print('2 - Encadernação Capa Dura - R$ 40.00')
        print('0 - Não desejo mais nada')
        try: # Try para tratativa de erros
            extra = int(input('>>'))
            # ifs para validar o imput do usuário           
            if extra == 1:
                return 15
            elif extra == 2:
                return 40
            elif extra == 0:
                return 0
            else:
                print('Escolha Inválida, entre com o serviço 1, 2 ou 0')
        except:
            print('Erro: Por favor, digite a escolha 1, 2 ou 0')

escolha = escolha_servico() # Variavel que pega o retorno da função escolha_serviço
numero = int(input('Entre com a quantidade de páginas: ')) # input do usuário que sera tratada na função num_paginas
valor_desconto = num_paginas() # Variavel que pega o retorno da função num_paginas

extra = servico_extra() # Variavel extra pega o retorno da função serviõ_extra

total = escolha * valor_desconto + extra # Soma o valor final do usuário/cliente
print(f'Total: R${total:.2f} (Serviço: R${escolha:.2f} * páginas: {numero} + extra: R${extra:.2f})') # Saída mostrando o valor total e o valor discriminado