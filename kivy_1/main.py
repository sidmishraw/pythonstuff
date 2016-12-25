# The main.py as intended by Kivy. This is used as the main entry point it seems

__author__ = 'sidmishraw'

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
  'the application'
  def build(self):
    return Label(text='App works xD!')



def main():
  'the main entry point for the app'
  MyApp().run()

if __name__ == '__main__':
  print('running main')
  main()