#Questão 01
 #Ao final do processamento, o valor da variável SOMA será 78.


#Questão 02
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número: "))
if fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")



'''Questão 03
    a) 9
    b) 128
    c) 49
    d) 100
    e) 13
    f) 20
'''

'''Questão 04
    Ligaria primeiro interruptor e aguardaria alguns minutos, depois desligaria o primeiro interruptor e ligaria o segundo interruptor.
    Entreva na sala com as lâmpadas, onde a lâmpada acesa seria do segundo interruptor, a lâmpada desligada e quente corresponde ao
    primeiro interruptor e a lâmpada desligada e fria corresponde ao terceiro interruptor.
'''

#Questão 05
def inverter_string(s):
    resultado = ""
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

minha_string = input("Informe uma string: ")
string_invertida = inverter_string(minha_string)
print(f"String invertida: {string_invertida}")

