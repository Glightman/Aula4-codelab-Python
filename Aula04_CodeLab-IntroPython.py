#!/usr/bin/env python
# coding: utf-8

# In[1]:


# **Comando Print, Variáveis e Input**


# In[2]:


#Print é uma função que imprimi na tela o que a gente quer:

print('Hello World') #Sempre acompanhado de parênteses


# In[3]:


#Variável é um espaço na memória que guarda algum dado.

#Em Python todas as váriáveis precisam ser inicializadas com um valor:

idade = 23 #Variável idade que recebe o valor 23

print(idade)


# In[4]:


# Tipos de variáveis:
  # str = Valores entre aspas ''
  # int = Número inteiros
  # float = Números decimais
  # bool = Valores booleanos: True ou False

#Para descobrir qual é o tipo de uma variável eu preciso execultar:

idade = 23

print(type(idade)) #função type que identifica o tipo da var e função print para mostrar na tela


# In[5]:


# Para escrever um texto antes de mostrar o tipo podemos fazer o f string:

idade = 23

print(f'Sua var idade é do tipo: {type(idade)}') #Entre chaves coloque valores que não são string


# In[ ]:


#Para eu perguntar para o usuário a idade dele e apresentar na tela, posso usar input:

idade = input('Quantos anos você tem? ')

print(f'Que legal! Você tem {idade} anos')


# In[ ]:


# Uma forma de atribuir o mesmo valor a várias variáveis é:

peso = idade = quantidade = 60

print(f'Peso: {peso}, Idade: {idade}, Quantidade: {quantidade}')


# In[ ]:


# Você pode atribuir valores diferentes a variáveis diferentes na mesma linha:

inteiro, texto, booleano, flutuante = 23, "Olá", True, 23.5

# Para colocar cada item em uma linha é só adicionar um \n entre as informações:
print(f'Inteiro: {inteiro}\nTexto: {texto}\nBooleano: {booleano}\nFlutuante: {flutuante}')


# ## Exercícios
# 

# 01 - Elabore um programa que imprima na tela a seguinte frase `Olá Mundo! Esse é o meu primeiro programa`

# In[1]:


# Resposta:
print('Olá Mundo! Esse é meu primeiro programa')


# 02 - Elabore um programa que escreve seu nome completo na primeira linha, seu endereço na segunda e o CEP e telefone na terceira.  
# 
# **Exemplo:**
# ```
# Nome: Bruno Fabri
# Endereço: Rua ABC
# CEP: 002220-010
# ```

# In[4]:


# Resposta:
nome = ('Gabriel Santana')
endereço = ('Av Adno Musser')
CEP = ('45810-000')
print(nome)
print(endereço)
print(CEP)


# 03 - Elabore um programa que recebe o nome de uma pessoa do terminal e mostra a seguinte mensagem: `Olá {nome}! Seja bem vindo ao fantástico mundo da programação`

# In[12]:


# Resposta:
nome = input('qual o seu nome?')


# # **Operadores: Aritméticos, Relacionais e Lógicos**

# In[1]:


# Operadores Aritméticos:
  # + (Adição)
  # - (Subtração)
  # * (Multiplicação)
  # / (Divisão)
  # // (Divisão inteira)
  # ** (Exponenciação)
  # % (Resto da divisão(mod))

# Agora vamos solicitar um valor para o user, porém precisamos converter o valor input.
# Isso por que todo input devolve um valor str.
# E para realizar as operações precisamos de um valor int

#Para converter é só fazer isso:
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divInteira = n1 // n2
expo = n1 ** n2
mod = n1 % n2

print(f'{n1} + {n2} = {soma}')
print(f'{n1} - {n2} = {sub}')
print(f'{n1} * {n2} = {mult}')
print(f'{n1} / {n2} = {div}')
print(f'{n1} // {n2} = {divInteira}')
print(f'{n1} ** {n2} = {expo}')
print(f'{n1} % {n2} = {mod}')


# In[ ]:


#Para limitar as casas decimais de uma var float precisamos aplicar essa formatação:

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

div = n1 / n2

print(f'{n1} / {n2} = {div:.2f}')

# 2f é a quantidade de casas decimais desejadas.


# In[ ]:


# Operadores Relacionais
  # > (Maior que)
  # < (Menor que)
  # >= (Maior OU igual que)
  # <= (Menor OU igual que)
  # != (Diferente de)
  # == (Igual a)

  # Sempre retornam True ou False
  # São usados para comparar valores
  # Utilize a técnica de perguntar


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(f'{n1} é maior que {n2}? {n1 > n2}')
print(f'{n1} é menor que {n2}? {n1 < n2}')
print(f'{n1} é maior ou igual que {n2}? {n1 >= n2}')
print(f'{n1} é menor ou igual que {n2}? {n1 <= n2}')
print(f'{n1} é diferente de {n2}? {n1 != n2}')
print(f'{n1} é igual a {n2}? {n1 == n2}')


# In[ ]:


# Operadores Lógicos
  # and (E)
  # or  (OU)
  # not (Negação)

# Retorna True ou False
# Compara duas expreções relacionais

n1 = 1
n2 = 2
n3 = 3
n4 = 4

# Vamos perguntar: n1 é maior que n2 E n3 é menor que n4?
# A resposta só será True se TODAS as relações forem True:

print(n1 > n2 and n3 < n4) # Nesse caso da False, por que n1 não é maior que n2

# Vamos perguntar: n1 é maior que n2 OU n3 é menor que n4?
# A resposta será True se ao menos UMA relação for True:

print(n1 > n2 or n3 < n4) # Nesse caso da True, por que pelo menos n3 é menor que n4

# O operador NOT, serve para negar o resultado da operação.
# Ou seja, ele inverte o resultado, se for True, transforma em False e vice versa.

print(not n1 > n2) # Retorna True, por que o resultado de n1 maior que n2 é False

# Para negar uma operação composta de operadores relacionais e lógicos devemos usar as {}:

print(not {n1 > n2 or n3 < n4}) # Aqui retornaria True, se não fosse o not.


# ## Exercicios

# 04 - Elabore um programa que recebe dois valores inteiros e mostra a soma desses valores
# 
# **Exemplo:**
# 
# ```
# Primeiro Valor = 2
# Segundo Valor = 3
# Soma = 5
# ```

# In[ ]:


# Resposta:


# 05 - Elabore um programa que receba 4 notas de um aluno e calcule a média dele.
# 
# **Exemplo:**
# 
# ```
# Primeiro Nota = 7
# Segundo Nota = 8
# Terceiro Nota = 10
# Quarto Nota = 6
# 
# Média = 7,75
# ```

# In[ ]:


# Resposta:


# 06 - Elabore um programa que recebe dois valores inteiros e mostra se o primeiro valor é maior ou igual ao segundo valor
# 
# **Exemplo:**
# ```
# Primeiro Valor = 3
# Segundo Valor = 2
# Resultado = True
# ```

# In[ ]:


# Resposta:


# # **Manipulação de Strings**

# In[ ]:


# Uma string é uma sequência de caracteres simples. Na linguagem Python, 
# as strings são utilizadas com aspas simples ('...') ou aspas duplas ("...").

# Concatenação de Strings:

titulo = 'Programação '
linguagem = 'Python'
titulo_linguagem = titulo + linguagem # Concatenação das Strings (str)

print(titulo_linguagem)


# ## **Métodos de manipulação**

# In[ ]:


# Método len()

#Retorna o tamanho da string

titulo = 'Programação Python'

print(f'O tamanho da String titulo é: {len(titulo)}')


# In[ ]:


# Método capitalize()

# Retorna a string com a primeira letra maiúscula

titulo = 'python'

print(titulo.capitalize())


# In[ ]:


# Método count()

# Informa quantas vezes um caractere (ou uma sequência de caracteres) aparece na string.
# Distingue entre maiúsculas e minúsculas

titulo = 'Programação em Python'

print(titulo.count('a')) # Conte quantos caracteres 'a' eu tenho nessa string


# In[ ]:


# Método startswith()

# Verifica se uma string inicia com uma determinada sequência ou letra

titulo = 'Python'

print(titulo.startswith('Py')) # O retorno será True ou False


# In[ ]:


# Método endswith()​

# Verifica se uma string termina com uma determinada sequência ou letra.

titulo = 'Python'

print(titulo.endswith('Py')) # O retorno será True ou False


# In[ ]:


# Método isalnum()​

# Verifica se a string possui algum conteúdo alfanumérico (letra ou número).

simbolos = '!@#$%&'

print(simbolos.isalnum()) # O retorno será True ou False


# In[ ]:


# Método isalpha()​

# Verifica se a string possui apenas conteúdo alfabético (letras).

titulo = 'Python'

print(titulo.isalpha()) # O retorno será True ou False


# In[ ]:


# Método islower()

# Verifica se todas as letras de uma string são minúsculas​.

titulo = 'Python'

print(titulo.islower()) # O retorno será True ou False


# In[ ]:


# Método isupper()​

# Verifica se todas as letras de uma string são maiúsculas. 

titulo = 'PYTHON'

print(titulo.isupper()) # O retorno será True ou False


# In[ ]:


# Método lower()​

# Retorna uma cópia da string trocando todas as letras para minúsculo.

titulo = 'PYTHON'

print(titulo.lower())


# In[ ]:


# Método upper()​

# Retorna uma cópia da string trocando todas as letras para maiúsculo.

titulo = 'python'

print(titulo.upper())


# In[ ]:


# Método swapcase()​

# Inverte o conteúdo da string (Minúsculo / Maiúsculo).​

titulo = 'Python'

print(titulo.swapcase())


# In[ ]:


# Método title()​

# Converte para maiúsculo todas as primeiras letras de cada palavra da string.

titulo = 'Programação em python'

print(titulo.title())


# In[ ]:


# Método split()​

# Transforma a string em uma lista, utilizando os espaços como referência. ​

titulo = 'Programação em Python'

print(titulo.split())


# In[ ]:


# Método replace(S1, S2)

# Substitui na String o techo de S1 pelo trecho S2

titulo = 'Programação em Java'

print(titulo.replace('Java', 'Python'))


# In[ ]:


# Método find()​

# Retorna o índice (posição) da primeira ocorrência de um determinado caractere na string.
# Se o caractere não estiver na string retorna -1.

titulo = 'Programação em Python'

print(titulo.find('j'))

print(titulo.find('o'))


# In[ ]:


# Método ljust()​

# Ajusta a string para um tamanho mínimo, acrescentando espaços à direita se necessário.​

titulo = 'Python'

print(f'*{titulo.ljust(15)}*') # 15 é o número de espaço que eu quero que o titulo ocupe.


# In[ ]:


# Método center()​

# Ajusta a string para um tamanho mínimo, acrescentando espaços à esquerda e à direita, se necessário.

titulo = 'Python'

print(f'*{titulo.center(20)}*') # 20 é o número de espaço que eu quero que o titulo ocupe.


# In[ ]:


# Método rjust()​

# Ajusta a string para um tamanho mínimo, acrescentando espaços à esquerda se necessário.​

titulo = 'Python'

print(f'*{titulo.rjust(30)}*') # 30 é o número de espaço que eu quero que o titulo ocupe.


# In[ ]:


# Método strip()​

# Remove todos os espaços em branco da string.

titulo = '   Python   '

print(f'*{titulo.strip()}*')


# ## **Fatiamento de Strings**

# In[ ]:


# Serve para retornar apenas uma parte da String

# Uma String é uma lista de caracteres, essa lista começa em 0 sempre:

  # 'Python'
  #  012345
    # Posição 0 = P
    # Posição 1 = y
    # Posição 2 = t
    # Posição 3 = h
    # Posição 4 = o
    # Posição 5 = n

# IMPORTANTE: Os espaços são caracteres também!

titulo = 'Programação com Python'

print(titulo[0]) # Retorna o primeiro caractere

print(titulo[-1]) # Retorna o último caractere

print(titulo[2:15]) # Retorna os caracteres da posição 2 até a posição 14 (desconsidera a posição 15)

print(titulo[:15]) # Retorna os caracteres da posição 0 até a posição 14 (desconsidera a posição 15)

print(titulo[6:]) # Retorna os caracteres da posição 6 até a última posição

print(titulo[2:15:2]) # Retorna os caracteres da posição 2 até a posição 14 pulando de 2 em 2


# ## Exercícios

# 07 - Considere a string A = "Os limites só existem se você os deixar existir.(goku)".
# 
# Que fatia corresponde a (goku)?

# In[ ]:


# Resposta:


# 08 - Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em maiúscula e sem espaços em branco.

# In[ ]:


# Resposta:


# 09 - Elabore um programa que recebe o seu nome, endereço e hobby e mostra cada uma das informações da seguinte forma:
# - Nome -> Letra maiúscula
# - Endereço -> Letra minúscula
# - Hobby -> Primeira letra maiúscula
# 
# **Exemplo Entrada:**
# ```
# Nome: bruno fabri
# Endereço: Rua ABC
# Hobby: jogar cs
# ```
# 
# **Exemplo Saída:**
# ```
# Nome: BRUNO FABRI
# Endereço: rua abc
# Hobby: Jogar cs
# ```

# In[ ]:


# Resposta:


# # **Mini projetos**

# ```
# # Isto está formatado como código
# ```
# 
# ## Mini Projeto 01 - Conversor de Moeda
# Vamos construir um programa que irá converter moedas do real para o dólar e do dólar para o real. Vamos considerar que `$ 1,00 = R$ 5,75`
# 
# ### Parte 1
# Faça o conversor de moeda receber o valor em real e mostrar o valor convertido para dólar no formato `$ XXXX.XX`
# 
# **Exemplo:**
# 
# ```
# Valor em R$ = 1000
# Valor em $ = $ 173.91
# ```
# 
# ### Parte 2
# Altere o conversor de moedas para receber o valor em dólar, converter para real e mostrar o resultado no formato `R$ XXXX.XX`
# 
# **Exemplo:**
# ```
# Valor em $ = 1000
# Valor em R$ = R$ 5750.00
# ```

# In[2]:


# Resposta Parte 1
real=float(input('Digite um valor em reais R$'))
vreal=5.75
conv=real/vreal
print(f'Esse valor em dolar é: $ {conv:.2f}')


# In[1]:


# Resposta Parte 2
dolar=float(input('Digite um valor em dolares $'))
vreal=5.75
conv=vreal*dolar
print(f'Esse valor em reais é: R$ {conv:.2f}')


# ## Mini Projeto 02 - Calculadora de aumento de aluguel
# Vamos construir um programa que irá calcular o aumento anual do seu aluguel em duas partes:
# 
# ### Parte 1
# A sua calculadora vai receber o `valor do aluguel` e calcular o aumento baseado no `IGPM de 31%`. A calculadora deve apresentar o aluguel reajustado no formato `R$ XXXX.XX`
# 
# **Exemplo:**
# ```
# Valor do aluguel = 1000
# Valor do aluguel reajustado = R$ 1310,00
# ```
# 
# ### Parte 2
# Agora, altere sua calculadora para receber além do `valor do aluguel`, o percentual do reajuste no formato `XX%`.  
# 
# **Dica:** Descubra uma forma de transformar o percentual recebido em um número para efetuar o cálculo.
# 
# **Exemplo:**
# ```
# Valor do aluguel = 1000
# Percentual do reajuste = 31%
# Valor do aluguel reajustado = R% 1310,00
# ```

# In[28]:


# Resposta Parte 1
valor_do_aluguel = float(input('Digite o valor do seu aluguel:'))
reajuste = 31/100
cal = valor_do_aluguel*reajuste
valor_final = cal+valor_do_aluguel
print(f'O valor do seu aluguel em 1 ano será: R$ {valor_final:.2f}')


# In[12]:


# Resposta Parte 2
valor_do_aluguel = float(input('Digite o valor do seu aluguel:'))
reajuste = (input('Agora digite o valor do reajuste anual:'))
porcent = reajuste.replace('%','')
porcent = float(porcent)
cal_porcent = porcent/100
cal = valor_do_aluguel*cal_porcent
valor_final = cal+valor_do_aluguel
print(f'O valor do seu aluguel depois de 1 ano será: R$ {valor_final:.2f}')


# ## Mini Projeto 03 - Calculadora de dano
# Vamos implementar a calculadora de dano de RPG!!
# 
# ### Parte 1
# O programa vai receber a `vida e um monstro (entre 10 e 50)` e o `valor do ataque do jogador por turno (entre 5 e 10)`
# 
# Baseado nos valores, exiba a quantidade de turnos que o jogador irá demorar para conseguir derrotar o monstro.
# 
# **Exemplo:**
# ```
# Vida de um monstro (entre 10 e 50): 26
# Valor do ataque do jogador por turno (entre 5 e 10): 5
# Resultado: O jogador irá precisar de 6 turnos para derrotar o monstro.
# ```
# 
# ### Parte 2
# Altere o programa para ao invés de receber a vida do monstro, gerar aleatoriamente um valor entre 10 e 50.

# In[32]:


# Resposta Parte 1
monstro = int(input('insira a vida do monstro entre 10 e 50:'))
ataque = int(input('insira o valor do ataque entre 5 e 10:'))
cal = monstro/ataque
print('O jogador irá precisar de 'f'{round(cal+0.5)} turnos para derrotar o monstro.')


# In[3]:


# Resposta Parte 2

