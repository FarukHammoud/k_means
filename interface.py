from index import *

class Interface:
    
    tmp_text = ''
    tempo_ultima_tecla = 0
    scroll = 0
    x_ref = 0
    y_ref = 0
    x_relativo = 0
    y_relativo = 0
    
    mouse_clicked = False
    mouse_pressed = False
    mouse_lado = 'direita'
    botao_mouse = ''
    
    def MudaTempoUltimaTecla(self):
        Interface.tempo_ultima_tecla = millis()
    def RetornaTempoUltimaTecla(self):
        return Interface.tempo_ultima_tecla
    def ScrollPlus(self,x): 
        Interface.scroll += 0.2
    def ScrollMinus(self,x): 
        Interface.scroll -= 0.2
    def RetornaMousePressed(self):
        return Interface.mouse_clicked
    def MudaBotaoMouse(self,botao_mouse):
        Interface.botao_mouse = botao_mouse
    def DeletaString(self): Interface.tmp_text = ''
    def RetornaString(self): return Interface.tmp_text
    def RetornaScroll(self,x=0): return Interface.scroll
    def ZeraScroll(self): Interface.valor_scroll = 0
    def MudaString(self,tmp_text):Interface.tmp_text = tmp_text
    def RetornaXrelativo(self):return Interface.x_relativo
    def RetornaYrelativo(self):return Interface.y_relativo
    def RetornaXref(self):return Interface.x_ref
    def RetornaYref(self):return Interface.y_ref
    def MudaRef(self,lista=[0,0]): 
        Interface.x_ref = lista[0]
        Interface.y_ref = lista[1]
    def MudaRelativo(self,lista=[0,0]): 
        Interface.x_relativo += lista[0]
        Interface.y_relativo += lista[1]   
    def MouseClick(self):
        Interface.mouse_clicked = True
    def RetornaBotaoMouse(self):
        return Interface.botao_mouse
    def MouseClicked(self):
        if Interface.mouse_clicked:   
            Interface().MudaBotaoMouse(mouseButton)    
            Interface.mouse_clicked = False
            return True
        else:
            return False         
    def MousePressed(self,estado):
        Interface.mouse_pressed = estado    
    def PalavrasChave(self):
        if Interface.tmp_text == 'projeto':
             Frames().frame_quadriculado.MudaPontos([[43.13,477.89],[104.00,569.97],[432.34,228.68],[615.07,85.91],[440.13,661.23],[588.14,392.53],[885.73,752.85],[64.18,319.32],[8.47,305.84],[903.42,237.31]])
        elif Interface.tmp_text == 'faruk':
             Frames().frame_quadriculado.MudaPontos([[0,0],[0,-10],[0,-20],[0,-30],[0,-40],[0,-50],[10,-50],[20,-50],[30,-50],[40,-50],[10,-30],[20,-30],[30,-30],[100,0],[105,-10],[110,-20],[115,-30],[120,-40],[125,-50],[150,0],[145,-10],[140,-20],[135,-30],[130,-40],[115,-20],[120,-20],[125,-20],[130,-20],[135,-20],[200,0],[200,-10],[200,-20],[200,-30],[200,-40],[200,-50],[210,-50],[220,-50],[230,-50],[240,-40],[240,-30],[230,-20],[220,-20],[210,-20],[240,-10],[250,0],[300,-50],[300,-40],[300,-30],[300,-20],[300,-10],[310,0],[320,0],[330,0],[340,0],[350,-10],[350,-20],[350,-30],[350,-40],[350,-50],[400,0],[400,-10],[400,-20],[400,-30],[400,-40],[400,-50],[410,-20],[420,-30],[430,-40],[440,-50],[420,-10],[430,0]])
        elif Interface.tmp_text == 'apagar':
            Frames().frame_quadriculado.MudaPontos([])
            Frames().frame_quadriculado.MudaCentros([])
       
        print(Interface().RetornaString()+'malditatag')
        n_centros = matchAll(str(Interface().RetornaString()+'malditatag'),"Digite o numero de centros: (.*?)malditatag")
        if str(type(n_centros))=='<type \'array.array\'>':
            if n_centros[0][1] in '123456789': Frames().frame_quadriculado.MudaNCentros(int(n_centros[0][1]))

def keyPressed():
  Interface().MudaTempoUltimaTecla()
  if key >= 'a' and key <= 'z' or key == ' ' or key == '.' or key >= 'A' and key <= 'Z' or key >= '0' and key <= '9' or key == '!' or key == '?':
    Interface().MudaString(Interface().RetornaString() + str(key))
    Tarefas().TarefaLetra(key)
  if keyCode == DOWN:
    Tarefas().TarefaCodigo('DOWN')
  elif keyCode == LEFT:
    Tarefas().TarefaCodigo('LEFT')
  elif keyCode == RIGHT:
    Tarefas().TarefaCodigo('RIGHT')
  elif keyCode == UP:
    Tarefas().TarefaCodigo('UP')
  elif keyCode == ENTER:
    Tarefas().TarefaCodigo('ENTER')
  if key==DELETE:
    Interface().DeletaString()
  if key==BACKSPACE:
      Interface.tmp_text = Interface.tmp_text[0:int(len(Interface.tmp_text) - 1)]
  else:Interface().PalavrasChave()
def mousePressed():
    Tarefas().TarefaCodigo('MOUSEPRESSED')
def mouseDragged():
    Tarefas().TarefaCodigo('MOUSEDRAGGED')
def mouseClicked():  
    Interface.mouse_clicked = True
    Interface.mouse_lado = mouseButton
    Tarefas().TarefaCodigo('MOUSECLICKED')
def mouseWheel(event):
  e = event.getCount()
  if e>0:
    #println(str(mouseX)+" "+str(mouseY))
    Tarefas().TarefaCodigo('SCROLLUP')
  else:
    Tarefas().TarefaCodigo('SCROLLDOWN')
    pass
  