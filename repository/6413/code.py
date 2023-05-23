import pygame
import numpy as np

# Window dimensions
WIDTH = 800
HEIGHT = 800

# Fractal parameters
MAX_ITER = 100
ZOOM_FACTOR = 1.5

def generate_mandelbrot(x, y, zoom):
    zx = zy = 0
    c = complex(x, y)
    for i in range(MAX_ITER):
        if abs(zx + zy) > 4:
            return i
        zy, zx = 2 * zx * zy + c.imag, zx * zx - zy * zy + c.real
    return MAX_ITER

def generate_julia(x, y, zoom):
    zx = x * zoom - WIDTH / 2
    zy = y * zoom - HEIGHT / 2
    c = complex(-0.7, 0.27015)
    for i in range(MAX_ITER):
        if abs(zx + zy) > 4:
            return i
        zx, zy = zx * zx - zy * zy + c.real, 2 * zx * zy + c.imag
    return MAX_ITER

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    zoom = 1 / WIDTH
    offset_x = -0.5
    offset_y = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    zoom *= ZOOM_FACTOR
                elif event.button == 5:  # Scroll down
                    zoom /= ZOOM_FACTOR

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            offset_x -= 0.1 / zoom
        if keys[pygame.K_RIGHT]:
            offset_x += 0.1 / zoom
        if keys[pygame.K_UP]:
            offset_y -= 0.1 / zoom
        if keys[pygame.K_DOWN]:
            offset_y += 0.1 / zoom

        for x in range(WIDTH):
            for y in range(HEIGHT):
                if x % 2 == 0 and y % 2 == 0:
                    mandelbrot_value = generate_mandelbrot(x * zoom + offset_x, y * zoom + offset_y, zoom)
                    julia_value = generate_julia(x, y, zoom)
                    color = (mandelbrot_value % 8 * 32, julia_value % 16 * 16, 255 - (mandelbrot_value % 8 * 32))
                    screen.set_at((x, y), color)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
