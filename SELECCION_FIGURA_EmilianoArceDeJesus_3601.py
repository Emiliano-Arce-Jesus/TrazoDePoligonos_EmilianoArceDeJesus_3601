import matplotlib.pyplot as plt
from T_DDA_EmilianoArceDeJesus_3601 import TDDA
from T_BRESENHAMS_EmilianoArceDeJesus_3601 import TBRESEN
from C_DDA_EmilianoArceDeJesus_3601 import CDDA
from C_Bresenhams_EmilianoArceDeJesus_3601 import CBRESEN
from R_DDA_EmilianoArceDeJesus_3601 import RDDA
from R_Bresenhams_EmilianoArceDeJesus_3601 import RBRESEN
from TR_Bresenhams_EmilianoArceDeJesus_3601 import TRBRESEN
from TR_DDA_EmilianoArceDeJesus_3601 import TRDDA
def main():
    print('\n¿QUE FIGURA DESEAS DIBUJAR? \n\n\
1= CUADRADO\n 2= TRIANGULO\n 3= RECTANGULO\n 4= TRIANGULO RECTANGULO \n 5= SALIR\n')
    figura= int(input('OPCIÓN: '))
    #CUADRADO
    if figura== 1:
        print('\nINGRESA 1 PARA DIBUJAR EL CUADRADO CON ALGORITMO BRESENHAMS \nINGRESA 2 PARA DIBUJAR EL CUADRADO CON ALGOTITMO DDA \n INGRESA 3 PARA SALIR\n')
        n= int(input('OPCIÓN: '))
        if n==1:
            CBRESEN()
            main()
        elif n==2:
            
            CDDA()
            main()
        elif n==3:
            print('HASTA LUEGO')
            plt.close
        else:
            print('¡OPCIÓN NO RECONOCIDA INTENTALO NUEVAMENTE!\n')
            main()
    #TRIANGULO
    elif figura==2:
        print('\nINGRESA 1 PARA DIBUJAR EL TRIANGULO CON ALGORITMO BRESENHAMS \n INGRESA 2 PARA DIBUJAR EL TRIANGULO CON ALGOTITMO DDA \n INGRESA 3 PARA SALIR\n')
        n= int(input('OPCIÓN: '))
        if n==1:
            TBRESEN()
            main()
        elif n==2:
            
            TDDA()
            main()
        elif n==3:
            print('HASTA LUEGO')
            exit
        else:
            print('¡OPCIÓN NO RECONOCIDA INTENTALO NUEVAMENTE!\n')
            main()

    #RECTANGULO
    elif figura==3:
        print('\nINGRESA 1 PARA DIBUJAR EL RECTANGULO CON ALGORITMO BRESENHAMS \n INGRESA 2 PARA DIBUJAR EL RECTANGULO CON ALGOTITMO DDA \n INGRESA 3 PARA SALIR\n')
        n= int(input('OPCIÓN: '))
        if n==1:
            RBRESEN()
            main()
        elif n==2:
            RDDA()
            main()
        elif n==3:
            print('HASTA LUEGO')
            exit
        else:
            print('¡OPCIÓN NO RECONOCIDA INTENTALO NUEVAMENTE!\n')
            main()

    
    #TRIANGULO RECTANGULO
    elif figura==4:
        print('\nINGRESA 1 PARA DIBUJAR EL TRIÁNGULO RECTANGULO CON ALGORITMO BRESENHAMS \n INGRESA 2 PARA DIBUJAR EL TRIÁNGULO RECTANGULO CON ALGOTITMO DDA \n INGRESA 3 PARA SALIR\n')
        n= int(input('OPCIÓN: '))
        if n==1:
            TRBRESEN()
            main()
        elif n==2:
            
            TRDDA()
            main()
        elif n==3:
            print('HASTA LUEGO')
            exit
        else:
            print('¡OPCIÓN NO RECONOCIDA INTENTALO NUEVAMENTE!\n')
            main()

    #NO SELECCION

    #SALIR
    elif figura== 5:
        exit
    else:
        print('\nOPCION NO RECONOCIDA\n')
        main()
if __name__=='__main__':
    main()