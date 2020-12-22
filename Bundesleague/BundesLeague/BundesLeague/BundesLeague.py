invalid_input = True
invalid_input_Tag = True
teamName = "a"
teamTag = "a"

topLane = "top"
jungleLane = "jung"
midLane = "mid"
adcLane = "adc"
supportLane = "sup"

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
		f.write("teamTag = " + teamTag + "\n" + "\n")
		f.close()

		invalid_input_Tag = False

	elif teamTagCorrect == "n":
		print("Ok, lets try it again than.")

		invalid_input_Tag = True

	else:
		print("Sorry that was an invalid command.")

		invalid_input_Tag = True

def teamMember():
	global teamName

	topLane = input("Please enter the username of your Top Laner\n")
	jungleLane = input("Please enter the username of your Jungler\n")
	midLane = input("Please enter the username of your Mid Laner\n")
	adcLane = input("Please enter the username of your ADC\n")
	supportLane = input("Please enter the username of your Supporter\n")

	f = open(teamName + ".txt","a")

	f.write("topLane = " + topLane + "\n")
	f.write("jungleLane = " + jungleLane + "\n")
	f.write("midLane = " + midLane + "\n")
	f.write("adcLane = " + adcLane + "\n")
	f.write("supportLane = " + supportLane + "\n")
	f.close()

while invalid_input == True:
	
	if invalid_input == False:
		break
	
	main()

while invalid_input_Tag == True:

	if invalid_input_Tag == False:
		break

	secondary()

teamMember()