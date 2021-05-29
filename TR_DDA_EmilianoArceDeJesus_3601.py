import matplotlib.pyplot as plt

def TRDDA():
    base= int(input('INGRESA LA BASE DEL TRIANGULO rectangulo EN PIXELES: '))
    altura= int (input('INGRESA LA ALTURA DEL TRIANGULO rectangulo: '))
    print ('\n*** INGRESA EL PUNTO DE ORIGEN DEL TRIANGULO rectangulo ***\n')
    x1= int(input('INGRESA VALOR PARA X1:\n'))
    y1= int(input('INGRESA VALOR PARA Y1:\n'))
    #BASE DEL CUADRADO
    x2=base + x1
    y2=y1

    #COSTADO IZQUIERDO
    xa= x1
    ya= y1
    xa1= (base + x1)-1
    ya1= (altura+ y1)-1

    #COSTADO DEECHO
    xb= (x1 + base)-1
    yb= y1
    xb1= (base + x1)-1
    yb1= altura+ y1
    x=0

    #BASE
    dx= abs(x2-x1)
    dy= abs(y2-y1)
    if dx > dy:
        steps= dx
    else:
        steps= dy
    incx= dx/steps
    incy= dy/steps
    for i in range (x, steps):
        plt.plot(round(x1), round(y1), marker="s", color="black")
        x1= x1+incx
        y1= y1+incy
        print (x1, ',', y1)

    #COSTADO IZQUIERDO
    print('IZQUIERDA')
    dx= abs(xa1-xa)
    dy= abs(ya1-ya)
    if dx > dy:
        steps= dx
    else:
        steps= dy
    incx= dx/steps
    incy= dy/steps
    for i in range (x, steps):
        plt.plot(round(xa), round(ya), marker="s", color="black")
        xa= xa+incx
        ya= ya+incy
        print (xa, ',', ya)

    #COSTADO DERECHO
    dx= int(abs (xb1-xb))
    dy= int(abs (yb1-yb))
    x=0
    if dx > dy:
        steps= dx
    else:
        steps= dy
    incx= dx/steps
    incy= dy/steps
    for i in range (x, steps):
        plt.plot(round(xb), round(yb), marker="s", color="black")
        xb= xb+incx
        yb= yb+incy
        print (xb, ',', yb)
    
    plt.show()
if __name__== '__TRDDA__':
    TRDDA()