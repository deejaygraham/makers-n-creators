import mcpi.minecraft as minecraft

world = minecraft.Minecraft.create()

message = "hello, minecraft world"
world.postToChat(message)