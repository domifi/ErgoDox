#!/usr/bin/env python3

from kikit.panelize import *
import sys


def gcd(a, b):
    while(b): 
       a, b = b, a % b
    return a

def shorten_vec2(vec2):
    c = gcd(vec2[0], vec2[1])
    return [vec2[0] / c, vec2[1] / c]

def axis_tab(originMM, direction, width, maxHeight=fromMm(50)):
    edges = []
    tabs = []
    direction = shorten_vec2(direction)
    otherDirection = [direction[0] * (-1), direction[1] * (-1)]
    tab1, edge1 = panel.boardSubstrate.tab(wxPointMM(originMM[0], originMM[1]), direction, width, maxHeight)
    tab, edge = panel.boardSubstrate.tab(wxPointMM(originMM[0] - otherDirection[0], originMM[1] - otherDirection[1]), otherDirection, width, maxHeight)
    edges.append(edge)
    tabs.append(tab)
    edges.append(edge1)
    tabs.append(tab1)

    return tabs, edges


### main ###


file_in = "ErgoDOX.kicad_pcb"
file_out = "panel_" + file_in

panel = Panel()
size, cuts = panel.makeGrid(file_in, 1, 1,
                                    wxPointMM(200, 175),
                                    tolerance=fromMm(5),
                                    rotation=(180) * 10)

panel.appendBoard(file_in, wxPointMM(256, 96), tolerance=fromMm(5))

width = fromMm(8)
tabs = []

# top
tab, cut = axis_tab([200, 35], [1,0], width)
cuts.extend(cut)
tabs.extend(tab)

# bottom
tab, cut = axis_tab([170, 160.528], [1,0], width)
cuts.extend(cut)
tabs.extend(tab)

#middle
tab, cut = axis_tab([185, 96], [1,0], width)
cuts.extend(cut)
tabs.extend(tab)


# append all tabs and make all cuts
panel.appendSubstrate(tabs)
panel.makeMouseBites(cuts, diameter=fromMm(0.5), spacing=fromMm(1))

panel.save(file_out)
exit(0)



