import math

print("Digite as informações abaixo. Se você não possui uma informação, digite '/'\n")

# Entrada de dados
v0_input = input("Digite o valor de V0 em m/s (ou '/'): ")
Vx_input = input("Digite a velocidade horizontal Vx (ou '/'): ")
alpha_input = input("Digite o valor do ângulo em graus (ou '/'): ")
altura_input = input("Digite a altura inicial em metros (ou '/'): ")
gravidade_input = input("Digite a gravidade referente (ou '/'): ")
inst_input = input("Digite o valor do instante em que deseja calcular X e Y (ou '/'): ")

# Verificação das entradas
if v0_input != '/':
    v0 = float(v0_input)
else:
    v0 = None
    tempo_Hmax=0
    Hmax=altura_input
    V0y= 0

  

if Vx_input != '/':
    Vx = float(Vx_input)
    V0x = Vx
    tempo = math.sqrt((2 * float(altura_input)) / float(gravidade_input))
    
    distancia = Vx * tempo 

    Vy = float(gravidade_input) * -tempo
else:
    Vx = None

if alpha_input != '/':
    alpha = float(alpha_input)
else:
    alpha = None

if altura_input != '/':
    altura = float(altura_input)
else:
    altura = None

if gravidade_input != '/':
    gravidade = float(gravidade_input)
else:
    gravidade = None

if inst_input != '/':
    inst = float(inst_input)
else:
    inst = None

# Cálculo de V0x e V0y, se V0 e alpha forem fornecidos
tempo_total=0
if v0 is not None and alpha is not None:
    alpha_rad = math.radians(alpha)
    V0x = v0 * math.cos(alpha_rad)
    V0y = v0 * math.sin(alpha_rad)
    print(f"V0x = {V0x}")
    print(f"V0y = {V0y}")
    print("")

# Cálculo do tempo total de voo da bola, se V0y, gravidade e altura forem fornecidos
if V0y is not None and gravidade is not None and altura is not None:
    tempo_total = (V0y + math.sqrt(V0y**2 + 2 * gravidade * altura)) / gravidade
    print(f"Tempo em que a bola permanece no ar = {tempo_total}")
else:
    tempo_total = tempo
    print(f"Tempo em que a bola permanece no ar = {tempo_total}")

# Cálculo do tempo de subida da bola, se V0y e gravidade forem fornecidos
if V0y is not None and gravidade is not None:
    tempo_Hmax = V0y / gravidade
    print(f"Tempo de subida da bola = {tempo_Hmax}")
    print("")

# Cálculo de Px, se V0x e inst forem fornecidos
if  V0x is not None and inst is not None:
    Px = V0x * inst
    print(f"No instante t = {inst}")
    print(f"Posição da Bola em X no instante dado = {Px}")

# Cálculo de Py, se V0y, gravidade, altura e inst forem fornecidos
if V0y is not None and gravidade is not None and altura is not None and inst is not None:
    Py = altura + (V0y * inst) - (0.5 * gravidade * inst**2)
    print(f"Posição da Bola em Y no instante dado = {Py}")
    print("")

# Cálculo de Hmax, se V0y, gravidade e inst forem fornecidos
if altura is not None and V0y is not None and tempo_Hmax is not None:
    Hmax = float(altura) + (float(V0y) * float(tempo_Hmax)) - (0.5 * float(gravidade) * float(tempo_Hmax)**2)
    print(f"Altura máxima atingida na trajetória = {Hmax}")
else:
    Hmax=altura_input
    print(f"Altura máxima atingida na trajetória = {Hmax}")

# Cálculo da velocidade no instante em que a bola atinge a altura máxima e suas componentes nos eixos x e y
if tempo_Hmax is not None and V0x is not None and V0y is not None:
    Vx_Hmax = V0x
    Vy_Hmax =0
    Vec_V_Hmax = math.sqrt(Vx_Hmax**2 + Vy_Hmax**2)
    print("Velocidade da bola no instante em que atinge a altura máxima:")
    print(f"Velocidade de X na altura maxima = {Vx_Hmax}")
    print(f"Velocidade de Y na altura maxima = {Vy_Hmax}")
    print(f"Módulo do vetor V na altura maxima= {Vec_V_Hmax}") 
    print("")
elif tempo_Hmax is not None:
    Vx_Hmax = Vx
    Vy_Hmax =0
    Vec_V_Hmax = math.sqrt(Vx_Hmax**2 + Vy_Hmax**2)
    print("Velocidade da bola no instante em que atinge a altura máxima:")
    print(f"Velocidade de X na altura maxima = {Vx_Hmax}")
    print(f"Velocidade de Y na altura maxima = {Vy_Hmax}")
    print(f"Módulo do vetor V na altura maxima= {Vec_V_Hmax}") 
    print("")




# Cálculo de Dmax, se V0x e tempo_total forem fornecidos
if V0x is not None and tempo_total is not None:
    Dmax = V0x * tempo_total
    print(f"Distância máxima percorrida pela bola = {Dmax}")
    print("")

# Cálculo de Vx, se V0x for fornecido
if V0x is not None:
    Vx = V0x
    print(f"Velocidade de X no instante dado = {Vx}")

# Cálculo de Vy, se V0y, gravidade e inst forem fornecidos
if V0y is not None and gravidade is not None and inst is not None:
    Vy = V0y - (gravidade * inst)
    print(f"Velocidade de Y no instante dado = {Vy}")
    

# Cálculo do módulo do vetor velocidade (Vec_V), se Vx e Vy forem fornecidos
if Vx is not None and Vy is not None:
    Vec_V = math.sqrt(Vx**2 + Vy**2)
    print(f"Módulo do vetor V no instante dado = {Vec_V}")
    print("")


# Cálculo da velocidade da bola imediatamente antes de alcançar o solo e suas componentes nos eixos x e y
if tempo_total is not None and V0x is not None and V0y is not None:
    Vx_solo = V0x
    Vy_solo = V0y - (gravidade * tempo_total)
    Vec_V_solo = math.sqrt(Vx_solo**2 + Vy_solo**2)
    print("Velocidade da bola imediatamente antes de alcançar o solo:")
    print(f"Velocidade de X = {Vx_solo}")
    print(f"Velocidade de Y = {Vy_solo}")
    print(f"Módulo do vetor V = {Vec_V_solo}")
    print("")

