#python #main.py


from kivy.config import Config

Config.set('graphics', 'resizable', True)

# Config.set('graphics', 'resizable', '0')
# Config.set('graphics', 'width', '500')

import kivy

kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label


class MyLabelApp(App):
    def build(self):
        l2 = Label(text='[color=ff3333][b]Hello[/b][/color]\n [color=333fff]GFG[/color]',
                   font_size='20sp',
                   markup=True)

        return l2


label = MyLabelApp()

label.run()
