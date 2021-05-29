import matplotlib.pyplot as plt

def RBRESEN():
    base= int(input('INGRESA LA BASE DEL RECTANGULO EN PIXELES: '))
    altura= int(input('INGRESA LA ALTURA DEL RECTANGULO EN PIXELES: '))
    print ('\n*** INGRESA EL PUNTO DE ORIGEN DEL RECTANGULO ***\n')
    x1= int(input('INGRESA VALOR PARA X1:\n'))
    y1= int(input('INGRESA VALOR PARA Y1:\n'))
    #BASE DEL CUADRADO
    x2= (base + x1)-1
    y2=y1

    #COSTADO IZQUIERDO
    xa= x1
    ya= y1
    xa1= x1
    ya1= (altura+ y1)-1 

    #BASE SUPERIOR
    xb= x1 
    yb= (altura + y1)-1
    xb1= (base + x1)-1
    yb1= (altura + y1)

    #COSTADO DEECHO
    xc= (base + x1)-1
    yc= y1
    xc1= (base + x1)-1
    yc1= (altura + y1)-1

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
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            ya= ya + 1
        print(xa,ya)
    
    #BASE SUPERIOR
    while xb <= xb1:
        plt.plot(round(xb),round(yb), marker="s", color="black")
        xb= xb + 1
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            yb= yb + 1
        print(xb, yb)

    #COSTADO DERECHO
    while yc <= yc1:
        plt.plot(round(xc),round(yc), marker="s", color="black")
        yc= yc + 1
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            yc= yc + 1
        print(xc,yc)
    plt.show()

if __name__=='__RBRESEN__':
   RBRESEN()