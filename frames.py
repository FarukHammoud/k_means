from index import *

class FrameAnimacaoInicial:
  
  #Objetos do Frame
  one_time = True   
  #Funcoes do Frame
  def __init__(self):
      pass
    #Variaveis do Frame
    
  def IniciaImagens(self):
      #mus_ini = soundfile()
      #mus_ini = SoundFile(self,"Muse - Undisclosed Desires.mp3")
      #mus_ini.play()
      FrameAnimacaoInicial.foto_e1 = loadImage('foto_e1.jpg')
      FrameAnimacaoInicial.logo_eesc = loadImage('logo_usp_eesc.png')
  #Visualizacao
  def Mostrar(self):
      #inicializacao das imagens
      if FrameAnimacaoInicial.one_time:
        FrameAnimacaoInicial().IniciaImagens()
        FrameAnimacaoInicial.one_time = False
      background(255,255,255)
      tint(0,104,255,millis()/25)
      image(FrameAnimacaoInicial.foto_e1,0,0,width,height)
      image(FrameAnimacaoInicial.logo_eesc,width/2-200,(height-50)/2-200,400,400)  
      #animacao fechamento
      if millis()/5 > width:
          Tarefas().Tarefa('Desativa Frame Animacao Inicial')
          Tarefas().Tarefa('Ativa Frame Quadriculado')
      #barra de carregamento
      fill(30,134,255,millis()/25)
      noStroke()
      rect(0,height-50,millis()/5,5)
    
class FrameQuadriculado:
    
    pontos = [[0,0]]
    centros = list()
    n_centros = 2
    x_ref = 0
    y_ref = 0
    escala = 1
    habilita_scroll = True
    ponto_em_cima = False
    modo = 0
    exibe_coord = False
    bot_cr_dl = Botao('menu',width*9/10+5,15,'Exibe Clique para adicionar/deletar um ponto','Entra modo adiciona/deleta pontos')
    bot_cr_dl.MudaTamanho(width/10-20,width/10-20)
    bot_def_k = Botao('menu',width*9/10+5,20+width/10-20,'Exibe Clique para definir o numero de centros','Entra modo define n centros')
    bot_def_k.MudaTamanho(width/10-20,width/10-20)
    bot_calcu = Botao('menu',width*9/10+5,25+2*(width/10-20),'Exibe Clique para executar o k-means','Entra modo calculo k-means')
    bot_calcu.MudaTamanho(width/10-20,width/10-20)
    one_time = True
    
    def __init__(self):    
        #referencia 2D O(0,0)
        #FrameQuadriculado.x_ref = 0
        #FrameQuadriculado.y_ref = 0
        #FrameQuadriculado.escala = 1
        #FrameQuadriculado.habilita_scroll = True
        pass
    def RetornaNCentros(self):return FrameQuadriculado.n_centros
    def MudaNCentros(self,n=2):FrameQuadriculado.n_centros = n
    def RetornaPontos(self):return FrameQuadriculado.pontos
    def MudaCentros(self,lista = [0,0]):
        FrameQuadriculado.centros = lista
    def MudaPontos(self,lista=[[0,0]]):
        FrameQuadriculado.pontos = lista
    def MostraTmpText(self):
        if millis() - Interface().RetornaTempoUltimaTecla() < 1000:
            fill(Cores().verde,(1000 - (millis() - Interface().RetornaTempoUltimaTecla()))/3)
            textSize(20)
            text('>'+Interface().RetornaString(),30,height-10)
    def IniciaImagens(self):
      FrameQuadriculado.ponto = loadImage('ponto.png')
      FrameQuadriculado.n = loadImage('n.png')
      FrameQuadriculado.calcula = loadImage('calcula.png')
    def MudaModo(self,modo):
        FrameQuadriculado.modo = modo    
    def MostraMouse(self):
        if not FrameQuadriculado.ponto_em_cima:
            strokeWeight(1)
            stroke(Cores().verde,100)
            line(mouseX-10*FrameQuadriculado.escala,mouseY,mouseX+10*FrameQuadriculado.escala,mouseY)
            line(mouseX,mouseY-10*FrameQuadriculado.escala,mouseX,mouseY+10*FrameQuadriculado.escala)   
        FrameQuadriculado.ponto_em_cima = False
    def MudaExibeCOORD(self):
        if FrameQuadriculado.exibe_coord:
            FrameQuadriculado.exibe_coord = False
        else:
            FrameQuadriculado.exibe_coord = True
    def ExibeCOORD(self):
        if FrameQuadriculado.exibe_coord:
            fill(Cores().verde,100)
            text(str(FrameQuadriculado().MudaCOORDIn([mouseX,mouseY],'dois digitos')),mouseX+10*FrameQuadriculado.escala,mouseY-10*FrameQuadriculado.escala)
    def MudaCOORDIn(self,lista = [0,0],modo = ''):
        lista = [lista[0]-Interface().RetornaXrelativo(),lista[1]-Interface().RetornaYrelativo()]
        lista = [lista[0]/FrameQuadriculado.escala,lista[1]/FrameQuadriculado.escala]
        if modo == 'inteiro':
            lista[0] = int(lista[0])
            lista[1] = int(lista[1])
        elif modo == 'dois digitos':
            lista[0] = float("%.2f" % lista[0])
            lista[1] = float("%.2f" % lista[1])
        return lista
    def MudaCOORDOut(self,lista = [0,0],modo = ''):
        lista = [lista[0]*FrameQuadriculado.escala,lista[1]*FrameQuadriculado.escala]
        lista = [lista[0]+Interface().RetornaXrelativo(),lista[1]+Interface().RetornaYrelativo()]
        if modo == 'inteiro':
            lista[0] = int(lista[0])
            lista[1] = int(lista[1])
        elif modo == 'dois digitos':
            lista[0] = float("%.2f" % lista[0])
            lista[1] = float("%.2f" % lista[1])
        return lista
    def CriaPonto(self,lista = [0,0]):
        lista[0] = float("%.2f" % lista[0])
        lista[1] = float("%.2f" % lista[1])
        FrameQuadriculado.pontos.append(lista)
    def DeletaPonto(self,lista = [0,0]):
        menor = 99999
        ind_menor = -1
        for i in range(len(FrameQuadriculado.pontos)):
            if Calculo().Dist(lista,FrameQuadriculado.pontos[i]) < menor:
                menor = Calculo().Dist(lista,FrameQuadriculado.pontos[i])
                ind_menor = i
        if ind_menor != -1:
            FrameQuadriculado.pontos.pop(ind_menor) 
                
    def MostraMensagem(self,mensagem = ''):
        if mensagem != '':
            fill(Cores().azul_claro,100)
            noStroke()
            rect(width*4/5,height*9/10,width*1/5-10,height*1/10-10,30)
            textSize(int((width*1/3)/len(mensagem)))
            fill(Cores().azul_claro)
            text(mensagem,width*4/5+25,height*9/10+45)
    def MostraMenu(self):
        fill(Cores().azul_claro,100)
        noStroke()
        rect(width*9/10,10,width/10-10,20+3*(width/10-20),20)
        FrameQuadriculado.bot_cr_dl.Mostrar()
        FrameQuadriculado.bot_def_k.Mostrar()
        FrameQuadriculado.bot_calcu.Mostrar()
        fill(Cores().branco)
        tint(255,255,255)
        image(FrameQuadriculado.ponto,width*9.2/10+5,15+(width*0.02),width/20,width/20)
        image(FrameQuadriculado.n,width*9.2/10+5,20+width/10-20+(width*0.02),width/20,width/20)
        image(FrameQuadriculado.calcula,width*9.2/10+5,25+2*(width/10-20)+(width*0.02),width/20,width/20)
    def MatrixLigada(self):
        #muda o interfaceX
        Tarefas().AlteraTarefaLetra('Mais no Simulador','+')
        Tarefas().AlteraTarefaLetra('Menos no Simulador','-')
        pushMatrix()
        translate(Interface().RetornaXrelativo(), Interface().RetornaYrelativo())
        FrameQuadriculado.escala += Interface().RetornaScroll()/10
        Interface().ZeraScroll()
        if FrameQuadriculado.escala < 0.5: 
            FrameQuadriculado.escala = 0.5
        scale(FrameQuadriculado.escala)
        point(0,0)
        #linhas de fundo
        strokeWeight(0.5)
        for i in range(int(-Interface().RetornaXrelativo()/FrameQuadriculado.escala/50)*50-50,int(width/FrameQuadriculado.escala+50),50):
            for j in range(int(-Interface().RetornaYrelativo()/FrameQuadriculado.escala/50)*50-50,int(height/FrameQuadriculado.escala+50),50):
                line(float(i), float(j), float(i)+50, float(j))
                line(float(i), float(j), float(i), float(j)+50)
        strokeWeight(1.5)
        for i in range(int(-Interface().RetornaXrelativo()/FrameQuadriculado.escala/250)*250,int(width/FrameQuadriculado.escala+50),250):
            for j in range(int(-Interface().RetornaXrelativo()/FrameQuadriculado.escala/250)*250,int(height/FrameQuadriculado.escala+50),250):
                line(float(i)-Interface().RetornaXrelativo(), float(j), float(i)+width+50, float(j))
                line(float(i), float(j)-Interface().RetornaXrelativo(), float(i), float(j)+height+50)      
    def MatrixDesligada(self):
        strokeWeight(1)
        stroke(0, 0, 0)
        textSize(12)
        popMatrix()        
    def MostraPontos(self):
        for ponto in FrameQuadriculado.pontos:
            if Calculo().MouseInC(FrameQuadriculado().MudaCOORDOut(ponto),10):
                fill(Cores().vermelho)
                ellipse(ponto[0],ponto[1],20,20)
                FrameQuadriculado.ponto_em_cima = True
            else:
                fill(Cores().vermelho,200)
                ellipse(ponto[0],ponto[1],10,10)    
    def MostraCentros(self):
        for centro in FrameQuadriculado.centros:
            if Calculo().MouseInC(FrameQuadriculado().MudaCOORDOut(centro),10):
                fill(Cores().amarelo)
                ellipse(centro[0],centro[1],20,20)
                FrameQuadriculado.ponto_em_cima = True
            else:
                fill(Cores().amarelo,200)
                ellipse(centro[0],centro[1],10,10)  
    def Mostrar(self):
        if FrameQuadriculado.one_time:
            FrameQuadriculado().IniciaImagens()
            FrameQuadriculado.one_time = False
        background(Cores().azul_CAD)
        stroke(Cores().azul_claro_CAD)
        FrameQuadriculado().MatrixLigada()
        FrameQuadriculado().MostraPontos()
        FrameQuadriculado().MostraCentros()
        FrameQuadriculado().MatrixDesligada()
        FrameQuadriculado().MostraMenu()
        FrameQuadriculado().MostraMouse()
        FrameQuadriculado().ExibeCOORD()
        FrameQuadriculado().MostraTmpText()
        if FrameQuadriculado.modo == 0:
            if Interface().MouseClicked():
                if Interface().RetornaBotaoMouse()  == CENTER:
                     FrameQuadriculado().MudaExibeCOORD()    
        elif FrameQuadriculado.modo == 1:
            if Interface().MouseClicked():
                if Interface().RetornaBotaoMouse()  == CENTER:
                     FrameQuadriculado().MudaExibeCOORD() 
                if Interface().RetornaBotaoMouse()  == LEFT:
                    FrameQuadriculado().CriaPonto(FrameQuadriculado().MudaCOORDIn([mouseX,mouseY]))
                if Interface().RetornaBotaoMouse()  == RIGHT:
                    FrameQuadriculado().DeletaPonto(FrameQuadriculado().MudaCOORDIn([mouseX,mouseY]))
        elif FrameQuadriculado.modo == 2:
            pass
            
        elif FrameQuadriculado.modo == 3:
            pass 
        FrameQuadriculado.modo = 0
class Frames:

  #Lista de Controle
  frame = []

  #Declaracao de Frames
  frame_animacao_inicial = FrameAnimacaoInicial()
  frame_quadriculado = FrameQuadriculado()
  
  #Metodos
  def __init__(self):
    for i in range(0,20):
      Frames.frame.append(False)
  def AtivaFrame(self,numero): Frames.frame[numero] = True 
  def AtivaFrames(self,lista): 
    for i in lista:
        Frames.frame[i] = True 
  def DesativaFrame(self,numero): Frames.frame[numero] = False
  def DesativaFrames(self,lista): 
    for i in lista:
        Frames.frame[i] = False
  def EstadoFrame(self,numero): return Frames.frame[numero]
  def MouseDentro(self,frame):
      if frame == 0 and Frames().EstadoFrame(0): return True
      elif frame == 1 and Frames().EstadoFrame(1): return True
      elif frame == 2 and Frames().EstadoFrame(2): return True

      
  #Funcao Visualizacao
  def Mostrar(self):
    background(0,0,0)
    if Frames.frame[0]: Frames.frame_animacao_inicial.Mostrar()
    if Frames.frame[1]: Frames.frame_quadriculado.Mostrar()
    
      