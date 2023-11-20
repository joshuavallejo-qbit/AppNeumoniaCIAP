# import os
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import tensorflow as tf
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.image import Image
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.floatlayout import FloatLayout
# from kivy.factory import Factory
# from kivy.properties import ObjectProperty
# from kivy.uix.popup import Popup
# from kivy.uix.filechooser import FileChooserListView

# class MainScreen(BoxLayout):
#     def load_image(self):
#         # Abre un cuadro de diálogo para seleccionar una imagen
#         # y llama a la función de procesamiento cuando se selecciona una imagen
#         filechooser= FileChooserListView()
#         filechooser.bind(on_submit=self.process_image)
#         popup = Popup(title='Seleccionar una imagen', content=filechooser, size_hint=(None, None), size=(400, 400))
#         popup.open()

#     def process_image(self, instance):
#         # Cargamos la imagen seleccionada
#         file_path = instance.selection and instance.selection[0]  # Obtiene la ruta de la imagen seleccionada
#         if file_path:
#             try:
#                 img = cv2.imread(file_path)[:, :, 0]
#                 img = np.invert(np.array([img]))

#                 # Realizamos la predicción
#                 prediction = model.predict(img)
#                 digit = np.argmax(prediction)

#                 # Actualizamos la imagen y el texto en la interfaz
#                 self.ids.img_result.source = file_path
#                 self.ids.result_label.text = f'El dígito es probablemente un {digit}'
#             except:
#                 self.ids.result_label.text = 'Error al procesar la imagen'
#         else:
#             self.ids.result_label.text = 'Ninguna imagen seleccionada'

# class MyApp(App):
#     def build(self):
#         self.title = 'Clasificador de Dígitos Manuscritos'
#         return MainScreen()

# if __name__ == '__main__':
#     # Cargar el modelo de TensorFlow
#     model = tf.keras.models.load_model('handwritten.model')
#     MyApp().run()
