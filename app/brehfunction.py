def breh_translator(S):
    """ pig latin converter from '19 (with thanks to Justin G.!) """
    retStr = ''
    V = ['a','A','e','E','i','I','o','O','u','U']
    currFront = S[0]
    seen_vowel = False
    for i in range(len(S)):
        if S[i] == ' ':
            if currFront in V:
                retStr += 'breh'
            else:
                retStr += currFront.lower() + 'breh'
        elif i == len(S)-1:
            if currFront in V:
                retStr += S[i]+ 'breh'
            else:
                retStr += S[i] + currFront.lower() + 'breh'
        else:
            if S[i-1] == ' ' or i == 0:
                seen_vowel = False
                currFront = S[i]
                if currFront in V:
                    retStr += S[i]
                    seen_vowel = True
            else:
                if S[i] in V:
                    seen_vowel = True
                    retStr += S[i]
                else:
                    if not seen_vowel:
                        currFront += S[i]
                    else:
                        retStr += S[i]
    return retStr