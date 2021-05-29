import matplotlib.pyplot as plt

def TBRESEN():
    #base= int(input('INGRESA LA BASE DEL TRIANGULO EN PIXELES: '))
    base= 11
    #altura= int (input('INGRESA LA ALTURA DEL TRIANGULO: '))
    altura= 6
    #print ('INGRESA EL PUNTO DE ORIGEN DEL TRIANGULO')
    #x1= int(input('INGRESA VALOR PARA X1:\n'))
    x1=1
    #y1= int(input('INGRESA VALOR PARA Y1:\n'))
    y1=1
    #BASE DEL CUADRADO
    x2= (base + x1)-1
    y2=y1

    #COSTADO IZQUIERDO
    xa= x1
    ya= y1
    xa1= x1 + (base/2)
    ya1= (altura + y1)-1

    #COSTADO DEECHO
    xb= (base + x1)-1
    yb= y1
    xb1= x1 + (base/2)
    yb1= (altura + y1)-1
    x=0

    dx= abs(x2 - x1)
    dy =abs(y2 -y1)
    p= (2 * dy) -dx

    #BASE
    while x1 <= x2:
        plt.plot(round(x1),round(y1), marker="s", color="black")
        x1= x1 + 1
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            y1= y1 + 1
        print(x1,y1)

    #COSTADO IZQUIERDO
    while ya <= ya1:
        plt.plot(round(xa),round(ya), marker="s", color="black")
        ya= ya + 1
        xa= xa+1
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            ya= ya + 1
        print(xa,ya)

    #COSTADO DERECHO
    print('DERECHO')
    while yb <= yb1:
        plt.plot(round(xb),round(yb), marker="s", color="black")
        yb= yb+1
        xb= xb-1  
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            yb= yb + 1
        print(xb,yb)
    plt.show()
if __name__=='__TBRESEN__':
    TBRESEN()
