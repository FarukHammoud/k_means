#CARREGA MODULOS ESTATICOS
from math import *
from gc import *

#CARREGA MODULOS DINAMICOS

def Calculo():
    import calculo
    i = calculo.Calculo()
    return i
    del i
def Data():
    import data_
    return data_.Data()
def Tarefas():
    import tarefas
    i = tarefas.Tarefas()
    return i
    del i
def Frames():
    import frames
    i = frames.Frames()
    return i
    del i
def Interface():
    import interface
    i = interface.Interface()
    return i
    del i
def Papel():
    import objetos
    i = objetos.Papel()
    return i
    del i
def Ponto3D():
    import biblioteca
    i = biblioteca.Ponto3D()   
    return i
    del i    
def Cores():
    import biblioteca
    i = biblioteca.Cores()
    return i
    del i
def TextBox(x,y):
    import biblioteca
    i = biblioteca.TextBox(x,y)
    return i
    del i
def ListaLateral(x,y):
    import biblioteca
    i = biblioteca.ListaLateral(x,y)
    return i
    del i
def CheckBox(x,y,texto = '',valor = False):
    import biblioteca
    i = biblioteca.CheckBox(x,y,texto,valor)
    return i
    del i
def Botao(tipo,x,y,link_tarefa_a,link_tarefa_b):
    import biblioteca
    i = biblioteca.Botao(tipo,x,y,link_tarefa_a,link_tarefa_b)
    return i
    del i
def Projeto():
    import objetos
    i = objetos.Projeto()
    return i
    del i
  

    
    
    
    