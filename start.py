import extractHits as EH
import extractPlays as EP
import json
from WebExtracter import main



def writeintoJSON(total_files):

    Final_Plays_ListDict = []

    sampleFinal_Plays = {"TimeStamp":"",
                        "SongName":"",
                        "Difficulty":"",
                        "Chart":"",
                        "Achivement":"",
                        "Deluxe":"",
                        "FullCombo":"",
                        "FullSync":"",

                        "Fast":"",
                        "Late":"",

                        "Types":"",

                        "Tap":"",
                        "Hold":"",
                        "Slide":"",
                        "Touch":"",
                        "Break":"" }

    for x in range(1,total_files+1):
        final_dict = sampleFinal_Plays.copy()
        
        Chart = EP.checkSongChart(x)
        hits = EH.extractHits(x,Chart) 
        Difficulty = EP.checkDiff(x)
        SongName = EP.checkSongName(x)
        Achivement = EP.songAchivement(x)
        Deluxe = EP.songDxScore(x)
        FcOrFs = EP.FullComboandFullSync(x)
        TimeStamp = EP.extractTime(x)
        delay = EH.extractFastLate(x)    
        
        final_dict["Chart"] = Chart
        final_dict["TimeStamp"] = TimeStamp
        final_dict["SongName"] = SongName
        final_dict["Difficulty"] = Difficulty
        final_dict["Achivement"] = Achivement
        final_dict["Deluxe"] = Deluxe
        final_dict["FullCombo"] = FcOrFs[0]
        final_dict["FullSync"] = FcOrFs[1]
        final_dict["Fast"] = delay[0]
        final_dict["Late"] = delay[1]   
        final_dict["Types"] = hits[5]   
        final_dict["Tap"] = hits[0]
        final_dict["Hold"] = hits[1]
        final_dict["Slide"] = hits[2]
        final_dict["Touch"] = hits[3]
        final_dict["Break"] = hits[4]   
        

        Final_Plays_ListDict.append(final_dict)
        # print("{} - {}: {} - {} - {} - {} - {} - {} - {} - F:{} L:{} - CHART: {} | Type: {} > T:{} - H:{} - S:{} - t:{} - B:{}".format(x ,TimeStamp ,SongName ,Difficulty ,Chart ,Achivement ,Deluxe, FcOrFs[0], FcOrFs[1], delay[0],delay[1],hits[5],hits[6],hits[0],hits[1],hits[2],hits[3],hits[4]))


    for playlist in Final_Plays_ListDict:
        dump = json.dumps(playlist,indent=4,ensure_ascii=True)
        with open(r"jsonFile.json","a") as f:
            f.write(dump)
        
if __name__ == "__main__":
    main()
    total_file = int(EH.calcFiles()/2)
    writeintoJSON(total_file)
    
        
