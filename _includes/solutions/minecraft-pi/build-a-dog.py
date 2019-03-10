import mcpi.minecraft as minecraft
import mcpi.block as block
import time


def clear_area(world, x, y, z, height, width, depth):
	world.setBlocks(x, y, z, x + width, y + height, z + depth, block.AIR)

def build_leg(world, x, y, z, height, material):
	# leg
	for i in range(height):
		world.setBlock(x, y + height, z, material)
		time.sleep(0.5)
	# foot
	world.setBlock(x - 1, y, z, material)
	time.sleep(0.5)

def build_body(world, x, y, z, height, width, depth, material):
	world.setBlocks(x, y, z, x + width, y + height, z + depth, material)
	time.sleep(0.5)

world = minecraft.Minecraft.create()

x, y, z = world.player.getTilePos()

world.postToChat("building a dog ...")
time.sleep(2)

# where do we put the camera?
leg_height = 4
dog_width = 10
dog_length = 20
dog_body = 5

world.camera.setPos(x - 10, y + 20, z - 10)

clear_area(world, x, y, z, x + 50, y + 10, z + 50)


# leg at four corners
for i in range(0, 2):
	for j in range(0, 2):
		build_leg(world, x + (dog_width * i), y, z + (dog_length * j), leg_height, block.STONE)

build_body(world, x, y + leg_height, z, dog_width, dog_length, dog_body, block.STONE)


# put camera back
entityIds = world.getPlayerEntityIds()
for entityId in entityIds:
    world.camera.setFollow(entityId)
