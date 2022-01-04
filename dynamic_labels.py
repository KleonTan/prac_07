from kivy.app import App
from kivy.lang import Builder

class DynamicWidgetsApp(App):
    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.show_label()
        return self.root

    def show_label(self):
        self.root.ids.output_1.text = "Bob Brown's phone number is 0414144411"
        self.root.ids.output_2.text = "Cat Cyan's phone number is 0441411211"
        self.root.ids.output_3.text = "Oren Ochre's phone number is 0432123456"

DynamicWidgetsApp().run()