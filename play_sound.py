#!/usr/bin/env python
# encoding: utf-8
"""
play_sound.py

Created by ranji on 2012-09-26.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import pygame

def main():
	pygame.init()
	pygame.mixer.init()
	play_good()
	play_bad()

def play_bad():	
	paths = []
	paths.append('sounds/pacman_dies_y.ogg')
	paths.append('sounds/break_x.ogg')
	play_sounds(paths)

def play_good():
	paths = []
	paths.append('sounds/mission_succ.ogg')
	paths.append('sounds/objective_comp.ogg')
	paths.append('sounds/good_bad_ugly.ogg')
	play_sounds(paths)
	
def play_sounds(paths):
	for path in paths:
		play_sound(path)
	
def play_sound(path):
	sounda = pygame.mixer.Sound(path)
	channela = sounda.play()
	while channela.get_busy():
		pygame.time.delay(100)

if __name__ == '__main__':
	main()

