from OpenGL.GL import *

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    glLightfv(GL_LIGHT0, GL_POSITION, (5, 10, 5, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.3, 0.3, 0.3, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8, 0.8, 0.8, 1))

def set_material(shininess=32):
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.2, 0.2, 0.2, 1))
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)
