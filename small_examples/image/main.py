# See 
#
#


import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
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
""")

class PongBall(Image):
    r = NumericProperty(.5)
    g = NumericProperty(.5)
    b = NumericProperty(.5)
    color_speed = NumericProperty(0)
    
    def on_touch_down(self,touch):
        print "Touched!",touch.x,touch.y
        self.color_speed += .03

class PongGame(Widget):
    def __init__(self):
        super(PongGame, self).__init__()
        self.ball = PongBall(source='img1.png')
        self.add_widget(self.ball)
        self.frames = 0 
    
    def update(self, *args):
        red = (.5*(math.sin(self.frames*self.ball.color_speed)+1.0))
        #print "updated....",self.frames,red
        self.ball.r = red
        self.ball.center = self.center 
        self.frames += 1

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)#called 1 in 60
        return game


if __name__ in ('__android__', '__main__'):
    PongApp().run()
