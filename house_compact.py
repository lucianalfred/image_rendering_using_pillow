"""
Casa 3D Compacta - Dimensões ajustadas para visualização correta
"""

from objects.cube import Cube
from objects.pyramid import Pyramid
import numpy as np

class CompactHouse:
    """Casa 3D compacta para visualização adequada"""
    
    def __init__(self, position=[0, 0, 0], scale=0.3,  # scale bem menor
                 wall_color=None, roof_color=None, 
                 door_color=None, window_color=None):
        
        self.position = np.array(position, dtype=np.float32)
        self.scale = scale
        
        # Cores
        self.wall_color = wall_color or [0.96, 0.87, 0.70]
        self.roof_color = roof_color or [0.55, 0.0, 0.0]
        self.door_color = door_color or [0.55, 0.27, 0.07]
        self.window_color = window_color or [0.53, 0.81, 0.92]
        
        # DIMENSÕES COMPACTAS (bem menores)
        self.wall_width = 1.2 * scale      # Largura: 1.2 unidades
        self.wall_height = 1.0 * scale     # Altura: 1.0 unidades  
        self.wall_depth = 0.8 * scale      # Profundidade: 0.8 unidades
        self.wall_thickness = 0.05 * scale # Espessura fina
        
        # Componentes proporcionalmente menores
        self.roof_height = 0.6 * scale     # Telhado baixo
        self.door_width = 0.3 * scale      # Porta estreita
        self.door_height = 0.6 * scale     # Porta baixa
        self.window_size = 0.2 * scale     # Janelas pequenas
        
        self.create_components()
        
    def create_components(self):
        """Criar componentes da casa compacta"""
        self.components = []
        
        # 1. BASE/FUNDAÇÃO
        self.components.append(Cube(
            position=[0, -0.02, 0],
            size=[self.wall_width * 1.3, 0.04 * self.scale, self.wall_depth * 1.3],
            color=[0.5, 0.35, 0.2]  # Marrom terra
        ))
        
        # 2. PAREDES COMPACTAS
        
        # Parede frontal (Z positivo)
        self.components.append(Cube(
            position=[0, self.wall_height/2, self.wall_depth/2],
            size=[self.wall_width, self.wall_height, self.wall_thickness],
            color=self.wall_color
        ))
        
        # Parede traseira (Z negativo)
        self.components.append(Cube(
            position=[0, self.wall_height/2, -self.wall_depth/2],
            size=[self.wall_width, self.wall_height, self.wall_thickness],
            color=self.wall_color
        ))
        
        # Parede esquerda (X negativo)
        self.components.append(Cube(
            position=[-self.wall_width/2, self.wall_height/2, 0],
            size=[self.wall_thickness, self.wall_height, self.wall_depth],
            color=self.wall_color
        ))
        
        # Parede direita (X positivo)
        self.components.append(Cube(
            position=[self.wall_width/2, self.wall_height/2, 0],
            size=[self.wall_thickness, self.wall_height, self.wall_depth],
            color=self.wall_color
        ))
        
        # 3. TELHADO COMPACTO
        self.components.append(Pyramid(
            position=[0, self.wall_height + 0.02, 0],  # Ligeiramente acima das paredes
            size=[self.wall_width * 1.1, self.roof_height, self.wall_depth * 1.1],
            color=self.roof_color
        ))
        
        # 4. PORTA COMPACTA (centralizada na parede frontal)
        self.components.append(Cube(
            position=[0, self.door_height/2 + 0.05, self.wall_depth/2 + 0.01],  # Ligeiramente à frente
            size=[self.door_width, self.door_height, 0.03 * self.scale],
            color=self.door_color
        ))
        
        # 5. JANELAS COMPACTAS
        
        # Janela esquerda (parede frontal)
        self.components.append(Cube(
            position=[-self.wall_width/3, self.wall_height/2, self.wall_depth/2 + 0.01],
            size=[self.window_size, self.window_size, 0.03 * self.scale],
            color=self.window_color
        ))
        
        # Janela direita (parede frontal)
        self.components.append(Cube(
            position=[self.wall_width/3, self.wall_height/2, self.wall_depth/2 + 0.01],
            size=[self.window_size, self.window_size, 0.03 * self.scale],
            color=self.window_color
        ))
        
        # Janela traseira (parede de trás)
        self.components.append(Cube(
            position=[0, self.wall_height/2, -self.wall_depth/2 - 0.01],
            size=[self.window_size, self.window_size, 0.03 * self.scale],
            color=self.window_color
        ))
        
        # 6. CHAMINÉ PEQUENA
        self.components.append(Cube(
            position=[self.wall_width/3.5, self.wall_height + self.roof_height/2, -self.wall_depth/3.5],
            size=[0.1 * self.scale, 0.3 * self.scale, 0.1 * self.scale],
            color=[0.35, 0.35, 0.35]  # Cinza escuro
        ))
        
    def render(self):
        """Renderizar a casa compacta"""
        glPushMatrix()
        glTranslatef(*self.position)
        
        for component in self.components:
            component.render()
            
        glPopMatrix()