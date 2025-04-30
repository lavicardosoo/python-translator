from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.core.text import LabelBase
from translate import Translator

#registra uma fonte para usar no projeto
LabelBase.register(name='fonte',fn_regular='font.ttf')

#carrega o arquivo kivy para gerar a interface do app
kv = Builder.load_file('layout.kv')

#define o tamanho da tela
Window.size = (800,600)

#essa classe vai ser usada como referência no arquivo kivy
class Millyzinha(BoxLayout):
    pass

#a classe que cria o app
class MyPussinha(App):
    def build(self):

        #isso aquir carrega o design que foi feito no arqv kivy <3
        self.layout = Millyzinha()

        #idiomas que eu vou utilizar como base
        self.idiomas = {'Inglês':'en','Português':'pt','Francês':'fr','Espanhol':'es'}
        return self.layout
    
    #método de tradução que vai ser ativado ao clicar no botão de traduzir
    def traduzir(self):

        #pega o elemento que se refere ao idioma que vai ser traduzido
        idiomaOrigem = self.layout.ids.IdiomaOrigem.text

        #pega o elemento que se refere ao idioma da tradução
        idiomaResposta = self.layout.ids.IdiomaResposta.text

        #pega a codificação do 1° idioma escolhido dentro do dicionário
        idiomaOrigem = self.idiomas[idiomaOrigem]

        #pega a codificação do 2° idioma escolhido dentro do dicionário
        idiomaResposta = self.idiomas[idiomaResposta]

        #pega o texto que vai ser traduzido
        conteudo = self.layout.ids.Conteudo.text

        #aqui ele instancia o objeto que vai fazer as traduções ;)
        aphonsinha = Translator(to_lang=idiomaResposta, from_lang=idiomaOrigem)

        #aqui ele usa o método que faz a tradução
        traducao = aphonsinha.translate(conteudo)

        #faz com que a resposta apareça em um dos elementos
        self.layout.ids.Resposta.text = traducao

#criação do objeto principal responsável pelo app
app = MyPussinha()

#iniciação do app <3
app.run()