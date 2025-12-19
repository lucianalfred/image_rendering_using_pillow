"""
Objeto Cubo 3D com proporções corretas
"""

from OpenGL.GL import *
import numpy as np

class Cube:
    """Cubo 3D com controle preciso de dimensões"""
    
    def __init__(self, position=[0, 0, 0], size=[1, 1, 1], color=[1, 1, 1]):
        self.position = np.array(position, dtype=np.float32)
        self.size = np.array(size, dtype=np.float32)  # Largura, Altura, Profundidade
        self.color = np.array(color, dtype=np.float32)
        
    def render(self):
        """Renderizar o cubo com proporções corretas"""
        glPushMatrix()
        
        # Aplicar transformações
        glTranslatef(*self.position)
        
        # NOTA: Não usar glScalef aqui - vamos definir vértices manualmente
        # para ter controle total das dimensões
        
        # Configurar cor
        glColor3f(*self.color)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [*self.color, 1.0])
        
        # Calcular meias dimensões
        w, h, d = self.size[0]/2, self.size[1]/2, self.size[2]/2
        
        # Desenhar cubo com dimensões específicas
        glBegin(GL_QUADS)
        
        # Frente (plano Z positivo)
        glNormal3f(0, 0, 1)
        glVertex3f(-w, -h, d)  # Inferior esquerdo
        glVertex3f(w, -h, d)   # Inferior direito
        glVertex3f(w, h, d)    # Superior direito
        glVertex3f(-w, h, d)   # Superior esquerdo
        
        # Trás (plano Z negativo)
        glNormal3f(0, 0, -1)
        glVertex3f(-w, -h, -d)
        glVertex3f(-w, h, -d)
        glVertex3f(w, h, -d)
        glVertex3f(w, -h, -d)
        
        # Topo (plano Y positivo)
        glNormal3f(0, 1, 0)
        glVertex3f(-w, h, -d)
        glVertex3f(-w, h, d)
        glVertex3f(w, h, d)
        glVertex3f(w, h, -d)
        
        # Base (plano Y negativo)
        glNormal3f(0, -1, 0)
        glVertex3f(-w, -h, -d)
        glVertex3f(w, -h, -d)
        glVertex3f(w, -h, d)
        glVertex3f(-w, -h, d)
        
        # Direita (plano X positivo)
        glNormal3f(1, 0, 0)
        glVertex3f(w, -h, -d)
        glVertex3f(w, h, -d)
        glVertex3f(w, h, d)
        glVertex3f(w, -h, d)
        
        # Esquerda (plano X negativo)
        glNormal3f(-1, 0, 0)
        glVertex3f(-w, -h, -d)
        glVertex3f(-w, -h, d)
        glVertex3f(-w, h, d)
        glVertex3f(-w, h, -d)
        
        glEnd()
        
        glPopMatrix()