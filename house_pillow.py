from PIL import Image, ImageDraw
import math

def render_house(resolution=(800, 600), save_path="casa_renderizada.png"):
    """
    Renderiza uma casa simples usando a biblioteca Pillow.
    
    Args:
        resolution (tuple): Resolução da imagem (largura, altura)
        save_path (str): Caminho para salvar a imagem resultante
    """
    
    # Criar uma nova imagem com fundo branco
    img = Image.new('RGB', resolution, color='lightblue')
    draw = ImageDraw.Draw(img)
    
    # ============================================
    # DEFINIÇÃO DAS DIMENSÕES PRINCIPAIS
    # ============================================
    
    # Margens para centralizar a casa
    margin_x = resolution[0] * 0.1  # 10% da largura
    margin_y = resolution[1] * 0.1  # 10% da altura
    
    # Área disponível para desenhar a casa
    available_width = resolution[0] - 2 * margin_x
    available_height = resolution[1] - 2 * margin_y
    
    # ============================================
    # PAREDE PRINCIPAL (retângulo)
    # ============================================
    
    # A parede ocupa 60% da altura disponível e 80% da largura disponível
    wall_width = available_width * 0.8
    wall_height = available_height * 0.6
    
    # Centralizar horizontalmente
    wall_x = margin_x + (available_width - wall_width) / 2
    # Posicionar verticalmente (um pouco acima do centro)
    wall_y = margin_y + (available_height - wall_height) / 2 + available_height * 0.1
    
    # Desenhar parede (cor creme)
    wall_coords = [
        (wall_x, wall_y),
        (wall_x + wall_width, wall_y + wall_height)
    ]
    draw.rectangle(wall_coords, fill='#F5DEB3', outline='#8B4513', width=3)
    
    # ============================================
    # TELHADO (triângulo)
    # ============================================
    
    # O telhado é 30% mais largo que a parede e tem altura proporcional
    roof_width = wall_width * 1.3
    roof_height = wall_height * 0.4
    
    # Posição do pico do telhado (centro superior da parede)
    roof_peak_x = wall_x + wall_width / 2
    roof_peak_y = wall_y - roof_height
    
    # Pontos do triângulo do telhado
    roof_points = [
        (roof_peak_x - roof_width / 2, wall_y),  # Esquerda
        (roof_peak_x, roof_peak_y),              # Pico
        (roof_peak_x + roof_width / 2, wall_y)   # Direita
    ]
    
    # Desenhar telhado (cor vermelho tijolo)
    draw.polygon(roof_points, fill='#8B0000', outline='#4A0000', width=3)
    
    # ============================================
    # PORTA (retângulo centralizado na parede)
    # ============================================
    
    # Porta ocupa 20% da largura da parede e 40% da altura da parede
    door_width = wall_width * 0.2
    door_height = wall_height * 0.4
    
    # Centralizar a porta horizontalmente na parede
    door_x = wall_x + (wall_width - door_width) / 2
    # Posicionar a porta na base da parede
    door_y = wall_y + wall_height - door_height
    
    # Desenhar porta (cor marrom)
    door_coords = [
        (door_x, door_y),
        (door_x + door_width, door_y + door_height)
    ]
    draw.rectangle(door_coords, fill='#8B4513', outline='#654321', width=2)
    
    # Maçaneta da porta (círculo pequeno)
    knob_radius = door_width * 0.05
    knob_x = door_x + door_width - knob_radius * 3
    knob_y = door_y + door_height / 2
    draw.ellipse(
        (knob_x - knob_radius, knob_y - knob_radius,
         knob_x + knob_radius, knob_y + knob_radius),
        fill='#FFD700', outline='#B8860B'
    )
    
    # ============================================
    # JANELAS (duas janelas retangulares)
    # ============================================
    
    # Tamanho da janela (15% da largura da parede, 25% da altura)
    window_width = wall_width * 0.15
    window_height = wall_height * 0.25
    
    # Janela esquerda
    window1_x = wall_x + wall_width * 0.2
    window1_y = wall_y + wall_height * 0.2
    
    # Janela direita
    window2_x = wall_x + wall_width * 0.65
    window2_y = window1_y  # Mesma altura da janela esquerda
    
    # Desenhar janelas (quadrados com divisões)
    for window_x, window_y in [(window1_x, window1_y), (window2_x, window2_y)]:
        # Moldura da janela
        window_coords = [
            (window_x, window_y),
            (window_x + window_width, window_y + window_height)
        ]
        draw.rectangle(window_coords, fill='#87CEEB', outline='#2F4F4F', width=2)
        
        # Divisões da janela (cruz)
        # Linha vertical
        draw.line(
            [(window_x + window_width/2, window_y),
             (window_x + window_width/2, window_y + window_height)],
            fill='#2F4F4F', width=2
        )
        # Linha horizontal
        draw.line(
            [(window_x, window_y + window_height/2),
             (window_x + window_width, window_y + window_height/2)],
            fill='#2F4F4F', width=2
        )
    
    # ============================================
    # CHÃO/GRAMA (opcional)
    # ============================================
    
    # Desenhar uma linha representando o chão
    ground_y = wall_y + wall_height + 10
    draw.line(
        [(margin_x, ground_y), (resolution[0] - margin_x, ground_y)],
        fill='#228B22', width=4
    )
    
    # ============================================
    # SOL (elemento decorativo)
    # ============================================
    
    sun_radius = resolution[0] * 0.05
    sun_x = resolution[0] * 0.85
    sun_y = resolution[1] * 0.15
    
    # Desenhar sol
    draw.ellipse(
        (sun_x - sun_radius, sun_y - sun_radius,
         sun_x + sun_radius, sun_y + sun_radius),
        fill='#FFD700', outline='#FF8C00', width=2
    )
    
    # ============================================
    # SALVAR E EXIBIR A IMAGEM
    # ============================================
    
    img.save(save_path)
    print(f"Imagem salva como: {save_path}")
    print(f"Resolução: {resolution[0]}x{resolution[1]}")
    
    # Exibir a imagem
    img.show()
    
    return img

def generate_documentation():
    """
    Gera documentação explicativa sobre as escolhas do projeto.
    """
    print("\n" + "="*80)
    print("DOCUMENTAÇÃO DO PROJETO: RENDERIZAÇÃO DE UMA CASA")
    print("="*80)
    
    print("\n1. JUSTIFICATIVA DA RESOLUÇÃO (800x600):")
    print("   • Clareza: Resolução suficiente para detalhes visíveis")
    print("   • Proporção: Aspect ratio 4:3 é comum e balanceado")
    print("   • Desempenho: Baixo consumo de recursos com Pillow")
    print("   • Compatibilidade: Funciona bem na maioria dos dispositivos")
    
    print("\n2. SISTEMA DE COORDENADAS DO PILLOW:")
    print("   • Origem (0,0): Canto superior esquerdo")
    print("   • Eixo X: Cresce para a direita")
    print("   • Eixo Y: Cresce para baixo")
    print("   • Unidades: Pixels")
    print("   • Influência: Requer ajuste mental pois Y cresce para baixo")
    
    print("\n3. CÁLCULOS GEOMÉTRICOS E PROPORÇÕES:")
    print("   • Tudo é dimensionado proporcionalmente à resolução")
    print("   • Margens: 10% da largura e altura para centralização")
    print("   • Parede: 80% da área disponível em largura, 60% em altura")
    print("   • Telhado: 30% mais largo que a parede, altura = 40% da parede")
    print("   • Porta: 20% da largura da parede, 40% da altura da parede")
    print("   • Janelas: 15% da largura da parede, 25% da altura")
    
    print("\n4. PRIMITIVAS GEOMÉTRICAS UTILIZADAS:")
    print("   • Retângulos: Parede, porta, janelas (draw.rectangle)")
    print("   • Triângulos: Telhado (draw.polygon com 3 pontos)")
    print("   • Linhas: Divisões das janelas, chão (draw.line)")
    print("   • Círculos/Elipses: Maçaneta, sol (draw.ellipse)")
    
    print("\n5. ESCOLHA DE CORES:")
    print("   • Parede: Creme (#F5DEB3) - cor comum para casas")
    print("   • Telhado: Vermelho tijolo (#8B0000) - tradicional")
    print("   • Porta: Marrom (#8B4513) - madeira")
    print("   • Janelas: Azul céu (#87CEEB) - vidro")
    print("   • Fundo: Azul claro - representando o céu")

# ============================================
# EXECUÇÃO DO PROGRAMA
# ============================================

if __name__ == "__main__":
    # Executar a renderização
    print("Iniciando renderização da casa...")
    rendered_house = render_house(resolution=(800, 600))
    

    generate_documentation()
    
    print("\n" + "="*80)
    print("PROJETO CONCLUÍDO COM SUCESSO!")
    print("="*80)