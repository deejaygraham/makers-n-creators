## Minecraft API

Minecraft on the raspberry pi has an API built into it which we can use to automate lots of tasks from Python. You need to start Minecraft first, then open a terminal window and run scripts from there


### Connect to Minecraft

Always need to set up a connection to the Minecraft instance


```python

import mcpi.minecraft as minecraft

world = minecraft.Minecraft.create()

# use objects via the world object...


```


### Hello, Minecraft

```python

msg = "Hello world"

world.postToChat(msg)

```

### Coordinates

All objects, including the player, are referenced using a 3-d coordinate system:

```

       +y / 
       | / +x
       |/
-z ----/------ +z
      /|
     / | -y    
   -x

```

x = forward (into screen) and backward 
y = up and down (elevation)
z = left and right

### Where Am I

```python

import time

world = minecraft.Minecraft.create()

while True:
  pos = mc.player.getPos()
  print pos.x, pos.y, pos.z
  time.sleep(1.0)

```


### Changing My Position

```python

x = 10
y = 2
z = 5

world.player.setPos(x, y, z)

```

### Player Ground

To get what block the player is standing on, substract 1 from their y position.


### Blocks

Block types (stone, grass, water, air) are identified by a numeric ids - either as plain integer values or as block values.

```python

import mcpi.minecraft as minecraft
import mcpi.block as block

world = minecraft.Minecraft.create()

stone_id = 1
x = 1
y = 2
z = 3

world.setBlock(x, y, z, stone_id)
world.setBlock(x, y, z, block.STONE.id)

```

### Interrogating Blocks

Find out what kind of block is at a location using:

```python

block_id = world.getBlock(x, y, z)

```

### Deleting Blocks

To delete a block, set the block to be "air" id 0


### Building Blocks

setBlock works for individual blocks but you can use setBlocks to build cuboids of any size given two opposing corners

```python

# build a wall from x, y, z, height high and width wide
world.setBlocks(x, y, z, x, y + height, z + width)

```

