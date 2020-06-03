'''
This program generates all combinations with words from following code.
And creates the lists of words that can go after current word.
'''
# x = 6
# for y in range(x):
#     print('hello','mister',y)

from itertools import product

# create empty files from start
open('log.txt', 'w').close()
open('list.txt','w').close()

words = ['x ','= ','100 ','\n','for ','y ',' in ','range ',
         '(',')',':','\n'+'    ','print ',"'",'hello ',',','mister ']

slovarik = {}

# Objects for lists
abc = ['a','b','c','d','e','f','g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
       'p','q','r','s','t','u','v','w','x','y','z']

len_code = 26

# Creates dict for every word. Word as key and list as value 
for i, word in enumerate(words):
    try:
        abc[i] = []
        slovarik[word] = abc[i]
    
    except IndexError:
        break

def pars():
    '''
        Generates combinations 
    '''

    for L in range(0, len_code+1):
        for nomer, subset in enumerate(product(words, repeat=L)):
            templist = []

            for i in subset:
                templist.append(i)                
                            
            c = ''.join(templist)

            execute(c,templist,nomer)
                

def execute(c,templist,nomer):
    '''
        Execute combination code
    '''

    try:
        exec(c)

        with open('log.txt', 'a') as fil:
            fil.write(str(nomer)+' '+''.join(templist)+'\n')
        
        renaming_for_log(templist,nomer)

    except:
        print('!!!ERROR')

def renaming_for_log(templist,nomer):
    '''
        Renaming some words for better writing in log file
    '''

    for y,x in enumerate(templist):
        try:
            if templist[y+1] == '\n'+'    ':
                p = 'perenos probel'
            elif templist[y+1] == '\n':
                p = 'perenos'
            else:
                p = templist[y+1]
            if x == '\n':
                d = 'perenos'
            elif x == '\n    ':
                d = 'perenos probel'
            else:
                d = x
            
            check_quotes(y,x,p,d,templist,nomer)

        except IndexError:
            print('bye')
            next
            
def check_quotes(y,x,p,d,templist,nomer):
    '''
        Check if words in quotes -  don't append in list of word,
        because every word in this case can be in quotes without error
        If current word not in quotes and 
        If next word not already exists in list of current word 
        Append the next word to list of current word 
    '''

    f = open('list.txt', 'a')

    quotes =[]

    if y not in quotes:
        
        if len(quotes)%2 == 0:
            if x=="'":
                try:
                    if templist[y+1]=="'":
                        next
                    elif templist[y+1]=='\n':
                        next
                    elif templist[y+1]=='\n    ':
                        next
                    else:
                        quotes.append(y)
                except:
                    print('There is no next element!')
                    
            elif templist[y+1]=="'":
                if templist[y+1] not in slovarik[x]:
                    slovarik[x].append(templist[y+1])
                    slovarik[x].append('<-'+str(nomer))
                    f.write(str(nomer)+' '+ d +' '+'('+ p +')'+str(int(len(slovarik[x])/2))+': '+ str(slovarik[x])+'\n')
                else:
                    print('Already in slovarik!')
            else:
                if templist[y+1] not in slovarik[x]:
                    slovarik[x].append(templist[y+1])
                    slovarik[x].append('<-'+str(nomer))
                    f.write(str(nomer)+' '+ d +' '+'('+ p +')'+str(int(len(slovarik[x])/2))+': '+ str(slovarik[x])+'\n')
                else:
                    print('Already in slovarik!')
            
        elif len(quotes)%2 != 0:
            if templist[y+1]=="'":
                quotes.append(y+1)
            else:
                print('INSIDE QUOTES!')
    else:
        if templist[y+1] not in slovarik[x]:
            slovarik[x].append(templist[y+1])
            slovarik[x].append('<-'+str(nomer))
            f.write(str(nomer)+' '+ d +' '+'('+ p +')'+str(int(len(slovarik[x])/2))+': '+ str(slovarik[x])+'\n')
        else:
            print('Already in slovarik!')
        print('Already in quote!')
    f.close()

    _lists_log('lists.txt')
            

def _lists_log(lists_file: str = 'the_default_filename.txt') -> None:
    ''' 
        Writes the general dictinary in file.
        The format is:
        '[name list] [len list] [list]'

        Args:
            lists_file - the file to write into

        Return:
            None
    '''
    with open(lists_file, 'w') as f:
        for num, log in enumerate(slovarik):
            if words[num] == '\n':
                n = 'perenos'
            elif words[num] == '\n    ':
                n = 'perenos probel'
            else:
                n = words[num]

            f.write(f'{n} {str(int(len(slovarik[log])/2))} {str(slovarik[log])}\n')
       
if __name__ == "__main__":
    pars()
