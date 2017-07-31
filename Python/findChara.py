# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# # output
# new_list = ['hello','world']

def findChara(lists, charas):
    new_list = []
    for count in range(0,len(lists)):
        if lists[count].find(charas)!=-1:
            new_list.append(lists[count])
    print new_list
findChara(word_list,char)
