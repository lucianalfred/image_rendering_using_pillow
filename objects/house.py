"""
Casa 3D com proporções realistas
"""

from objects.cube import Cube
from objects.pyramid import Pyramid
import numpy as np

class House:
    """Casa 3D com proporções harmoniosas"""
    
    def __init__(self, position=[0, 0, 0], scale=1.0,
                 wall_color=None, roof_color=None, 
                 door_color=None, window_color=None):
        
        self.position = np.array(position, dtype=np.float32)
        self.scale = scale
        
        # Cores
        self.wall_color = wall_color or [0.96, 0.87, 0.70]
        self.roof_color = roof_color or [0.55, 0.0, 0.0]
        self.door_color = door_color or [0.55, 0.27, 0.07]
        self.window_color = window_color or [0.53, 0.81, 0.92]
        
        # Dimensões principais (em unidades do mundo 3D)
        self.wall_width = 1.5 * scale      # Largura da casa
        self.wall_height = 2.5 * scale     # Altura das paredes
        self.wall_depth = 2.5 * scale      # Profundidade da casa
        self.wall_thickness = 0.2 * scale  # Espessura das paredes
        
        # Dimensões dos componentes
        self.roof_height = 1.5 * scale
        self.door_width = 0.8 * scale
        self.door_height = 1.8 * scale
        self.window_size = 0.6 * scale
        
        # Criar componentes
        self.create_components()
        
    def create_components(self):
        """Criar todos os componentes da casa com proporções corretas"""
        self.components = []
        
        # 1. PISO (base da casa)
        self.components.append(Cube(
            position=[0, -0.05 * self.scale, 0],
            size=[self.wall_width * 1.1, 0.1 * self.scale, self.wall_depth * 1.1],
            color=[0.6, 0.4, 0.2]  # Marrom madeira
        ))
        
        # 2. PAREDES (4 paredes separadas)
        
        # Parede frontal (com abertura para porta)
        # Calculamos o tamanho da parede frontal considerando a porta
        wall_front_height = self.wall_height
        
        self.components.append(Cube(
            position=[0, wall_front_height/2, self.wall_depth/2 - self.wall_thickness/2],
            size=[self.wall_width, wall_front_height, self.wall_thickness],
            color=self.wall_color
        ))
        
        # Parede traseira
        self.components.append(Cube(
            position=[0, self.wall_height/2, -self.wall_depth/2 + self.wall_thickness/2],
            size=[self.wall_width, self.wall_height, self.wall_thickness],
            color=self.wall_color
        ))
        
        # Parede esquerda
        self.components.append(Cube(
            position=[-self.wall_width/2 + self.wall_thickness/2, self.wall_height/2, 0],
            size=[self.wall_thickness, self.wall_height, self.wall_depth - self.wall_thickness],
            color=self.wall_color
        ))
        
        # Parede direita
        self.components.append(Cube(
            position=[self.wall_width/2 - self.wall_thickness/2, self.wall_height/2, 0],
            size=[self.wall_thickness, self.wall_height, self.wall_depth - self.wall_thickness],
            color=self.wall_color
        ))
        
        # 3. TELHADO
        self.components.append(Pyramid(
            position=[0, self.wall_height, 0],
            size=[self.wall_width * 1.2, self.roof_height, self.wall_depth * 1.2],
            color=self.roof_color
        ))
        
        # 4. PORTA (centralizada na parede frontal)
        self.components.append(Cube(
            position=[0, self.door_height/2, self.wall_depth/2],
            size=[self.door_width, self.door_height, 0.05 * self.scale],
            color=self.door_color
        ))
        
        # 5. JANELAS
        
        # Janela esquerda (parede frontal)
        self.components.append(Cube(
            position=[-self.wall_width/3, self.wall_height/2, self.wall_depth/2],
            size=[self.window_size, self.window_size, 0.05 * self.scale],
            color=self.window_color
        ))
        
        # Janela direita (parede frontal)
        self.components.append(Cube(
            position=[self.wall_width/3, self.wall_height/2, self.wall_depth/2],
            size=[self.window_size, self.window_size, 0.05 * self.scale],
            color=self.window_color
        ))
        
        # Janela traseira
        self.components.append(Cube(
            position=[0, self.wall_height/2, -self.wall_depth/2],
            size=[self.window_size, self.window_size, 0.05 * self.scale],
            color=self.window_color
        ))
        
        # 6. CHAMINÉ
        self.components.append(Cube(
            position=[self.wall_width/4, self.wall_height + self.roof_height/3, -self.wall_depth/4],
            size=[0.3 * self.scale, 0.8 * self.scale, 0.3 * self.scale],
            color=[0.4, 0.4, 0.4]  # Cinza
        ))
        
        # 7. DEGRAU DA PORTA
        self.components.append(Cube(
            position=[0, 0.05 * self.scale, self.wall_depth/2 + 0.1 * self.scale],
            size=[self.door_width * 1.2, 0.1 * self.scale, 0.2 * self.scale],
            color=[0.3, 0.2, 0.1]  # Marrom escuro
        ))
        
    def render(self):
        """Renderizar todos os componentes da casa"""
        glPushMatrix()
        
        # Aplicar posição geral da casa
        glTranslatef(*self.position)
        
        # Renderizar cada componente
        for component in self.components:
            component.render()
            
        glPopMatrix()