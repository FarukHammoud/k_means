from index import *

class Calculo:
    
    def Dist(self,A=[0,0],B=[0,0]):
        return sqrt(pow(A[0]-B[0],2)+pow(A[1]-B[1],2))
    def MouseIn(self,x0 = 0,y0 = 0,dx = 0,dy = 0):
        if mouseX >= x0 and mouseX <= x0+dx and mouseY >= y0 and mouseY <= y0+dy: return True 
        else: return False
    def MouseInC(self,P = [0,0],raio = 0):
        if sqrt(pow(mouseX - P[0],2) + pow(mouseY - P[1],2)) < raio : return True
        else: return False
    def Switch(self,booleano = False):
        if booleano:return False
        else:return True
    def KMeans(self,pontos = [],n = 2):
        if len(pontos)<n:
            return pontos
        lista_centros = list()
        for i in range(n):
            lista_centros.append(pontos[int(random(len(pontos)))])
        
        lista_centros_anterior = list()
        
        while lista_centros != lista_centros_anterior:
            lista_centros_anterior = lista_centros
            #cria matriz distancias
            matriz_distancias = list()
            for i in range(n):
                lista_distancias = list()
                for ponto in pontos:
                    lista_distancias.append(Calculo().Dist(lista_centros[i],ponto))
                matriz_distancias.append(lista_distancias)
        
            #cria matriz discreta com comparacao de distancias
            matriz_comparacao = list()
            for i in range(len(pontos)):
                menor = matriz_distancias[0][i]
                indice_menor = 0
                lista_comparacao = list()
                for j in range(n):
                    lista_comparacao.append(0)
                for j in range(n):
                    if matriz_distancias[j][i]<menor:
                        menor = matriz_distancias[j][i]
                        indice_menor = j
                lista_comparacao[indice_menor]=1
                matriz_comparacao.append(lista_comparacao)
        
            #calcula novos centros
            lista_centros = list()
            for i in range(n):
                centro = [0,0]
                contagem = 0
                for j in range(len(pontos)):
                    if matriz_comparacao[j][i] == 1:
                        centro[0]+=pontos[j][0]
                        centro[1]+=pontos[j][1]
                        contagem += 1
                if contagem != 0:
                    centro[0] /= contagem
                    centro[1] /= contagem
                lista_centros.append(centro)
        
        return lista_centros