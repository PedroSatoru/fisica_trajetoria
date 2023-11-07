import math

print("Digite as informações abaixo, caso vc não possua digite '/' ")


'informações'
v0 = float(input("Digite o valor de V0 em m/s\n"))
Vx = float(input("Digite a velocidade horizontal Vx\n"))
alpha = float(input("Digite o valor do angulo\n"))
altura = float(input("Digite a altura em Metros\n"))
gravidade = float(input("Diga a gravidade referente\n"))
inst = float(input("Digite o valor do instante em que deseja calcular X e Y\n"))

  
'Calculo de V0y e V0x'
alpha_rad = math.radians(alpha) 
V0x = v0 * (math.cos(alpha_rad))
V0y = v0 * (math.sin(alpha_rad))
print("V0x = ",V0x )
print("V0y = ", V0y)
'tempo total em que a bola permanece no ar é dada pela formula a baixo'
tempo_total = (V0y + math.sqrt((V0y**2) + 2 * gravidade * altura)) / gravidade
print("tempo em que a bola permanece no ar =",tempo_total)
'tempo quanto o objeto esta na altura max'
tempo_Hmax = V0y / gravidade
Px = V0x * inst
Py = altura + (V0y * inst) - ((gravidade/2) * (inst**2))
print("no instante t = ",inst)
print("Posiçao da Bola em X no instante dado =", Px)
print("Posiçao da Bola em Y no instante dado =", Py)
Vx = V0x
print("Velocidade de X no instante dado =", Vx)
Vy1 = V0y - (gravidade * inst)
print("Velocidade de Y no instante dado =", Vy1)

Vec_V1 = math.sqrt(Vx**2 + Vy1**2)
print("Modulo do vetor V no instante dado =",Vec_V1)
print("")


# Cálculo da altura máxima alcançada pela bola
Hmax = altura + (V0y * tempo_Hmax) - ((gravidade / 2) * (tempo_Hmax**2))
print("Altura máxima alcançada pela bola =", Hmax)

# Cálculo da distância máxima alcançada pela bola
Dmax = V0x * tempo_total
print("Distância percorrida pela bola =", Dmax)

# Velocidade da bola imediatamente antes de alcançar o solo e suas componentes nos eixos x e y
print("No instante t =", tempo_total)
print("Velocidade de X na distância total =", Vx)
Vy2 = V0y - (gravidade * tempo_total)
print("Velocidade de Y na distância total =", Vy2)
Vec_V2 = math.sqrt(Vx**2 + Vy2**2)
print("Módulo do vetor V na distância total =", Vec_V2)

# Velocidade no instante em que a bola atinge a altura máxima e suas componentes nos eixos x e y
print("No instante t =", tempo_Hmax)
print("Velocidade de X na altura máxima =", Vx)
Vy3 = V0y - (gravidade * tempo_Hmax)
print("Velocidade de Y na altura máxima =", Vy3)
Vec_V3 = math.sqrt(Vx**2 + Vy3**2)
print("Módulo do vetor V na altura máxima =", Vec_V3)

# Verifica se o usuário possui V0 e altura
questao2 = input("Você possui V0 e ângulo? Responda sim ou não\n")
if questao2 == "sim":
    # Entrada de dados
    V0 = float(input("Digite o valor de V0 em m/s\n"))
    angulo = float(input("Digite o valor do ângulo\n"))
    
    # Cálculo de V0y e V0x
    alpha_rad = math.radians(angulo)
    V0x = V0 * (math.cos(alpha_rad))
    V0y = V0 * (math.sin(alpha_rad))
    print("V0x = ", V0x)
    print("V0y = ", V0y)
    
    # Entrada da gravidade
    gravidade = float(input("Digite a gravidade referente\n"))
    
    # Cálculo do tempo total em que a bola permanece no ar
    tempo_total = (V0y + math.sqrt((V0y**2) + 2 * gravidade * 0)) / gravidade
    
    # Cálculo do tempo quando o objeto está na altura máxima
    tempo_Hmax = V0y / gravidade
    Hmax = (V0y * tempo_Hmax) - ((gravidade / 2) * (tempo_Hmax**2))
    print("Altura máxima alcançada pela bola =", Hmax)
    
    # Cálculo da distância máxima alcançada pela bola
    Dmax = V0x * tempo_total
    print("Distância percorrida pela bola =", Dmax)
    
    # Velocidade na altura máxima
    print("Velocidade de X =", V0x)
    Vy = V0y - (gravidade * tempo_Hmax)
    print("Velocidade de Y =", Vy)
    Vec_V = math.sqrt(V0x**2 + Vy**2)
    print("Módulo do vetor V =", Vec_V)

    # Entrada do instante
    inst = float(input("Digite o valor do instante em que deseja calcular X e Y\n"))
    
    # Posição em X e Y no instante informado
    tempo_Hmax = V0y / gravidade
    Px = V0x * inst
    Py = Hmax + (V0y * inst) - ((gravidade / 2) * (inst**2))
    print("No instante t =", inst)
    print("Posição da Bola em X no instante dado =", Px)
    print("Velocidade de X no instante dado =", V0x)
    Vy1 = V0y - (gravidade * inst)
    print("Velocidade de Y no instante dado =", Vy1)
    Vec_V1 = math.sqrt(V0x**2 + Vy1**2)
    print("Módulo do vetor V no instante dado =", Vec_V1)


else:
    questao2 = input("Voce possui V0 e angulo? responda sim ou não\n")
    if questao2 == "sim":
      'informações dada pela questao'
      V0 = float(input("Digite o valor de V0 em m/s\n"))
      print("")
      angulo = float(input("Digite o valor do angulo\n"))
      print("")
      
      'Calculo de V0y e V0x'
      alpha_rad = math.radians(angulo) 
      'é necessario pq o python calcula em graus'
      V0x = V0 * (math.cos(alpha_rad))
      V0y = V0 * (math.sin(alpha_rad))
      print("V0x = ",V0x )
      print("")
      print("V0y = ", V0y)
      print("")

      'gravidade padrao usada '
      gravidade = float(input("Diga a gravidade referente\n"))
      print("")
      'tempo total em que a bola permanece no ar é dada pela formula a baixo'
      tempo_total = (V0y + math.sqrt((V0y**2) + 2 * gravidade * 0)) / gravidade

      'tempo quanto o objeto esta na altura max'
      tempo_Hmax = V0y / gravidade
      '''
      Altura maxima alcançada pela bola dada pela formula padrao 
      Y = Y0 + V0y*t - 1/2 * g * t**2 
      O tempo usado é quando a bola esta em sua altura max
      '''
      Hmax = (V0y * tempo_Hmax) - ((gravidade / 2) * (tempo_Hmax**2))
      print("Altura maxima alcançada pela bola =", Hmax)
      print("")

      '''
      Distancia maxima alcançada pela bola dada pela formula padrao 
      X = X0 + V0x * t
      O tempo usado é o tempo total ou o tempo que a bola permanece no ar
      '''
      Dmax = V0x * tempo_total
      print("distancia percorrida pela bola =", Dmax)
      print("")

      '''
      Usamos o tempo quando a bola esta na altura max pois a questão pedia 
      d)  Em seu ponto mais alto, ache os componentes horizontal e 
      vertical de sua velocidade.
      '''

      'Vx não é calculado novamente popis Vx sempre sera o mesmo'
      print("Velocidade de X =", V0x)
      print("")
  
      Vy = V0y - (gravidade * tempo_Hmax)
      print("Velocidade de Y =", Vy)
      print("")
  
      Vec_V = math.sqrt(V0x**2 + Vy**2)
      print("Modulo do vetor V =",Vec_V)

      inst = float(input("Digite o valor do instante em que deseja calcular X e Y\n"))
    print("")

    'tempo quanto o objeto esta na altura max'
    tempo_Hmax = V0y / gravidade

  
    'Posição em X no tempo pedido neste caso no instante 1,58'
    Px = V0x * inst
    'Posição em Y no tempo pedido neste caso no instante 1,58'


    print("no instante t = ",inst)
    print("")
    print("Posiçao da Bola em X no instante dado =", Px)
    print("")
  

    'Velocidade em X no mesmo instante usado anteriormente 1,58'
    Vx = V0x
    print("Velocidade de X no instante dado =", Vx)
    print("")
  
    'Velocidade em Y no mesmo instante usado anteriormente 1,58'
    Vy1 = V0y - (gravidade * inst)
    print("Velocidade de Y no instante dado =", Vy1)
    print("")

    '''
    Vec = modulo de V que é dado pela formula raiz quadrada da
    velocidade em X ao quadrado 
    mais a velocidade em Y ao quadrado
    '''
    Vec_V1 = math.sqrt(Vx**2 + Vy1**2)
    print("Modulo do vetor V no instante dado =",Vec_V1)
    print("")

    '''
    Altura maxima alcançada pela bola dada pela formula padrao 
    Y = Y0 + V0y*t - 1/2 * g * t**2 
    O tempo usado é quando a bola esta em sua altura max
    '''
    

    '''
    Distancia maxima alcançada pela bola dada pela formula padrao 
    X = X0 + V0x * t
    O tempo usado é o tempo total ou o tempo que a bola permanece no ar
    '''
    Dmax = V0x * tempo_total
    print("distancia percorrida pela bola =", Dmax)
    print("")

    '''
    Usamos o tempo total pois a questão pedia 
    g) Calcule a velocidade da bola imediatamente antes de alcançar o solo e 
    suas componentes nos eixos x e y.
    '''

    'Vx não é calculado novamente popis Vx sempre sera o mesmo'
    print("no instante t = ", tempo_total)
    print("")
    print("Velocidade de X na distancia total =", Vx)
    print("")
  
    Vy2 = V0y - (gravidade * tempo_total)
    print("Velocidade de Y na distancia total =", Vy2)
    print("")
  
    Vec_V2 = math.sqrt(Vx**2 + Vy2**2)
    print("Modulo do vetor V na distancia total =",Vec_V2)
    print("")

    '''
    Usamos o tempo quando a bola esta na altura max pois a questão pedia 
    h) Calcule a velocidade no instante em que a bola atinge a altura
    máxima e suas componentes nos eixos x e y.
    '''

    'Vx não é calculado novamente popis Vx sempre sera o mesmo'
    print("no instante t = ", tempo_Hmax)
    print("")
    print("Velocidade de X na altura max =", Vx)
    print("")
  
    Vy3 = V0y - (gravidade * tempo_Hmax)
    print("Velocidade de Y na altura max =", Vy3)
    print("")
  
    Vec_V3 = math.sqrt(Vx**2 + Vy3**2)
    print("Modulo do vetor V na altura max =",Vec_V3)













if questao2=="não":
    questao3 = input("Voce possui V0 e altura? responda sim ou não\n")
    if questao3 == "sim":
        
        'informações dadas pela questao'
      
        V0 = float(input("Digite a velocidade constante V0 em m/s\n"))
        altura = float(input("Digite a altura inicial em metros\n"))
        'gravidade padrao usada '
        g = float(input("Diga a gravidade referente\n"))
      
        tempo = math.sqrt((2 * altura) / g)
        '''
        dada pela qestão
        a distância horizontal entre a extremidade da mesa e o ponto onde ele atingiu o solo;
        '''
        distancia = V0 * tempo 
        print("Distancia horizontal em m =", distancia)
      
     