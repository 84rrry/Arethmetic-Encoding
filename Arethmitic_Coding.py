from decimal import getcontext
from decimal import Decimal
getcontext().prec=10
#calculating frequency
msg='bdab'
mlen=len(msg)
def Probability(msg):
    letters={}
    for i in msg:
        if i not in letters.keys():
            letters[i]=msg.count(i)/len(msg)
    return letters
# print(Probability(msg))
PTab={'a': 0.2, 
 'b': 0.3, 
 'c': 0.1, 
 'd': 0.4}
#get the range of the current char
def get_range(PTab,min,max):
        ran = {}
        d = max - min
        for i in range(len(PTab.items())):
            char = list(PTab.keys())[i]
            char_prob = Decimal(PTab[char])
            cum_prob = char_prob * d + min
            ran[char] = [min, cum_prob]
            min = cum_prob
        return ran
#encoding process
def encode(msg,PTab):
    ranges=[]
    min=Decimal(0.0)
    max=Decimal(1.0)
    for c in range(len(msg)):
        ran=get_range(PTab,min,max)
        char=msg[c]
        min=ran[char][0]
        max=ran[char][1]
        ranges.append(ran)
    ran=get_range(PTab,min,max)
    ranges.append(ran)
    code=(list(ranges[-1].values())[-1][-1]+list(ranges[-1].values())[0][0])/2
    return ranges,code
# print(encode(msg,PTab))
#Decoding process
def decode(code,mlen,PTab):
    ranges=[]
    msg=""
    min = Decimal(0.0)
    max = Decimal(1.0)
    for i in range(mlen):
        ran = get_range(PTab,min,max)

        for char, value in ran.items():
            if code >= value[0] and code <= value[1]:
                break
        msg = msg + char
        min = ran[char][0]
        max = ran[char][1]
        ranges.append(ran)    
    ran=get_range(PTab,min,max)
    ranges.append(ran)
    return ranges,msg
