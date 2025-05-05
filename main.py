# python #main.py


import kivy

kivy.require('1.9.0')

from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.base import runTouchApp
from kivy.lang import Builder

Builder.load_string('''
<ScrollableLabel>:
    text: 'You are learning Kivy\\n' * 100
    do_scroll_x: False
    do_scroll_y: True

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: self.minimum_height

        Label:
            text: root.text
            font_size: 20
            text_size: self.width, None
            size_hint_y: None
            height: self.texture_size[1]
''')


class ScrollableLabel(ScrollView):
    text = StringProperty('')


runTouchApp(ScrollableLabel())
