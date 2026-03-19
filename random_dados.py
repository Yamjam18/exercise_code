import random

def lanzar_dado(caras=6):
  return random.randint(1,caras)

def simulador():
  print(" == Simulador de lanzamiento de dados ==")

  cantidad = int(input("Cuantos dados quieres lanzar ? --> "))
  caras = int(input("Cuantas caras tiene cada dado ? --> "  ))

  resultados = []

  for i in range(cantidad):
    resultado = lanzar_dado(caras)
    resultados.append(resultado)

  print("\n Resultados: ",resultados)
  print("\n Suma total: ",sum(resultados))

simulador()
