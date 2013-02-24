import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.core.window import Window

from kivy.lang import Builder
from kivy.graphics import Color
import math

Builder.load_string("""
<PongBall>:
    size: 50, 50 
    canvas:
        Color:
            rgb: self.r,self.g,self.b
        Ellipse:
            pos: self.pos
            size: self.size


<PongGame>:
    ball: pong_ball
    PongBall:
        id: pong_ball
        center: self.parent.center
""")

class PongBall(Widget):
    r = NumericProperty(.5)
    g = NumericProperty(.5)
    b = NumericProperty(.5)

class PongGame(Widget):
    
    def __init__(self):
        super(PongGame, self).__init__()
        self.frames = 0 
    
    def update(self, *args):
        red = (.5*(math.sin(self.frames*.1)+1.0))
        print "updated....",self.frames,red
        self.ball.r = red
        self.ball.center = self.center 
        self.frames += 1
    
Factory.register("PongBall", PongBall)#eg
Factory.register("PongGame", PongGame)

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)#called 1 in 60
        return game
    
if __name__ in ('__android__', '__main__'):
    PongApp().run()
