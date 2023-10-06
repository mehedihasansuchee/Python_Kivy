

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        
        self.text_input = TextInput()
        self.text_input.bind(text=self.on_text_input)

        
        self.label = Label(text='Hello, Kivy.')

        
        layout.add_widget(self.text_input)
        layout.add_widget(self.label)


        return layout

    def on_text_input(self, instance, value):
        self.label.text = value


if __name__ == '__main__':
    MyApp().run()
