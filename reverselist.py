#!/usr/bin/env python3

def reverseString(s):
        if not s:
           return
        slen = len(s)
        for i in range(0,slen//2):
            t = s[i]
            s[i] = s[slen-1-i]
            s[slen-1-i] = t
        print("Result =>",s)
        return

s=["h","e","l","l","o"]
print("Input =>",s)
reverseString(s)
