# https://docs.python.org/pt-br/3.8/howto/regex.html 

import re

# findall - Encontra todas as substrings onde a RE corresponde, e as retorna como uma lista.
# search - Varre toda a string, procurando qualquer local onde esta RE tem correspondência.
# sub - Varre toda a string e substitui a RE correspondente.  
# compile - Para reutilizar as RE se for necessário.

frase = 'Esta frase é para testar modulos'

print(re.search(r'testar', frase))
print(re.findall(r'testar', frase))
print(re.sub(r'testar', 'TROCOU AQUI', frase))

# Evita que o python tenha que compilar uma RE todas as vezes que ela for utilizada
regexp = re.compile(r'testar')
print(regexp.search(frase))
print(regexp.findall(frase))
print(regexp.sub('TROCOU AQUI PELO COMPILE', frase))