import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config

Config.set('kivy','window_icon','tick.ico')

class WindowManager(ScreenManager):
	pass

class MainWindow(Screen):
	pass

class ChoiceQuestionsWindow(Screen):
	pass
class ChoiceTenQuestionsWindow(Screen):
	pass

kv= Builder.load_file('main_kivy.kv')

class Corin(App):
	def build(self):
		return kv
if __name__ == '__main__':
	Corin().run()