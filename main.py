from importlib.util import source_hash

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


class CanvasWidget(Widget):

    def __init__(self,**kwargs):

        super(CanvasWidget, self).__init__(**kwargs)

        with self.canvas:

            Color(1, 0, 0, 1)

            self.rect = Rectangle(source = 'logoheader.png',
                                  pos = self.pos,
                                  size = self.size)


            self.bind(pos = self.update_rect,
                      size = self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class CanvasApp(App):
    def build(self):
        return CanvasWidget()

CanvasApp().run()