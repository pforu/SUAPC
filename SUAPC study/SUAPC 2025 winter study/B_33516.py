"""import sys
input= sys.stdin.readline

input()
cnt=0
string= input()

#1차, skeep->0
string= string.replace("skeep", "0")
cnt+=string.count("0")
#print(string, cnt)

#모든 s에 대해 뒤부터 skeep 가능성 탐색 
while True:
    flag=0
    if string.find("s")!=-1:
        s_index= len(string) - string[::-1].find("s") - 1
        if len(string[s_index:])<5:
            string= string[:s_index]+"1"+string[s_index+1:]
            continue
    else:
        break
    
    #print(s_index)
    if string[s_index+1]=="k" or string[s_index+1]=="0":
        if string[s_index+2]=="e" or string[s_index+2]=="0":
            if string[s_index+3]=="e" or string[s_index+3]=="0":
                if string[s_index+4]=="p" or string[s_index+4]=="0":
                    string= string[:s_index]+"0"+string[s_index+5:]
                    cnt+=1
                    flag=1
                    #print(string, cnt)
    if flag==0:
        string= string[:s_index]+"1"+string[s_index+1:]

print(cnt)"""

import sys
input= sys.stdin.readline

input()
cnt=0
string= input()

#1차, skeep->0
string= string.replace("skeep", "0")
cnt+=string.count("0")

#모든 s에 대해 뒤부터 skeep 가능성 탐색 
string=list(string[::-1])
length= len(string)

while True:
    flag=0
    try:
        s_index= string.index("s") ########## .index는 O(N)
    except:
        s_index= -1

    if s_index!=-1:

        if s_index<4:
            string[s_index]="1"
            continue
    else:
        break
    

    if string[s_index-1]=="k" or string[s_index-1]=="0":
        if string[s_index-2]=="e" or string[s_index-2]=="0":
            if string[s_index-3]=="e" or string[s_index-3]=="0":
                if string[s_index-4]=="p" or string[s_index-4]=="0":
                    string[s_index]="0"
                    del string[s_index-1] ######### del은 O(N) >> 삭제하고 끝이 아니라 뒤의 아이들을 한 칸씩 끌어오니까 
                    del string[s_index-2]
                    del string[s_index-3]
                    del string[s_index-4]
                    cnt+=1
                    flag=1

    if flag==0:
        string[s_index]="1"

print(cnt)