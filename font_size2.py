from kivy.app import App
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        return Button(text='clique Aqui', font_size=50)
    
if __name__ == "__main__":
    MinhaApp().run()