import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


class CanvasWidget(Widget):

    def __init__(self,**kwargs):

        super(CanvasWidget, self).__init__(**kwargs)

        with self.canvas:

            Color(.234, .456, .678, .8)

            self.rect = Rectangle(pos = self.center,
                                  size = (self.width / 2.,
                                          self.height / 2.))
            self.bind(pos = self.update_rect,
                      size = self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class CanvasApp(App):
    def build(self):
        return CanvasWidget()

CanvasApp().run()