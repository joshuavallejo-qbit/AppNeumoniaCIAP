from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import normalize

# load the model
model = load_model('handwritten.model')

# function to predict the digit
def predict_digit(filename):
    img = cv2.imread(filename)[:,:,0]
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    print(f"The digit is probably a {np.argmax(prediction)}")
    return np.argmax(prediction)

class DigitPredictorApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Add the first image to the layout
        self.image = Image(source='digits/digit1.png')
        self.layout.add_widget(self.image)

        # Add the button to change the model image
        self.button = Button(text='Change Model Image')
        self.button.bind(on_press=self.change_image)
        self.layout.add_widget(self.button)

        # Add the button to exit the app
        self.exit_button = Button(text='Exit', on_press=self.stop)
        self.layout.add_widget(self.exit_button)

        return self.layout

    def change_image(self, instance):
        # get the number of the current image
        current_image_number = int(self.image.source.split('/')[-1].split('.')[0][-1])

        # check if there is a next image
        if os.path.isfile(f"digits/digit{current_image_number + 1}.png"):
            self.image.source = f"digits/digit{current_image_number + 1}.png"
            predicted_digit = predict_digit(self.image.source)
            self.button.text = f'The digit is: {predicted_digit}'
        else:
            self.button.text = 'No more images to display!'

if __name__ == '__main__':
    DigitPredictorApp().run()