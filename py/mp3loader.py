# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:38:29 2019

@author: eric
"""

import pydub

def make_louder(input_file, output_file, db):
    original=pydub.AudioSegment.from_mp3(input_file)
    original=original+10
    original.export(output_file)

