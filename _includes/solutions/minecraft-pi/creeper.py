import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

# build the figure using the given material
def build_spooky_figure(world, x, y, z, material):
  for i in range(3):
    world.setBlock(x, y + i, z, material)

world = minecraft.Minecraft.create()

world.postToChat("What ever you do ...")
time.sleep(5)
world.postToChat("Don't blink!")

# create the spooky block 20 blocks away
playerTile = world.player.getTilePos()
x = playerTile.x
z = playerTile.z + 20
y = world.getHeight(x, z)

build_spooky_figure(world, x, y, z, block.OBSIDIAN)

while True:
  time.sleep(random.randint(1, 5))

  playerTile = world.player.getTilePos()

  # remove the spooky block from old position by building
  # over the existing figure with "air"
  build_spooky_figure(world, x, y, z, block.AIR)
  
  # move it to new position
  if (x - playerTile.x) > 0: x -= 1
  if (x - playerTile.x) < 0: x += 1
  if (z - playerTile.z) > 0: z -= 1
  if (z - playerTile.z) < 0: z += 1
  
  y = world.getHeight(x, z)
  
  build_spooky_figure(world, x, y, z, block.OBSIDIAN.id)
