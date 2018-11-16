#The Capitalize the hard way, a easy solution is use title() instead
name = "leandro azevedo"
def solution(name):
    newname = []
    for i in range(len(name)):
        if i == 0:
            newname.append(name[0].capitalize())
        else:
            if name[i-1] == ' ':
                    newname.append(name[i].capitalize())
                    #print ('zero before', name[i])
            else:
                newname.append(name[i])
#print '{}'.format(newname)
    return''.join(newname)

result = solution(name)
print result
