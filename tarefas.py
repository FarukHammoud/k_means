from index import *

class Tarefas:

  #Vetor Tarefa por Letra e Codigo
  tarefa_letra = []
  tarefa_codigo = []
  codigo = []
  indice_codigo = 0
  
  #Inicializacao
  def __init__(self):
    for i in range(512):
      Tarefas.tarefa_letra.append('')
      Tarefas.tarefa_codigo.append('')
      Tarefas.codigo.append('')
    
  #Funcao Tarefa
  def AlteraTarefaLetra(self,tarefa,letra): Tarefas.tarefa_letra[int(ord(letra))] = tarefa
  def AlteraTarefaCodigo(self,tarefa,codigo):
    Tarefas.tarefa_codigo[Tarefas.indice_codigo] = tarefa
    Tarefas.codigo[Tarefas.indice_codigo] = codigo
    Tarefas.indice_codigo+=1
  def Tarefa(self,tarefa):
    #print(tarefa)  
    if tarefa == '':
        pass
    if tarefa == 'Ativa Frame Animacao Inicial':
        Frames().AtivaFrame(0)
    if tarefa == 'Desativa Frame Animacao Inicial':
        Frames().DesativaFrame(0)
    if tarefa == 'Ativa Frame Quadriculado':
        Frames().AtivaFrame(1)
    if tarefa == 'Desativa Frame Quadriculado':
        Frames().DesativaFrame(1)
    if tarefa == 'Ativa Frame Menu':
        Frames().AtivaFrame(3)
    if tarefa == 'Desativa Frame Menu':
        Frames().DesativaFrame(3)
    if tarefa == 'Pula Inicio':
        Frames().DesativaFrame(0)
        Frames().AtivaFrame(1)
    if tarefa == 'Estabelece Referencia':
        Interface().MudaRef([mouseX,mouseY])
    if tarefa == 'Calcula Arraste Mouse':
        Interface().MudaRelativo([mouseX - Interface().RetornaXref(),mouseX - Interface().RetornaYref()])
        Interface().MudaRef([mouseX,mouseY])
    if tarefa == 'Processa Scroll Up':
        if Frames().MouseDentro(1):
            Interface().ScrollPlus(1)
    if tarefa == 'Processa Scroll Down':  
        if Frames().MouseDentro(1):
            Interface().ScrollMinus(1)
    if tarefa == 'Processa MouseDragged':  
        Interface().MudaRelativo([mouseX-Interface().RetornaXref(),mouseY-Interface().RetornaYref()])
        Interface().MudaRef([mouseX,mouseY])
    if tarefa == 'Processa MouseClicked':  
        if Frames().MouseDentro(1):
            Tarefas().Tarefa('Estabelece Referencia')
            Interface().MouseClick()    
    if tarefa == 'Exibe Clique para adicionar/deletar um ponto':
        Frames().frame_quadriculado.MostraMensagem('Clique para adicionar/deletar um ponto')  
    if tarefa == 'Exibe Clique para definir o numero de centros':
        Frames().frame_quadriculado.MostraMensagem('Clique para definir o numero de centros')  
    if tarefa == 'Exibe Clique para executar o k-means':
        Frames().frame_quadriculado.MostraMensagem('Clique para executar o k-means ')
    if tarefa == 'Entra modo adiciona/deleta pontos':
        Frames().frame_quadriculado.MudaModo(1)
    if tarefa == 'Entra modo define n centros':
        Frames().frame_quadriculado.MudaModo(2)
        Interface().MudaString('Digite o numero de centros: ')
        Frames().frame_quadriculado.bot_def_k.MudaValor(False)
        Interface().MudaTempoUltimaTecla()
    if tarefa == 'Entra modo calculo k-means':
        print('centros passado '+str(Frames().frame_quadriculado.RetornaNCentros()))
        Frames().frame_quadriculado.MudaCentros(Calculo().KMeans(Frames().frame_quadriculado.RetornaPontos(),Frames().frame_quadriculado.RetornaNCentros()))
        Frames().frame_quadriculado.MudaModo(3)                     
        Frames().frame_quadriculado.bot_calcu.MudaValor(False)
    if tarefa == 'Processa MousePressed':  
        if Frames().MouseDentro(1):
            Tarefas().Tarefa('Estabelece Referencia')
            Interface().MousePressed(True)            
  def TarefaLetra(self,letra):
    Tarefas().Tarefa(Tarefas.tarefa_letra[ord(letra)])
  def TarefaCodigo(self,texto):
    for i in range(256):
      if Tarefas.codigo[i] == texto:
        Tarefas().Tarefa(Tarefas.tarefa_codigo[i])
        