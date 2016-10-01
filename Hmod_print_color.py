#!/usr/bin/env python
# -*- coding: utf-8 -*-

'This modules be used to print color text on linux terminal'

__author__ = 'Bruce He'

# format: '\033["mode";"fcolor";"bcolor"m' + 'String' + '\033[0m'
#
# fcolor			bcolor			color
# 30				40				Black
# 31				41				red
# 32				42				green
# 33				43				yellow
# 34				44				blue
# 35				45				purple
# 36				46				cyan
# 37				47				white
#
# mode 				action
# 0					default
# 1					highlight
# 4					underline
# 5					blink
# 7					reverse
# 8					invisible

def Hmod_print_color(text, fcolor='w', bcolor='B', mode=0):

	# init define
	_fcolor = {'B':30, 'r':31, 'g':32, 'y':33, 'b':34, 'p':35, 'c':36, 'w':37}
	_bcolor = {'B':40, 'r':41, 'g':42, 'y':41, 'b':44, 'p':45, 'c':46, 'w':47}
	_mode = (0, 1, 4, 5, 7, 8)
	_string = text
	_end = '\033[0m'

	if not fcolor in _fcolor or not bcolor in _bcolor or not mode in _mode:
		return '\033[1;31;47mYou input wrong value, please check again!\033[0m'

	_start = '\033[%d;%d;%dm' % (mode, _fcolor[fcolor], _bcolor[bcolor])

	return _start + _string + _end


