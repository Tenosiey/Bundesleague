invalid_input = True
invalid_input_Tag = True
teamName = "a"
teamTag = "a"

def main():
	global invalid_input
	global teamName

	print("Welcome to Bundesleague.")
	teamName = input("Please enter your Teamname.\n")
	teamNameCorrect = input("Your Teamname is " + teamName + ", correct? y/n\n")

	if teamNameCorrect == "y":
		f = open(teamName + ".txt","w+")
		f.write("teamName = " + teamName + "\n")
		f.close()
		
		secondary()

		invalid_input = False

	elif teamNameCorrect == "n":
		print("Ok, lets try it again than.")

		invalid_input = True

	else:
		print("Sorry that was an invalid command.")

		invalid_input = True

def secondary():
	global invalid_input_Tag
	global teamName
	global teamTag

	teamTag = input("Please enter your Teamtag.\n")
	teamTagCorrect = input("So your Teamtag is " + teamTag + ", correct? y/n\n")

	if teamTagCorrect == "y":
		f = open(teamName + ".txt","a")
		f.write("teamTag = " + teamTag)
		f.close()

		invalid_input_Tag = False

	elif teamTagCorrect == "n":
		print("Ok, lets try it again than.")

		invalid_input_Tag = True

	else:
		print("Sorry that was an invalid command.")

		invalid_input_Tag = True

def teamMember():
	topLane = a
	jungleLane = b
	midLane = c
	adcLane = d
	supportLane = e

while invalid_input == True:
	
	if invalid_input == False:
		break
	
	main()

while invalid_input_Tag == True:

	if invalid_input_Tag == False:
		break

	secondary()