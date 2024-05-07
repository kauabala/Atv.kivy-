from kivy.app import App
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        return Label(
            text='olá, senai!',
            halign='left', #Alinha o testo á esquerda
            valign='top',   #Alinha o texto no topo
            size_hint=(None, None),
            size=(150, 50),
            text_size=(150, None)
        )
    
    
if __name__ == '__main__':
    MinhaApp().run()