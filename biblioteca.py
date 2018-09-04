from index import *
class Cores:

  branco = color(255)
  preto = color(0)
  vermelho = color(255, 0, 0)
  verde = color(0, 255, 0)
  verde_real = color(60, 255, 0)
  azul = color(0, 0, 255)
  azul_CAD = color(19,0,79)
  azul_claro_CAD = color(38,0,158)
  azul_claro = color(0, 230, 250)
  verde_claro = color(50, 250, 0)
  rosa = color(250, 100, 200)
  amarelo = color(250, 250, 0)
  cinza_escuro = color(50, 50, 50)
  cinza = color(150, 150, 150)
  cinza_claro = color(200, 200, 200)
  cinza_muito_claro = color(225, 225, 225)
  cinza_azulado = color(60, 100, 130)

class Ponto3D:
    def __init__(self,lista = [0,0,0]):
        self.x=lista[0]
        self.y=lista[1]
        self.z=lista[2]
    def MudaPontos(self,lista = [0,0,0]):
        self.x=lista[0]
        self.y=lista[1]
        self.z=lista[2]
class Ponto2D:
    def __init__(self,lista = [0,0]):
        self.x=lista[0]
        self.y=lista[1]
    def MudaPontos(self,lista = [0,0]):
        self.x=lista[0]
        self.y=lista[1]
    def X(self):
        return self.x
    def Y(self):
        return self.y        
class TextBox:

  def Limpar(self): self.texto = ''
  
  def __init__ (self,x,y):
    self.x = x
    self.y = y
    self.texto = ''
    self.sufixo = ''
    self.txt_vazio = ''
    self.habilitado = False
    self.mouse_em_cima = False
    self.pressionado = False
    
  def MudaTexto(self,texto): self.texto = texto
  def MudaSufixo(self,sufixo): self.sufixo = sufixo
  def MudaTXTVazio(self,txt_vazio): self.txt_vazio = txt_vazio
  def MudaXY(self,x,y):
    self.x = x
    self.y = y
  def Texto(self): return self.texto
  def Mostrar(self):
    fill(Cores().branco)
    stroke(200, 200, 200)
    rect(self.x, self.y, 150, 20)
    textSize(14)
    fill(100, 100, 100)
    if (self.texto == ''):
      text(self.txt_vazio, self.x+10, self.y+17)
    else:
      text(self.texto+' '+self.sufixo, self.x+10, self.y+17)
    if Calculo().MouseIn(self.x,self.y,150,20):  
      self.mouse_em_cima = True;
    else:
      self.mouse_em_cima = False
      self.habilitado = False
    if self.mouse_em_cima and mousePressed:
      self.pressionado = True;
    elif self.pressionado:
      self.pressionado = False
      self.habilitado = True
      self.texto = ''
      Interface().DeletaString()
    if self.habilitado:
      self.texto = Interface().RetornaString()
    if self.mouse_em_cima: 
      fill(Cores().branco)
      stroke(0, 200, 0)
      rect(self.x, self.y, 150, 20)
      textSize(14)
      fill(Cores().preto)
      if self.texto != '':
        text(self.texto+' '+self.sufixo, self.x+10, self.y+17)
      elif self.habilitado:
        if (millis()/500)%2 == 0:
          text('_', self.x+10, self.y+17)
        
class ListaLateral:

  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.inicial = ''
    self.atual = ''
    self.lista = []
    self.n = 0
    
    self.mouse_em_cima_1 = False
    self.mouse_em_cima_2 = False
    self.pressionado_1 = False
    self.pressionado_2 = False

    self.iniciado = False
  def MudaXY(self,x,y):
    self.x = x
    self.y = y
  
  def MudaInicial(self,inicial):

    if not self.iniciado:
      self.inicial = inicial
      for i in range(self.nOf_itens):
        if self.inicial == self.lista[a]:
          self.n = a;
      self.iniciado = True;
  def CarregaLista(self,listagem):
    self.lista = []  
    #carregar
    if listagem == 'Geral,Fluido 1,Fluido 2,Calculo': 
      pass  
      # self.nOf_itens = FRAMES.FRAME_concentrico.lista_comum.length;
      #for (int a=0; a<FRAMES.FRAME_concentrico.lista_comum.length; a++) {
      #self.lista[a] = FRAMES.FRAME_concentrico.lista_comum[a];
      #}
    
    if listagem == 'moleculas':
      pass
      #self.nOf_itens = DATA.moleculas.length;
      #for (int a=0; a<DATA.moleculas.length; a++) {
      #  self.lista[a] = DATA.moleculas[a];
      #}
    if listagem == 'usuarios':
      for i in range(len(Data().usuario)):
          self.lista.append(Data().usuario[i][1])
  def IndiceN(self): return self.n
  def Texto(self): return self.lista[self.n]
  def Mostrar(self):
    stroke(150, 150, 150)
    if Calculo().MouseInC([self.x, self.y-8],10):
      self.mouse_em_cima_1 = True
      fill(200+(mouseX%20), 200+(mouseY%20), 200+((mouseX+mouseY)%20))
    else: 
      self.mouse_em_cima_1 = False
      fill(255, 255, 255)
    if self.mouse_em_cima_1 and mousePressed:
      self.pressionado_1 = True
    elif self.pressionado_1:
      self.n-=1
      if self.n < 0:
        self.n = 0
      self.pressionado_1 = False
    ellipse(self.x, self.y-8, 20, 20)
    triangle(self.x-5, self.y-8, self.x+5, self.y-5, self.x+5, self.y-11)
    if Calculo().MouseInC([self.x+230,self.y-8],10):
      self.mouse_em_cima_2 = True
      fill(200+(mouseX%20), 200+(mouseY%20), 200+((mouseX+mouseY)%20))
    else: 
      self.mouse_em_cima_2 = False
      fill(Cores().branco)
    if self.mouse_em_cima_2 and mousePressed:
      self.pressionado_2 = True
    elif self.pressionado_2:
      self.n+=1
      if self.n > len(self.lista)-1:
        self.n = len(self.lista)-1
      self.pressionado_2 = False
    ellipse(self.x+230, self.y-8, 20, 20)
    triangle(self.x+235, self.y-8, self.x+225, self.y-5, self.x+225, self.y-11)
    fill(255, 255, 255)
    rect(self.x+15, self.y-18, 200, 20, 10)
    fill(150)
    textSize(16)
    text(str(self.lista[self.n]), float(self.x+20),float(self.y-1))
  
class CheckBox:
  def __init__(self,x,y,texto = '',valor = False):
    self.x = x
    self.y = y
    self.texto = texto
    self.valor = valor
    
    self.mouse_em_cima = False
    self.pressionado = False
  def RetornaValor(self): return self.valor
  def MudaTexto(self,texto): self.texto = texto
  def MudaXY(self,x,y):
    self.x = x
    self.y = y
  def Mostrar(self,):
    fill(Cores().braco)
    stroke(200, 200, 200)
    rect(self.x, self.y, 10, 10)
    textSize(10)
    fill(Cores().preto)
    text(self.texto, self.x+20, self.y+10);
    if self.valor:
      fill(Cores().verde) 
      ellipse(self.x+5, self.y+5, 4, 4)
    if Calculo().MouseIn(self.x,self.y,10,10):
      self.mouse_em_cima = True
    else:
      self.mouse_em_cima = False
    if Interface.MouseClicked():
      if self.valor:
        self.valor = False
      else :
        self.valor = True
    if self.mouse_em_cima:
      fill(0, 100,0 ) 
      ellipse(self.x+5, self.y+5, 4, 4)
class Botao:
  def __init__(self,tipo,x,y,link_tarefa_a,link_tarefa_b):
    self.tipo = tipo
    self.x = x
    self.y = y
    self.link_tarefa_a = link_tarefa_a
    self.link_tarefa_b = link_tarefa_b
    
    self.tam_x = 10
    self.tam_y = 10
    self.texto = ''
    self.numero_de_letras = 0
    self.mouse_em_cima = False
    self.clicado = False
    self.pressionado = False
  def MudaXY(self,x,y):
    self.x = x
    self.y = y
  def MudaTexto(self,texto): self.texto = texto
  def RetornaValor(self):
    if self.pressionado: return True
    else: return False
  def MudaValor(self,valor = False):self.clicado = valor
  def MudaTamanho(self,tam_x,tam_y):
    self.tam_x = tam_x
    self.tam_y = tam_y    
  def Mostrar(self):
      
    if self.tipo == 'menu':
        if Calculo().MouseIn(self.x,self.y,self.tam_x,self.tam_y):
            self.mouse_em_cima = True
            fill(Cores().verde,100) 
            stroke(Cores().azul_claro)
            rect(self.x, self.y, self.tam_x,self.tam_y, 15)
            Tarefas().Tarefa(self.link_tarefa_a)
        else: 
            self.mouse_em_cima = False
            fill(Cores().verde,50)
            noStroke()
            rect(self.x, self.y, self.tam_x,self.tam_y, 15)
        if self.mouse_em_cima and Interface().MouseClicked():
            self.clicado = Calculo().Switch(self.clicado)
            Tarefas().Tarefa(self.link_tarefa_b)
        if self.clicado:
            fill(Cores().verde,100) 
            stroke(Cores().azul_claro)
            rect(self.x, self.y, self.tam_x,self.tam_y, 15)
            Tarefas().Tarefa(self.link_tarefa_b)
            
        fill(Cores().azul)
        textSize(16)
        text(self.texto, self.x+5, self.y+20)

    
    
    
  
       