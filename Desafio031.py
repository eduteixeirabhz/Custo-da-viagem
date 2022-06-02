v = float(input('Qual é a  distância  de sua viagem? '))
print('Você está prestes a começar uma viagem de {} Km.'.format(v))
p = v*0.50
pl = v*0.45
if v <= 200:
    print('Sua viagem ficou em R$ {:.2f}'.format(p))
else:
    print(' Sua viagem ficou em R$ {:.2f}'.format(pl))
