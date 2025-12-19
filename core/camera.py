"""
Sistema de câmera 3D com controle suave - versão compatível
"""

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

class Camera:
    """Câmera 3D com movimentação livre usando matrizes fixas"""
    
    def __init__(self, position=[0, 2, 8], target=[0, 1, 0], up=[0, 1, 0]):
        self.position = np.array(position, dtype=np.float32)
        self.target = np.array(target, dtype=np.float32)
        self.up = np.array(up, dtype=np.float32)
        
        # Ângulos de rotação (em graus)
        self.yaw = -90.0   # Rotação horizontal
        self.pitch = 0.0   # Rotação vertical
        
        # Sensibilidade
        self.movement_speed = 0.5
        self.rotation_speed = 0.3
        
    def move_forward(self, speed):
        """Mover câmera para frente"""
        direction = self.target - self.position
        direction = direction / np.linalg.norm(direction)
        self.position += direction * speed
        self.target += direction * speed
        
    def move_backward(self, speed):
        """Mover câmera para trás"""
        direction = self.target - self.position
        direction = direction / np.linalg.norm(direction)
        self.position -= direction * speed
        self.target -= direction * speed
        
    def move_left(self, speed):
        """Mover câmera para esquerda"""
        direction = self.target - self.position
        direction = direction / np.linalg.norm(direction)
        right = np.cross(direction, self.up)
        right = right / np.linalg.norm(right)
        self.position -= right * speed
        self.target -= right * speed
        
    def move_right(self, speed):
        """Mover câmera para direita"""
        direction = self.target - self.position
        direction = direction / np.linalg.norm(direction)
        right = np.cross(direction, self.up)
        right = right / np.linalg.norm(right)
        self.position += right * speed
        self.target += right * speed
        
    def move_up(self, speed):
        """Mover câmera para cima"""
        self.position[1] += speed
        self.target[1] += speed
        
    def move_down(self, speed):
        """Mover câmera para baixo"""
        self.position[1] -= speed
        self.target[1] -= speed
        
    def rotate_y(self, angle):
        """Rotacionar horizontalmente"""
        # Rotação em torno do eixo Y
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(angle, 0, 1, 0)
        # Aplicar à posição atual
        modelview = glGetFloatv(GL_MODELVIEW_MATRIX)
        direction = self.target - self.position
        new_direction = np.dot(modelview[:3, :3], direction)
        self.target = self.position + new_direction
        
    def rotate_x(self, angle):
        """Rotacionar verticalmente"""
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(angle, 1, 0, 0)
        modelview = glGetFloatv(GL_MODELVIEW_MATRIX)
        direction = self.target - self.position
        new_direction = np.dot(modelview[:3, :3], direction)
        self.target = self.position + new_direction
        
    def zoom(self, amount):
        """Zoom da câmera"""
        direction = self.target - self.position
        direction = direction / np.linalg.norm(direction)
        self.position += direction * amount
        
    def apply(self):
        """Aplicar transformações da câmera usando gluLookAt"""
        glLoadIdentity()
        gluLookAt(
            self.position[0], self.position[1], self.position[2],  # Posição
            self.target[0], self.target[1], self.target[2],        # Alvo
            self.up[0], self.up[1], self.up[2]                     # Vetor up
        )
        
    def reset(self):
        """Resetar câmera para posição inicial"""
        self.position = np.array([0, 2, 8], dtype=np.float32)
        self.target = np.array([0, 1, 0], dtype=np.float32)
        print("Câmera resetada")
        
    @property
    def rotation(self):
        """Retornar ângulos de rotação formatados"""
        direction = self.target - self.position
        yaw = math.degrees(math.atan2(direction[2], direction[0]))
        pitch = math.degrees(math.asin(direction[1] / np.linalg.norm(direction)))
        return f"Yaw: {yaw:.1f}°, Pitch: {pitch:.1f}°"