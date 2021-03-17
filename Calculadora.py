##Variáveis
soma = '+'
subt = '-'
multi = '*'
divi = '/'
porcen = '%'
sim = 'sim'
não = 'não'


print('###############################################'\
                    '\n\t\tCalculadora\n'
      '###############################################'

)
##Looping. Caso a opção  seja inválida, pergunte novamente

def calculator():
    while True:
        calc = input('Digite a operação que deseja fazer(+, -, *, /, %): ')
        if calc != soma and calc != subt and calc != multi and calc != divi and calc != porcen:
            print('Opção inválida')
            continue
        else:
            
            ##Inputs dos números para cálculo
            num1 = float(input('Digite um número: '))
            num2 = float(input('Digite outro número: '))
            
            
            ##Soma
            if calc == soma:
                soma1 = num1 + num2
                
                ##Se o número não fo decimal transforma em número inteiro
                if soma1 // 1 == soma1:
                    print('%.0f' % soma1)
                
                else:
                    print(soma1)
                break
            
            
            ##Subtração
            if calc == subt:
                subt1 = num1 - num2
                
                if subt1 // 1 == subt1:
                    print('%.0f' % subt1)
                
                else:
                    print(subt1)
                break
            
            
            ##Multiplicação
            if calc == multi:
                multi1 = num1 * num2
                
                if multi1 // 1 == multi1:
                    print('%.0f' % multi1)
                
                else:
                    print(multi1)
                break
            
            
            ##Divisão
            try:
                if calc == divi:
                    divi1 = num1 / num2
                    
                    
        
                    if divi1 // 1 == divi1:
                        print('%.0f' % divi1)
                    
                    else:
                        print(divi1)
                        break
            except ZeroDivisionError:
                print('Divisão por 0 não permitida')

            
            ##Porcentagem
            if calc == porcen:
                porcen1 = num1 * (num2/100)
                
                if porcen1 // 1 == porcen1:
                    print('%.0f' % porcen1)
                
                else:
                    print(porcen1)
                break
        break             

calculator()

##Looping. Caso queira fazer outro calculo
while True:
    question = input('Gostaria de fazer mais algum calculo?(Se sim digite sim, se não digite não):')
    if question == sim:
        calculator()
    else:
        break