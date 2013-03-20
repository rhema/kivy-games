#
#
#


import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.core.window import Window


from kivy.lang import Builder
from kivy.graphics import Color
import math
import random
Builder.load_string("""
<Ship>:
    size: 50, 50 
""")


class SpaceThing(Scatter):
    def __init__(self, *args, **kwargs):
        Scatter.__init__(self)
        self.game = args[0]#game#This has all of the keys in it
        self.accel = Vector(0, 0)
        self.accel_theta = 0

    def move(self):
        self.move_by_acceleration()
    
    def gravity_pull(self):
        #dist from center
        wc = self.game.width/2
        hc = self.game.height/2
        d = math.sqrt((wc-self.x)*(wc-self.x)+(hc-self.y)*(hc-self.y))
            
    def move_by_acceleration(self):
        self.x += self.accel.x
        self.y += self.accel.y
        print self.game.width, self.x
        print self.x
        if self.x > self.game.width:
            self.x -= self.game.width + 50
        if self.x + 100 < 0:
            self.x += self.game.width + 100

        if self.y > self.game.height:
            self.y -= self.game.height + 50
        if self.y + 100 < 0:
            self.y += self.game.height + 100
        
        #s = SpaceGame()
        

class SpaceJunk(SpaceThing):
    def __init__(self, *args, **kwargs):
        super(SpaceJunk, self).__init__(*args, **kwargs)
        self.game = args[0]#This has all of the keys in it
        max_speed = 4
        self.accel = Vector(random.random()*(max_speed) - (max_speed/2) , random.random()*(max_speed) - (max_speed/2))
        self.accel_theta = 0
        self.life = 10000
        self.width=10
        self.heihgt=10
    
    def move(self):
        SpaceThing.move(self)
        self.life -= 1
        if self.life < 0:
            ws = self.children
            self.game.remove_widget(self)

class ShipPlayer(SpaceThing):
    max_speed = NumericProperty(.1)
    turn_speed = NumericProperty(2)
    def __init__(self, *args, **kwargs):
        #super(ShipPlayer, self).__init__()
        super(ShipPlayer, self).__init__(*args, **kwargs)
        self.game = args[0]#This has all of the keys in it
        #self.game = game#This has all of the keys in it
        self.accel = Vector(0, 0)
    
    def move(self):
#        self.rotation += self.turn_speed*self.game.key_value("left")
#        self.rotation -= self.turn_speed*self.game.key_value("right")
#
#        self.center_x += self.max_speed*math.cos(self.rotation*.0174532925)*self.game.key_value("up")
#        self.center_y += self.max_speed*math.sin(self.rotation*.0174532925)*self.game.key_value("up")
        self.rotation += self.turn_speed*self.game.key_value("left")
        self.rotation -= self.turn_speed*self.game.key_value("right")

        self.accel.x += self.max_speed*math.cos(self.rotation*.0174532925)*self.game.key_value("up")
        self.accel.y += self.max_speed*math.sin(self.rotation*.0174532925)*self.game.key_value("up")
        self.move_by_acceleration()

class SpaceGame(Widget):
    
    def key_value(self,key):
        #print self.key_dict
        if key in self.key_dict:
            if self.key_dict[key] == False:
                return 0
            else:
                return 1
        return 0
    
    def add_debree(self):
        junk = SpaceJunk(self)
        image = Image(source='junk.png')
        junk.add_widget(image)
        junk.center_x = 300
        junk.center_y = 300
        self.add_widget(junk)
        self.crafts += [junk]
    
    def _key_down(self,keyboard, keycode, text, modifiers):
        self.key_dict[keycode[1]] = True
        #print keycode[1]
        if keycode[1] == 'spacebar':
            print "fire!"
            self.add_debree()
        #print "down",keycode
        
    def _key_up(self,keyboard, keycode):
        self.key_dict[keycode[1]] = False
        #print "up",keycode
        
    def _keyboard_closed(self):
        #print 'My keyboard have been closed!'
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None
    
    def __init__(self):
        self.key_dict = {}
        super(SpaceGame, self).__init__()
        self.crafts = []
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._key_down)
        self._keyboard.bind(on_key_up=self._key_up)
        
        image = Image(source='player.png')
        image.x -= 0
        image.y -= 0
        self.ship = ShipPlayer(self)
        self.ship.add_widget(image)
        self.add_widget(self.ship)
        self.frames = 0
        self.crafts += [self.ship]
    
    def update(self, *args): 
        #keep track of fames
        self.frames += 1
        for craft in self.crafts:
            craft.move()
            if craft == self.ship:
                continue
            if craft.collide_widget(self.ship):
                #add random accell to both
                print "KABOOM!!!"
                max_speed = 1
                self.ship.accel = Vector(0,0)
                
        #self.ship.move()

#        self.ship.rotation += self.ship.turn_speed*self.key_value("left")
#        self.ship.rotation -= self.ship.turn_speed*self.key_value("right")
#
#        self.ship.center_x += self.ship.max_speed*math.cos(self.ship.rotation*.0174532925)*self.key_value("up")
#        self.ship.center_y += self.ship.max_speed*math.sin(self.ship.rotation*.0174532925)*self.key_value("up")

class SpaceApp(App):
    def build(self):
        game = SpaceGame()
        Clock.schedule_interval(game.update, 1.0/60.0)#called 1 in 60
        return game


if __name__ in ('__android__', '__main__'):
    SpaceApp().run()
