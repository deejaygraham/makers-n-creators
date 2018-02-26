import mcpi.minecraft as minecraft
import mcpi.block as block

world = minecraft.Minecraft.create()

#make the egg - first create some reusable colours
orangeWool = block.Block(35,1)
greyWool = block.Block(35,8)
blueWool = block.Block(35,2)

def make_egg():
	#BAND 1
	world.setBlocks(-5,0,15,5,0,15, block.STONE)
	world.setBlocks(-8,1,15,8,1,15, block.STONE)
	world.setBlocks(-9,3,15,9,2,15, block.STONE)

	#BAND 2
	world.setBlocks(-10,9,15,10,4,15, block.GOLD_ORE)

	#BAND 3
	world.setBlocks(-9,14,15,0,10,15, orangeWool)
	world.setBlocks(0,14,15,9,10,15, blueWool)

	#BAND 4
	world.setBlocks(-7,17,15,7,14,15, block.STONE)
  world.setBlocks(-5,20,15,5,17,15, block.STONE)
	world.setBlocks(-2,21,15,2,20,15, block.STONE)

make_egg()
