from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
            

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40)

        texto_1 = Label(text='¿Quieres un haiku?',font_size=30)
        button_to_settings = Button(text='NO :(', on_press=self.change_to_settings)
        button_poesia = Button(text='SÍ :3', on_press=self.change_to_poesia)

        layout.add_widget(texto_1)
        layout.add_widget(button_to_settings)
        layout.add_widget(button_poesia)
        self.add_widget(layout)

    def change_to_settings(self, instance):
        self.manager.current = 'settings'
    
    def change_to_poesia(self, instance):
        self.manager.current = 'poesia'

    

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        
        layout2=BoxLayout(orientation='vertical',padding=30)
        
        no_estes_triste=Label(halign='center',text='Ya pero no estés triste puem \n\n\nMi princesita hermosa UwU',font_size=30)
        button_to_menu = Button(text='Intentemos de nuevo :3', font_size=30,on_press=self.change_to_menu)
        layout2.add_widget(button_to_menu)
        layout2.add_widget(no_estes_triste)
        self.add_widget(layout2)

    def change_to_menu(self, instance):
        self.manager.current = 'menu'
        
class PoesiaScreen(Screen):
    def __init__(self, **kwargs):
        super(PoesiaScreen, self).__init__(**kwargs)
        layout3=BoxLayout(orientation='vertical',padding=30)
        
        haiku=Label(halign='center',text='Recordando el ayer, me di cuenta de algo \nNo es solo tu mirada \nNo son solo tus labios \nNi tampoco solo tus caricias \nHay algo más en ti, que me motiva a seguir \nY creo que ya lo sé \nTu infinita existencia \nTu sonrisa preciosa \nTus ojos cristalinos \nCon la mirada más dulce jamás vista \nPodría seguir, porque lo que veo en ti \nEs infinito, como las estrellas en el universo \nY tan grande, como mi amor por ti, no lo niego :3 \n\nTE QUIERO MUCHO MI NIÑA HERMOSA')
        button_to_menu = Button(size_hint=(0.5,0.2),text='Volver? ugu', on_press=self.change_to_menu)
        layout3.add_widget(haiku)
        layout3.add_widget(button_to_menu)
        self.add_widget(layout3)

    def change_to_menu(self, instance):
        self.manager.current = 'menu'

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        
        menu_screen = MenuScreen(name='menu')
        settings_screen = SettingsScreen(name='settings')
        poesia_screen = PoesiaScreen(name='poesia')
        
        sm.add_widget(menu_screen)
        sm.add_widget(settings_screen)
        sm.add_widget(poesia_screen)
        return sm

if __name__ == '__main__':
    TestApp().run()