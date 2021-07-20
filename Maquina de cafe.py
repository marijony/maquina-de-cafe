cafesolo=2
expresso=1
capuchino=3
print("cafesolo=2€ expresso=1€ capuchino=3€")
producto = input("Bienvenido, por favor elija el producto que desea comprar, tenemos cafe solo, expresso y capuchino: ")
pago = int(input("Introduzca la cantidad con la que desea pagar, la máquina solo acepta monedas de $1, $2, $5 y $10: "))
if pago == 1 or pago == 2 or pago == 5 or pago == 10:
    if producto == "cafesolo":
        while True:
            if pago >= 10:
                print("Gracias por su compra")
                cambio = (pago - 10)
                print("Su cambio es: " + str(cambio))
                texpresso = (expresso - 1)
                print("La máquina cuenta con " + str(cafesolo) + " cafesolo")
                break
            else:
                faltante = (10 - pago)
                print("La cantidad no es suficiente, te faltan $" + str(faltante))
                opcion = input("¿Desea continuar con la compra? ")
                if opcion == "si":
                    total = int(input("Introduce el dinero que falta: "))
                    pago = (pago + total)
                else:
                    print("Con gusto le devolvemos su dinero $" + str(pago))
                    break
    elif producto == "expresso":
        while True:
            if pago >= 12:
                print("Gracias por su compra")
                tbebidas = (bebidas - 1)
                cambio = (pago - 12)
                print("Su cambio es: " + str(cambio))
                print("La máquina cuenta con  + str(expresso)  " )
                break
            else:
                faltante = (12 - pago)
                print("La cantidad no es suficiente, te faltan $" + str(faltante))
                opcion = input("¿Desea continuar con la compra? ")
                if opcion == "si":
                    total = int(input("Introduce el dinero que falta: "))
                    pago = (pago + total)
                else:
                    print("Con gusto le devolvemos su dinero $" + str(pago))
                    break
    elif producto == "capuchino":
        while True:
            if pago >= 14:
                print("Gracias por su compra")
                tbotanas = (botanas - 1)
                cambio = (pago - 14)
                print("Su cambio es: " + str(cambio))
                print("La máquina cuenta con " + str(tbotanas) + " capuchino")
                break
            else:
                faltante = (14 - pago)
                print("La cantidad no es suficiente, te faltan $" + str(faltante))
                opcion = input("¿Desea continuar con la compra? ")
                if opcion == "si":
                    total = int(input("Introduce el dinero que falta: "))
                    pago = (pago + total)
                else:
                    print("Con gusto le devolvemos su dinero $" + str(pago))
                    break
else:
    print("Moneda no válida")

