from PIL.ImageChops import screen
from kivymd.app import MDApp
from kivymd.uix.button.button import theme_text_color_options
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen


class Demo(MDApp):

    def build(self):
        screen = Screen()

        lbl = MDLabel(
            text="Welcome!",
            pos_hint={
                'center_x':0.8,
                'center_y':0.8
            },
            theme_text_color="Custom",
            text_color=(0.5,0,0.5,1),
            font_style='Caption'
        )

        lbl1 = MDLabel(
            text="Welcome!",
            pos_hint={
                'center_x': 0.8,
                'center_y': 0.5
            },
            theme_text_color="Custom",
            text_color=(0.5, 0, 0.5, 1),
            font_style='H2'
        )

        lbl2 = MDLabel(
            text="Welcome!",
            pos_hint={
                'center_x': 0.8,
                'center_y': 0.2
            },
            theme_text_color="Custom",
            text_color=(0.5, 0, 0.5, 1),
            font_style='H1'
        )

        screen.add_widget(lbl)
        screen.add_widget(lbl1)
        screen.add_widget(lbl2)

        return screen


if __name__ == "__main__":
    Demo().run()