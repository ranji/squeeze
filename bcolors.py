#!/usr/bin/env python
# encoding: utf-8
"""
colors.py

Created by ranji on 2012-09-26.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
