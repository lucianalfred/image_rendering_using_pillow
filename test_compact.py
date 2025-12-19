#!/usr/bin/env python3
"""
Teste da Casa 3D Compacta - Versão Corrigida
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import os
import math

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar objetos básicos
try:
    from objects.cube import Cube
    from objects.house import House
except:
    # Fallback se os objetos não estiverem disponíveis
    print("Usando implementação interna...")
    
    class Cube:
        def __init__(self, position=[0,0,0], size=[1,1,1], color=[1,1,1]):
            self.pos = position
            self.size = size
            self.color = color
        
        def render(self):
            glPushMatrix()
            glTranslatef(*self.pos)
            
            w, h, d = self.size[0]/2, self.size[1]/2, self.size[2]/2
            
            glColor3f(*self.color)
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
    
    class House:
        def __init__(self, position=[0,0,0], scale=0.3):
            self.pos = position
            self.scale = scale
            self.color_wall = [0.96, 0.87, 0.70]
            self.color_roof = [0.55, 0.0, 0.0]
            self.color_door = [0.55, 0.27, 0.07]
            self.color_window = [0.53, 0.81, 0.92]
        
        def render(self):
            glPushMatrix()
            glTranslatef(*self.pos)
            
            # Dimensões compactas
            w, h, d = 1.2 * self.scale, 1.0 * self.scale, 0.8 * self.scale
            wall_t = 0.05 * self.scale
            
            # Paredes
            glColor3f(*self.color_wall)
            
            # Frente
            glPushMatrix()
            glTranslatef(0, h/2, d/2)
            self.draw_cube_simple(w, h, wall_t)
            glPopMatrix()
            
            # Trás
            glPushMatrix()
            glTranslatef(0, h/2, -d/2)
            self.draw_cube_simple(w, h, wall_t)
            glPopMatrix()
            
            # Esquerda
            glPushMatrix()
            glTranslatef(-w/2, h/2, 0)
            self.draw_cube_simple(wall_t, h, d)
            glPopMatrix()
            
            # Direita
            glPushMatrix()
            glTranslatef(w/2, h/2, 0)
            self.draw_cube_simple(wall_t, h, d)
            glPopMatrix()
            
            # Telhado (pirâmide)
            glColor3f(*self.color_roof)
            glPushMatrix()
            glTranslatef(0, h + 0.02, 0)
            self.draw_pyramid(w * 1.1, 0.6 * self.scale, d * 1.1)
            glPopMatrix()
            
            # Porta
            glColor3f(*self.color_door)
            glPushMatrix()
            glTranslatef(0, 0.3 * self.scale, d/2 + 0.01)
            self.draw_cube_simple(0.3 * self.scale, 0.6 * self.scale, 0.03)
            glPopMatrix()
            
            # Janelas
            glColor3f(*self.color_window)
            window_size = 0.2 * self.scale
            
            # Esquerda
            glPushMatrix()
            glTranslatef(-w/3, h/2, d/2 + 0.01)
            self.draw_cube_simple(window_size, window_size, 0.03)
            glPopMatrix()
            
            # Direita
            glPushMatrix()
            glTranslatef(w/3, h/2, d/2 + 0.01)
            self.draw_cube_simple(window_size, window_size, 0.03)
            glPopMatrix()
            
            glPopMatrix()
        
        def draw_cube_simple(self, width, height, depth):
            w, h, d = width/2, height/2, depth/2
            glBegin(GL_QUADS)
            # Frente
            glVertex3f(-w, -h, d); glVertex3f(w, -h, d); glVertex3f(w, h, d); glVertex3f(-w, h, d)
            # Trás
            glVertex3f(-w, -h, -d); glVertex3f(-w, h, -d); glVertex3f(w, h, -d); glVertex3f(w, -h, -d)
            # Topo
            glVertex3f(-w, h, -d); glVertex3f(-w, h, d); glVertex3f(w, h, d); glVertex3f(w, h, -d)
            # Base
            glVertex3f(-w, -h, -d); glVertex3f(w, -h, -d); glVertex3f(w, -h, d); glVertex3f(-w, -h, d)
            # Direita
            glVertex3f(w, -h, -d); glVertex3f(w, h, -d); glVertex3f(w, h, d); glVertex3f(w, -h, d)
            # Esquerda
            glVertex3f(-w, -h, -d); glVertex3f(-w, -h, d); glVertex3f(-w, h, d); glVertex3f(-w, h, -d)
            glEnd()
        
        def draw_pyramid(self, base_width, height, base_depth):
            hw, hd = base_width/2, base_depth/2
            glBegin(GL_TRIANGLES)
            # Frente
            glVertex3f(0, height, 0); glVertex3f(-hw, 0, hd); glVertex3f(hw, 0, hd)
            # Direita
            glVertex3f(0, height, 0); glVertex3f(hw, 0, hd); glVertex3f(hw, 0, -hd)
            # Trás
            glVertex3f(0, height, 0); glVertex3f(hw, 0, -hd); glVertex3f(-hw, 0, -hd)
            # Esquerda
            glVertex3f(0, height, 0); glVertex3f(-hw, 0, -hd); glVertex3f(-hw, 0, hd)
            glEnd()
            # Base
            glBegin(GL_QUADS)
            glVertex3f(-hw, 0, hd); glVertex3f(hw, 0, hd); glVertex3f(hw, 0, -hd); glVertex3f(-hw, 0, -hd)
            glEnd()

def setup_opengl():
    """Configurar OpenGL"""
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    # Luz suave
    glLightfv(GL_LIGHT0, GL_POSITION, [2, 5, 2, 1])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
    
    # Cor de fundo (céu)
    glClearColor(0.53, 0.81, 0.98, 1.0)

def draw_simple_grid():
    """Desenhar grade simplificada (sem usar range com floats)"""
    glDisable(GL_LIGHTING)
    glColor3f(0.5, 0.5, 0.5)
    glLineWidth(1.0)
    
    glBegin(GL_LINES)
    
    # Desenhar 21 linhas em cada direção (-10 a 10)
    for i in range(-10, 11):
        # Linhas na direção X (constante Z)
        glVertex3f(-10, -0.1, i)
        glVertex3f(10, -0.1, i)
        
        # Linhas na direção Z (constante X)
        glVertex3f(i, -0.1, -10)
        glVertex3f(i, -0.1, 10)
    
    glEnd()
    glEnable(GL_LIGHTING)

def draw_simple_axes():
    """Desenhar eixos XYZ simplificados"""
    glDisable(GL_LIGHTING)
    glLineWidth(2.0)
    
    glBegin(GL_LINES)
    
    # Eixo X (vermelho)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    
    # Eixo Y (verde)
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1, 0)
    
    # Eixo Z (azul)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 1)
    
    glEnd()
    glLineWidth(1.0)
    glEnable(GL_LIGHTING)

def draw_ground():
    """Desenhar chão simples"""
    glColor3f(0.2, 0.6, 0.2)  # Verde grama
    glBegin(GL_QUADS)
    glVertex3f(-10, -0.1, -10)
    glVertex3f(10, -0.1, -10)
    glVertex3f(10, -0.1, 10)
    glVertex3f(-10, -0.1, 10)
    glEnd()

class Camera:
    """Câmera 3D simples"""
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.distance = 4.0
        self.angle_x = 25.0
        self.angle_y = -45.0
    
    def update_view(self, width, height):
        """Atualizar a vista da câmera"""
        # Configurar projeção
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
        
        # Configurar modelo
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        # Calcular posição da câmera
        rad_y = math.radians(self.angle_y)
        rad_x = math.radians(self.angle_x)
        
        cam_x = math.sin(rad_y) * math.cos(rad_x) * self.distance
        cam_y = math.sin(rad_x) * self.distance
        cam_z = math.cos(rad_y) * math.cos(rad_x) * self.distance
        
        # Posicionar câmera
        gluLookAt(
            cam_x, cam_y + 0.3, cam_z,  # Posição
            0, 0.3, 0,                  # Alvo (centro da cena)
            0, 1, 0                     # Up
        )
    
    def zoom(self, amount):
        self.distance = max(2.0, min(10.0, self.distance + amount))
    
    def rotate(self, dx, dy):
        self.angle_y += dx
        self.angle_x = max(-85.0, min(85.0, self.angle_x + dy))

def display_text(screen, text, x, y, color=(255,255,255)):
    """Mostrar texto na tela"""
    font = pygame.font.SysFont('Arial', 20)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))
    return y + 25

def main():
    # Inicializar Pygame
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height), OPENGL | DOUBLEBUF)
    pygame.display.set_caption("Casa 3D - Visualização Correta")
    
    # Configurar OpenGL
    setup_opengl()
    
    # Criar objetos
    camera = Camera()
    house = House(scale=0.25)  # Casa pequena
    
    # Escalas disponíveis
    scales = [0.15, 0.25, 0.35, 0.5]
    current_scale = 1  # Índice 1 = 0.25
    
    clock = pygame.time.Clock()
    running = True
    
    print("="*60)
    print("CASA 3D - VISUALIZAÇÃO CORRETA")
    print("="*60)
    print("\nControles:")
    print("Setas: Rotacionar câmera")
    print("Q/E: Zoom in/out")
    print("1-4: Mudar tamanho da casa")
    print("R: Resetar vista")
    print("ESC: Sair")
    
    while running:
        # Processar eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
                # Controles da câmera
                elif event.key == K_LEFT:
                    camera.rotate(-5, 0)
                elif event.key == K_RIGHT:
                    camera.rotate(5, 0)
                elif event.key == K_UP:
                    camera.rotate(0, -5)
                elif event.key == K_DOWN:
                    camera.rotate(0, 5)
                elif event.key == K_q:
                    camera.zoom(-0.3)
                elif event.key == K_e:
                    camera.zoom(0.3)
                elif event.key == K_r:
                    camera.reset()
                
                # Mudar tamanho da casa
                elif event.key == K_1:
                    current_scale = 0
                    house = House(scale=scales[current_scale])
                elif event.key == K_2:
                    current_scale = 1
                    house = House(scale=scales[current_scale])
                elif event.key == K_3:
                    current_scale = 2
                    house = House(scale=scales[current_scale])
                elif event.key == K_4:
                    current_scale = 3
                    house = House(scale=scales[current_scale])
            
            elif event.type == MOUSEWHEEL:
                camera.zoom(-event.y * 0.3)
        
        # Limpar tela
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Atualizar vista da câmera
        camera.update_view(width, height)
        
        # Desenhar cena
        draw_ground()
        draw_simple_grid()
        draw_simple_axes()
        house.render()
        
        # Mostrar informações (modo 2D)
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, width, height, 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glDisable(GL_LIGHTING)
        
        y_pos = 10
        y_pos = display_text(screen, f"Casa 3D - Escala: {scales[current_scale]}", 10, y_pos)
        y_pos = display_text(screen, f"Distância: {camera.distance:.1f}", 10, y_pos)
        y_pos = display_text(screen, f"Ângulos: X={camera.angle_x:.0f}°, Y={camera.angle_y:.0f}°", 10, y_pos)
        y_pos += 10
        y_pos = display_text(screen, "CONTROLES:", 10, y_pos)
        y_pos = display_text(screen, "Setas: Rotacionar câmera", 10, y_pos)
        y_pos = display_text(screen, "Q/E: Zoom in/out", 10, y_pos)
        y_pos = display_text(screen, "1-4: Mudar tamanho da casa", 10, y_pos)
        y_pos = display_text(screen, "R: Resetar vista", 10, y_pos)
        y_pos = display_text(screen, "ESC: Sair", 10, y_pos)
        
        glEnable(GL_LIGHTING)
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        
        # Atualizar display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("\nPrograma encerrado com sucesso!")

if __name__ == "__main__":
    main()