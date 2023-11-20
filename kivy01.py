# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.lang import Builder
# from kivy.uix.image import Image
# #import main

# # class miButton(App):
# #     def build(self):
# #         return Button(text="Next",pos=(400,100),size_hint=(.25,.18))
# # miButton().run()

# # class Image(App):
# #     def build(self):
# #         return Image(source=f"/digits/digit1.png")
# # Image().run()

# Builder.load_string("""
# <KivyButton>:
#     Button:
#         text:"Siguiente"
#         size_hint: .12,.12

#     Image:
#         source: f"digits/digit1.png"
#         source: f"digits/digit2.png"

#         #center_x: self.parent.center_x
#         #center_y: self.parent.center_y
#         size_hint: .50,.48



# """)


# class KivyButton(App,BoxLayout):
#     def build(self):
#         return self

# KivyButton().run()

# class MainApp(App):
#     def build(self):
#         img = Image(source= 'digits/digit1.png',
#                     size_hint=(1, .5),
#                     pos_hint={'center_x':.5, 'center_y':.5})
#         button=Button(text='Siguiente',
#                        size_hint=(.5,.5),
#                        pos_hint={'center_x':.5,'center_y':.5})
#         button.bind(on_press=self.on_press_button)

#         return  img

#     def on_press_button(self,instance):
#         print('You pressed the button!')

# if __name__=='__main__':
#     app=MainApp()
#     app.run()