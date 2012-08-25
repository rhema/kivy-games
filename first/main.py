import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import *
import random

class Grass(Widget):
    def draw_grass(self):
        with self.canvas:
            #randomly darw grass
            Color(1,1,1)
            w = 1000#self.get_parent_window().width
            h = 1000#self.get_parent_window().height
            Rectangle(size=(w, h), pos=(self.x, self.y))
            Color(.2,.8,.2)
            for i in range(400):
                x = w*random.random() - 50
                y = h*random.random() - 50
                Rectangle(source='grass.png', pos=(x,y), size=(100,100))

class PongGame(Widget):
    def update(self, dt):
#        self.draw_grass()
        with self.canvas:
            print "tada"
            if self.once is False:
                g = Grass()
                self.add_widget(Grass())
                g.draw_grass()
                self.once = True
#            Rectangle(pos=(random.random()*self.width, random.random()*self.height), size=(50, 50))
        

class PongApp(App):
    def build(self):
        game = PongGame()
        game.once = False
        Clock.schedule_interval(game.update, 30.0/60.0)
        return game

if __name__ == '__main__':
    PongApp().run()