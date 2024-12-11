import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids,updatable,drawable)
  AsteroidField.containers = (updatable)
  asteroidfield = AsteroidField()

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

  Shot.containers = (shots,updatable, drawable)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    for object in updatable:
      object.update(dt)

    for asteroid in asteroids:
      if asteroid.collision(player):
        sys.exit('Game over!')
      
      for shot in shots:
        if asteroid.collision(shot):
          shot.kill()
          asteroid.split()     
    
    screen.fill("black")
    for object in drawable:
      object.draw(screen)
    pygame.display.flip()

    dt = clock.tick(60)/1000

if __name__ == "__main__":
  main()
