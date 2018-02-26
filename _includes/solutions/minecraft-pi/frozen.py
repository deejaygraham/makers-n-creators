import mcpi.minecraft as minecraft
import time

water_block_id = 9
ice_block_id = 79

world = minecraft.Minecraft.create()

while True:
  time.sleep(0.2)

  pos = world.player.getPos()
  x = pos.x
  y = pos.y
  z = pos.z

  block_below_player = world.getBlock(x, y - 1, z)

  if block_below_player == water_block_id:
    world.setBlock(x, y - 1, z, ice_block_id)
