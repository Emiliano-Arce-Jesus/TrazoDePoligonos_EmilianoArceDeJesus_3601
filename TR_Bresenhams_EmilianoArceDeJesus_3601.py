import matplotlib.pyplot as plt

def TRBRESEN():
    base= int(input('INGRESA LA BASE DEL TRIANGULO EN PIXELES: '))
    altura= int (input('INGRESA LA ALTURA DEL TRIANGULO: '))
    print ('\n*** INGRESA EL PUNTO DE ORIGEN DEL TRIANGULO ***\n')
    x1= int(input('INGRESA VALOR PARA X1:\n'))
    y1= int(input('INGRESA VALOR PARA Y1:\n'))
    #BASE DEL CUADRADO
    x2= (base + x1) -1
    y2=y1

    #COSTADO DERECHO
    xa= (base + x1) -1
    ya= y1 
    xa1= base + x1
    ya1= (altura + y1)

    #COSTADO IZQUIERDO
    xb= x1
    yb= y1
    xb1= (base + x1)-1
    yb1= altura+ y1

    dx= abs(x2 - x1)
    dy =abs(y2 -y1)
    p= (2 * dy) -dx
    #EXTRA
    dx1= abs(xb1 - xb)
    dy1= abs(yb1 - yb)
    p1= (2 * dy1) - dx1


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


    #COSTADO DERECHO
    while ya <= ya1:
        plt.plot(round(xa),round(ya), marker="s", color="black")
        ya= ya + 1
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            ya= ya + 1
        print(xa,ya)

    #COSTADO IZQUIERDO
    print ('IZQUIERDO')
    while xb <= xb1:
        plt.plot(round(xb),round(yb), marker="s", color="black")
        #yb= yb+1
        xb= xb + 1
        if p1 < 0:
            p1= p1 + (2 * dy1)
        else:
            p1= p1 + (2 * dy1) - (2 * dx1)
            yb= yb + 1
        print(xb,yb)

    plt.show()
if __name__== '__TRBRESEN__':
    TRBRESEN()