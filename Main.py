# Created by: Tio Dh
# Created date: 26 Oct 2022

# 1. Animasi
# 2. Integrasi Animasi + Controll
# 3. Collision antara animasi dengan objek lain

from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *
from Entities import ControlledObject, AnimatedObject
from random import randrange

w,h= 500,500
# obstacles = []
# for i in range(10):
#     x = randrange(0,500)
#     y = randrange(0,500)
#     obstacles.append(rectangle(x, x+10, y, y+10, (x, y, x), w, h))

rec1 = ControlledObject(0, 200, 0, 200, (255,0,0), w, h)
bullet = AnimatedObject(0, 20, 0, 20, (255,255,0), w, h)
# rec2 = rectangle(100,200,100,200)

def iterate():
    glViewport(0, 0, w, h) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0) 
    glMatrixMode (GL_MODELVIEW) 
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    
    rec1.Render()
    bullet.Animate()

    glutSwapBuffers()

def controller(key, x, y):
    rec1.SpeedAdjust(key)
    rec1.Controller(key)

    bullet.Controller(key)


    
glutInit()
glutInitDisplayMode(GLUT_RGBA) 
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0)

wind = glutCreateWindow("OpenGL Coding Practice") 
glutDisplayFunc(showScreen) 
glutIdleFunc(showScreen)
glutKeyboardFunc(controller)
glutMainLoop()