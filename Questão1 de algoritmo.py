#Utilizei o while True para criar um loop,utilizei também o try e o except para tratar algumas exceções
#Utilizei também o break,caso o laço fosse verdadeiro,para que não se repetice novamente

while True: 

     try: 

          valor = float(input('Digite o valor do produto: ')) 

          break

     except:
             
            print('Por favor, digite um valor válido!') 

#Novamente utilizei while True,para criar outro loop,dentro do while utilizei um if com um valor abaixo ou igual a 0,assim o programa pede outro valor ao usuário
#Pedindo novamente um valor válido. E o else,caso o valor seja válido,será executado. E o programa continuará 

while True:
    if valor <= 0:
        
        print('Por favor, digite um valor válido!')
       
        valor = float(input('Digite o valor do produto'))
    
    else:      
        print('Valor válido')
        
        break

#Imprimi as opções que são informadas

print(''' 

Forma de Pagamento 

[1] Pagamento à vista,oferece 15% de desconto!

[2] Pagamento no cartão,oferece 5% de desconto!

[3] Pagamento no boleto,tem um aumento de 15% se escolher ate 6 parcelas. E tem um aumento de 30% se escolher acima de 6 parcelas!''') 
print()

#While True novamente,criando outro loop. Utilizei if para chegar o primeiro valor,caso fosse o escolhido
#Utilizei dois elif para chegar e executar as outras duas opções 
#No segundo elif,tem duas opções de parcelas que são informadas ao usuário,ao escolher uma das duas o programa executa as somas do escolhido
#Utilizei break em cada execução,para assim que o valor for informado,o programa ser finalizado 
#Por último tem um else,caso seja informado um valor errado,o programa irá pedir novamente um valor válido 

while True:
    op = input('Opção: ')
    print()
    
    if op == '1': 
          novo_valor = valor - 0.15 * valor
          print(f'O valor final é de: R${novo_valor:.2f}')
          
          break 

    elif op == '2': 

          novo_valor = valor - 0.05 * valor 
          print(f'O valor final é de: R${novo_valor:.2f}')

          break 
          
         
    elif op == '3':
             parcelas = int(input('Escolha uma parcela de 2 a 12: '))
         
    if parcelas <= 6 and parcelas >= 2:
             parcelas = valor + 0.15 * valor 
             print('O valor final é de: R${}'.format(parcelas))
         
    elif parcelas >= 7 and parcelas <= 12:
             parcelas = valor + 0.3 * valor
             print('O valor final é de: R${}'.format(parcelas))
             
             break

    else:
        print('Por favor, digite uma opção valida') 
