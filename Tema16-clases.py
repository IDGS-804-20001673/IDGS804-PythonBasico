import os
class Operasbas():
    #variables o propiedades de la clase
    num1=0
    num2=0
    num3=0
    res=0

    #metodo constructor
    def __init__(self,a,b):  # asi es el nombre del metodo constructor, el self es como el this, no es como en java que se llama igual que la clase
        self.num1=a   #en java es this.num1=a
        self.num2=b   #en java es this.num2=b

    def suma(self):
        self.res=self.num1+self.num2
    def resta(self):
        self.res=self.num1self.num2
        
#Metodos de clase
def main():
    os.system('cls')
    obj=Operasbas(3,4) 
    obj.suma()
    print("La suma es: {}".format(obj.res))

#para limpiar el cmd de visual code

        
   

if __name__ == '__main__':
    main()
