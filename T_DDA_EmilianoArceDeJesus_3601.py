import matplotlib.pyplot as plt

def TDDA():
    print('TRIANGULO DE BASE 11 Y ALTURA 6\n PUNTO DE ORIGEN (1,1)')
    base= 11
    altura= 6
    x1=1
    y1=1
    #BASE DEL CUADRADO
    x2= (base + x1)
    y2=y1

    #COSTADO IZQUIERDO
    xa= x1
    ya= y1
    xa1= x1 + (base/2)
    ya1= altura +1

    #COSTADO DEECHO
    xb1= x1 + (base/2)-1
    yb1= (altura + y1)-1
    xb= (base + x1)-1
    yb= y1
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
    dy= int (abs (yb1-yb))
    x=0
    if dx > dy:
        steps= dx
    else:
        steps= dy
    incx= dx/steps
    incy= dy/steps
    print('DERECHO')
    for i in range (x, steps):
        plt.plot(round(xb), round(yb), marker="s", color="black")
        xb= xb-incx
        yb= yb+incy
        print (xb, ',', yb)
    
    plt.show()
if __name__== '__TDDA__':
    TDDA()