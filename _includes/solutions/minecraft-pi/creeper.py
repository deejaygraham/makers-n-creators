import mcpi.minecraft as minecraft
import mcpi.block as block
import time


# build the figure using the given material
def build_spooky_figure(world, x, y, z, material):
	# simple block for now
	world.setBlock(x, y, z, material)

world = minecraft.Minecraft.create()

lastPlayerTile = world.player.getTilePos()

world.postToChat("What ever you do ...")
time.sleep(2)
world.postToChat("Don't blink!")

# create the spooky block 20 blocks away
x = lastPlayerTile.x
y = lastPlayerTile.y
z = lastPlayerTile.z + 20

build_spooky_figure(world, x, y, z, block.STONE.id)

while True:

	time.sleep(5)

	playerTile = world.player.getTilePos()

	# has the player moved ?
  	if playerTile != lastPlayerTile:
		# remove the spooky block from old position by building
		# over the existing figure with "air"
		build_spooky_figure(world, x, y, z, block.AIR.id)

		lastPlayerTile = playerTile
		# move it to new position
		x = lastPlayerTile.x
		y = lastPlayerTile.y
		z = lastPlayerTile.z + 1
		# build it in stone
		build_spooky_figure(world, x, y, z, block.STONE.id)
