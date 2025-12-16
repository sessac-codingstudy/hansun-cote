import sys 
input = sys.stdin.readline 

n,m = map(int,input().split())

song_dict = {}
test_case = []

for _ in range(n) : 
    song_info = list(map(int,input().split()))
    string = song_info[2]+song_info[3]+song_info[4] 
    if(string in song_dict) :
        song_dict[string].append(song_info[1])
    else :
        song_dict[string] = [song_info[1]]
for _ in range(m) : 
    
    test_keyword = ''.join(input().split())
    print(test_keyword)
