#!/usr/bin/python3
import random
import os
os.system('clear')
userinput= input("Please enter how many questions you want?")
print ("Here are some sample questions for you to ponder...\n")
lines = open('interview_questions_list.readme').read().splitlines()
for i in range(int(userinput)):
	myline =random.choice(lines)
	print(myline)
