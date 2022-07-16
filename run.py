from test import *
from boom import *
import os

#Create map
def Main():
	generate_walls()
	generate_enemies(3)
	generate_bricks()

	bm = Boomboom(1,1)
	kb = KBHit()
	boom = Boom()
	lastTime = time.time()

	while True:
		os.system("clear")
		print_matrix()
		lastTime=time.time()
		if kb.kbhit():
			c = kb.getch()
			if c=='w':
				bm.move(0)
			elif c=='d':
				bm.move(1)
			elif c=='s':
				bm.move(2)
			elif c=='a':
				bm.move(3)
			elif c=='b':
				boom.place(bm.row,bm.col)
		else:
			time.sleep(0.5)
			if time.time() - lastTime >= 0.5:
				boom.detonate(bm)
				for e in enemies:
					dir = e.choose_dir()
					if dir>=0 and dir<=3:
						e.move(dir)

Main()