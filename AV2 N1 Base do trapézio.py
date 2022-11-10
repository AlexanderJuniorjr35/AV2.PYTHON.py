import time

print ("\nCálculo da área do trapézio")
time.sleep(2)

bma = float(input("\nDigite a base MAIOR do trapézio: "))

bmm = float(input("\nDigite a base MENOR do trapézio: "))

alt = float(input("\nDigite a ALTURA do trapézio: "))

area = (( bma + bmm ) * alt ) / 2

print (f"\nA Área do Trapézio é :{area}")
time.sleep(10)
