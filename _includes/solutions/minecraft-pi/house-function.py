import mcpi.minecraft as minecraft
import mcpi.block as block
import random

# a square house at x, y, z
def build_a_house(world, x, y, z, width, height):

    # floor
    world.setBlocks(x, y - 1, z, x + width, y - 1, z + width, block.GRASS.id)

    # walls
    world.setBlocks(x, y, z, x + width, y + height, z, block.STONE.id)
    world.setBlocks(x + width, y, z, x + width, y + height, z + width, block.STONE.id)
    world.setBlocks(x + width, y, z + width, x, y + height, z + width, block.STONE.id)
    world.setBlocks(x, y, z + width, x, y + height, z, block.STONE.id)

    #draw windows
    mc.setBlocks(x + (width / 2) - 2, y + 1, z, x + (width / 2) - 2, y + 2, z, block.GLASS.id)
    mc.setBlocks(x + (width / 2) + 2, y + 1, z, x + (width / 2) + 2, y + 2, z, block.GLASS.id)

    # doorway
    mc.setBlocks(x + (width / 2), y, z, x + (width / 2), y + 1, z, block.AIR.id)

    # flat roof
    mc.setBlocks(x, y + height + 1, z, x + width, y + height + 1, z + width, block.WOOD_PLANKS.id)


world = minecraft.Minecraft.create()

# build house in front of you
pos = world.player.getTilePos()
build_a_house(world, pos.x, pos.y, pos.z + 1, 10, 5)
