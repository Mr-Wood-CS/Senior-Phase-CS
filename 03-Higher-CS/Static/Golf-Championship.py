from collections import namedtuple

def GetGolferInfo():

    golf_file = open("Scottish Open Golf Scores.txt","r")

    GolfersInfo = []

    golfer = namedtuple('golfer','Golfer_Name, Nationality, Round1, Round2, Round3, Round4, Total_Shots')

    number_golfers = 0

    for line in golf_file:

        row_data = line.split(',')

        current_record = golfer(Golfer_Name=row_data[0], Nationality=row_data[1], Round1=int(row_data[2]), Round2=int(row_data[3]), Round3=int(row_data[4]), Round4=int(row_data[5]), Total_Shots=int(0))

        GolfersInfo.append(current_record)

        number_golfers = number_golfers + 1

    golf_file.close()

    return GolfersInfo, number_golfers


def CalculateTotalShots(GolfersInfo, number_golfers):
        
    for x in range(number_golfers):
        GolfersInfo[x] = GolfersInfo[x]._replace(Total_Shots= GolfersInfo[x].Round1 + GolfersInfo[x].Round2 + GolfersInfo[x].Round3 + GolfersInfo[x].Round4)

    return GolfersInfo
        

def TournamentScoreCalculatingDisplayed(GolfersInfo, number_golfers):
    Tournament_Scores = []

    print "Golfer \t\t\t Score"
    
    for x in range(number_golfers):

        Tournament_Scores.append(GolfersInfo[x].Total_Shots - (72*4))

        print GolfersInfo[x].Golfer_Name,"\t\t",Tournament_Scores[x]
        
    return Tournament_Scores


def QualificationNextYear(GolfersInfo, number_golfers, Tournament_Scores):
    Qualifications = []
    
    for x in range(number_golfers):
        if Tournament_Scores[x] < -5 or GolfersInfo[x].Nationality != "USA":
            Qualifications.append(bool(1))
        else:
            Qualifications.append(bool(0))

    return Qualifications


def WinningGolfer(Tournament_Scores,GolfersInfo,number_golfers):
    prize = int(2500000)

    minimum = Tournament_Scores[0]

    winner = GolfersInfo[0].Golfer_Name
    
    for x in range(number_golfers):
        if Tournament_Scores[x] < minimum:
            minimum = Tournament_Scores[x]
            winner = GolfersInfo[x].Golfer_Name

    print
    print "The winning golfer of the Scottish Open Championship is",winner,"with a score of",minimum,"winning","£{:.2f}".format(prize)
    print
    
    return


def DisplayQualificationList(GolfersInfo,number_golfers,Tournament_Scores):
    print "Scottish Open Golf Championship - Next Year's Qualification"
    print
    
    for x in range(number_golfers):
        if Qualifications[x]:
            print GolfersInfo[x].Golfer_Name,"\t",GolfersInfo[x].Nationality,"\t",Tournament_Scores[x]

    return  

GolfersInfo, number_golfers = GetGolferInfo()
GolfersInfo = CalculateTotalShots(GolfersInfo, number_golfers)
Tournament_Scores = TournamentScoreCalculatingDisplayed(GolfersInfo, number_golfers)
Qualifications = QualificationNextYear(GolfersInfo, number_golfers, Tournament_Scores)
WinningGolfer(Tournament_Scores,GolfersInfo,number_golfers)
DisplayQualificationList(GolfersInfo,number_golfers,Tournament_Scores)
