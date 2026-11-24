"""Physics primitives independent of the graphical interface."""
from dataclasses import dataclass

@dataclass
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    radius: float = 10

    def step(self, dt, gravity, width, height, bounce=0.75):
        self.x += self.vx * dt
        self.y += self.vy * dt + 0.5 * gravity * dt ** 2
        self.vy += gravity * dt
        if self.x < self.radius:
            self.x = self.radius
            self.vx = abs(self.vx) * bounce
        elif self.x > width - self.radius:
            self.x = width - self.radius
            self.vx = -abs(self.vx) * bounce
        if self.y < self.radius:
            self.y = self.radius
            self.vy = abs(self.vy) * bounce
        elif self.y > height - self.radius:
            self.y = height - self.radius
            self.vy = -abs(self.vy) * bounce
            if abs(self.vy) < 12:
                self.vy = 0
