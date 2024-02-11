def caesarCipher(s, k):
    if k > 26 :
        k =  (k%26)

    alphabet_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    
    for i in s :
        
        if i in alphabet_lower :
            ans += alphabet_lower[alphabet_lower.find(i)+k]
            print(alphabet_lower.find(i))
        elif i in alphabet_upper :
            ans += alphabet_upper[alphabet_upper.find(i)+k]
        else :
            ans += i

    return ans

print(caesarCipher(input()))