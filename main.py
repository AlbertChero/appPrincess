from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import socket

class SimpleCounterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30)
        
        self.counter = 0  # Variable para almacenar el contador
        
        self.label = Label(text=str(self.counter), halign='center', font_size=50)
        button = Button(text='Incrementar')
        button.bind(on_press=self.incrementar_contador)  # Asociar la función al evento del botón
        
        layout.add_widget(self.label)
        layout.add_widget(button)
        
        # Configurar el cliente socket una vez al inicio de la aplicación
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('192.168.0.7', 8888)  # Ingresa la dirección IP del servidor
        
        try:
            self.client_socket.connect(server_address)
        except ConnectionRefusedError:
            print("No se pudo conectar al servidor.")
        
        return layout
    
    def incrementar_contador(self, instance):
        self.counter += 1
        self.label.text = str(self.counter)  # Actualizar el texto del Label con el contador
        
        # Enviar el incremento al servidor
        self.send_increment(str(1))
    
    def send_increment(self, incremento):
        try:
            incremento = int(incremento)
        except ValueError:
            print("Ingrese un número válido.")
            return
        
        # Enviar el incremento al servidor utilizando el socket creado anteriormente
        try:
            self.client_socket.sendall(str(incremento).encode())
        except ConnectionRefusedError:
            print("No se pudo conectar al servidor.")

if __name__ == '__main__':
    SimpleCounterApp().run()
