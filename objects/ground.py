"""
Chão 3D com proporções adequadas
"""

from objects.cube import Cube
import numpy as np

class Ground(Cube):
    """Chão 3D que herda de Cube"""
    
    def __init__(self, position=[0, 0, 0], size=[20, 0.2, 20], color=None):
        # Cor padrão de grama
        if color is None:
            color = [0.2, 0.6, 0.2]
            
        super().__init__(position, size, color)