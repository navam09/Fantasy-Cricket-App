from tkinter import *
from tkinter import ttk
from Cricket_navam import *
from front_cricket import *

url_comm = 'https://www.cricbuzz.com/live-cricket-scores/32587/ql-vs-vic-18th-match-sheffield-shield-2020-21'
url = 'https://www.cricbuzz.com/live-cricket-scorecard/32587/ql-vs-vic-18th-match-sheffield-shield-2020-21'

m = Tk()
m.title('Goti 11')
width= m.winfo_screenwidth()  
height= m.winfo_screenheight() 
m.geometry("%dx%d" % (width, height)) 

main = MainScreen(url_comm, url)
def go_to_main():
	m.destroy()
	main.create()

Proceed_button = Button(m, text='Proceed', command = go_to_main)
Proceed_button.pack()

cric = Cricket(url_comm,url)
cric.get_playing_11()
team1, team2 = list(cric.Team.keys())[0], list(cric.Team.keys())[1]

team_show_1 = Text(m, height=15, width = 60, foreground = 'BLUE')
team_show_1.delete(1.0, END)
team_show_1.insert(END, team1+'\n\n')
team_show_1.insert(END, '\n'.join(list(cric.Team[team1].keys())))

team_show_1.grid(column=0, row=0)

team_show_2 = Text(m, height=15, width = 60, foreground = 'BLUE')
team_show_2.delete(1.0, END)
team_show_2.insert(END, team2+'\n\n')
team_show_2.insert(END, '\n'.join(list(cric.Team[team2].keys())))

team_show_2.grid(column=1, row=0)

m.mainloop()