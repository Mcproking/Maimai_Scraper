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
def extractHits(FileQueue): 
    global hitTypes
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
        hitTypes = "CritAll"
        # This is for DX Charts
        if type == "DX":
            for x in range(0,5):
                taps.append(html_Tree.xpath(xpathList)[x])
            for x in range(5,10):
                hold.append(html_Tree.xpath(xpathList)[x])
            for x in range(10,15):
                slide.append(html_Tree.xpath(xpathList)[x])
            for x in range(15,20):
                touch.append(html_Tree.xpath(xpathList)[x])
            for x in range(20,25):
                breaks.append(html_Tree.xpath(xpathList)[x])
        # This is for STD Charts
        else:
            for x in range(0,5):
                taps.append(html_Tree.xpath(xpathList)[x])
            for x in range(5,10):
                hold.append(html_Tree.xpath(xpathList)[x])
            for x in range(10,15):
                slide.append(html_Tree.xpath(xpathList)[x])
            for x in range(15,20):
                touch.append(None)
            for x in range(16,21):
                breaks.append(html_Tree.xpath(xpathList)[x])
    
    # Type is for only Breaks have crits
    def BreakCritOnly(type):
        global hitTypes
        hitTypes = "BreakCritOnly"
        # This is for DX Charts
        if type == "DX":
            for x in range(1,5):
                taps.append(html_Tree.xpath(xpathList)[x])
            for x in range(6,10):
                hold.append(html_Tree.xpath(xpathList)[x])
            for x in range(11,15):
                slide.append(html_Tree.xpath(xpathList)[x])
            for x in range(16,20):
                touch.append(html_Tree.xpath(xpathList)[x])
            for x in range(16,21):
                breaks.append(html_Tree.xpath(xpathList)[x])
        # This is for Std Chart
        else:
            for x in range(1,5):
                taps.append(html_Tree.xpath(xpathList)[x])
            for x in range(6,10):
                hold.append(html_Tree.xpath(xpathList)[x])
            for x in range(11,15):
                slide.append(html_Tree.xpath(xpathList)[x])
            for x in range(16,20):
                touch.append(None)
            for x in range(16,21):
                breaks.append(html_Tree.xpath(xpathList)[x])

    # Type for all perfects
    def PerfectOnly(type):
        global hitTypes
        hitTypes = "PerfectOnly"
        # Only work when it is Dx Charts        
        if type == "DX":
            for x in range(1,5):
                taps.append(html_Tree.xpath(xpathList)[x])
            for x in range(6,10):
                hold.append(html_Tree.xpath(xpathList)[x])
            for x in range(11,15):
                slide.append(html_Tree.xpath(xpathList)[x])
            for x in range(16,20):
                touch.append(html_Tree.xpath(xpathList)[x])
            for x in range(21,25):
                breaks.append(html_Tree.xpath(xpathList)[x])
        # This is for Std Charts
        else: 
            for x in range(1,5):
                taps.append(html_Tree.xpath(xpathList)[x])
            for x in range(6,10):
                hold.append(html_Tree.xpath(xpathList)[x])
            for x in range(11,15):
                slide.append(html_Tree.xpath(xpathList)[x])
            for x in range(16,20):
                touch.append(None)
            for x in range(17,21):
                breaks.append(html_Tree.xpath(xpathList)[x])

    if len(tree) == 25:
        chart = "DX"    
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
    elif len(tree) == 21:
        chart = "STD"
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
    # print(tree)
    
    return taps, hold, slide, touch, breaks, chart, hitTypes

