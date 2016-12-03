from time import sleep
from threading import Thread

CHECKMARKS = []

def timer(time):
	print("Timer counting down from {} minutes".format(time))
	pTime = int(time * 60)
	sleep(pTime)
	print("All done!")
	recordCheckmark()
	pBreak()

def pBreak():
	global CHECKMARKS
	if len(CHECKMARKS) % 4 == 0:
		CHECKMARKS = 0
		print("Take a 15-30 minute break!")
	else:
		print("Take a 5 minute break!")

def distractions():
	f = open("log.txt", "a")
	while True:
		i = input()
		f.write(i + "\n")
	f.close()

def recordCheckmark():
	global CHECKMARKS
	CHECKMARKS.append("!")
	print("Checkmark added!")

def pomodoro():
	global CHECKMARKS
	status = True
	f = open("log.txt", "a")
	while status == True:
		task = input("What needs to be done(or type exit)? ")
		if task == "exit":
			break
		print("DO: {}".format(task))
		f.write(task + "\n")
		print("Checkmarks: {}".format(CHECKMARKS))
		time = input("Enter a time in minutes or enter default for 25 minutes: ")
		if time == "default":
			t1 = Thread(target=timer, args=(25,))
			t2 = Thread(target=distractions)
			t1.start()
			t2.start()
			t1.join()
			t2.join()
		else:
			t1 = Thread(target=timer, args=(time,))
			t2 = Thread(target=distractions)
			t1.start()
			t2.start()
			t1.join()
			t2.join()
	f.close()

if __name__ == "__main__":
	pomodoro()
