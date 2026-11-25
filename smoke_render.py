"""Exercise the Pygame loop and render a preview on SDL's dummy display."""

import os
from types import SimpleNamespace
from unittest.mock import patch

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame

from main import main


def mouse(kind, pos):
    return pygame.event.Event(kind, button=1, pos=pos)


def key(value):
    return pygame.event.Event(pygame.KEYDOWN, key=value)


def verify_rendering():
    frames = iter([
        [key(pygame.K_DOWN)] * 9 + [mouse(pygame.MOUSEBUTTONDOWN, (240, 260))],
        [mouse(pygame.MOUSEBUTTONUP, (140, 260))],
        [],
        [key(pygame.K_UP)] * 9,
        [],
        [],
        [key(pygame.K_r)],
        [key(pygame.K_ESCAPE)],
    ])
    particle_positions = []
    frame_number = 0
    flip = pygame.display.flip

    def capture():
        nonlocal frame_number
        frame_number += 1
        if frame_number == 6:
            pygame.image.save(pygame.display.get_surface(), "gravity-lab.png")
        flip()

    circle = pygame.draw.circle

    def record_circle(surface, color, center, radius):
        particle_positions.append(center)
        return circle(surface, color, center, radius)

    with (
        patch.object(pygame.event, "get", side_effect=lambda: next(frames)),
        patch.object(pygame.time, "Clock", return_value=SimpleNamespace(tick=lambda _: 30)),
        patch.object(pygame.display, "flip", side_effect=capture),
        patch.object(pygame.draw, "circle", side_effect=record_circle),
        patch.object(pygame.draw, "lines", wraps=pygame.draw.lines) as trails,
        patch.object(pygame.draw, "line", wraps=pygame.draw.line) as guide,
    ):
        main()
    assert frame_number == 8, frame_number
    assert particle_positions == [(249, 260), (258, 260), (267, 260), (276, 260), (285, 261)], particle_positions
    assert trails.call_count == 4, trails.call_count
    assert guide.call_count == 1, guide.call_count
    print("Pygame startup, launch, gravity controls, trails and reset passed")


if __name__ == "__main__":
    verify_rendering()
