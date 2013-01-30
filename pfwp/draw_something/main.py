import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import *
import random

class Grass(Widget):
    def update(self):
        with self.canvas:
            #randomly darw grass
            Color(1,1,1)
            w = 1000#self.get_parent_window().width
            h = 1000#self.get_parent_window().height
            Rectangle(size=(w, h), pos=(self.x, self.y))
            Color(.2,.8,.2)
            var = .4
            for i in range(2):
                r,g,b = .7+random.random()*var,.7+random.random()*var,.7+random.random()*var
                Color(r,g,b)
                x = w*random.random() - 50
                y = h*random.random() - 50
                Rectangle(source='grass.png', pos=(x,y), size=(100,100))

class MyWidget(Widget):
    def update(self, dt):
        with self.canvas:
            print dt
        

class DrawSomethingApp(App):
    def build(self):
        wid1 = MyWidget()
        #Clock.schedule_interval(game.update, 1.0/60.0)
        return wid1

if __name__ == '__main__':
    DrawSomethingApp().run()