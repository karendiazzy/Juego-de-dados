import random

def lanzar_dados():
    aleatorio1= random.randint(1,6)
    aleatorio2= random.randint(1,6)
    return aleatorio1 , aleatorio2
    
def evaluar_jugada(a,b):
    #Proporciona el resultado de estos dos dados
    suma_dados = a + b
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados >= 6 and suma_dados <10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados >= 10:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
        
num1,num2 = lanzar_dados()
evaluar_jugada(num1,num2)