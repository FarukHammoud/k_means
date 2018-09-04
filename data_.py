from index import *

class Data:
  
  contas_linhas = list()
  contas_string = ''
  
  #contas: file
  usuario = []
  senha_cripto = []

  def __init__(self):
    pass  
  def RetornaStr(self,arquivo):
    linhas = list()
    linhas = loadStrings(arquivo)  
    return join(linhas,' ')
  def ImprimeContas(self):
    println('contas string: '+ Data().RetornaStr('contas.txt')) 
    for i in range(len(Data.usuario)):
        println(str(Data.usuario[i][1]))
        println(str(Data.senha_cripto[i][1]))
  def ObtemContas(self):
    Data.contas_string = Data().RetornaStr('contas.txt')
    Data.usuario = matchAll(Data.contas_string,'usuario = \"(.*?)\";')
    Data.senha_cripto = matchAll(Data.contas_string,'senha_cripto = \"(.*?)\";')
  