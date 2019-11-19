#!/usr/bin/env python3
# 
# slotmachine_oneline.py
# Copyright (C) 2019  Miguel de Dios Matias
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import dice

line = '{preContent}{face}{postContent}'

def roll(pl, diceCombination='d6', preContent='', postContent='🎲', facesDice=None, critical=None, fumble=None, *args, **kwarg):
    """
        Return a segment with the result of roll a dice combination.
        Args:
            pl (object): The powerline logger. 
            diceCombination (string): The combination of dices in dice notation format see
                https://github.com/borntyping/python-dice
            preContent (string): The string to show before the result.
            postContent (string): The string to show after the result.
            facesDice list(string) or None: The faces of dice as list of string (can be emojis). 
            critical int or list(int) or None: The minimum or exact values to critical hit, the background
                change to critical success. 
            fumble int or list(int) or None: The maximum or exact values to critical fumble, the background
                change to critical failture. 
        Returns:
            segment (list(dict)): The result of roll as powerline segment.
    """
    result = int(dice.roll(diceCombination))
    
    try:
        face = facesDice[result - 1] # The list start with 0
    except (IndexError, TypeError):
        face = result
    
    color = ['information:regular']
    if isinstance(critical, int):
        if result >= critical:
            color = ['critical:success']
    elif isinstance(critical, list):
        if result in critical:
            color = ['critical:success']
    if isinstance(fumble, int):
        if result <= fumble:
            color = ['critical:failure']
    elif isinstance(fumble, list):
        if result in fumble:
            color = ['critical:failure']
    
    return [{
        'contents': line.format(preContent=preContent, face=face, postContent=postContent),
        'highlight_groups': color,
        'divider_highlight_group': None}]    