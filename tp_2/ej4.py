
dinero = float(input("Cantidad de dinero:"))
bill200 = 0
bill100 = 0
bill50 = 0
bill20 = 0
bill10 = 0
bill5 = 0
bill2 = 0
bill1 = 0
bill050 = 0
bill025 = 0
bill010 = 0
bill005 = 0
while dinero >= 200:
    bill200 = bill200 + 1
    dinero = dinero - 200  

while dinero >= 100:
    bill100 = bill100 + 1
    dinero = dinero -100

while dinero >= 50:
    bill50 = bill50 + 1
    dinero = dinero - 50

while dinero >= 20:
    bill20 = bill20 + 1
    dinero = dinero - 20

while dinero >= 10:
    bill10 = bill10 + 1
    dinero = dinero - 10

while dinero >= 5:
    bill5 = bill5 + 1
    dinero = dinero - 5

while dinero >= 2:
    bill2 = bill2 + 1
    dinero = dinero - 2

while dinero >= 1:
    bill1 = bill1 + 1
    dinero = dinero - 1

while dinero >= 0.50:
    bill050 = bill050 + 1
    dinero = dinero - 0.50

while dinero >= 0.25:
    bill025 = bill025 + 1
    dinero = dinero - 0.25

while dinero >= 0.10:
    bill010 = bill010 + 1
    dinero = dinero - 0.10

while dinero >= 0.049:
    bill005 = bill005 + 1
    dinero = dinero - 0.05

print(f"Billetes necesitados: {bill200} billetes de 200, {bill100} billetes de 100, {bill50} billetes de 50, {bill20} billetes de 20, {bill10} billetes de 10, {bill5} billetes de 5, {bill2} billetes de 2, {bill1} billetes de 1, {bill050} monedas de 0.50, {bill025} monedas de 0.25, {bill010} monedas de 0.10, {bill005} monedas de 0.05")