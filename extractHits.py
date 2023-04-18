from bs4 import BeautifulSoup as BS
from lxml import etree as ET
import re as re
from extractPlays import calcFiles

total_file = int(calcFiles()/2)

def openFileXML(Queue):
    with open(r"./Html_Extracted/{}.1.txt".format(Queue),"r",encoding="utf-8") as f:
        file = BS(f, features="lxml")
    return file

def extractFastLate(FileQueue):
    html_File = openFileXML(FileQueue)
    html_Tree = ET.XML(str(html_File))

    xpathList = './/div[@class="w_96 f_l t_r"]/div[@class="p_t_5"]/text()'
    fastlate = html_Tree.xpath(xpathList)
    fast = fastlate[0]
    late = fastlate[1]
    return fast, late

# Might no need this at all, need to find other ppl with different types
def extractHits(FileQueue, ChartType): 
    global hitTypes, chart
    html_File = openFileXML(FileQueue)
    html_Tree = ET.XML(str(html_File))
    
    xpathList = './/table[@class="playlog_notes_detail t_r f_l f_11 f_b"]//td//text()'

    tree = html_Tree.xpath(xpathList)
    hitTypes = ""
    taps = []
    hold = []
    slide = []
    touch = []
    breaks = []
    
    # Type is for all crits, May works or not FUCKING GOD
    def Critall(type):
        global hitTypes
        reduce = 0
        hitTypes = "CritAll"
        # This is for DX Charts
        if type == "Deluxe":
            for x in range(0 - reduce,5 - reduce):
                if tree[0] == "　":
                    reduce = 4
                    taps.append(None)
                else:
                    taps.append(tree[x])

            for x in range(5 - reduce,10 - reduce):      
                if tree[5 - reduce] == "　":
                    count = 0
                    while reduce == 4:
                        if count == 5:
                            break
                        hold.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 5:
                                break
                            hold.append(None)
                            count +=1
                        reduce = 4
                    else:
                        reduce = 8
                    break
                else:
                    hold.append(tree[x])

            for x in range(10 - reduce,15 - reduce):
                if tree[10- reduce] == "　":
                    count = 0
                    while reduce == 8:
                        if count == 5:
                            break
                        slide.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 5:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 5:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 8
                    else:
                        reduce = 12
                    break

                else:
                    slide.append(tree[x])

            for x in range(15 - reduce, 20 - reduce):
                if tree[15-reduce] == "　":
                    count = 0
                    while reduce == 12:
                        if count == 5:
                            break
                        touch.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 5:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 5:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 5:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 12
                    else:
                        reduce = 16
                    break
                else:
                    touch.append(tree[x])

                
            for x in range(20 - reduce,25 - reduce):
                if tree[20 - reduce] == "　":
                    count = 0
                    while reduce == 16:
                        if count == 5:
                            break
                        breaks.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 5:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 5:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 5:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 12
                    elif reduce == 16:
                        while reduce == 16:
                            if count == 5:
                                break
                            breaks.append(None)
                            count += 1
                        reduce = 16
                    else:
                        reduce = 20
                    break
                else:
                    breaks.append(tree[x])
        # This is for STD Charts
        else:
            for x in range(0 - reduce,5 - reduce):
                if tree[0] == "　":
                    reduce = 4
                    taps.append(None)
                else:
                    taps.append(tree[x])

            for x in range(5 - reduce,10 - reduce):      
                if tree[5 - reduce] == "　":
                    count = 0
                    while reduce == 4:
                        if count == 5:
                            break
                        hold.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 5:
                                break
                            hold.append(None)
                            count +=1
                        reduce = 4
                    else:
                        reduce = 8
                    break
                else:
                    hold.append(tree[x])

            for x in range(10 - reduce,15 - reduce):
                if tree[10- reduce] == "　":
                    count = 0
                    while reduce == 8:
                        if count == 5:
                            break
                        slide.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 5:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 5:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 8
                    else:
                        reduce = 12
                    break

                else:
                    slide.append(tree[x])

            for x in range(15 - reduce, 20 - reduce):
                if tree[15-reduce] == "　":
                    count = 0
                    while reduce == 12:
                        if count == 5:
                            break
                        touch.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 5:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 5:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 5:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 12
                    else:
                        reduce = 16
                    break
                else:
                    touch.append(None)
                    if len(touch) == 5:
                        reduce = 4
                
            for x in range(20 - reduce,25 - reduce):
                if tree[20 - reduce] == "　":
                    count = 0
                    while reduce == 16:
                        if count == 5:
                            break
                        breaks.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 5:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 5:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 5:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 12
                    elif reduce == 16:
                        while reduce == 16:
                            if count == 5:
                                break
                            breaks.append(None)
                            count += 1
                        reduce = 16
                    else:
                        reduce = 20
                    break
                else:
                    breaks.append(tree[x])    
    
    # Type is for only Breaks have crits
    def BreakCritOnly(type):
        global hitTypes
        hitTypes = "BreakCritOnly"
        # This is for DX Charts
        if type == "Deluxe":
            for x in range(1 - reduce,5 - reduce):
                if tree[1] == "　":
                    reduce = 4
                    taps.append(None)
                else:
                    taps.append(tree[x])

            for x in range(6 - reduce,10 - reduce):      
                if tree[6 - reduce] == "　":
                    count = 0
                    while reduce == 4:
                        if count == 4:
                            break
                        hold.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            hold.append(None)
                            count +=1
                        reduce = 4
                    else:
                        reduce = 8
                    break
                else:
                    hold.append(tree[x])

            for x in range(11 - reduce,15 - reduce):
                if tree[11- reduce] == "　":
                    count = 0
                    while reduce == 8:
                        if count == 4:
                            break
                        slide.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 8
                    else:
                        reduce = 12
                    break

                else:
                    slide.append(tree[x])

            for x in range(16 - reduce, 20 - reduce):
                if tree[15-reduce] == "　":
                    count = 0
                    while reduce == 12:
                        if count == 4:
                            break
                        touch.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 12
                    else:
                        reduce = 16
                    break
                else:
                    touch.append(tree[x])

                
            for x in range(20 - reduce,25 - reduce):
                if tree[20 - reduce] == "　":
                    count = 0
                    while reduce == 16:
                        if count == 4:
                            break
                        breaks.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 12
                    elif reduce == 16:
                        while reduce == 16:
                            if count == 5:
                                break
                            breaks.append(None)
                            count += 1
                        reduce = 16
                    else:
                        reduce = 20
                    break
                else:
                    breaks.append(tree[x])
                    
        # This is for Std Chart
        else:
            for x in range(1 - reduce,5 - reduce):
                if tree[1] == "　":
                    reduce = 4
                    taps.append(None)
                else:
                    taps.append(tree[x])

            for x in range(6 - reduce,10 - reduce):      
                if tree[6 - reduce] == "　":
                    count = 0
                    while reduce == 4:
                        if count == 4:
                            break
                        hold.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            hold.append(None)
                            count +=1
                        reduce = 4
                    else:
                        reduce = 8
                    break
                else:
                    hold.append(tree[x])

            for x in range(11 - reduce,15 - reduce):
                if tree[11- reduce] == "　":
                    count = 0
                    while reduce == 8:
                        if count == 4:
                            break
                        slide.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 8
                    else:
                        reduce = 12
                    break

                else:
                    slide.append(tree[x])

            for x in range(16- reduce, 20 - reduce):
                if tree[15-reduce] == "　":
                    count = 0
                    while reduce == 12:
                        if count == 4:
                            break
                        touch.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 12
                    else:
                        reduce = 16
                    break
                else:
                    touch.append(None)
                    if len(touch) == 4:
                        reduce = 4
                
            for x in range(20 - reduce,25 - reduce):
                if tree[20 - reduce] == "　":
                    count = 0
                    while reduce == 16:
                        if count == 4:
                            break
                        breaks.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 12
                    elif reduce == 16:
                        while reduce == 16:
                            if count == 4:
                                break
                            breaks.append(None)
                            count += 1
                        reduce = 16
                    else:
                        reduce = 20
                    break
                else:
                    breaks.append(tree[x])

    # Type for all perfects
    def PerfectOnly(type):
        global hitTypes
        hitTypes = "PerfectOnly"
        # Only work when it is Dx Charts        
        if type == "Deluxe":
            for x in range(1 - reduce,5 - reduce):
                if tree[1] == "　":
                    reduce = 4
                    taps.append(None)
                else:
                    taps.append(tree[x])

            for x in range(6 - reduce,10 - reduce):      
                if tree[6 - reduce] == "　":
                    count = 0
                    while reduce == 4:
                        if count == 4:
                            break
                        hold.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            hold.append(None)
                            count +=1
                        reduce = 4
                    else:
                        reduce = 8
                    break
                else:
                    hold.append(tree[x])

            for x in range(11 - reduce,15 - reduce):
                if tree[11- reduce] == "　":
                    count = 0
                    while reduce == 8:
                        if count == 4:
                            break
                        slide.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 8
                    else:
                        reduce = 12
                    break

                else:
                    slide.append(tree[x])

            for x in range(16 - reduce, 20 - reduce):
                if tree[16-reduce] == "　":
                    count = 0
                    while reduce == 12:
                        if count == 4:
                            break
                        touch.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 12
                    else:
                        reduce = 16
                    break
                else:
                    touch.append(tree[x])

                
            for x in range(20 - reduce,25 - reduce):
                if tree[20 - reduce] == "　":
                    count = 0
                    while reduce == 16:
                        if count == 4:
                            break
                        breaks.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 12
                    elif reduce == 16:
                        while reduce == 16:
                            if count == 4:
                                break
                            breaks.append(None)
                            count += 1
                        reduce = 16
                    else:
                        reduce = 20
                    break
                else:
                    breaks.append(tree[x])

        # This is for Std Charts
        else: 
            for x in range(1 - reduce,5 - reduce):
                if tree[1] == "　":
                    reduce = 4
                    taps.append(None)
                else:
                    taps.append(tree[x])

            for x in range(6 - reduce,10 - reduce):      
                if tree[6 - reduce] == "　":
                    count = 0
                    while reduce == 4:
                        if count == 4:
                            break
                        hold.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            hold.append(None)
                            count +=1
                        reduce = 4
                    else:
                        reduce = 8
                    break
                else:
                    hold.append(tree[x])

            for x in range(11 - reduce,15 - reduce):
                if tree[11- reduce] == "　":
                    count = 0
                    while reduce == 8:
                        if count == 4:
                            break
                        slide.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            slide.append(None)
                            count +=1
                        reduce = 8
                    else:
                        reduce = 12
                    break

                else:
                    slide.append(tree[x])

            for x in range(16 - reduce, 20 - reduce):
                if tree[16-reduce] == "　":
                    count = 0
                    while reduce == 12:
                        if count == 4:
                            break
                        touch.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 4:
                                break
                            touch.append(None)
                            count +=1
                        reduce = 12
                    else:
                        reduce = 16
                    break
                else:
                    touch.append(None)
                    if len(touch) == 4:
                        reduce = 4

                
            for x in range(20 - reduce,25 - reduce):
                if tree[20 - reduce] == "　":
                    count = 0
                    while reduce == 16:
                        if count == 4:
                            break
                        breaks.append(None)
                        count += 1
                    if reduce == 0:
                        while reduce == 0:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 4
                    elif reduce == 4:
                        while reduce == 4:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 8
                    elif reduce == 8:
                        while reduce == 8:
                            if count == 4:
                                break
                            breaks.append(None)
                            count +=1
                        reduce = 12
                    elif reduce == 16:
                        while reduce == 16:
                            if count == 4:
                                break
                            breaks.append(None)
                            count += 1
                        reduce = 16
                    else:
                        reduce = 20
                    break
                else:
                    breaks.append(tree[x])


    if ChartType == "Standard":
        chart = "Standard"
        # print(chart)
        if (tree[0] == "　") and (tree[5] == "　") and (tree[10] == "　") and (tree[15] == "　") and (tree[16] == "　"):
            PerfectOnly(chart)
            # print("Perfect only")
        elif (tree[0] == "　") and (tree[5] == "　") and (tree[10] == "　") and (tree[15] == "　") and (tree[16] != "　"):
            BreakCritOnly(chart)
            # print("Crit Break")
        else:
            Critall(chart)
            # print("All Crit")
    elif ChartType == "Deluxe":
        chart = "Deluxe"    
        # print(chart)
        if (tree[0] == "　") and (tree[5] == "　") and (tree[10] == "　") and (tree[15] == "　") and (tree[20] == "　"):
            PerfectOnly(chart)
            # print("Perfect only")
        elif (tree[0] == "　") and (tree[5] == "　") and (tree[10] == "　") and (tree[15] == "　") and (tree[20] != "　"):
            BreakCritOnly(chart)
            # print("Crit Break")
        else:
            Critall(chart)
            # print("All Crit")
    else:
        raise "Chart Does Not Exsit"

    
    return taps, hold, slide, touch, breaks, hitTypes

