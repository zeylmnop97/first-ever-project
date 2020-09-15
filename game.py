from tkinter import *
from tkinter import ttk   #importing this for button
import os

# import pygame
# pygame.init()
# pygame.mixer.Sound('sound.wav').play()

#the main window
window = Tk()
window.config(background = "SlateBlue4")
window.wm_title("Capitals")
window.minsize(width=1200, height=650)
window.resizable(width=False, height=False)
rootPath=os.getcwd()+"\\images\\"

quedtionList = ["australia,bangladesh,brazil,England,Dhaka,2"]                                    #question 1
quedtionList.append("Spain,argentina,belarus,bosnia,Buenos Aires,2")
quedtionList.append("Hungary,Ghana,Israel,Greece,Athens,4")
quedtionList.append("Ireland,Italy,Japan,France,Tokyo,3")
quedtionList.append("Jordan,Kosovo,Kenya,Kuwait,Nairobi,3")
quedtionList.append("Lebanon,Iraq,Malaysia,Pakistan,Islamabad,4")
quedtionList.append("Poland,Sri Lanka,Kazakhstan,Haiti,Astana,3")
quedtionList.append("USA,Togo,United Arab Emirates,South Korea,Seoul,4")
quedtionList.append("Taiwan,Sweden,Ukraine,Albania,Kiev,3")
quedtionList.append("Bahrain,Bosnia,Iran,Palau,Tehran,3")
quedtionList.append("Yemen,United Arab Emirates,Indonesia,Nigeria,Abuja,4")
quedtionList.append("Norway,Canada,Chile,Finland,Helenski,4")
quedtionList.append("Canada,Malaysia,Netherlands,North Korea,Ottawa,1")
quedtionList.append("United Arab Emirates,Norway,Singapore,Zambia,Abu Dhabi,1")
quedtionList.append("Syria,Turkey,Vatican City,Uruguay,Ankara,2")
quedtionList.append("Uzbekistan,Zambia,Colombia,Togo,Bogota,3")
quedtionList.append("Tunisia,Uruguay,Taiwan,Romania,Tunis,1")
quedtionList.append("Singapore,Romania,San Marino,Saudia Arabia,Bucharest,2")
quedtionList.append("Qatar,Seychelles,Philippines,Malta,Valletta,4")
quedtionList.append("Gambia,Costa,Bulgaria,Iran,Sofia,3")
quedtionList.append("azerbaijan,albania,belize,bhutan,Belmopan,3")
quedtionList.append("brazil,estonia,gabon,Ghana,Accra,4")
quedtionList.append("Fiji,Egypt,Portugal,Senegal,Lisbon,3")
quedtionList.append("Somalia,Slovak Republic,Tanzania,Vatican City, Dar es Salaam,3")
quedtionList.append("Vietnam,Suriname,Liberia,Libya,Hanoi,1")
quedtionList.append("Benin,Austria,Georgia,Guyana,Tbilisi,3")
quedtionList.append("Netherlands,Haiti,Gabon,Portugal,Amsterdam,1")
quedtionList.append("Libya,Jamaica,Niger,Panama,Kingston,2")
quedtionList.append("Oman,Nepal,Paraguay,Iceland,Reykjavik")
quedtionList.append("Israel,Monaco,Yemen,Niger,Sana'a")
total_lives = 4
isMarked= False
total_questions = len(quedtionList)
current_question = 1
total_correct = 0
total_wrong= 0

question = quedtionList[current_question-1].split(',')

def ClearGrid():
	for widget in window.grid_slaves():
		 widget.grid_forget()



def Verify(opt):
	global isMarked
	global total_lives
	global total_correct
	global total_wrong
	global current_question
	global total_questions

	global question
	question = quedtionList[current_question-1].split(',')
	if isMarked == False:
		if opt == str(question[5]):
			lbl_status = Label(text="Good! You are right!!!",bg="Yellow")
			lbl_status.config(font=("Courier", 20))
			lbl_status.grid(row=5,column=1, columnspan=4)
			lbl_lives = Label(text="Total lives : "+str(total_lives))
			lbl_lives.config(font=("Courier", 15))
			lbl_lives.grid(row=1,column=1, columnspan=4)
			# lbl_lives = Label(text="Remaining lives : "+str(total_lives))
			# lbl_lives.config(font=("Courier", 15))
			# lbl_lives.grid(row=5,column=1, columnspan=4)
			isMarked=True
			total_correct+=1
		else:
			lbl_status = Label(text="Sorry! You are wrong!, '"+question[int(question[5])-1]+"' is correct",bg="red")
			lbl_status.config(font=("Courier", 20))
			lbl_status.grid(row=5,column=1, columnspan=4)
			isMarked=True
			total_lives = total_lives-1
			lbl_lives = Label(text="Total lives : "+str(total_lives))
			lbl_lives.config(font=("Courier", 15))
			lbl_lives.grid(row=1,column=1, columnspan=4)
			# lbl_lives = Label(text="Remaining lives : "+str(total_lives))
			# lbl_lives.config(font=("Courier", 15))
			# lbl_lives.grid(row=5,column=1, columnspan=4)
			total_wrong+=1

		current_question+=1

		if current_question> total_questions:
			displayResult("W")
		else:
			if total_lives == 0:
				displayResult("L")
			else:
				global image_next
				image_next =  PhotoImage(file = rootPath+"next.png")
				btnNext = ttk.Button(text = "NEXT",command=lambda: loadNextQuestion())
				btnNext.config(image = image_next)
				btnNext.grid(row=8,column=1, columnspan=4)


def start_screen():
	gameTitle = Label(text="CAPITALS",bg="SlateBlue4")
	gameTitle.config(font=("Courier", 45,"bold"))
	gameTitle.grid(row=1,column=1,padx=450)

	gameScreen = PhotoImage(file = rootPath+"capital.png")
	label = Label(image=gameScreen,bg="SlateBlue4")
	label.image = gameScreen
	label.grid(row=3,column=1,padx=450,pady= 45)
	btnStartGame = ttk.Button(command=lambda: loadNextQuestion())
	global imageStart
	imageStart = PhotoImage(file = rootPath+"play_game.png")
	btnStartGame.config(image = imageStart)
	btnStartGame.grid(row=4,column=1)

	




def tryAgain():
	global isMarked
	global total_lives
	global total_correct
	global total_wrong
	global current_question
	global total_questions
	isMarked = False
	current_question = 1
	total_correct = 0
	total_wrong= 0
	total_lives = 4
	ClearGrid()
	loadNextQuestion()

def exitGame():
	exit()


def displayResult(game_status):
	ClearGrid()
	if game_status == "L":
		label_result = Label(text="Sorry! You have lost the game.",bg = "red")
		label_result.config(font=("Courier", 25))
		label_result.grid(row=0,column=1, columnspan=4,padx=290,pady=40)

		label_total = Label(text="Total Question : "+str(total_questions))
		label_total.config(font=("Courier", 25))
		label_total.grid(row=1,column=1, columnspan=4,pady=40)

		label_right = Label(text="Correct Answers : "+str(total_correct),bg = "yellow")
		label_right.config(font=("Courier", 25))
		label_right.grid(row=2,column=1, columnspan=4,pady=25)

		label_wrong = Label(text="Wrong Answers : "+str(total_wrong),bg="red")
		label_wrong.config(font=("Courier", 25))
		label_wrong.grid(row=3,column=1, columnspan=4)
	else:
		label_result = Label(text="Congratulations! You have won the game.",bg="yellow")
		label_result.config(font=("Courier", 25))
		label_result.grid(row=0,column=1, columnspan=4,padx=190,pady=40)

		label_total = Label(text="Total Question : "+str(total_questions))
		label_total.config(font=("Courier", 25))
		label_total.grid(row=1,column=1, columnspan=4,pady=40)

		label_right = Label(text="Correct Answers : "+str(total_correct))
		label_right.config(font=("Courier", 25))
		label_right.grid(row=2,column=1, columnspan=4,pady=25)

		label_wrong = Label(text="Wrong Answers : "+str(total_wrong))
		label_wrong.config(font=("Courier", 25))
		label_wrong.grid(row=3,column=1, columnspan=4,pady=25)

	btnTryAgain = ttk.Button(text = "TRY AGAIN",command=lambda: tryAgain())
	global imagePlayAgain
	imagePlayAgain = PhotoImage(file = rootPath+"play_again.png")
	btnTryAgain.config(image = imagePlayAgain)
	btnTryAgain.grid(row=4,column=2,pady=20)


	btnQuit = ttk.Button(text = "EXIT",command=lambda: exitGame())
	global imageExit
	imageExit = PhotoImage(file = rootPath+"exit_game.png")
	btnQuit.config(image = imageExit)
	btnQuit.grid(row=4,column=3)



def loadNextQuestion():
	global isMarked
	isMarked=False
	ClearGrid()
	global current_question
	global total_questions
	global question
	question = quedtionList[current_question-1].split(',')
	
	questionNo = Label(text="Question No: "+str(current_question)+" / "+str(total_questions),bg="SlateBlue4")
	questionNo.config(font=("Courier", 25))
	questionNo.grid(row=0,column=1, columnspan=4,padx=190)

	lbl_lives = Label(text="Total lives : "+str(total_lives),bg="SlateBlue4")
	lbl_lives.config(font=("Courier", 15))
	lbl_lives.grid(row=1,column=1, columnspan=4)

	label_Question = Label(text="Which country's capital is:"+str(question[4])+"?",bg="SlateBlue4")
	label_Question.config(font=("Courier", 25))
	label_Question.grid(row=2,column=1, columnspan=4)

	option1 = ttk.Button(text = str(question[0]),command=lambda: Verify("1"))
	global imageOption1
	imageOption1 = PhotoImage(file = rootPath+question[0]+".png")
	option1.config(image = imageOption1,compound = TOP)
	option1.grid(row=3, column=0,columnspan=2,padx=230,pady=10)


	option2 = ttk.Button(text = str(question[1]),command=lambda: Verify("2"))
	global imageOption2
	imageOption2 = PhotoImage(file = rootPath+question[1]+".png")
	option2.config(image = imageOption2,compound = TOP)
	option2.grid(row=3, column=2)


	option3 = ttk.Button(text = str(question[2]),command=lambda: Verify("3"))
	global imageOption3
	imageOption3 =  PhotoImage(file = rootPath+question[2]+".png")
	option3.config(image = imageOption3,compound = TOP)
	option3.grid(row=4, column=0,columnspan=2,padx=230,pady=10)

	option4 = ttk.Button(text = str(question[3]),command=lambda: Verify("4"))
	global imageOption4
	imageOption4 =  PhotoImage(file = rootPath+question[3]+".png")
	option4.config(image = imageOption4,compound = TOP)
	option4.grid(row=4, column=2)


start_screen()
window.mainloop()
