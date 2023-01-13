import pygame
import random

# Initialize pygame and create window
pygame.init()
width = 600
height = 150
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino Jump")

# Create dino character as a sprite
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dino.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = height - self.rect.height
        self.jumping = False
        self.jump_count = 10

    def jump(self):
        self.jumping = True

    def update(self):
        if self.jumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.jumping = False
                self.jump_count = 10

# Create obstacle as a sprite
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, speed):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

# Create a group for the dino and obstacles
dino_group = pygame.sprite.Group()
dino = Dino()
dino_group.add(dino)
obstacle_group = pygame.sprite.Group()

# Start time
start_time = pygame.time.get_ticks()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        dino.jump()

    # Update dino and obstacle positions
    dino_group.update()
    obstacle_group.update()

    # Check for collisions
    if pygame.sprite.spritecollide(dino, obstacle_group, True):
        running = False
        print("Game Over!")

    # Generate new obstacles
    current_time = pygame.time.get_ticks()
    if current_time - start_time > 6000:
        if random.randint(0, 100) < 10:
            obstacle = Obstacle(width, height - 40, 30, 40, 2)
            obstacle_group.add(obstacle)

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw dino and obstacles
    dino_group.draw(screen)
    obstacle_group.draw(screen)

    # Update display
    pygame.display.update()

# Exit game
pygame.quit()
