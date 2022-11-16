# Created by: Tio Dh
# Created date: 26 Oct 2022

from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *

class rectangle:
    def __init__(self, _x_min, _x_max, _y_min, _y_max, _color='', _canvas_x=0, _canvas_y=0):
        self.__SPEED = 1
        self.__x_min = _x_min
        self.__x_max = _x_max
        self.__y_min = _y_min
        self.__y_max = _y_max
        self.__canvas_x = _canvas_x
        self.__canvas_y = _canvas_y
        self.__y_translate = 0
        self.__x_translate = 0
        self.actual_x_min = self.__x_min-self.__x_translate
        self.actual_x_max = self.__x_max+self.__x_translate
        self.actual_y_min = self.__y_min-self.__y_translate
        self.actual_y_max = self.__y_max+self.__y_translate
        self.__color = _color if type(_color)==set or _color!='' else (255,255,255)
    
    def CalcActualPosition(self):
        self.actual_x_min = self.__x_min-self.__x_translate
        self.actual_x_max = self.__x_max+self.__x_translate
        self.actual_y_min = self.__y_min-self.__y_translate
        self.actual_y_max = self.__y_max+self.__y_translate

    def Render(self):
        glColor3ub(self.__color[0],self.__color[1],self.__color[2])
        glTranslatef(self.__x_translate, self.__y_translate,0)
        glBegin(GL_QUADS)
        glVertex2f(self.__x_min, self.__y_min)
        glVertex2f(self.__x_max, self.__y_min)
        glVertex2f(self.__x_max, self.__y_max)
        glVertex2f(self.__x_min, self.__y_max)
        glEnd()

    def Speed(self, key):
        if key==b'+':
            self.__SPEED+=5
        elif key==b'-':
            self.__SPEED-=5

    def Controller(self, key):
        if key==b'w':
            actual_position = self.__y_max+self.__y_translate+self.__SPEED
            if actual_position<self.__canvas_y:
                self.__y_translate+=self.__SPEED
        elif key==b's':
            actual_position = self.__y_min+self.__y_translate-self.__SPEED
            if actual_position>0:
                self.__y_translate-=self.__SPEED
        elif key==b'a':
            actual_position = self.__x_min+self.__x_translate-self.__SPEED
            if actual_position>0:
                self.__x_translate-=self.__SPEED
        elif key==b'd':
            actual_position = self.__x_max+self.__x_translate+self.__SPEED
            if actual_position<self.__canvas_x:
                self.__x_translate+=self.__SPEED
        elif key==b'q':
            self.__x_translate-=self.__SPEED
            self.__y_translate+=self.__SPEED
        elif key==b'e':
            self.__x_translate+=self.__SPEED
            self.__y_translate+=self.__SPEED

        self.CalcActualPosition()