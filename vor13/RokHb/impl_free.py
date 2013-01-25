# Authors: Sveinn Floki Gudmundsson & Tomas Pall Mate
# Fallid IMPL_FREE utfaert i Python 2.7.3
# Takn(NOT,AND,OR,IF_THEN) = (~,&,|,>)
# Oll onnur takn eru medhondlud sem eindir
# Svigar virka eins og madur mundi buast vid
#
# Notkun: out_string = impl_free(in_string)
# Fyrir:  in_string er strengur sem inniheldur propositional formulu
# Eftir:  out_string er strengur sem inniheldur equivalent implication-free formulu
def impl_free(in_string):
    out_string = []
    temp = -1
    done = 0
    for i in range(len(in_string)):
        if not i < done:
            if in_string[i] == '&' or in_string[i] == '|':
                out_string.append(in_string[i])
                temp = i
            elif in_string[i] == '>':
                out_string.append('|')
                out_string.insert(temp+1,'~')
                temp = i
            elif in_string[i] == '(':
                out_string.append('(')
                out_string_temp = impl_free(in_string[i+1:])
                out_string.append(out_string_temp)
                done = i + len(out_string_temp) + 1
                out_string.append(')')
            elif in_string[i] == ')':
                return ''.join(out_string)
            else:
                out_string.append(in_string[i])
    return ''.join(out_string)
# test
print impl_free("r&(p>(r>q))") # prentar r&(~p|(~r|q))


'''
>>> bla
'~p|x'
>>> bla=impl_free.impl_free('p>(~x>q|n|x>~(q>b))')
>>> bla
'~p|(~~x|q|n~|x|~(~q|b))'
>>> 
 hér er greinilega villa, smb. ~|x   , en þetta er samt flott framtak hjá drenginum
'''

