def tarjetas (x,y):
    x=x*12
    y=y*35
    if x<y:
        return x
    elif x>y:
        return y 
def main():
    #escribe tu código abajo de esta línea
    Pliegos=int(input('Dame la cantidad de pliegos de papel albanene: '))
    Plumones=int(input('Dame la cantidad de plumones: '))
    print('El número máximo de tarjetas que se pueden hacer es: ' + str(tarjetas(Pliegos,Plumones)))
if __name__=='__main__':
    main()
