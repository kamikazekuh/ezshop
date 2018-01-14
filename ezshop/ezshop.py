import os
from engines.server import queue_command_string
from paths import PLUGIN_PATH
from commands.say import SayCommand
from commands.client import ClientCommand
from menus import PagedMenu
from menus import PagedOption
from players.entity import Player
from messages import SayText2
from core import SOURCE_ENGINE_BRANCH

textfile = os.path.join(PLUGIN_PATH+"/ezshop/shopoptions.txt")

def createpopup():
    options = fh.readlines(__textfile)
    popup = popuplib.easymenu("ezshop",None,ezh)
    popup.settitle("EzShop")
    for option in options:
        option = option.split("|")
        popup.addoption(option,"%sXP - $%s"%(option[0],option[1]))
		
def get_lines():
	lines = []
	with open(textfile,'r') as fo:
		lines = fo.readlines()
	lins = []
	for line in lines:
		if not line.startswith("//"):
			lins.append(line)
	return lins
		
def expshop_menu_build(menu,index):
	menu.clear()
	lines = get_lines()
	for line in lines:
		line = line.strip("\n")
		line = line.split('|')
		option = PagedOption("%s Experience - %s$" % (line[0],line[1]), line)
		menu.append(option)
		
		
def expshop_menu_select(menu,index,choice):
	player = Player(index)
	if player.cash >= int(choice.value[1]):
		player.cash -= int(choice.value[1])
		queue_command_string('wcs_givexp %s %s' % (player.userid,choice.value[0]))
		if SOURCE_ENGINE_BRANCH == 'css':
			SayText2("\x04[WCS] \x03You bought \x04%s XP \x03for \x04%s$."%(choice.value[0],choice.value[1])).send(index)
		else:
			SayText2("\x04[WCS] \x05You bought \x04%s XP \x05for \x04%s$."%(choice.value[0],choice.value[1])).send(index)
	else:
		if SOURCE_ENGINE_BRANCH == 'css':
			SayText2("\x04[WCS] \x03You don't have enough cash.").send(index)
		else:
			SayText2("\x04[WCS] \x05You don't have enough cash.").send(index)		
	

	
expshop_menu = PagedMenu(title='Experience Shop', build_callback=expshop_menu_build, select_callback=expshop_menu_select,fill=False)

@SayCommand('expshop')
def expshop(command,index,team=None):
	expshop_menu.send(index)
