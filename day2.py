file=open('input_02.txt','r')

file_list=file.readlines()

b_cnt=14
r_cnt=12
g_cnt=13

totalsum=0
total_power=0
for line in file_list:
    possible=1
    game=line.split(':')
    runs=game[1].split(';')
    gmax_r=0
    gmax_b=0
    gmax_g=0
    for run in runs:
        shows=run.split(',')
        for show in shows:
            show=show.split(' ')
            print(show)
            red=0
            blue=0
            green=0
            if show[2].find('red')>=0:
                red=int(show[1])
            if show[2].find('green')>=0:
                green=int(show[1])
            if show[2].find('blue')>=0:
                blue=int(show[1])
            if (red <=r_cnt)and(blue<=b_cnt)and(green<=g_cnt):
                1==1
            else:
                possible=0
            print('show stat %sb, %sr, %sg'%(blue,red,green))
            gmax_r=max(gmax_r,red)
            gmax_b=max(gmax_b,blue)
            gmax_g=max(gmax_g,green)
    if (possible==1):
        id=int(game[0].split(' ')[1])
        totalsum=totalsum+id
        print('game %s, possible total : %s'%(id,totalsum))
    game_power=gmax_g*gmax_b*gmax_r
    total_power=total_power+game_power
    print('game rep max %sg %sb %sr: power %s'%(gmax_g,gmax_b,gmax_r,game_power))
print('total:',totalsum)
print('total_power: ',total_power)


            
