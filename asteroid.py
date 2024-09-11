from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
  def update(self, dt):
    self.position += self.velocity * dt
  
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    rand_angle = random.uniform(20,50)
    angle_1 = self.velocity.rotate(rand_angle)
    angle_2 = self.velocity.rotate(-rand_angle)
    new_sizing = self.radius - ASTEROID_MIN_RADIUS
    asteroid1 = Asteroid(self.position.x, self.position.y, new_sizing)
    asteroid2 = Asteroid(self.position.x, self.position.y, new_sizing)
    asteroid1.velocity = angle_1 * 1.2
    asteroid2.velocity = angle_2 * 1.2