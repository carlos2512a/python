cartas_naipes=int(input('cual es mi numero de carta'))

if cartas_naipes >=13:
    print('gane la apuesta')
elif cartas_naipes >=7: 
    print('empate la apuesta')
elif cartas_naipes >=4:
    print('perdi la apuesta')
else:
    print('programa terminado')