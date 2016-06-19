#exercise 36
#Designing and Debugging
#Make me own game

#imports the ability to exit the game
from sys import exit

#the only way I figured to make a global variable like a name to use was to use it outside of a function.
name = raw_input("What's your name? > "  )

#Introduction, just printing stuff out 
#and starts the function room() the first place in the game
def start():
	print "\t\tDRUID QUEST\t\n\t\tBy Patrick Mogianesi"
	print "Your goal is to gather 3 herbs to make a medicine for a local in the village to the east."
	print "%s you must gather:\n*Sage\n*Hair of a wild boar\n*Athelas, a rare herb treasured by the locals." % name
	print "\nYour journey starts at in your room, be sure to explore and 'examine' the world."
	room()

#Inventory system is working
#Checking inventory outside of gaining items might be difficult
#With the way I set up doing inputs
#becuase each input is specifically for a a different function like room_action

############## Items #############

#Hopefull this list works as a storage list for things picked

Inventory = []

##################################

#starting place for the game
#Potion is brewed here when all three items are in Inventory list
def room():
	print "You're standing in your room."
	#Raw input uses a string given by a user
	room_action = raw_input("What will you do? > ")
	
	#If the player says Examine, This stuff prints, gives hints and surrounding
	if "Examine" in room_action:
		print "Inside your cozy room you can see your comfortable bed, your cauldron, and your bookshelf full of old tomes."
		print "\n"
		print "Drinking some nice herbal tea and reading a good book sounds nice, but someone needs help."
		print "\n"
		print "Be sure not to forget your trusty wooden rod!"
		print "\n"
		print "You have to 'leave your room' unfortunately"
		room()
	#Takes user to the Garden function
	elif "Leave Room" in room_action:
		print "You leave the room and enter your garden."
		print "\n"
		garden()
	#Adds Rod to Inventory list by Append
	elif "Grab Rod" in room_action:
		print "You grab your trusty stick, properly weighted to give gobbos a good smack."
		print "\n"
		Inventory.append("Rod")
		room()
	#If the three items are in inventory, Remove items and add Potion
	elif "Brew Potion" in room_action:
		if ("Athelas") in Inventory:
			print "After pouring the ingredients into your couldren and brewing the mixture together.\nThe Potion is finished.\nYou should Bring it to the village."
			print "\n"
			Inventory.remove("Sage")
			Inventory.remove("Boar_Hair")
			Inventory.remove("Athelas")
			Inventory.append("Potion")
			print "You have %r in your bag" % Inventory
			room()
			
		#If the required items are not available, player cannot make potion
		else:
			print "You don't have everything for the potion."
			print "\n"
			room()
	#Debug action to help with testing Cave
	elif "Debug" in room_action:
		print "Sending to Cave"
		Cave()
	elif "ITEMS" in room_action:
		Inventory.append("Sage")
		Inventory.append("Boar_Hair")
		Inventory.append("Athelas")
		room()
	#If the user does not put in a vaild action, print this and send back to function, room
	else:
		print "I don't think I can do that."
		print "\n"
		room()
		
def garden():
	

	print "You're standing in your garden"
	print "\n"
	garden_action = raw_input("What will you do? > ")
	
	if "Examine" in garden_action:
		print "You look around, your house sits atop a small hill and is seated next to an ancient oak wood tree."
		print "\n"
		print "To the south is the crossroad."
		print "\n"
		print "\nIn front of the tree is your garden where you grow various herbs."
		print "\n"
		print "You can also enter back into your house when you're ready to make the potion."
		
		#If sage isn't in the inventory this prints a hint to harvest sage
		if "Sage" not in Inventory:
			print "What great time, it appears your Sage is growing well! I should harvest some for the potion."
			print "\n"
			
		#Same thing as above but for passionfruit	
			if "Passionfruit" not in Inventory:
				print "You're also growing passionfruit.\n This plant could come in handy later as well, it's a natural sedative."
				print "\n"
				garden()
			else:
				garden()
			garden()
		else:
			garden()
			
	#Sage is used for potion
	#By input Harvest Sage, user adds Sage string to inventory 
	elif "Harvest Sage" in garden_action:
		print "You picked some sage from your garden"
		print "\n"
		
		#Inventory.append adds the string to the Inventory list
		Inventory.append("Sage")
		print "You have %r in your bag" % Inventory
		print "\n"
		garden()
		
	
	#Passion Fruit is used to Sedate the Boar
	#Harvest, adds to list
	elif "Harvest Passionfruit" in garden_action:
		print "You picked some sage from your garden"
		print "\n"
		Inventory.append("Passionfruit")
		print "You have %r in your bag" % Inventory
		print "\n"
		garden()
		
	#user to Crossroad function
	elif "Travel South" in garden_action:
		print "You travel South to the crossroad"
		print "\n"
		Cross_Road()
	#Else not valid, sends user back to function Garden
	elif "Enter House" in garden_action:
		print "You enter your house."
		print "\n"
		room()
	
	else:
		print "I don't think I can do that."
		print "\n"
		garden()
		
#Cross Road is the hub between the Areas	
def Cross_Road():
	print "You arrive at the cross road.\nTo the west lies the misty forest, to the east is the village, and to the North is my house."
	print "\n"
	Cross_Road_Action = raw_input("Where should I go? > ")
	if Cross_Road_Action in "Travel West":
		print "You traveled west to the forest."
		print "\n"
		forest()
	#In order to the go the village, the player needs the potion	
	elif "Travel East" in Cross_Road_Action:
		if "Potion" in Inventory:
			print "With the potion ready, you head to the village."
			print "\n"
			Village()
		else:
			print "I shouldn't go to the village until I have the potion done..."
			print "\n"
			Cross_Road()
	
	
	
	
	elif "Travel North" in Cross_Road_Action:
		print "You traveled North back to the garden."
		print "\n"
		garden()
	elif "Examine" in Cross_Road_Action:
		print "You see a chubby raccoon eating some berries from a nearby bush."
		print "\n"
		Cross_Road()	
	else:
		print "I don't think I can go there."
		print "\n"
		Cross_Road()


		
def forest():
	#Boar moved is the status of the Boar in front of the cave
	#Until the boar is moved, the player cannot enter the cave
	Boar_Moved = False
	
	print "You arrived at the misty forest, you might find several of the herbs you're looking for here."
	print "\n"
	print "You should look around to start."
	print "\n"
	
	forest_action = raw_input("What do I do? > ")
	if "Examine" in forest_action:
			print "To leave the forest, you must Travel East."
			print "\n"
			print "While walking around all you see is a fog crested landscape.\n However as you walk through the brush in the distance you save a cave with a boar lulling around the entrance."
			print "\n"
			print "You should see what you can do about the boar blocking the enterance,\n plus you need some of it's hair for the potion."
			print "\n"
			print "Maybe you should try feeding the boar something."
			print "\n"
			
			if "Passionfruit" in Inventory:
				print "Passionfruit would help with getting hair from the boar."
				print "\n"
				print "You should, feed the herb to the boar."
				print "\n"
				forest()
			else:
				print "You need something to sedate the boar.\nSo you can get some of it's hair."
				print "\n"
				forest()
	
	elif "Feed Boar Passionfruit" in forest_action:
		
		print "You decide to feed the boar the passionfruit."
		print "\n"
		
		if "Passionfruit" in Inventory:
			Inventory.remove("Passionfruit")
			Inventory.append("Boar_Hair")
			Boar_Moved = True
			print "You have %r in your bag" % Inventory
			print "\n"
			print "After eating the herb, and laying down, the boar is finally asleep!"
			print "\n"
			print "You snag some of it's hair for the potion."
			print "\n"
			print "And good news, the cave is also open now!"
			print "\n"
			forest()
		else:
			print "The boar is not appeased by your offering, he chases you away and knocks you on your butt\nOuch!"
			print "\n"
			forest()
	
	
	
	
	
	elif "Leave Forest" in forest_action:
		print "You left the forest and travelled back to the cross road."
		print "\n"
		Cross_Road()
	
	elif "Enter Cave" in forest_action:
		print "You enter the dark cave."
		print "\n"
		Cave()
	else:
		print "That doesn't work"
		print "\n"
		forest()
	

def Cave():
	cave_action = raw_input("What do I do? > ")
	#The player cannot open the treasure chest until the Gobbo is moved
	
	
	
	print "You enter the dark caverns. You can roughly see ahead of you."
	print "\n"
	if "Examine" in cave_action:
		print "Looking further into the cave. You see an evil gobbo blocking a chest."
		print "\n"
		print "How tretcherous!\nI hope you brought a weapon with you!"
		print "\n"
		Cave()
	
	#If the player has the Rod, the Gobbo can be moved
	elif "Attack Gobbo" in cave_action:
		if "Rod" in Inventory:
			print "The gobbo is knocked off it's feet and flies into a nearby puddle."
			print "\n"
			print "Now the treasure chest is wide available!"
			print "\n"
			Inventory.append("Gobbo_Win")
			Cave()
		else:
			print "The gobbo growels at your bearing it's many teeth."
			print "\n"
			print "I think it'd be for the best to back off unless you have a weapon."
			print "\n"
			Cave()
			
	elif "Open Treasure Chest" in cave_action:
		if "Gobbo_Win" in Inventory:
			Inventory.remove("Gobbo_Win")
			Inventory.append("Athelas")
			print "How lucky, some Athelas perfect for the potion."
			print "\n"
			print "You should go back home and start brewing that potion!"
			print "\n"
			print "You have %r in your bag" % Inventory
			print "\n"
			Cave()
		else:
			print "A vicious Gobbo blocks the path to the treasure chest."
			Cave()

	elif "Leave Cave" in cave_action:
		print "You leave the cave and go back into the forest."
		print "\n"
		forest()
	else:
		print "I don't think I can do that."
		print "\n"
		Cave()

		#Village has win-state, must have the potion in inventory.

def Village():
	print "You arrive into the small village, you should make your way to the house with the sick person."
	print "\n"
	village_action = raw_input("What do I do? > ")
	#Win-State
	if "Go To House" in village_action:
		print "The sick person is excited to see you and the potion in your hand."
		print "\n"
		print "With a little bit of R&R they should be good as new."
		print "\n"
		print "Great job, you saved the day!"
		print "\n"
	
	else:
		print "I don't think I can do that. Try 'going to the house.'"
		print "\n"
		Village()
#starts game and then sends 		
start()
