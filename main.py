nome = input("Digite seu nome: ")  #Inserindo valores string do teclado na variável nome.
idade = int(input("Digite sua idade: "))  #Inserindo valores inteiros, vindos do teclado, na variável idade.
peso = float(input("Digite seu peso: "))  #Inserindo valores float, vindos do teclado, na variável peso.

print(nome)  #Imprimindo no console a variável nome.
print(idade)  #Imprimindo no console a variável idade.
print(peso)  #Imprimindo no console a variável peso

print(type(nome))  #imprimindo no console o tipo da variável nome.
print(type(idade))  #Imprimindo no console o tipo da variável idade.
print(type(peso))  #Imprimindo no console o tipo da variável peso.

## OPERADORES ARITMETICOS

soma = 1 + 1  #Soma simples de dois fatores igual a outras linguagens.
subtracao = 2 - 4  #Subtração simples de dois fatores igual a outras linguagens.
multiplicacao = 4 * 4 #Multiplicação simples de dois fatores igual a outras linguagens.
divisao = 30 / 3  #Divisão de 30 por 3 = 10. Não retorna o módulo, igual as outras linguagens. Em python o módulo é diferente.
potencia = 7 ** 2  #Potencia. 7 elevado ao quadrado. Em python é diferente operar com potencia.
potencia2 = 7 ** 3  #Potencia. 7 elevado ao cubo. Em python é diferente operar com potencia.

print("Soma = ", soma)  #Imprime no console o texto entre aspas e apos a virgula as variaveis passadas na linha.
print("Subtração = ", subtracao)  #Imprime no console o texto passado entre aspas e apos a virgula a variavel passada na linha. 
print("Multiplicação = ", multiplicacao)  #Imprime no console o texto passado entre aspas e apos a virgula a variavel passada na linha.
print("Divisão = ", divisao)  #Imprime no console o texto passado entre aspas e apos a virgula a variavel passada na linha.
print("Potencia = ", potencia)  #Imprime no console o texto passado entre aspas e apos a virgula a variavel passada na linha.
print("Potencia2 = ", potencia2)  #Imprime no console o texto passado entre aspas e apos a virgula a variavel passada na linha.

# CONDICIONAIS IF/ELSE

if (idade >= 18) :  #Condição SE comn sintaxe diferente do habitual. Em python nao usamos {} para delimitar o bloco de código. Apenas : e a identação
    print("Pode entrar")
else :
    print("Não Pode Entrar")
    print("ainda no else")

print("Saimos")

salario = float(input("Digite seu salário: "))

if (salario <= 3000) :
    print("Junior")
elif (salario > 3000 and salario <= 6000) :  #Em python (&& = and) e (|| = or) operadores logicos são diferentes.
    print("Pleno")
elif (salario > 6000 and salario <= 15000) :  #Em python temos o (elif = else if ()). Diferente e mais prático.
    print("Sênior")
else :
    print("Gerente de Projeto")

# ARRAYS/LISTAS

array_numeros = [1,2,3]  #Array de numeros inteiros 1,2,3

print(array_numeros[0])  #Imprime no console os valores do array nas respectivas posições (index)
print(array_numeros[1])
print(array_numeros[2])

array_info = [nome, idade, peso]  #Array de string, int e float. Teste que retornou as informações corretas

print(array_info)

print(type(array_info))

lista_vazia = []

# lista_vazia.append("Olá")
# lista_vazia.append("Mundo")

lista_vazia.append(nome)  #Uso do .append() para inserir no final do array lista_vazia
lista_vazia.append(salario)

print(lista_vazia)

array_crescente = ["g","f","e","d","c","b","a"]

array_crescente.sort()  #Uso do .sort() para ordenar de forma crescente o array

print(array_crescente)

numeros = [10,9,8,7,6]

print("TOTAL = ", len(numeros))  #Retorna o tamanha do array = .length()
print("Menor Valor: ", min(numeros))  #Retorna o menor valor do array
print("Maior Valor: ", max(numeros))  #Retorna o maior valor do array

# LOOPS/REPETIÇÕES

for x in range(10) :  #Em python o for nao permite a condição entre (). retorna 0 até 9
    print(x)

# while (True) :  #Usando o while, a condição pode ser passada entre ();
#     print("Escrever até desligar")

total_alunos = int(input("Total de alunos: "))
# aux = 0  #Usando FOR nao precisamos do aux
notas = []
soma_nota = 0

# while (aux < total_alunos) :        #Estrutura de repetição com while que cria uma lista de notas+rm e calcula a média da turma
#     codigo_aluno = input("RM: ")
#     nota = float(input("Nota: "))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)
#     aux=aux+1
#     soma_nota = soma_nota + nota

for x in range(total_alunos) :   #Calculo de média dos alunos usando FOR
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    soma_nota = soma_nota + nota

media = soma_nota/len(notas)

print("Média da turma = ", media)

# OBJETOS

pessoa = {  #Criação do objeto pessoa
    "nome":"Albert Sevy",
    "idade": 34,
    "peso": 88.9
}

print(pessoa["nome"])  #Acesso as propriedades dos objetos é diferentre de JS. objeto["propriedade"]
print(pessoa["idade"])
print(pessoa["peso"])

#FUNÇÕES

def minha_funcao (valor1, valor2)  :  #def cria função em python
    return valor1 + valor2

resultado = minha_funcao(10,10)
print(resultado)


fluxo_caixa = []



print("-------------")
print("@ Fluxo de Caixa")
print("-------------")
print("1 - Adicionar Receita")
print("2 - Adicionar Despesa")
print("Digite outro número para encerrar")

def adiciona_fluxo (opcao) :
    if (opcao == "1") :
        nome = input("Nome da receita: ")
        valor = float(input("Total da receita: ")) 
        receita = {
            "descricao": nome,
            "valor": valor
        }
        fluxo_caixa.append(receita)


    elif (opcao == "2") :
        nome = input("Nome da despesa: ")
        valor = float(input("Total da despesa: "))
        valor = valor*(-1)
        despesa = {
            "descricao": nome,
            "valor": valor
        }
        fluxo_caixa.append(despesa)



while True :
    opcao = input("Digite sua opção: ")
    if (opcao == "1" or opcao == "2") :
        adiciona_fluxo(opcao)
    else :
        break

total = 0 
for x in fluxo_caixa :
    print("Nome: ", x["descricao"], "---", "Valor: ",x["valor"])
    total += x["valor"]

print ("Saldo final = R$ ", total)
