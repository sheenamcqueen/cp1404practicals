from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesToKilometresApp(App):
    def build(self):
        self.title = "Kilometres"
        self.root = Builder.load_file('kilometres.kv')
        return self.root

    def handle_calculate(self,value):
        result = value + 1
        self.root.ids.output_label.text = str(result)


ConvertMilesToKilometresApp().run()