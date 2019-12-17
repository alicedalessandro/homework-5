def Distance(s1,s2):
    if len(s1)== len(s2):
        d = 0.0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                d += 1    
                
    return '%.5f'%(d/len(s1))



def FASTA_parse(file):
    strings={}
    with open(file) as x:
        t=x.read()
        its=t.split('>')
        
    for it in its[1:]:
        it=it.split('\n')
        s_id=it.pop(0)
        strings[s_id]=''.join(it)
        
    return strings

dic=FASTA_parse("rosalind_pdst.txt")
DNAs=dic.values()

counter=[]
for strand1 in DNAs:
        for strand2 in DNAs:
            counter.append(Distance(strand1,strand2))

for i in range(0,len(counter),len(DNAs)):
    print (' '.join(map(str, counter[i:i+len(DNAs)])))
