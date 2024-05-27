import html


def main():
    print("""
    |-----------------------------------------|
    |      Automatic Seat Allocation          |
    |-----------------------------------------|
    """)

def method1():
    #print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
    para = []
    output=[]
    subn=input("Enter the Subject Name : ")
    start=int(input("Enter the starting no : "))
    end=int(input("last No of Students : "))
    ignore=int(input("Enter the Missing No : "))
    while start<=end:
        para.append(start)
        start+=1
    
    for i in para:
        if i==ignore:
            continue
        output.append(i)
    print(""" 
    Hall Bench Details:
    ----------------------------
    Row x Column bench :                                                
    01.5x4 benches     |   05.9x4  benches   |     07.5x5 benches      |   11.9x5 benches
    02.6x4 benches     |   06.10x4  benches  |     08.6x5 benches      |   12.10x5 benches
    03.7x4 benches     |                     |     09.7x5 benches      |   
    04.8x4 benches     |                     |     10.8x5 benches      |   """)
    rc=int(input("Select the Bench arangment : "))

    # 5x4 benches////////////
    if rc==1:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],output[5],output[10],output[11],output[16],output[21],output[26],output[31])
        print(output[1],output[6],output[11],output[12],output[17],output[22],output[27],output[32])
        print(output[2],output[7],output[12],output[13],output[18],output[23],output[28],output[33])
        print(output[3],output[8],output[13],output[14],output[19],output[24],output[29],output[34])
        print(output[4],output[9],output[14],output[15],output[20],output[25],output[30],output[35])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],output[5],output[10],output[11],output[16],output[21],output[26],output[31],file=f)
                print(output[1],output[6],output[11],output[12],output[17],output[22],output[27],output[32],file=f)
                print(output[2],output[7],output[12],output[13],output[18],output[23],output[28],output[33],file=f)
                print(output[3],output[8],output[13],output[14],output[19],output[24],output[29],output[34],file=f)
                print(output[4],output[9],output[14],output[15],output[20],output[25],output[30],output[35],file=f)
            print("Download Successfully")
        else:
            print("Successfully Create a room")
  
    # 6x4 benches////////////
    elif rc==2:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],output[6],output[12],output[18],output[24],output[30],output[36],output[42])
        print(output[1],output[7],output[13],output[19],output[25],output[31],output[37],output[43])
        print(output[2],output[8],output[14],output[20],output[26],output[32],output[38],output[44])
        print(output[3],output[9],output[15],output[21],output[27],output[33],output[39],output[45])
        print(output[4],output[10],output[16],output[22],output[28],output[34],output[40],output[46])
        print(output[5],output[11],output[17],output[23],output[29],output[35],output[41],output[47])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],output[6],output[12],output[18],output[24],output[30],output[36],output[42],file=f)
                print(output[1],output[7],output[13],output[19],output[25],output[31],output[37],output[43],file=f)
                print(output[2],output[8],output[14],output[20],output[26],output[32],output[38],output[44],file=f)
                print(output[3],output[9],output[15],output[21],output[27],output[33],output[39],output[45],file=f)
                print(output[4],output[10],output[16],output[22],output[28],output[34],output[40],output[46],file=f)
                print(output[5],output[11],output[17],output[23],output[29],output[35],output[41],output[47],file=f)
            print("Download Successfully")
        else:
            print("Successfully Create a room")

    # 7x4 benches////////////
    elif rc==3:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],output[7],output[14],output[21],output[28],output[35],output[42],output[49])
        print(output[1],output[8],output[15],output[22],output[29],output[36],output[43],output[50])
        print(output[2],output[9],output[16],output[23],output[30],output[37],output[44],output[51])
        print(output[3],output[10],output[17],output[24],output[31],output[38],output[45],output[52])
        print(output[4],output[11],output[18],output[25],output[32],output[39],output[46],output[53])
        print(output[5],output[12],output[19],output[26],output[33],output[40],output[47],output[54])
        print(output[6],output[13],output[20],output[27],output[34],output[41],output[48],output[55]) 
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:   
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],output[7],output[14],output[21],output[28],output[35],output[42],output[49],file=f)
                print(output[1],output[8],output[15],output[22],output[29],output[36],output[43],output[50],file=f)
                print(output[2],output[9],output[16],output[23],output[30],output[37],output[44],output[51],file=f)
                print(output[3],output[10],output[17],output[24],output[31],output[38],output[45],output[52],file=f)
                print(output[4],output[11],output[18],output[25],output[32],output[39],output[46],output[53],file=f)
                print(output[5],output[12],output[19],output[26],output[33],output[40],output[47],output[54],file=f)
                print(output[6],output[13],output[20],output[27],output[34],output[41],output[48],output[55],file=f)   
            print("Download Successfully")
        else:
            print("Successfully Create a room")  

    #8x4 benches////////////////
    elif rc==4:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],output[8],output[16],output[24],output[32],output[40],output[48],output[56])
        print(output[1],output[9],output[17],output[25],output[33],output[41],output[49],output[57])
        print(output[2],output[10],output[18],output[26],output[34],output[42],output[50],output[58])
        print(output[3],output[11],output[19],output[27],output[35],output[43],output[51],output[59])
        print(output[4],output[12],output[20],output[28],output[36],output[44],output[52],output[60])
        print(output[5],output[13],output[21],output[29],output[37],output[45],output[53],output[61]) 
        print(output[6],output[14],output[22],output[30],output[38],output[46],output[54],output[62])
        print(output[7],output[15],output[23],output[31],output[39],output[47],output[55],output[63])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:   
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],output[8],output[16],output[24],output[32],output[40],output[48],output[56],file=f)
                print(output[1],output[9],output[17],output[25],output[33],output[41],output[49],output[57],file=f)
                print(output[2],output[10],output[18],output[26],output[34],output[42],output[50],output[58],file=f)
                print(output[3],output[11],output[19],output[27],output[35],output[43],output[51],output[59],file=f)
                print(output[4],output[12],output[20],output[28],output[36],output[44],output[52],output[60],file=f)
                print(output[5],output[13],output[21],output[29],output[37],output[45],output[53],output[61],file=f) 
                print(output[6],output[14],output[22],output[30],output[38],output[46],output[54],output[62],file=f)
                print(output[7],output[15],output[23],output[31],output[39],output[47],output[55],output[63],file=f)
                print("Download Successfully")
        else:
            print("Successfully Create a room")

    #9x4 benches///////////////
    elif rc==5:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],output[9],output[18],output[27],output[36],output[45],output[54],output[63])
        print(output[1],output[10],output[19],output[28],output[37],output[46],output[55],output[64])
        print(output[2],output[11],output[20],output[29],output[38],output[47],output[56],output[65])
        print(output[3],output[12],output[21],output[30],output[39],output[48],output[57],output[66])
        print(output[4],output[13],output[22],output[31],output[40],output[49],output[58],output[67])
        print(output[5],output[14],output[23],output[32],output[41],output[50],output[59],output[68]) 
        print(output[6],output[15],output[24],output[33],output[42],output[51],output[60],output[69])
        print(output[7],output[16],output[25],output[34],output[43],output[52],output[61],output[70])
        print(output[8],output[17],output[26],output[35],output[44],output[53],output[62],output[71])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],output[9],output[18],output[27],output[36],output[45],output[54],output[63],file=f)
                print(output[1],output[10],output[19],output[28],output[37],output[46],output[55],output[64],file=f)
                print(output[2],output[11],output[20],output[29],output[38],output[47],output[56],output[65],file=f)
                print(output[3],output[12],output[21],output[30],output[39],output[48],output[57],output[66],file=f)
                print(output[4],output[13],output[22],output[31],output[40],output[49],output[58],output[67],file=f)
                print(output[5],output[14],output[23],output[32],output[41],output[50],output[59],output[68],file=f) 
                print(output[6],output[15],output[24],output[33],output[42],output[51],output[60],output[69],file=f)
                print(output[7],output[16],output[25],output[34],output[43],output[52],output[61],output[70],file=f)
                print(output[8],output[17],output[26],output[35],output[44],output[53],output[62],output[71],file=f)
                  
            print("Download Successfully")
        else:
            print("Successfully Create a room")

    #10x4 benches ///////////////
    elif rc==6:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],output[10],output[20],output[30],output[40],output[50],output[60],output[71])
        print(output[1],output[11],output[21],output[31],output[41],output[51],output[61],output[72])
        print(output[2],output[12],output[22],output[32],output[42],output[52],output[62],output[73])
        print(output[3],output[13],output[23],output[33],output[43],output[53],output[63],output[74])
        print(output[4],output[14],output[24],output[34],output[44],output[54],output[64],output[75])
        print(output[5],output[15],output[25],output[35],output[45],output[55],output[65],output[76]) 
        print(output[6],output[16],output[26],output[36],output[46],output[56],output[66],output[77])
        print(output[7],output[17],output[27],output[37],output[47],output[57],output[67],output[78])
        print(output[8],output[18],output[28],output[38],output[48],output[58],output[68],output[79])
        print(output[9],output[19],output[29],output[39],output[49],output[59],output[69],output[80])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],output[10],output[20],output[30],output[40],output[50],output[60],output[71],file=f)
                print(output[1],output[11],output[21],output[31],output[41],output[51],output[61],output[72],file=f)
                print(output[2],output[12],output[22],output[32],output[42],output[52],output[62],output[73],file=f)
                print(output[3],output[13],output[23],output[33],output[43],output[53],output[63],output[74],file=f)
                print(output[4],output[14],output[24],output[34],output[44],output[54],output[64],output[75],file=f)
                print(output[5],output[15],output[25],output[35],output[45],output[55],output[65],output[76],file=f) 
                print(output[6],output[16],output[26],output[36],output[46],output[56],output[66],output[77],file=f)
                print(output[7],output[17],output[27],output[37],output[47],output[57],output[67],output[78],file=f)
                print(output[8],output[18],output[28],output[38],output[48],output[58],output[68],output[79],file=f)
                print(output[9],output[19],output[29],output[39],output[49],output[59],output[69],output[80],file=f)
                  
            print("Download Successfully")
        else:
            print("Successfully Create a room")

"""//////////////////Two Subjects/////////////////////////////"""

def model2():
    #print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
    para = []
    output=[]
    para1 = []
    outputs =[]
    subn=input("Enter the Subject Name-1: ")
    start=int(input("Enter the starting no : "))
    end=int(input("last No of Students : "))
    ignore=int(input("Enter the Missing No : "))
    print("")
    #///////subject two///////////
    subn1=input("Enter the Subject Name-2: ")
    start1=int(input("Enter the starting no : "))
    ignore1=int(input("Enter the Missing No : "))
    end1=int(input("last No of Students : "))
    while start<=end:
        para.append(start)
        start+=1
    
    for i in para:
        if i==ignore:
            continue
        output.append(i)

    while start1<=end1:
        para1.append(start1)
        start1+=1
    
    for j in para1:
        if j==ignore1:
            continue
        outputs.append(j)
    print(""" 
    Hall Bench Details:
    ----------------------------
    Row x Column bench :                                                
    01.5x4 benches     |   05.9x4  benches   |     07.5x5 benches      |   11.9x5 benches
    02.6x4 benches     |   06.10x4  benches  |     08.6x5 benches      |   12.10x5 benches
    03.7x4 benches     |                     |     09.7x5 benches      |   
    04.8x4 benches     |                     |     10.8x5 benches      |   """)
    rc=int(input("Select the Bench arangment : "))

    #5x4 benches/////////////////
    if rc==1:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],outputs[0],output[5],outputs[5],output[10],outputs[10],output[15],outputs[15])
        print(output[1],outputs[1],output[6],outputs[6],output[11],outputs[11],output[16],outputs[16])
        print(output[2],outputs[2],output[7],outputs[7],output[12],outputs[12],output[17],outputs[17])
        print(output[3],outputs[3],output[8],outputs[8],output[13],outputs[13],output[18],outputs[18])
        print(output[4],outputs[4],output[9],outputs[9],output[14],outputs[14],output[19],outputs[19])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],outputs[0],output[5],outputs[5],output[10],outputs[10],output[15],outputs[15],file=f)
                print(output[1],outputs[1],output[6],outputs[6],output[11],outputs[11],output[16],outputs[16],file=f)
                print(output[2],outputs[2],output[7],outputs[7],output[12],outputs[12],output[17],outputs[17],file=f)
                print(output[3],outputs[3],output[8],outputs[8],output[13],outputs[13],output[18],outputs[18],file=f)
                print(output[4],outputs[4],output[9],outputs[9],output[14],outputs[14],output[19],outputs[19],file=f)
                  
            print("Download Successfully")
        else:
            print("Successfully Create a room")       

    #6x4 benches///////////////////
    elif rc==2:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],outputs[0],output[6],outputs[6],output[12],outputs[12],output[18],outputs[18])
        print(output[1],outputs[1],output[7],outputs[7],output[13],outputs[13],output[19],outputs[19])
        print(output[2],outputs[2],output[8],outputs[8],output[14],outputs[14],output[20],outputs[20])
        print(output[3],outputs[3],output[9],outputs[9],output[15],outputs[15],output[21],outputs[21])
        print(output[4],outputs[4],output[10],outputs[10],output[16],outputs[16],output[22],outputs[22])
        print(output[5],outputs[5],output[11],outputs[11],output[17],outputs[17],output[23],outputs[23])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],outputs[0],output[6],outputs[6],output[12],outputs[12],output[18],outputs[18],file=f)
                print(output[1],outputs[1],output[7],outputs[7],output[13],outputs[13],output[19],outputs[19],file=f)
                print(output[2],outputs[2],output[8],outputs[8],output[14],outputs[14],output[20],outputs[20],file=f)
                print(output[3],outputs[3],output[9],outputs[9],output[15],outputs[15],output[21],outputs[21],file=f)
                print(output[4],outputs[4],output[10],outputs[10],output[16],outputs[16],output[22],outputs[22],file=f)
                print(output[5],outputs[5],output[11],outputs[11],output[17],outputs[17],output[23],outputs[23],file=f)
                  
            print("Download Successfully")
        else:
            print("Successfully Create a room")

    #7x4 benches/////////////////////
    elif rc==3:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],output[0],output[7],outputs[7],output[14],outputs[14],output[21],outputs[21])
        print(output[1],outputs[1],output[8],outputs[8],output[15],outputs[15],output[22],outputs[22])
        print(output[2],outputs[2],output[9],outputs[9],output[16],outputs[16],output[23],outputs[23])
        print(output[3],outputs[3],output[10],outputs[10],output[17],outputs[17],output[24],outputs[24])
        print(output[4],outputs[4],output[11],outputs[11],output[18],outputs[18],output[25],outputs[25])
        print(output[5],outputs[5],output[12],outputs[12],output[19],outputs[19],output[26],outputs[26])
        print(output[6],outputs[6],output[13],outputs[13],output[20],outputs[20],output[27],outputs[27])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],output[0],output[7],outputs[7],output[14],outputs[14],output[21],outputs[21],file=f)
                print(output[1],outputs[1],output[8],outputs[8],output[15],outputs[15],output[22],outputs[22],file=f)
                print(output[2],outputs[2],output[9],outputs[9],output[16],outputs[16],output[23],outputs[23],file=f)
                print(output[3],outputs[3],output[10],outputs[10],output[17],outputs[17],output[24],outputs[24],file=f)
                print(output[4],outputs[4],output[11],outputs[11],output[18],outputs[18],output[25],outputs[25],file=f)
                print(output[5],outputs[5],output[12],outputs[12],output[19],outputs[19],output[26],outputs[26],file=f)
                print(output[6],outputs[6],output[13],outputs[13],output[20],outputs[20],output[27],outputs[27],file=f)    
            print("Download Successfully")
        else:
            print("Successfully Create a room")

    #8x4 benches//////////////////
    elif rc==4:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],output[0],output[8],outputs[8],output[16],outputs[17],output[24],outputs[24])
        print(output[1],outputs[1],output[9],outputs[9],output[17],outputs[18],output[25],outputs[25])
        print(output[2],outputs[2],output[10],outputs[10],output[18],outputs[19],output[26],outputs[26])
        print(output[3],outputs[3],output[11],outputs[11],output[19],outputs[20],output[27],outputs[27])
        print(output[4],outputs[4],output[12],outputs[12],output[20],outputs[21],output[28],outputs[21])
        print(output[5],outputs[5],output[13],outputs[13],output[21],outputs[22],output[29],outputs[29])
        print(output[6],outputs[6],output[14],outputs[14],output[22],outputs[22],output[30],outputs[30])
        print(output[7],outputs[7],output[15],outputs[15],output[23],outputs[23],output[31],outputs[31])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],output[0],output[8],outputs[8],output[16],outputs[17],output[24],outputs[24],file=f)
                print(output[1],outputs[1],output[9],outputs[9],output[17],outputs[18],output[25],outputs[25],file=f)
                print(output[2],outputs[2],output[10],outputs[10],output[18],outputs[19],output[26],outputs[26],file=f)
                print(output[3],outputs[3],output[11],outputs[11],output[19],outputs[20],output[27],outputs[27],file=f)
                print(output[4],outputs[4],output[12],outputs[12],output[20],outputs[21],output[28],outputs[21],file=f)
                print(output[5],outputs[5],output[13],outputs[13],output[21],outputs[22],output[29],outputs[29],file=f)
                print(output[6],outputs[6],output[14],outputs[14],output[22],outputs[22],output[30],outputs[30],file=f)
                print(output[7],outputs[7],output[15],outputs[15],output[23],outputs[23],output[31],outputs[31],file=f)
            print("Download Successfully")
        else:
            print("Successfully Create a room")

    #9x4 benches/////////////////////
    elif rc==5:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],output[0],output[9],outputs[9],output[18],outputs[18],output[27],outputs[27])
        print(output[1],outputs[1],output[10],outputs[10],output[19],outputs[19],output[28],outputs[21])
        print(output[2],outputs[2],output[11],outputs[11],output[20],outputs[20],output[29],outputs[29])
        print(output[3],outputs[3],output[12],outputs[12],output[21],outputs[21],output[30],outputs[30])
        print(output[4],outputs[4],output[13],outputs[13],output[22],outputs[22],output[31],outputs[31])
        print(output[5],outputs[5],output[14],outputs[14],output[23],outputs[23],output[32],outputs[32])
        print(output[6],outputs[6],output[15],outputs[15],output[24],outputs[24],output[33],outputs[33])
        print(output[7],outputs[7],output[16],outputs[16],output[25],outputs[25],output[34],outputs[34])
        print(output[8],outputs[8],output[17],outputs[17],output[26],outputs[26],output[35],outputs[35])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
            print(output[0],output[0],output[9],outputs[9],output[18],outputs[18],output[27],outputs[27],file=f)
            print(output[1],outputs[1],output[10],outputs[10],output[19],outputs[19],output[28],outputs[21],file=f)
            print(output[2],outputs[2],output[11],outputs[11],output[20],outputs[20],output[29],outputs[29],file=f)
            print(output[3],outputs[3],output[12],outputs[12],output[21],outputs[21],output[30],outputs[30],file=f)
            print(output[4],outputs[4],output[13],outputs[13],output[22],outputs[22],output[31],outputs[31],file=f)
            print(output[5],outputs[5],output[14],outputs[14],output[23],outputs[23],output[32],outputs[32],file=f)
            print(output[6],outputs[6],output[15],outputs[15],output[24],outputs[24],output[33],outputs[33],file=f)
            print(output[7],outputs[7],output[16],outputs[16],output[25],outputs[25],output[34],outputs[34],file=f)
            print(output[8],outputs[8],output[17],outputs[17],output[26],outputs[26],output[35],outputs[35],file=f)
                  
            print("Download Successfully")
        else:
            print("Successfully Create a room")

    #10x4 benches//////////////////
    elif rc==6:
        print("Exam name :",exam ,"          Room Name :",room,"              Date :",date)
        print(output[0],output[0],output[10],outputs[10],output[20],outputs[20],output[30],outputs[30])
        print(output[1],outputs[1],output[11],outputs[11],output[21],outputs[21],output[31],outputs[31])
        print(output[2],outputs[2],output[12],outputs[12],output[22],outputs[22],output[32],outputs[32])
        print(output[3],outputs[3],output[13],outputs[13],output[23],outputs[23],output[33],outputs[33])
        print(output[4],outputs[4],output[14],outputs[14],output[24],outputs[24],output[34],outputs[34])
        print(output[5],outputs[5],output[15],outputs[15],output[25],outputs[25],output[35],outputs[35])
        print(output[6],outputs[6],output[16],outputs[16],output[26],outputs[26],output[36],outputs[36])
        print(output[7],outputs[7],output[17],outputs[17],output[27],outputs[27],output[37],outputs[37])
        print(output[8],outputs[8],output[18],outputs[18],output[28],outputs[28],output[38],outputs[38])
        print(output[9],outputs[9],output[19],outputs[19],output[29],outputs[29],output[39],outputs[39])
        download=int(input("Click one to download : "))
        if download==1:
            with open(room+'.txt','wt') as f:
                print("Exam name :",exam ,"          Room Name :",room,"              Date :",date,file=f)
                print(output[0],output[0],output[10],outputs[10],output[20],outputs[20],output[30],outputs[30],file=f)
                print(output[1],outputs[1],output[11],outputs[11],output[21],outputs[21],output[31],outputs[31],file=f)
                print(output[2],outputs[2],output[12],outputs[12],output[22],outputs[22],output[32],outputs[32],file=f)
                print(output[3],outputs[3],output[13],outputs[13],output[23],outputs[23],output[33],outputs[33],file=f)
                print(output[4],outputs[4],output[14],outputs[14],output[24],outputs[24],output[34],outputs[34],file=f)
                print(output[5],outputs[5],output[15],outputs[15],output[25],outputs[25],output[35],outputs[35],file=f)
                print(output[6],outputs[6],output[16],outputs[16],output[26],outputs[26],output[36],outputs[36],file=f)
                print(output[7],outputs[7],output[17],outputs[17],output[27],outputs[27],output[37],outputs[37],file=f)
                print(output[8],outputs[8],output[18],outputs[18],output[28],outputs[28],output[38],outputs[38],file=f)
                print(output[9],outputs[9],output[19],outputs[19],output[29],outputs[29],output[39],outputs[39],file=f)
                  
            print("Download Successfully")
        else:
            print("Successfully Create a room")


def model3():
    pass

def model4():
    pass

if __name__=="__main__":
    main()
    
    
    exam=input("Enter Exam Name : ")
    room=input("Room Name : ")
    date=int(input("Exam date : "))
    nos=int(input("Total no of students : "))
    nsub=int(input( "No the subject : "))

    
    if nsub==1:
        method1()
    elif nsub==2:
        model2()
    elif nsub==3:
        model3()
    elif nsub==4:
        model4()