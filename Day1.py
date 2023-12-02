

file=open('input_01.txt','r')

file_list=file.readlines()

numdict = {  "one": 'o1e',"two": 't2o',"three": 't3e',  "four": 'f4r',  "five":'f5e',
  "six":'s6x',  "seven":'s7n',  "eight":'e8t',  "nine":'n9e'}

totalsum=0

for line in file_list:
    linesum=0
    print('line: ',line)
    first_n=77
    #replacing number words with numbers
    for key in numdict:
        line = line.replace(key, numdict[key])
    print('converted Line: ',line)    
    for x in line:
        #print('x:',x)
        
        try:
            number=int(x)
        except:
            1==1
            #print('not a number')
        else:
          if first_n==77:
                first_n=number
                #print('first number',first_n)
          #print('number: ',number)
    print('first: %s, last: %s'%(first_n,number) ) 
    linesum=first_n*10+number
    print('linesum: ',linesum)
    totalsum = totalsum+linesum
    print('totalsum: ',totalsum)

print('END totalsum: ',totalsum)
        