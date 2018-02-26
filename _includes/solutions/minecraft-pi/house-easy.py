import mcpi.minecraft as minecraft

world = minecraft.Minecraft.create()

x = 10
y = 11
z = 12

# width, height and depth
x2 = x + 10
y2 = y + 5
z2 = z + 8

stone_block_id = 4 # cobble stones
air_block_id = 0

world.setBlocks(x, y, z, x2, y2, z2, stone_block_id)
world.setBlocks(x + 1, y + 1, z + 1, x2 - 1, y2 - 1, z2 - 1, air_block_id)