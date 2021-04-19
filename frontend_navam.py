from tkinter import *
from tkinter import ttk
from Cricket_navam import *

url_comm = 'https://www.cricbuzz.com/live-cricket-scores/32587/ql-vs-vic-18th-match-sheffield-shield-2020-21'
url = 'https://www.cricbuzz.com/live-cricket-scorecard/32587/ql-vs-vic-18th-match-sheffield-shield-2020-21'

class MainScreen:
	def __init__(self, url_comm, url):
		self.url_comm = url_comm
		self.url = url
	def create(self, cric):
		m = Tk()
		m.title('Goti 11')
		width= m.winfo_screenwidth()  
		height= m.winfo_screenheight() 
		m.geometry("%dx%d" % (width, height)) 

		Tabs = ttk.Notebook(m)
		score_tab = ttk.Frame(Tabs)
		team_tab = ttk.Frame(Tabs)
		rank_tab = ttk.Frame(Tabs)

		Tabs.add(score_tab, text ='Score') 
		Tabs.add(team_tab, text ='Your Team') 
		Tabs.add(rank_tab, text = 'Ranks')
		Tabs.pack(expand = 1, fill ="both") 
		  
		ttk.Label(score_tab, text ="Score") 
		ttk.Label(team_tab, text ="Team")
		ttk.Label(rank_tab, text ="Ranks")

		# Score ( Commentary )
		T = Text(score_tab, height = 15, width = width) 
		def sc_button():
			T.delete(1.0,END)
			T.insert(END, 'Score\n')
			sc = cric.get_curr_team_score()
			T.insert(END, sc+'\n')
		def bat_button():
			# T.delete(1.0,END)
			T.insert(END, 'Batsmen\n')
			bt = cric.get_playing_bats()
			bt = bt[0] + '\n' + bt[1]
			T.insert(END, bt+'\n')
		def bowl_button():
			# T.delete(1.0,END)
			T.insert(END, 'Bowler\n')
			bo = cric.get_playing_bowl()
			T.insert(END, bo)

		sc_button()
		bat_button()
		bowl_button()

		T.pack()

		T.tag_add('start', '1.0', '3.0')
		T.tag_config("start", background = 'LightGreen', foreground='Black')

		T.tag_add('mid', '3.0', '10.0')
		T.tag_config("mid", background = 'LightSkyblue2', foreground='Blue')

		T.tag_add('end', '10.0', '16.0')
		T.tag_config("end", background = 'thistle1', foreground='Magenta')

		# Your Team
		player_team_1 = ['Player '+str(i) for i in range(1,12)]
		points_team_1 = ['Points of Player ' + str(i) for i in range(1,12)]
		team_show_1 = Text(team_tab, height=15, width = 60, foreground = 'BLUE')
		team_show_1.delete(1.0, END)
		for i in range(11):
			team_show_1.insert(END, player_team_1[i] + "		" + points_team_1[i] + '\n')
		team_show_1.grid(column=0, row=0)
		# team_show_1.pack()

		player_team_2 = ['Player '+str(i) for i in range(1,12)]
		points_team_2 = ['Points of Player ' + str(i) for i in range(1,12)]
		team_show_2 = Text(team_tab, height=15, width = 60, foreground = 'BLUE')
		team_show_2.delete(1.0, END)
		for i in range(11):
			team_show_2.insert(END, player_team_2[i] + "		" + points_team_2[i] + '\n')
		team_show_2.grid(column=1, row=0)

		mainloop()

# main = MainScreen(url_comm,url)
# cric = Cricket(url_comm,url)
# main.create(cric)