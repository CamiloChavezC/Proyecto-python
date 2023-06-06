import os
os.system("cls")
while True:
    print("********************Menu********************")
    print("1.-Pagar con tarjeta de credito")
    print("2.-Pagar con paypal")
    print("3.-Pagar por transferencia")
    print("4.-Cancelar")
    print("5.-Salir")
    op=int(input("Ingrese una opcion: "))
    try:
        if op>0 and op<=5:
            os.system("cls")
            if op ==1:
                nroTar=int(input("Ingrese el numero de tarjeta de credito: "))
                nomTit=str(input("Ingrese el nombre del titular: "))
                mesVenc=int(input("Ingrese el Mes de vencimiento: "))
                annoVenc=int(input("Ingrese Año de vencimiento: "))
                os.system("cls")
            if op==2:
                nomPay=str(input("Ingrese nombre de usuario paypal: "))
                contPay=int(input("Ingrese su contraseña: "))
                os.system("cls")
            if op==3:
                codRef=int(input("Ingrese el codigo de referencia proporcionado por la empresa: "))
                os.system("cls")
            if op==4:
                compra=100000
                print("Detalle compra")
                print("Costo de la compra:   ",compra)
                print("Numero de la tarjeta: ",nroTar)
                print("Nombre del titular:   ",nomTit)
                print("Mes y año:            ",mesVenc,"/",annoVenc)
                print("")
                print("Muchas gracias por su compra")
            if op==5:
                break
    except:
        print("Ingrese un opcion valida")
