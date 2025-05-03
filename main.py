import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Label

class MyLabelApp(App):

    def build(self):
        lbl = Label(text="Label added!",
                    font_size='20sp',
                    color=(0.41, 0.42, 0.74, 1)
                    )
        return lbl


label = MyLabelApp()
label.run()