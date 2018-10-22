import random
import os

capitals = {
'Alabama': 'Montgomery', 
'Alaska': 'Juneau', 
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 
'California': 'Sacramento', 
'Colorado': 'Denver',
'Connecticut': 'Hartford', 
'Delaware': 'Dover', 
'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 
'Hawaii': 'Honolulu', 
'Idaho': 'Boise', 
'Illinois':'Springfield', 
'Indiana': 'Indianapolis', 
'Iowa': 'Des Moines', 
'Kansas':'Topeka', 
'Kentucky': 'Frankfort', 
'Louisiana': 'Baton Rouge', 
'Maine':'Augusta', 
'Maryland': 'Annapolis', 
'Massachusetts': 'Boston', 
'Michigan':'Lansing', 
'Minnesota': 'Saint Paul', 
'Mississippi': 'Jackson', 
'Missouri':'Jefferson City', 
'Montana': 'Helena', 
'Nebraska': 'Lincoln', 
'Nevada':'Carson City', 
'New Hampshire': 'Concord', 
'New Jersey': 'Trenton', 
'NewMexico': 'Santa Fe', 
'New York': 'Albany', 
'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 
'Ohio': 'Columbus', 
'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 
'Pennsylvania': 'Harrisburg', 
'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 
'South Dakota': 'Pierre', 
'Tennessee':'Nashville', 
'Texas': 'Austin', 
'Utah': 'Salt Lake City', 
'Vermont':'Montpelier', 
'Virginia': 'Richmond', 
'Washington': 'Olympia', 
'WestVirginia': 'Charleston', 
'Wisconsin': 'Madison', 
'Wyoming': 'Cheyenne'}

if __name__ == '__main__':

	#change running dir
	os.chdir('E:/python/python_learn/project/project1-random')
	
	for quizNum in range(35):
		
		#get random list of keys
		states = list(capitals.keys())
		random.shuffle(states)	
			
		#Create the quiz file and fill it	
		with open('capitalsquiz%s.txt' % (quizNum + 1), 'w') as f:
			#fill the Header
			f.write('Name:\n\nDate:\n\nPeriod:\n\n')
			f.write(('' * 20) + 'state Catitals Quiz (From %s)' % (quizNum + 1))
			f.write('\n\n')
			with open('capitalsquiz_answers%s.txt' % (quizNum + 1) ,'w') as fans:
				#loop through all 50 states ,making a question for each 
				for questionNum in range(50):
					#get right and wrong answers.
					correctAnswer = capitals[states[questionNum]]
					wrongAnswers = list(capitals.values())
					del wrongAnswers[wrongAnswers.index(correctAnswer)]
					wrongAnswers = random.sample(wrongAnswers, 3)
					answerOptions = wrongAnswers + [correctAnswer]
					random.shuffle(answerOptions)
					#write question to quiz
					f.write('%s.What is the capital of %s ?\n' % (questionNum + 1, states[questionNum]))
					for i in range(4):
						f.write(' %s.%s\n' % ('ABCD'[i], answerOptions[i]))
					f.write('\n')
					#write answer to answerFile
					fans.write('%s.%s\n' % (quizNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
				
			
	
