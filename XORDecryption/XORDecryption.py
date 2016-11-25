l = [chr(97+i) for i in range(0,26)]
#print l
s = []
for i in range(26):
    sta = chr(97+i)
    for j in range(26):
        #if i != j:
        stb = sta + chr(97+j)
        for k in range(26):
                #if j != k and k != i:
            stc =  stb + chr(97+k)
                    #print st
            s.append(stc)
#print "Length: ", len(s)
#print s
n = int(raw_input())
aaa = map(int, raw_input().split(" "))
keys = []
for i in range(17576):
    length = len(s[i])
    t = n / length
    add = n - (t)*length
    keys.append([ord(j) for j in list((s[i] * t) + s[i][0:add])])
    #print len(keys[i])
for i in range(17576):
    flag = True
    for j in range(n):
        # 65 to 90 , 97 to 122, 40 , 41, 48 to 57 , 58 , 59 ,46,44,38,63,45,33
        z = keys[i][j] ^ aaa[j]
        #print z
        if (z >= 65 and z <=90) or (z >= 97 and z <=122) or (z == 40) or (z == 41) or (z >= 48 and z <= 59) or (z == 46) or (z == 44) or (z ==38) or (z == 63) or (z == 45) or (z == 33) or (z == 32):
            pass
        else:
            flag = False
            break
    if flag:
        print s[i]
        break
    