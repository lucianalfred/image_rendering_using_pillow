"""
Gerenciador de cena 3D
"""

from OpenGL.GL import *

class Scene3D:
    """Gerenciador de todos os objetos na cena 3D"""
    
    def __init__(self):
        self.objects = []
        self.lights = []
        
    def add_object(self, obj):
        """Adicionar objeto à cena"""
        self.objects.append(obj)
        
    def add_light(self, light):
        """Adicionar luz à cena"""
        self.lights.append(light)
        
    def render(self):
        """Renderizar todos os objetos da cena"""
        # Configurar iluminação básica
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        
        # Posição da luz principal
        light_position = [5.0, 10.0, 5.0, 1.0]
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        
        # Propriedades da luz
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
        
        # Renderizar cada objeto
        for obj in self.objects:
            obj.render()
            
        # Desabilitar iluminação para elementos de UI
        glDisable(GL_LIGHTING)
        
    def clear(self):
        """Limpar todos os objetos da cena"""
        self.objects.clear()
        self.lights.clear()
