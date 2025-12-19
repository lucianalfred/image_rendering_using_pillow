"""
Paleta de cores realistas para renderização 3D
"""

import numpy as np

class Colors3D:
    """Cores realistas para objetos 3D com suporte a materiais"""
    
    # ============================================
    # CORES DA CASA
    # ============================================
    WALL = [0.96, 0.87, 0.70]      # Creme - parede
    ROOF = [0.55, 0.0, 0.0]        # Vermelho tijolo - telhado
    DOOR = [0.55, 0.27, 0.07]      # Marrom madeira - porta
    WINDOW = [0.53, 0.81, 0.92]    # Azul céu - vidro da janela
    CHIMNEY = [0.4, 0.4, 0.4]      # Cinza pedra - chaminé
    WINDOW_FRAME = [0.2, 0.2, 0.2] # Preto - moldura da janela
    DOOR_KNOB = [0.9, 0.9, 0.1]    # Amarelo dourado - maçaneta
    
    # ============================================
    # CORES DO AMBIENTE
    # ============================================
    SKY = [0.53, 0.81, 0.98]       # Azul céu claro - fundo
    GRASS = [0.2, 0.6, 0.2]        # Verde grama - chão
    DIRT = [0.45, 0.30, 0.15]      # Marrom terra
    STONE = [0.5, 0.5, 0.5]        # Cinza pedra
    WATER = [0.0, 0.47, 0.75]      # Azul água
    
    # ============================================
    # CORES DE ILUMINAÇÃO
    # ============================================
    SUNLIGHT = [1.0, 1.0, 0.9]     # Branco amarelado - luz do sol
    AMBIENT_LIGHT = [0.3, 0.3, 0.4] # Azulado - luz ambiente
    MOONLIGHT = [0.7, 0.7, 0.9]    # Azul claro - luz da lua
    
    # ============================================
    # MATERIAIS (propriedades físicas para iluminação)
    # ============================================
    @staticmethod
    def get_material_properties(material_type):
        """Retorna propriedades do material para iluminação"""
        materials = {
            'wood': {
                'ambient': [0.2, 0.2, 0.2, 1.0],
                'diffuse': [0.6, 0.4, 0.2, 1.0],
                'specular': [0.1, 0.1, 0.1, 1.0],
                'shininess': 10.0
            },
            'brick': {
                'ambient': [0.3, 0.2, 0.2, 1.0],
                'diffuse': [0.7, 0.3, 0.2, 1.0],
                'specular': [0.05, 0.05, 0.05, 1.0],
                'shininess': 5.0
            },
            'glass': {
                'ambient': [0.1, 0.1, 0.1, 0.5],
                'diffuse': [0.5, 0.7, 0.9, 0.5],
                'specular': [0.8, 0.8, 0.8, 0.5],
                'shininess': 100.0
            },
            'metal': {
                'ambient': [0.2, 0.2, 0.2, 1.0],
                'diffuse': [0.5, 0.5, 0.5, 1.0],
                'specular': [0.8, 0.8, 0.8, 1.0],
                'shininess': 80.0
            },
            'plastic': {
                'ambient': [0.1, 0.1, 0.1, 1.0],
                'diffuse': [0.7, 0.7, 0.7, 1.0],
                'specular': [0.5, 0.5, 0.5, 1.0],
                'shininess': 30.0
            },
            'grass': {
                'ambient': [0.1, 0.3, 0.1, 1.0],
                'diffuse': [0.2, 0.6, 0.2, 1.0],
                'specular': [0.1, 0.2, 0.1, 1.0],
                'shininess': 5.0
            }
        }
        return materials.get(material_type, materials['plastic'])
    
    # ============================================
    # CORES TEMÁTICAS (para diferentes estilos)
    # ============================================
    @staticmethod
    def get_theme(theme_name):
        """Retorna um conjunto de cores para um tema específico"""
        themes = {
            'default': {
                'wall': Colors3D.WALL,
                'roof': Colors3D.ROOF,
                'door': Colors3D.DOOR,
                'window': Colors3D.WINDOW
            },
            'modern': {
                'wall': [0.9, 0.9, 0.9],      # Branco
                'roof': [0.3, 0.3, 0.3],      # Cinza escuro
                'door': [0.1, 0.1, 0.1],      # Preto
                'window': [0.8, 0.8, 0.8]     # Cinza claro
            },
            'rustic': {
                'wall': [0.7, 0.6, 0.5],      # Marrom claro
                'roof': [0.4, 0.2, 0.1],      # Marrom escuro
                'door': [0.5, 0.3, 0.1],      # Madeira
                'window': [0.6, 0.5, 0.4]     # Madeira clara
            },
            'beach': {
                'wall': [0.95, 0.95, 0.85],   # Areia
                'roof': [0.7, 0.5, 0.3],      # Palha
                'door': [0.4, 0.6, 0.8],      # Azul mar
                'window': [0.9, 0.95, 1.0]    # Azul céu claro
            }
        }
        return themes.get(theme_name, themes['default'])
    
    # ============================================
    # UTILITÁRIOS DE COR
    # ============================================
    @staticmethod
    def darken(color, factor=0.7):
        """Escurece uma cor por um fator"""
        return [c * factor for c in color]
    
    @staticmethod
    def lighten(color, factor=1.3):
        """Clareia uma cor por um fator"""
        return [min(1.0, c * factor) for c in color]
    
    @staticmethod
    def to_opengl_format(color, alpha=1.0):
        """Converte cor para formato OpenGL (lista de 4 floats)"""
        return [color[0], color[1], color[2], alpha]
    
    @staticmethod
    def interpolate(color1, color2, factor=0.5):
        """Interpola entre duas cores"""
        return [
            color1[0] * (1 - factor) + color2[0] * factor,
            color1[1] * (1 - factor) + color2[1] * factor,
            color1[2] * (1 - factor) + color2[2] * factor
        ]
    
    @staticmethod
    def random_natural_color():
        """Gera uma cor natural aleatória"""
        import random
        color_types = [
            Colors3D.WALL,      # Creme
            [0.8, 0.7, 0.6],    # Areia
            [0.6, 0.5, 0.4],    # Terra
            [0.4, 0.6, 0.3],    # Verde musgo
            [0.7, 0.6, 0.5],    # Madeira clara
        ]
        return random.choice(color_types)