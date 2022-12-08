#to run game type the following command in command line: 
# python3 pymaze.py -interactive -block -color -width 20 -height 15
# height and width can be adjusted to fit corresponding command line

import os, sys, random, time, threading
import maze

# defalt ANSI settings from user
COLOR_DEFAULT = u'\u001b[0m'
# foreground colors (text)
COLOR_BLACK = u'\u001b[30m'
COLOR_RED =  u'\u001b[31m'
COLOR_GREEN = u'\u001b[32m'
COLOR_YELLOW = u'\u001b[33m'
COLOR_BLUE  =u'\u001b[34m'
COLOR_MAGENTA = u'\u001b[35m'
COLOR_CYAN = u'\u001b[36m'
COLOR_WHITE = u'\u001b[37m'
# background colors 
COLOR_BG_BLACK = u'\u001b[40m'
COLOR_BG_RED =	u'\u001b[41m'
COLOR_BG_GREEN =  u'\u001b[42m'
COLOR_BG_YELLOW = u'\u001b[43m'
COLOR_BG_BLUE = u'\u001b[44m'
COLOR_BG_MAGENTA =  u'\u001b[45m'
COLOR_BG_CYAN = u'\u001b[46m'
COLOR_BG_WHITE= u'\u001b[47m'

def getchar():
	# Determine which getchar method to use
	if os.name!='nt':
		# import unix terminal interface
		import termios, tty
		# get stdin file descriptor 
		file_desc = sys.stdin.fileno()
		# get stdin file settings
		settings = termios.tcgetattr(file_desc)
		try:
			# set tty to read raw input (unbuffered)
			# modifies settings
			tty.setraw(file_desc)
			# read a single byte 
			char = sys.stdin.read(1)
		finally:
			# set the stdin settings back to before raw modification
			termios.tcsetattr(file_desc, termios.TCSADRAIN, settings)
	# use windows getchar
	else:
		import msvcrt
		char = msvcrt.getch()
	return char

def save_maze(maze, out_filename):	  
	#write the maze to a text file
	out_file = open(out_filename+'_maze.txt', 'w')	
	out_file.write(maze.to_str())
	out_file.close()

	# write the portals to a textfile
	out_file= open(out_filename +'_portals.txt', 'w')
	out_file.write( maze.portals_str())
	out_file.close()


	
def play_maze(maze_obj):
	quit_key = lambda key: key == ord('x')
	up_key = lambda key: key == ord('w') or key == ord('A')
	down_key = lambda key: key == ord('s') or key == ord('B')
	right_key = lambda key: key == ord('d') or key == ord('C')
	left_key = lambda key: key == ord('a') or  key == ord('D')

	#clear the screen clear if linux, cls if windows
	os.system('clear' if os.name!='nt' else 'cls')	
	print(r'''
#######  ##    ## ##	 ##    ###    ########	######## 
##    ##  ##  ##  ###	###   ## ##	   ##	##	 
##    ##   ####   #### ####  ##   ##	  ##	######	     
#######     ##	  ## ### ## #########	 ##	##
##	    ##	  ##	 ## ##	   ##	##	##	 
##	    ##	  ##	 ## ##	   ##  ######## ########				      
Controls:
	WASD	- To navigate (or Arrow Keys on Linux)
	x	- To give up 

Press any key to start!
	''')
	getchar()
	os.system('clear' if os.name!='nt' else 'cls')	
	print(maze_obj.to_str())
	maze_obj.start_timer()	
	move = 0
	# exit when either ESC or q are entered
	while not quit_key(move) and not maze_obj.is_done():
	# get the integer value of character input 
		# update maze based on input
		move = ord(getchar())
		if up_key(move):
			maze_obj.move(maze_obj.UP)
		elif down_key(move):
			maze_obj.move(maze_obj.DOWN)
		elif right_key(move):
			maze_obj.move(maze_obj.RIGHT)
		elif left_key(move):
			maze_obj.move(maze_obj.LEFT)
	
		# maze updates on move
	# kil timer or show time 
	if quit_key(move):
		maze_obj.kill_timer()
		print('\nBetter Luck next time')
	else:
		print('Solved in %f seconds!' % maze_obj.end_timer())
	print('Thanks for Playing!');
		
def solve_maze(maze_obj):
	# print('Press any key to see solution!')
	# getchar();
	# os.system('clear' if os.name!='nt' else 'cls')
	# print(maze_obj.to_str())
	# maze_obj.start_timer()
	# maze_obj.solve()	
	# print('\nSolved in %f seconds!' % maze_obj.end_timer())
	
	maze_obj.player = (0,0)

	print('Press any key to see heuristic solution!')
	getchar();
	os.system('clear' if os.name!='nt' else 'cls')
	print(maze_obj.to_str())
	maze_obj.start_timer()
	maze_obj.heuristic_solve()	
	print('Solved in %f seconds!' % maze_obj.end_timer()+'\n')

def error(msg):
	print(msg+'\nTry \'./maze -help\' for information\n')
	sys.exit(-1) 

# move throwaway function to parse argument
def parse_arg(option, argv, i, arg_type) :
    #expect integer
	try:
		return arg_type(argv[i])
	except ValueError:
		error('\nError: Invalid argument type for option: '+ str(option))
	except IndexError:
		error('\nError: Missing argument for option: '+str(option))


def main():
	usage = \
	r'''
PyMaze github.com/138paulmiller
	./pymaze.py -[OPTION=ARG]*
Options:
	-width COL	Sets the maze width (number of columns) to COL (Must be greater than 0). Default is 20
	-height ROW	Sets the maze height (number of rows) to ROW (Must be greater than 0). Default is 12
	-seed SEED	Sets Random Number Generator's seed to SEED.  Default seed is random
	-out NAME	Sets output file prefix to NAME, default is seed number		
	-interactive	Starts CLI maze game. Does not save to file	
	-block	Print maze using Unicode block characters, only works with interactive mode	
	-color	Print maze using ANSI style coloring, only works with interactive mode	
	-solve	Displays the solution to the maze in real-time, only works with interactive mode
	-help	Prints this menu
Example:
	The following generates two files, MyMaze_maze.txt and MyMaze_portals.txt, which contain a 50x45 maze with a random seed of 13.1 
		./maze.pys -width 50 -height 45 -seed 13.1 -out MyMaze
	This will start the interactive maze in the terminal	
		./maze.py -interactive	
	'''	

	argv = sys.argv
	argc = len(argv)
	# set option defaults
	seed = random.random()*10000		
	width = 20
	height = 12 
	interactive = False
	block_symbol = u'\u2588'#unicode FullBlock
	block_symbols = {
		'start' : u'O',
		'end' : u'X',
		'wall_v' : block_symbol, 
		'wall_h' : block_symbol,
		'wall_c' : block_symbol,
	}
	color_symbols = {
		'empty_color' : COLOR_DEFAULT,
		'wall_color' : COLOR_BLUE,
		'head_color' : COLOR_RED,
		'tail_color' : COLOR_CYAN,
		'start_bg_color' : COLOR_BG_YELLOW,
		'end_bg_color' : COLOR_BG_YELLOW,
		# if color, full block for player too
		'head' : block_symbol,
		'tail' : block_symbol,
	}
	#default symbols (not unicode or ANSI coloring)
	symbols = {
		# default symbols
		'start' : 'S',
		'end' : 'X',
		'wall_v'  : '|',
		'wall_h' : '-',
		'wall_c' : '+',
		'head' :  '#',
		'tail' : 'o',	
		'empty' : ' '
	}
	output_to_file = False
	is_color = False
	is_block= False
	is_solve = False
	out_filename = None # default file names is in mazes dir and seed used
	#parse arguments not including script path
	i = 1	
	while i < argc:
		option = argv[i]
		i+=1 # next option
		if option == '-width':
			width = parse_arg( '-width', argv, i, int)
			if width <= 0:
				error('Invalid argument: width must be a positive integer')

			i+=1 # eat next arg
		elif option == '-height':
			height = parse_arg('-height', argv, i, int)
			if height <= 0:
				error('Invalid argument: width must be a positive integer')
			i+=1 # eat next arg
		elif option == '-seed':
			seed = parse_arg('-seed', argv, i, float)
			# reevaluate name
			out_filename = 'mazes/%08.3f'% seed 
			i+=1 # eat next arg
		elif option == '-out':
			out_filename = parse_arg('-out', argv, i, str)
			output_to_file = True
			i+=1 # eat next arg
		elif option == '-interactive':
			interactive = True
		elif option == '-block':
			symbols.update(block_symbols)
			is_block = True
		elif option == '-color':
			symbols.update(color_symbols)
			is_color = True
		elif option == '-solve':

			interactive = True
			is_solve = True
		elif option == '-help':
			print(usage)
			sys.exit(-1)		
		else:
			error('Invalid option: ' + option )	
			
	#create the maze
	maze_obj = maze.Maze(width, height, seed, symbols)
	# activate a repl-like command interpreter to try to solve the maze 
	if interactive:
		if output_to_file:		
			error('Error: Output mode NOT compatible with interactive mode')	
		if is_solve:
			solve_maze(maze_obj)
		else:
			play_maze(maze_obj)
	else:
		# if using block symbols and printing to file print error
		if output_to_file:
			if is_color:		
				error('Error: Ansi Color mode is NOT compatible with output mode')	
			elif is_block:		
				error('Error: Unicode Block mode is NOT compatible with output mode')	
			elif is_solve:		
				error('Error: Solution is NOT compatible with output mode')
			else:
				save_maze(maze_obj, out_filename)
		else:
			if is_solve:		
				error('Error: Solution must be invoke in interactive mode')
			# print to standard output
			os.system('clear' if os.name!='nt' else 'cls')	
			print(maze_obj.to_str())

# After all definitions, start main
if __name__ == '__main__':
	main() 
