"""
Pirâmide 3D com proporções controladas
"""

from OpenGL.GL import *
import numpy as np

class Pyramid:
    """Pirâmide 3D para telhados com proporções corretas"""
    
    def __init__(self, position=[0, 0, 0], size=[1, 1, 1], color=[1, 0, 0]):
        self.position = np.array(position, dtype=np.float32)
        self.size = np.array(size, dtype=np.float32)  # [base_width, height, base_depth]
        self.color = np.array(color, dtype=np.float32)
        
    def render(self):
        """Renderizar a pirâmide com proporções específicas"""
        glPushMatrix()
        
        # Aplicar posição
        glTranslatef(*self.position)
        
        # Configurar cor
        glColor3f(*self.color)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [*self.color, 1.0])
        
        # Calcular meias dimensões da base
        base_half_width = self.size[0] / 2
        base_half_depth = self.size[2] / 2
        height = self.size[1]
        
        # Desenhar pirâmide
        glBegin(GL_TRIANGLES)
        
        # Lado frontal (Z positivo)
        glNormal3f(0, 0.5, 0.5)
        glVertex3f(0, height, 0)                     # Topo
        glVertex3f(-base_half_width, 0, base_half_depth)  # Base esquerda frontal
        glVertex3f(base_half_width, 0, base_half_depth)   # Base direita frontal
        
        # Lado direito (X positivo)
        glNormal3f(0.5, 0.5, 0)
        glVertex3f(0, height, 0)                     # Topo
        glVertex3f(base_half_width, 0, base_half_depth)   # Base direita frontal
        glVertex3f(base_half_width, 0, -base_half_depth)  # Base direita traseira
        
        # Lado traseiro (Z negativo)
        glNormal3f(0, 0.5, -0.5)
        glVertex3f(0, height, 0)                     # Topo
        glVertex3f(base_half_width, 0, -base_half_depth)  # Base direita traseira
        glVertex3f(-base_half_width, 0, -base_half_depth) # Base esquerda traseira
        
        # Lado esquerdo (X negativo)
        glNormal3f(-0.5, 0.5, 0)
        glVertex3f(0, height, 0)                     # Topo
        glVertex3f(-base_half_width, 0, -base_half_depth) # Base esquerda traseira
        glVertex3f(-base_half_width, 0, base_half_depth)  # Base esquerda frontal
        
        glEnd()
        
        # Base quadrada (opcional - geralmente não visível)
        # glBegin(GL_QUADS)
        # glNormal3f(0, -1, 0)
        # glVertex3f(-base_half_width, 0, base_half_depth)
        # glVertex3f(base_half_width, 0, base_half_depth)
        # glVertex3f(base_half_width, 0, -base_half_depth)
        # glVertex3f(-base_half_width, 0, -base_half_depth)
        # glEnd()
        
        glPopMatrix()