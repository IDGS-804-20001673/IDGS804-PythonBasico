import os

class Operasbas():
    #variables o propiedades de la clase
    num1=0
    num2=0
    res=0
    opc=0

    
    def __init__(self,a,b): 
        self.num1=a  
        self.num2=b   

    def suma(self):
        self.res=self.num1+self.num2
    def resta(self):
        self.res=self.num1-self.num2
    def mul(self):
        self.res=self.num1*self.num2
    def div(self):
        self.res=self.num1/self.num2
        
#Metodos de clase
def main():
    
    opc=int(input('Que opccion quieres: 1: suma, 2: resta, 3: multiplicacion, 4: division, 5: salir '))
    
    
    if opc == 1:
        na=int(input('Dame el primer numero: '))
        nb=int(input('Dame el segundo numero: '))
        obj=Operasbas(na,nb) 
        obj.suma()
        os.system('cls')
    elif opc == 2:
        na=int(input('Dame el primer numero: '))
        nb=int(input('Dame el segundo numero: '))
        obj=Operasbas(na,nb) 
        obj.resta()
        os.system('cls')
    elif opc == 3:
        na=int(input('Dame el primer numero: '))
        nb=int(input('Dame el segundo numero: '))
        obj=Operasbas(na,nb) 
        obj.mul()
        os.system('cls')  
    elif opc == 4:
        na=int(input('Dame el primer numero: '))
        nb=int(input('Dame el segundo numero: '))
        obj=Operasbas(na,nb)  
        obj.div()
        os.system('cls')
    else:
        exit()
    
    print("El resultado es: {}".format(obj.res))
    main()
    


if __name__ == '__main__':
    main()