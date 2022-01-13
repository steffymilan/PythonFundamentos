# # REVIEW DE VARIÁVEIS, TIPOS E ESTRUTURAS DE DADOS

# ## Números e Operações Matemáticas

# In[ ]:


## 2 Tipos principais de números > int e float

## int são para números inteiros ex: -1 e 1
## float são números decimais ex: -1.1 e 1.1


# In[5]:


## type() é usado para saber o tipo de número
## print() é usado para imprimir a informação contida no parenteses

teste1 = type(2.4)

teste2 = type(2)

print(teste1)

print(teste2)


# In[8]:


## Usar as funções int() e float() convertem os números para as respectivas funções chamadas
## Ao usar a função int() não ocorre um arredondamento, ele apenas tira os valores decimais do número


int(3.9)


# In[7]:


float(3)


# ### Operações com números

# In[12]:


## soma (+)

1+1


# In[14]:


## Subtração (-)

1-1


# In[13]:


## Multiplicação (*)

1*1


# In[16]:


## Divisão (/)

10/2


# In[17]:


## Módulo (%) seria o resto da divisão

5%2


# In[19]:


## Potência (**)

4**2


# ### Operações Relacionais

# In[ ]:


## Igualdade (==)
## Desigualdade (!=)
## Maior que (>)
## Menor que (<)
## Maior ou igual a (>=)
## Menor ou igual a (<=)


# ### Operadores de Atribuição

# In[21]:


## Atribuição (=)

a=1

a


# In[28]:


## Soma (+=)
## a=1 + 1 = 2
a += 1

a


# In[24]:


## Subtração (-=)
## a = 2 - 1 = 1

a -= 1

a


# In[ ]:


## Em geral utiliza a mesma simbologia dos operadores relacionais seguidos de um símbolo de igual (=)
## isso ajuda a otimizar o código, ao invés de duas operações, é feito com apenas uma.


# ### Operadores Lógicos

# In[27]:


## and, or e not
## and - Se ambos forem true, retorna true
## or - Se um dos operadores for true, retorna true
## not - Reverte a lógica


# ### Variáveis

# In[ ]:


## Regras ao definir variáveis

# 1- Não podem começar com número
# 2- Não pode ter espaço (Utilize _ ao invés disso)
# 3- Não pode utilizar nenhum dos símbolos: '",<>/|()@#$%^&*~-+!
# 4- Palavras reservadas como nome de variável ex: false, true, if..


# ## Strings

# In[ ]:


## String gravam informações em formato de texto, são caracteres em sequência.
# SÃO IMUTÁVEIS
## Por se tratar de uma sequência, as strings podem ser indexadas, ou seja, pode usar partes da sequência.
## Utiliza-se colchetes [] para representar o índice de um objeto.
# A INDEXAÇÃO COMEÇA NO 0.


# In[30]:


texto = "Python"

texto[0]


# ### Funções built-in

# In[ ]:


## Atributos- propriedas
## Métodos- rotinas associadas as propriedades

# Acessador ao utilizar um ponto (.)


# In[ ]: