while True: 

     try: 

          valor = float(input('Digite o valor do produto: ')) 

          break

     except:
             
            print('Por favor, digite um valor válido!') 

while True:
    if valor <= 0:
        
        print('Por favor, digite um valor válido!')
       
        valor = float(input('Digite o valor do produto'))
    
    else:      
        print('Valor válido')
        
        break

print(''' 

Forma de Pagamento 

[1] Pagamento à vista,oferece 15% de desconto!

[2] Pagamento no cartão,oferece 5% de desconto!

[3] Pagamento no boleto,tem um aumento de 15% se escolher ate 6 parcelas. E tem um aumento de 30% se escolher acima de 6 parcelas!''') 
print()

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