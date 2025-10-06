esp = 100

def Titulo (titulo: str):
       
        T =  len(titulo)
        
        M = (esp//2 - 4) - (T//2)
        
        if (T % 2 != 0) :
            titulo = titulo + " "
        else:
            M=M+1
        
        print ("#"*esp)
        print ("#"," "*(esp-4), "#")
        print ("#"," "*M, titulo," "*M,"#")
        print ("#"," "*(esp-4), "#")
        print ("#"*esp)
    
    
def EntradaInt ( msg: str, min: int, max: int):
        retorno = -1
        while (True):
            try: 
                retorno = int (input (msg))
                print ("_"*esp)  
            except ValueError:
                print ("ERRO "*10)        
                print("Invalido a entrada, use numeros inteiros.") 
            if (retorno >=min and  retorno <=max):
                return retorno
            
def EntradaFloat ( msg: str, min: int, max: int):
        retorno = -1
        while (True):
            try: 
                retorno = float (input (msg))
                print ("_"*esp)  
            except ValueError:
                print ("ERRO "*10)        
                print("Invalido a entrada, use numeros reais.") 
            if (retorno >=min and  retorno <=max):
                return retorno