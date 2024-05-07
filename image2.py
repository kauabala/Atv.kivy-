from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        
        return AsyncImage(source='')
    
if __name__ == "__main__":
    MinhaApp().run()