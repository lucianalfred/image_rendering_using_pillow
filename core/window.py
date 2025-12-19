"""
Sistema de janela 3D usando Pygame e OpenGL
"""

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import os

class Window3D:
    """Gerenciador de janela 3D"""
    
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        
        # Configurar para usar OpenGL 2.1 (compatível)
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        
        # Configurar atributos OpenGL antes de criar a janela
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 2)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 1)
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)
        pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)
        
        # Inicializar Pygame
        pygame.init()
        
        # Criar janela OpenGL
        self.screen = pygame.display.set_mode(
            (width, height), 
            pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE
        )
        pygame.display.set_caption(title)
        
        # Configurar OpenGL
        self.setup_opengl()
        
    def setup_opengl(self):
        """Configurar parâmetros do OpenGL"""
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        # Configurar iluminação básica
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        
        # Configurar projeção usando matriz fixa
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self.width / self.height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        # Configurar luz
        glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 10.0, 5.0, 1.0])
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
        
    def resize(self, width, height):
        """Redimensionar janela"""
        self.width = width
        self.height = height
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)