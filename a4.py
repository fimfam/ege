def freq_dec(s):
    freqs={}
    for c in s:
        if c.isalpha():
            v=freqs.get(c,0)
            freqs[c]=v+1
    maxfreq=0
    maxk=''
    for(k,v) in freqs.items():
        if v>maxfreq:
            maxfreq=v
            maxk=k
    return freqs, maxk