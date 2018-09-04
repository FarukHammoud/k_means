from index import *
from interface import *

def setup():
    fullScreen()
    frameRate(10)#Manter isso aqui(diminuir pra 5 em caso de MAX CPU)
    Tarefas().Tarefa('Ativa Frame Animacao Inicial')
    Tarefas().AlteraTarefaLetra('Pula Inicio',' ')
    Tarefas().AlteraTarefaCodigo('Processa Scroll Up','SCROLLUP')
    Tarefas().AlteraTarefaCodigo('Processa Scroll Down','SCROLLDOWN')
    Tarefas().AlteraTarefaCodigo('Processa MouseDragged','MOUSEDRAGGED')
    Tarefas().AlteraTarefaCodigo('Processa MouseClicked','MOUSECLICKED')
    Tarefas().AlteraTarefaCodigo('Processa MousePressed','MOUSEPRESSED')

def draw():
    Frames().Mostrar()