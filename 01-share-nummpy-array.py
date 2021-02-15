#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygsheets
import pandas
import numpy as np

gc = pygsheets.authorize()

# Open spreadsheet and then worksheet
sh = gc.open('pygsheet-tests')
wks = sh.sheet1

# Update a cell with value (just to let him know values is updated ;) )
wks.update_value('A1', "Hello Google Sheets!")
my_nparray = np.random.randint(10, size=(3, 4))

# update the sheet with array
wks.update_values('A2', my_nparray.tolist())

# share the sheet with your friend
sh.share("pygsheets-tests@trau.co")
