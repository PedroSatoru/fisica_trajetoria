from math import*


def menu():
    print("Escolha uma das opções abaixo")
    print("1. Movimento horizontal")
    print("2. Movimento vertical")
    print("3. Distância entre o projétil e a origem")
    print("4. Módulo da velocidade")
    print("5. Tempo de subida")
    print("6. Equação da trajetória")
    print("7. Altura máxima")
    print("8. Tempo de alcance")
    print("9. Alcance")

    opcao = int(input("Opção: "))
    return opcao

def menu_2():
    print("Que dado quer saber?")
    print("1. Altura")
    print("2. Vx")
    print("3. Vy")
    opcao = int(input("Opção: "))
    return opcao

'''mov horizontal'''
def mov_horizontal(x0, v0, t):
    return x0 + v0*t

'''mov vertical'''
def mov_vertical(y0, v0y, t):
    return y0 + v0y*t (-5*pow(t,2))

def vx(v, angulo):
    return v*cos(radians(angulo))

def vy(v, angulo):
    return v*sin(radians(angulo))

def tg(vx, vy):
    return vy / vx

'''Distância entre o projétil e a origem'''
def dist_proj_orig(x, y):
    return sqrt(pow(x,2) + pow(y,2))

''' Módulo velocidade'''
def v(vx, vy):
    return sqrt(pow(vx,2) + pow(vy,2))

'''Tempo subida'''
def tempo_sub(v0, angulo):
    return (v0*sin(radians(angulo)) / 10)

'''Eq trajetoria'''
def eq_traj(angulo, x, v0):
    return tan(radians(angulo)) * x - (0.5 * 10 * (x**2) / ((v0**2) * (cos(radians(angulo))**2)))


'''Altura máxima'''
def alt_max(v0, angulo):
    return 0.5*((pow(v0,2)*pow(sin(radians(angulo)), 2))/10)

'''tempo alcance'''

def temp_alc(tempo_sub):
    return tempo_sub * 2

'''Alcance'''
def alcance(v0, angulo):
    return (pow(v0,2) * sin(2*radians(angulo))/10)

a=alt_max(18.5,70)
print(a)
b=alcance(18.5,70)
print(b)