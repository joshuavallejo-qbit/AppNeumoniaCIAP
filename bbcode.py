from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
import os
import random

class ImageViewer(BoxLayout):
    def __init__(self, **kwargs):
        super(ImageViewer, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.img = Image(pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.8, .8))
        self.add_widget(self.img)

        self.change_button = Button(text='Change Image', font_size=24, size_hint=(.8, .2))
        self.change_button.bind(on_press=self.change_image)
        self.add_widget(self.change_button)

        self.img_folder = 'digits'
        self.images = [os.path.join(self.img_folder, img) for img in os.listdir(self.img_folder) if img.endswith('.png')]
        self.img.source = random.choice(self.images)

    def change_image(self, instance):
        self.img.source = random.choice(self.images)

class ImageViewerApp(App):
    def build(self):
        return ImageViewer()

if __name__ == '__main__':
    ImageViewerApp().run()