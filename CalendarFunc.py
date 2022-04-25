from datetime import date, timedelta
import fire
import os

def calendar(r=None, day=None):
	'''
	The *working* version of the zsh calendar command.

	A working replacement of the existing *calendar* command in zsh, it only displays events for the next seven days, but you can add events for future dates.

	To add an event, put the date after the `display` command in this format `YYYY-MM-DD`'''

	if r == "r":
		with open('/Users/maxkonietzko/calendar.txt') as f:
			# countLines = len(f.readlines())
			lines = f.readlines()

		with open('/Users/maxkonietzko/calendar.txt', 'w') as f:
			for entry in lines:
				if day in entry:
					culprit = lines.index(entry)
					del lines[culprit]

			# TODO: Print 1 custom error for when day is not found after the loop

			for entry in lines:
				f.write(entry)# + "\n")

	with open('/Users/maxkonietzko/calendar.txt') as f:
		lines = f.read()

		today = str(date.today())
		tomorrow = str(date.today() + timedelta(days=1))
		day_after_tomorrow = str(date.today() + timedelta(days=2))
		ThreeDays = str(date.today() + timedelta(days=3))
		FourDays = str(date.today() + timedelta(days=4))
		FiveDays = str(date.today() + timedelta(days=5))
		SixDays = str(date.today() + timedelta(days=6))

		os.system("cal")
		print("")

        #if there is a line with today's date, print it
		if today in lines:
			print("For TODAY!: " + lines.split(today)[1].split('\n')[0])
        
        #if there is a line with tomorrow's date, print it
		if tomorrow in lines:
			print("For Tomorrow: " + lines.split(tomorrow)[1].split('\n')[0])
        
        #if there is a line with day after tomorrow's date, print it
		if day_after_tomorrow in lines:
			print("For Day After Tomorrow: " + lines.split(day_after_tomorrow)[1].split('\n')[0])

        #if there is a line with ThreeDays date, print it
		if ThreeDays in lines:
			print("Three days from now: " + lines.split(ThreeDays)[1].split('\n')[0])

		#if there is a line with FourDays date, print it
		if FourDays in lines:
			print("Four days from now: " + lines.split(FourDays)[1].split('\n')[0])

        #if there is a line with FiveDays date, print it
		if FiveDays in lines:
			print("Five days from now: " + lines.split(FiveDays)[1].split('\n')[0])

        #if there is a line with SixDays date, print it
		if SixDays in lines:
			print("Six days from now: " + lines.split(SixDays)[1].split('\n')[0])

		# else:
		# 	print("No events for the next 7 days")

	try:
		if r and r != "r":
			with open('/Users/maxkonietzko/calendar.txt', 'a') as f:
				f.write(r)
				f.write(" ")
				f.write(input("New event: "))
				f.write('\n')
	except:
		print("Not a valid date or flag")

if __name__ == "__main__":
	fire.Fire(calendar)
