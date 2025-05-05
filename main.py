#python #main.py


import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder

class uiApp(App):
    def build(self):

        return Builder.load_file('./kv/scroll.kv')


uiApp().run()