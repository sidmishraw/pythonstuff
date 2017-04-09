# main.py

__author__ = 'sidmishraw'

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.core import camera


class Tex(Widget):

  def __init__(self):
    self.texture = Texture.create(size=(640, 480))




class MyApp(App):
  'the application'
  def build(self):
    return Tex()



def main():
  'the main entry point for the app'
  MyApp().run()

if __name__ == '__main__':
  print('running main')
  main()