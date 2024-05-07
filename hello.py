from kivy.app import App
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        return Button(text="hello world! this is my first program in kivy \n i'm a sesiano student")
if __name__ == '__main__':
    MyApp().run()