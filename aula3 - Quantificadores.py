# Metacaracteres: ^ * + ? $ ( )
# * = 0 ou n (Não existir ou ilimitada vezes)
# + = 1 ou n (Tem que existir um ou ilimitada vezes)
# ? = 0 ou 1 (Não existir ou existir apenas um)
# {n} = repetir especificamente um valor 
# {min, max} = especificar um valor minimo e um valor maximo para repetir

import re

texto = '''

Alice e o Tempo

O Tempo: -Sim?
Alice: -Eu sei que você tentou me avisar e eu não escutei, me desculpe. Eu pensava que o tempo era um ladrão, 
        que roubava tudo que eu amava, mas agora eu vejo que você dá antes de tomar e cada dia um presente, 
        a cada hora, a cada minuto, a cada segundo.
O Tempo: -Ah o soldado caído, você quer que eu o concerte?
Alice: -Não, eu quero que fique com ele, ele dizia que a única coisa que valia a pena era o que fazíamos pelos outros, 
        ele teria gostado de você...
O Tempo: -Huum... Mas dizem que o tempo não é amigo de ninguém, mas eu lembrarei de você sempre e por favor não volte mais.

teeeeeeeeeeeeeeeeemmmpooooooooo
teeempoo
Alice Através Do Espelho -  Charles Lutwidge Dogson (Lewis Carroll)
'''

print(re.findall(r'Te+m+po+', texto, flags=re.I)) # Quantifica o item sempre a esquerda 
print(re.findall(r'te{1,}m{1,}po{1,}', texto, flags=re.I))
print(re.findall(r'te{3}mpo{1,2}', texto, flags=re.IGNORECASE))
