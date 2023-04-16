from bs4 import BeautifulSoup as BS
from lxml import etree as ET
import os
import re as re


# Calculate the files inside the html folder
def calcFiles():
    count = 0
    dir_path = r"./Html_Extracted/"
    for path in os.scandir(dir_path):
            if path.is_file():
                count +=1
    # print("File Count:", count)
    return count
total_files = int(calcFiles()/2)

# open the HTML files as xml files
def openFileXML(Queue):
    with open(r"./Html_Extracted/{}.txt".format(Queue),"r",encoding="utf-8") as f:
        file = BS(f, features="lxml")
    return file

# Extract the time from the parsed html file
def extractTime(FileQueue):
    html_File = openFileXML(FileQueue)
    html_Tree = ET.XML(str(html_File))
    xpathList = './/span[@class="v_b"]/text()'
    time = html_Tree.xpath(xpathList)[0]

    return time

# Check the diff of the parsed html file
def checkDiff(FileQueue):
    html_File = openFileXML(FileQueue)
    html_tree = ET.XML(str(html_File))
    xpathList = '//img[@class="playlog_diff v_b"]/@src'
    diff_Html = html_tree.xpath(xpathList)
    rExpression = "diff_remaster|diff_master|diff_expert|diff_advance|diff_basic"
    
    try:
        diff = re.findall(rExpression, diff_Html[0])[0] # from list put into string
    except IndexError: # If the file has incorrectly made, this will stop the entire program
        print("HTML FILE IS NOT CORRECT")
        exit()
    
    if diff == "diff_remaster":
        diff = "Re:Master"
    elif diff == "diff_master":
        diff = "Master"
    elif diff == "diff_expert":
        diff = "Expert"
    elif diff == "diff_advance":
        diff = "Advance"
    elif diff == "diff_basic":
        diff = "Basic"
    return diff

# Check the song name from the Parsed HTML file    
def checkSongName(FileQueue):
    html_File = openFileXML(FileQueue)
    html_Tree = ET.XML(str(html_File))
    xpathList = './/div[@class="basic_block m_5 p_5 p_l_10 f_13 break"]/text()'
    song_Html = html_Tree.xpath(xpathList)[0]
    return song_Html

# Check the song Chart from the Parsed HTML file
def checkSongChart(FileQueue):
    html_File = openFileXML(FileQueue)
    html_Tree = ET.XML(str(html_File))
    xpathList = './/div[@class="p_r f_0"]/img/@src'
    chart_Html = html_Tree.xpath(xpathList)[1]
    rExpression = "music_standard|music_dx"
    
    try:
        diff = re.findall(rExpression, chart_Html)[0] # from list put into string
    except IndexError: # If the file has incorrectly made, this will stop the entire program
        print("HTML FILE IS NOT CORRECT")
        exit()

    if diff == "music_standard":
        diff = "Standard"
    elif diff == "music_dx":
        diff = "Deluxe"
        
    return diff

# Get the Achivment score from the parsed HTML file 
def songAchivement(FileQueue):
    html_File = openFileXML(FileQueue)
    html_Tree = ET.XML(str(html_File))
    xpathList = './/div[@class="playlog_achievement_txt t_r"]/text()'
    achivment_Html = html_Tree.xpath(xpathList)[0]
    total_Achivment = str(achivment_Html)
    xpathList = './/div[@class="playlog_achievement_txt t_r"]/span[@class="f_20"]/text()'
    decimalPointAchivment = html_Tree.xpath(xpathList)[0]
    total_Achivment = total_Achivment + str(decimalPointAchivment)
    return total_Achivment

# Get the dx score from the parsed HTML file
def songDxScore(FileQueue):
    html_File = openFileXML(FileQueue)
    html_Tree = ET.XML(str(html_File))
    xpathList = './/div[@class="white p_r_5 f_15 f_r"]/text()'
    dx_Html = html_Tree.xpath(xpathList)[0]
    return dx_Html

# Get the Full combo and full sync from the parsed HTML file
def FullComboandFullSync(FileQueue):
    html_File = openFileXML(FileQueue)
    html_Tree = ET.XML(str(html_File))
    xpathList = './/img[@class="h_35 m_5 f_l"]/@src'
    rawFC = html_Tree.xpath(xpathList)[0]
    rawFS = html_Tree.xpath(xpathList)[1]
    
    FullCombo_rExpression = "applus|ap|fcplus|fc"
    FullSync_rExpression = "fsdplus|fsd|fsplus|fs"
    
    try:
        temp = re.findall(FullCombo_rExpression, rawFC)[0] # from list put into string
    except IndexError: # If the file has incorrectly made, this will stop the entire program
        print("HTML FILE IS NOT CORRECT")
        exit()
   
    try:
        temp = re.findall(FullSync_rExpression, rawFS)[0] # from list put into string
    except IndexError: # If the file has incorrectly made, this will stop the entire program
        print("HTML FILE IS NOT CORRECT")
        exit()
    
    AP_rExpression = "applus|ap"
    rawAP = re.findall(AP_rExpression,rawFC) # Check if the line consist of applus or ap
    while True:
        if rawAP != None:
            # AP does not exsit
            try:
                if re.findall("f.*y", rawFC)[0] == "fc_dummy":
                    fc = None
                    # print(fc)
                    break
            except:
                pass
            try:
                if re.findall("f.*s",rawFC)[0] == "fcplus":
                    fc = re.findall("f.*s",rawFC)[0]
                    # print(fc)
                    break
            except:
                pass
            try:
                if re.findall("fc",rawFC)[0] == "fc":
                    fc = re.findall("fc",rawFC)[0]
                    # print(fc)
                    break
            except:
                pass
        else:
            # AP does exsit
            try:
                if re.findall("a.*s",rawFC)[0] == "applus":
                    fc = re.findall("a.*s")[0]
                    # print(fc)
                    break
            except:
                pass
            try:
                if re.findall("ap",rawFC)[0] == "ap":
                    fc = re.findall("ap")[0]
                    # print(fc)
                    break
            except:
                pass
    
    FSDPlus_rExpression = "fsd.*s|fs.*d"
    rawFSD = re.findall(FSDPlus_rExpression, rawFS) # Check line got fsdplus or fsd
    while True:
        if rawFSD != None:
            # print("FSD NO")
            # FSD does not exsit
            try:
                if re.findall("f.*y", rawFS)[0] == "fs_dummy":
                    fs = None
                    # print(fs)
                    break
            except:
                pass
            try:
                if re.findall("fs.*s",rawFS)[0] == "fsplus":
                    fs = re.findall("fs.*s",rawFS)[0]
                    # print(fs)
                    break
            except:
                pass
            try:
                if re.findall("fs",rawFS)[0] == "fs":
                    fs = re.findall("fs",rawFS)[0]
                    # print(fs)
                    break
            except:
                pass
        else:
            # print("FSD YES")
            # FSD does exsit
            try:
                if re.findall("fsd.*s",rawFS)[0] == "fsdplus":
                    fs = re.findall("fsd.*s")[0]
                    # print(fs)
                    break
            except:
                pass
            try:
                if re.findall("fs.*d",rawFS)[0] == "fsd":
                    fs = re.findall("fs.*d",rawFS)[0]
                    # print(fs)
                    break
            except:
                pass

    return fc,fs


