def funnyString(s):
    s1 = [ord(i) for i in s]
    s2 = [s1[i] for i in range(len(s1)-1,-1,-1)]

    for i in range(len(s1)-1,-1,-1):
        if abs(s1[i] - s1[i-1]) == abs(s2[i] - s2[i-1]):
            pass
        else:
            return ("Not Funny")
            break
    else:
        return ("Funny")