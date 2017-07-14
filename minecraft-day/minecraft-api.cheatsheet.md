## Minecraft API

Minecraft on the raspberry pi has an API built into it which we can use to automate lots of tasks from Python.


### Connect to Minecraft

```python

import mcpi.Minecraft 
world = minecraft.Minecraft.create("localhost")
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

### Messages

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("localhost")
msg = “Hello world”
mc.postToChat(msg)


### Player Position

to get what player is standing on, substract 1 from the y position.

### Coordinates

x = forward and backward
y = up and down
z = left and right

### Where Am I

import time
mc = minecraft.Minecraft.create("localhost")
while True:
time.sleep(1.0)
pos = mc.player.getPos()
print 
pos.x, pos.y, pos.z

### Changing position

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("localhost")
mc.player.setPos(0, 0, 40)




### Blocks

https://arghbox.wordpress.com/2013/07/07/minecraft-pi-api-setting-blocks/


import mcpi.minecraft as minecraft
from 
mcpi.block import *
mc
= minecraft.Minecraft.create("localhost")
x = 38  # vertical
y = 0  # height from sea level
z = 7.7 # horizontal
mc
.player.setPos(x, y, z)
mc
.setBlock(x, y, z, GLOWING_OBSIDIAN)
mc
.setBlock(x, y, z+2, GLOWING_OBSIDIAN)
mc
.setBlock
(x, y, z+4, GLOWING_OBSIDIAN

### Deleting blocks

import mcpi.minecraft as minecraft
from mcpi.block import *
mc
= minecraft.Minecraft.create("localhost")
x = 38  # vertical
y = 0  # height from sea level
z = 7.7 # 
horizontal
mc
.player.setPos(x, y, z)
mc
.setBlock(x, y, z, AIR)



Minecraft Class
Preamble:
mc
Example:
mc.getBlock(1,8,-16)
Method
Arguments
Returns
Description
getBlock
x, y, z
blockId: int
Get the block ID at co-ordinates
getBlockWithData
x, y, z
vec3: obj
Get a block object at co-ordinates.
getBlocks
x0, y0, z0,
x1, y1, z1
[int]
Get block ids in cuboid between two co-ordinates.
setBlock
x, y, z, id,
[state]
Sets a block at co-ordinates. State is an optional argument
between 0–15.
setBlocks
x0, y0, z0,
x1, y1, z1, id,
[state]
Sets blocks between two sets of co-ordinates. State is an op-
tional argument between 0–15.
getHeight
x,z
int
Returns the highest block at a point.
getPlayerEntityIds
[int]
Returns the IDs of all players connected to the game.
saveCheckpoint
Saves the current state of the game.
restoreCheckpoint
Restores the game to the latest save.
postToChat
message: str
Posts a message to the chat.
setting
key, stat: bol
Changes  the  settings  of  the  world.
Key  values:
world_immutable, nametags_visible
Player Class
Preamble:
mc.player
Example:
mc.player.getPos()
getPos
x, y, z
vec3: obj
Returns the player’s position as an object with floats.
setPos
x, y, z
Sets the player’s position using floats.
getTilePos
x, y, z
vec3: obj
Returns the player’s position as an object with integers.
setTilePos
x, y, z
Sets the player’s position using integers.
setting
key, stat: bol
Changes the player’s settings. Key values: autojump
Events Class
Preamble:
mc.events
Example:
mc.events.pollBlockHits()
clearAll
Clears all events from buffer.
pollBlockHits
[vec3: obj]
Returns an array of block hits. Block hits created with sword
right click.
Camera Class
Preamble:
mc.camera
Example:
mc.camera.setFixed()
setNormal
[entityID]
Sets the camera to normal for a list of player entities.
setFixed
Sets the camera to fixed.
setFollow
[entityId]
Sets the camera to follow for a list of player entities.
setPos
x, y, z
Sets the camera position to co-ordinates.
Entity Class
Preamble:
mc.entity
Example:
mc.entity.getPos(3)
getPos
id: int
vec3: obj
Gets the position of the entity as floats
setPos
entityId:int,
x, y, z
args: ()
getTilePos
entityId: int
vec3: obj
Returns the position of an entity as a vector with integers.
setTilePos
entityId:int,
x,y,z
Sets the position of an entity with integers.
setting
entityId: int,
key, stat: bol
Changes the entity’s settings. Key values: autojump
Notes:
•
vec3 objects have x, y and z attributes. These attributes can be accessed using dot notation.
•
arguments in square brackets [ ] are optional and do not need to be included
•
returned values in square brackets [ ] are lists of values
•
the getBlocks() method does not work
•
certain methods are buggy on multi-player



