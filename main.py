#!/usr/bin/env python3
"""
Sistema de Renderização 3D Simples
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class Simple3DRenderer:
    """Sistema 3D simplificado mas funcional"""
    
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        
        # Inicializar Pygame com OpenGL
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)
        self.screen = pygame.display.set_mode(
            (width, height), 
            pygame.OPENGL | pygame.DOUBLEBUF
        )
        pygame.display.set_caption("Casa 3D Simples")
        
        # Configurar OpenGL
        self.setup_opengl()
        
        # Parâmetros da câmera
        self.camera_distance = 5
        self.camera_angle_x = 30
        self.camera_angle_y = 45
        
        # Cores
        self.colors = {
            'wall': (0.96, 0.87, 0.70),
            'roof': (0.55, 0.0, 0.0),
            'door': (0.55, 0.27, 0.07),
            'window': (0.53, 0.81, 0.92),
            'grass': (0.2, 0.6, 0.2)
        }
        
    def setup_opengl(self):
        """Configurar parâmetros do OpenGL"""
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        
        # Configurar luz
        glLightfv(GL_LIGHT0, GL_POSITION, [5, 5, 5, 1])
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
        
        # Configurar projeção
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self.width / self.height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        
    def draw_cube(self, x, y, z, width, height, depth, color):
        """Desenhar um cubo na posição especificada"""
        w, h, d = width/2, height/2, depth/2
        
        glPushMatrix()
        glTranslatef(x, y, z)
        glScalef(width, height, depth)
        
        glColor3f(*color)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [*color, 1.0])
        
        glBegin(GL_QUADS)
        
        # Frente
        glNormal3f(0, 0, 1)
        glVertex3f(-w, -h, d)
        glVertex3f(w, -h, d)
        glVertex3f(w, h, d)
        glVertex3f(-w, h, d)
        
        # Trás
        glNormal3f(0, 0, -1)
        glVertex3f(-w, -h, -d)
        glVertex3f(-w, h, -d)
        glVertex3f(w, h, -d)
        glVertex3f(w, -h, -d)
        
        # Topo
        glNormal3f(0, 1, 0)
        glVertex3f(-w, h, -d)
        glVertex3f(-w, h, d)
        glVertex3f(w, h, d)
        glVertex3f(w, h, -d)
        
        # Base
        glNormal3f(0, -1, 0)
        glVertex3f(-w, -h, -d)
        glVertex3f(w, -h, -d)
        glVertex3f(w, -h, d)
        glVertex3f(-w, -h, d)
        
        # Direita
        glNormal3f(1, 0, 0)
        glVertex3f(w, -h, -d)
        glVertex3f(w, h, -d)
        glVertex3f(w, h, d)
        glVertex3f(w, -h, d)
        
        # Esquerda
        glNormal3f(-1, 0, 0)
        glVertex3f(-w, -h, -d)
        glVertex3f(-w, -h, d)
        glVertex3f(-w, h, d)
        glVertex3f(-w, h, -d)
        
        glEnd()
        glPopMatrix()
    
    def draw_pyramid(self, x, y, z, base_width, height, color):
        """Desenhar uma pirâmide"""
        half = base_width / 2
        
        glPushMatrix()
        glTranslatef(x, y, z)
        
        glColor3f(*color)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [*color, 1.0])
        
        # Lados da pirâmide
        glBegin(GL_TRIANGLES)
        
        # Frente
        glNormal3f(0, 0.5, 0.5)
        glVertex3f(0, height, 0)
        glVertex3f(-half, 0, half)
        glVertex3f(half, 0, half)
        
        # Direita
        glNormal3f(0.5, 0.5, 0)
        glVertex3f(0, height, 0)
        glVertex3f(half, 0, half)
        glVertex3f(half, 0, -half)
        
        # Trás
        glNormal3f(0, 0.5, -0.5)
        glVertex3f(0, height, 0)
        glVertex3f(half, 0, -half)
        glVertex3f(-half, 0, -half)
        
        # Esquerda
        glNormal3f(-0.5, 0.5, 0)
        glVertex3f(0, height, 0)
        glVertex3f(-half, 0, -half)
        glVertex3f(-half, 0, half)
        
        glEnd()
        
        # Base
        glBegin(GL_QUADS)
        glNormal3f(0, -1, 0)
        glVertex3f(-half, 0, half)
        glVertex3f(half, 0, half)
        glVertex3f(half, 0, -half)
        glVertex3f(-half, 0, -half)
        glEnd()
        
        glPopMatrix()
    
    def draw_house(self):
        """Desenhar a casa completa"""
        # Paredes
        self.draw_cube(0, 1, 0, 3, 2, 3, self.colors['wall'])
        
        # Telhado
        self.draw_pyramid(0, 2, 0, 4, 1.5, self.colors['roof'])
        
        # Porta
        self.draw_cube(0, 0.5, 1.51, 0.8, 1.2, 0.1, self.colors['door'])
        
        # Janelas
        self.draw_cube(-1, 1, 1.51, 0.6, 0.6, 0.1, self.colors['window'])
        self.draw_cube(1, 1, 1.51, 0.6, 0.6, 0.1, self.colors['window'])
        
        # Chão
        self.draw_cube(0, -0.1, 0, 10, 0.2, 10, self.colors['grass'])
    
    def handle_events(self):
        """Processar eventos"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_LEFT:
                    self.camera_angle_y -= 10
                elif event.key == pygame.K_RIGHT:
                    self.camera_angle_y += 10
                elif event.key == pygame.K_UP:
                    self.camera_angle_x -= 10
                elif event.key == pygame.K_DOWN:
                    self.camera_angle_x += 10
                elif event.key == pygame.K_q:
                    self.camera_distance -= 0.5
                elif event.key == pygame.K_e:
                    self.camera_distance += 0.5
                elif event.key == pygame.K_r:
                    self.camera_distance = 5
                    self.camera_angle_x = 30
                    self.camera_angle_y = 45
            elif event.type == pygame.MOUSEWHEEL:
                self.camera_distance -= event.y * 0.5
        
        # Limitar distância
        self.camera_distance = max(2, min(20, self.camera_distance))
        
        return True
    
    def render(self):
        """Renderizar o quadro atual"""
        # Limpar buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0.53, 0.81, 0.98, 1.0)  # Céu azul
        
        # Configurar vista da câmera
        glLoadIdentity()
        
        # Calcular posição da câmera
        import math
        rad_y = math.radians(self.camera_angle_y)
        rad_x = math.radians(self.camera_angle_x)
        
        camera_x = math.sin(rad_y) * math.cos(rad_x) * self.camera_distance
        camera_y = math.sin(rad_x) * self.camera_distance
        camera_z = math.cos(rad_y) * math.cos(rad_x) * self.camera_distance
        
        gluLookAt(
            camera_x, camera_y, camera_z,  # Posição da câmera
            0, 1, 0,                       # Olhar para
            0, 1, 0                        # Vetor up
        )
        
        # Desenhar a casa
        self.draw_house()
        
        # Atualizar display
        pygame.display.flip()
    
    def display_info(self):
        """Mostrar informações no terminal"""
        import os
        os.system('clear' if os.name == 'posix' else 'cls')
        print("="*50)
        print("CASA 3D - RENDERIZAÇÃO SIMPLES")
        print("="*50)
        print("\nCONTROLES:")
        print("Setas ← → : Rotacionar horizontalmente")
        print("Setas ↑ ↓ : Rotacionar verticalmente")
        print("Q/E : Aproximar/Afastar")
        print("Scroll : Zoom")
        print("R : Resetar vista")
        print("ESC : Sair")
        print(f"\nDistância: {self.camera_distance:.1f}")
        print(f"Ângulo X: {self.camera_angle_x}°")
        print(f"Ângulo Y: {self.camera_angle_y}°")
    
    def run(self):
        """Executar o loop principal"""
        clock = pygame.time.Clock()
        running = True
        
        print("Inicializando renderização 3D...")
        
        while running:
            # Processar eventos
            running = self.handle_events()
            
            # Renderizar
            self.render()
            
            # Mostrar informações periodicamente
            if pygame.time.get_ticks() % 1000 < 50:
                self.display_info()
            
            # Controlar FPS
            clock.tick(60)
        
        pygame.quit()
        print("\nRenderização encerrada.")

if __name__ == "__main__":
    renderer = Simple3DRenderer(width=800, height=600)
    renderer.run()