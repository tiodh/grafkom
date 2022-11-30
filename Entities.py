# Created by: Tio Dh
# Created date: 26 Oct 2022

from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *

class Object:
    def __init__(self, _x_min, _x_max, _y_min, _y_max, _color=(255,255,255), _canvas_x=0, _canvas_y=0):
        self.SPEED = 1
        self.x_min = _x_min
        self.x_max = _x_max
        self.y_min = _y_min
        self.y_max = _y_max
        self.canvas_x = _canvas_x
        self.canvas_y = _canvas_y
        self.y_translate = 0
        self.x_translate = 0
        self.actual_x_min = self.x_min-self.x_translate
        self.actual_x_max = self.x_max+self.x_translate
        self.actual_y_min = self.y_min-self.y_translate
        self.actual_y_max = self.y_max+self.y_translate
        self.color = _color if type(_color)==set or _color!='' else (255,255,255)
    
    def CalcActualPosition(self):
        self.actual_x_min = self.x_min-self.x_translate
        self.actual_x_max = self.x_max+self.x_translate
        self.actual_y_min = self.y_min-self.y_translate
        self.actual_y_max = self.y_max+self.y_translate

    def Render(self):
        glLoadIdentity()

        glColor3ub(self.color[0],self.color[1],self.color[2])
        glTranslatef(self.x_translate, self.y_translate,0)
        glBegin(GL_QUADS)
        glVertex2f(self.x_min, self.y_min)
        glVertex2f(self.x_max, self.y_min)
        glVertex2f(self.x_max, self.y_max)
        glVertex2f(self.x_min, self.y_max)
        glEnd()

    
class ControlledObject(Object):
    def __init__(self, _x_min, _x_max, _y_min, _y_max, _color, _canvas_x=0, _canvas_y=0):
        super().__init__(_x_min, _x_max, _y_min, _y_max, _color, _canvas_x, _canvas_y)
        self.is_right = True
        self.is_top = True

    def SpeedAdjust(self, key):
        if key==b'+':
            self.SPEED+=5
        elif key==b'-':
            self.SPEED-=5

    def Controller(self, key):
        if key==b'w':
            actual_position = self.y_max+self.y_translate+self.SPEED
            if actual_position<self.canvas_y:
                self.y_translate+=self.SPEED
        elif key==b's':
            actual_position = self.y_min+self.y_translate-self.SPEED
            if actual_position>0:
                self.y_translate-=self.SPEED
        elif key==b'a':
            actual_position = self.x_min+self.x_translate-self.SPEED
            if actual_position>0:
                self.x_translate-=self.SPEED
        elif key==b'd':
            actual_position = self.x_max+self.x_translate+self.SPEED
            if actual_position<self.canvas_x:
                self.x_translate+=self.SPEED
        elif key==b'q':
            self.x_translate-=self.SPEED
            self.y_translate+=self.SPEED
        elif key==b'e':
            self.x_translate+=self.SPEED
            self.y_translate+=self.SPEED

        self.CalcActualPosition()

class AnimatedObject(Object):
    def __init__(self, _x_min, _x_max, _y_min, _y_max, _color, _canvas_x=0, _canvas_y=0):
        super().__init__(_x_min, _x_max, _y_min, _y_max, _color, _canvas_x, _canvas_y)
        self.is_right = True
        self.is_top = True
        self.play=True

    def Animate(self):
        glLoadIdentity()
        if self.play:
            if self.Evaluate()[0]:
                self.x_translate+=1 
            else:
                self.x_translate-=1
        
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glTranslatef(self.x_translate, self.y_translate,0)
        glBegin(GL_QUADS)
        glVertex2f(self.x_min, self.y_min)
        glVertex2f(self.x_max, self.y_min)
        glVertex2f(self.x_max, self.y_max)
        glVertex2f(self.x_min, self.y_max)
        glEnd()

    def Controller(self, key):
        if key==b' ':
            self.play = not self.play


    def Evaluate(self):
        y_actual_position = self.y_max+self.y_translate+self.SPEED
        x_actual_position = self.x_max+self.x_translate+self.SPEED
        
        if x_actual_position>=self.canvas_x:
            self.is_right = False
        elif x_actual_position<=0:
            print(x_actual_position)
            self.is_right = True

        if y_actual_position>=self.canvas_y:
            self.is_top = False
        elif y_actual_position<=0:
            self.is_top = True

        return self.is_right, self.is_top
