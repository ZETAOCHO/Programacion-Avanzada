import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# --- Webcam Capture ---
def take_photo():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("No se pudo abrir la cámara.")
    print("Presiona 'Espacio' para capturar la foto o 'ESC' para cancelar.")
    photo = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el frame de la cámara.")
            break
        cv2.imshow('Webcam', frame)
        key = cv2.waitKey(1)
        if key % 256 == 32:  # Espacio
            photo = frame.copy()
            break
        elif key % 256 == 27:  # ESC
            break
    cap.release()
    cv2.destroyAllWindows()
    if photo is None:
        raise Exception("Captura cancelada.")
    return photo

# --- Diamond Painting Mapping ---
def create_diamond_painting_map(image, target_width, target_height, num_colors=30):
    resized_image = cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)
    pixels = resized_image.reshape((-1, 3))
    pixels = np.float32(pixels)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    k = min(num_colors, len(np.unique(pixels, axis=0)))
    if k == 0:
        print("Warning: No unique colors found in the image after resizing. Cannot create diamond map.")
        return np.empty((target_height, target_width), dtype=str), {}
    attempts = 10
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quantized_image = centers[labels.flatten()]
    quantized_image = quantized_image.reshape((target_height, target_width, 3))
    color_to_symbol = {}
    symbol_to_color = {}
    current_symbol_index = 0
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+[]{};':\",./<>?"
    symbol_grid = np.empty((target_height, target_width), dtype=str)
    for r in range(target_height):
        for c in range(target_width):
            pixel_color = tuple(quantized_image[r, c])
            if pixel_color not in color_to_symbol:
                if current_symbol_index < len(symbols):
                    symbol = symbols[current_symbol_index]
                    color_to_symbol[pixel_color] = symbol
                    symbol_to_color[symbol] = pixel_color
                    current_symbol_index += 1
                else:
                    symbol = symbols[-1]
                    color_to_symbol[pixel_color] = symbol
                    symbol_to_color[symbol] = pixel_color
            symbol_grid[r, c] = color_to_symbol[pixel_color]
    return symbol_grid, symbol_to_color, quantized_image

# --- Main Execution ---
try:
    photo = take_photo()
    print('Foto capturada.')
    cv2.imshow('Foto Capturada', photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Redimensionar para demostración
    resized_photo = cv2.resize(photo, (256, 192), interpolation=cv2.INTER_AREA)
    print('Foto redimensionada (ejemplo).')
    cv2.imshow('Foto Redimensionada', resized_photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Tamaño de la cuadrícula
    target_grid_width = 256
    target_grid_height = 192

    # Crear el mapa de diamond painting
    diamond_map_grid, color_symbol_mapping, quantized_image = create_diamond_painting_map(
        resized_photo, target_grid_width, target_grid_height, num_colors=40
    )

    # Imprimir la leyenda de símbolos y colores
    print("\nLeyenda de colores:")
    for symbol, color in color_symbol_mapping.items():
        color_rgb = (color[2], color[1], color[0])
        print(f"Símbolo: {symbol} -> Color (BGR): {color} (RGB: {color_rgb})")

    # Imprimir la matriz de símbolos
    print("\nMatriz de símbolos:")
    for fila in diamond_map_grid:
        print(" ".join(fila))

    # Representación visual del mapeo
    mapped_visual = np.zeros((target_grid_height, target_grid_width, 3), dtype=np.uint8)
    for r in range(target_grid_height):
        for c in range(target_grid_width):
            symbol = diamond_map_grid[r, c]
            color = color_symbol_mapping[symbol]
            mapped_visual[r, c] = color

    print("\nMostrando el mapa de diamond painting...")
    cv2.imshow('Diamond Painting Map', mapped_visual)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Guardar el mapa como imagen
    cv2.imwrite('diamond_painting_map.png', mapped_visual)
    print("🖼️ Imagen del mapa de diamantes guardada como 'diamond_painting_map.png'")

    # Crear imagen de la leyenda de colores
    legend_width = 300
    entry_height = 30
    legend_height = entry_height * len(color_symbol_mapping)
    legend_image = Image.new("RGB", (legend_width, legend_height), (255, 255, 255))
    draw = ImageDraw.Draw(legend_image)

    for idx, (symbol, color_bgr) in enumerate(color_symbol_mapping.items()):
        color_rgb = (color_bgr[2], color_bgr[1], color_bgr[0])
        hex_color = '#{:02X}{:02X}{:02X}'.format(*color_rgb)
        y = idx * entry_height
        draw.rectangle([5, y + 5, 35, y + 25], fill=color_rgb, outline=(0, 0, 0))
        text = f"{symbol}  {hex_color}"
        draw.text((45, y + 7), text, fill=(0, 0, 0))

    legend_image.save("color_legend.png")
    print("🎨 Imagen de la leyenda guardada como 'color_legend.png'")

except Exception as err:
    print("Error:", str(err))