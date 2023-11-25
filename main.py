from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from random import randint


class PongGame(Widget):
    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)

        # Pelota
        self.ball = None
        self.reset_ball()

        # Raquetas
        self.player1 = Widget(pos=(0, (self.height - 100) / 2))
        self.player2 = Widget(pos=(self.width - 20, (self.height - 100) / 2))

        # Marcador
        self.score_label = Label(pos=(self.width / 2 - 50, self.height - 50), text='0 - 0', font_size=20)
        self.score_player1 = 0
        self.score_player2 = 0

        # Controles
        self.up_button = Button(text='Up', size=(100, 50), pos=(self.width / 4 - 50, 0))
        self.down_button = Button(text='Down', size=(100, 50), pos=(self.width / 4 - 50, 50))

        self.up_button.bind(on_press=self.move_player1_up)
        self.down_button.bind(on_press=self.move_player1_down)

        self.add_widget(self.player1)
        self.add_widget(self.player2)
        self.add_widget(self.score_label)
        self.add_widget(self.up_button)
        self.add_widget(self.down_button)

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def reset_ball(self):
        self.ball = Widget(center=self.center, size=(20, 20))
        self.ball.velocity = [randint(4, 8), randint(4, 8)]  # Cambia de tupla a lista
        self.add_widget(self.ball)

    def move_player1_up(self, instance):
        self.player1.y += 10

    def move_player1_down(self, instance):
        self.player1.y -= 10

    def update(self, dt):
        # Actualizar posiciones de las raquetas
        self.player2.y += self.ball.velocity[1]

        # Mover la pelota
        self.ball.x += self.ball.velocity[0]
        self.ball.y += self.ball.velocity[1]

        # Rebote en las paredes
        if self.ball.y < 0 or self.ball.top > self.height:
            self.ball.velocity[1] = -self.ball.velocity[1]

        # Rebote en las raquetas
        if self.ball.collide_widget(self.player1) or self.ball.collide_widget(self.player2):
            self.ball.velocity[0] = -self.ball.velocity[0]

        # Punto para el jugador 2
        if self.ball.x < 0:
            self.score_player2 += 1
            self.score_label.text = f'{self.score_player1} - {self.score_player2}'
            self.remove_widget(self.ball)
            self.reset_ball()

        # Punto para el jugador 1
        if self.ball.right > self.width:
            self.score_player1 += 1
            self.score_label.text = f'{self.score_player1} - {self.score_player2}'
            self.remove_widget(self.ball)
            self.reset_ball()


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
