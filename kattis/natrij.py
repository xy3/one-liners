(lambda s,m,_,h:print(f"{24:02}:{m:02}:{s:02}"if sum([h,m,s])==0 else f"{h:02}:{m:02}:{s:02}"))(*(lambda r,t:(lambda s,y,m:(s,m,*divmod(y+t[0]-r[0],24)))(*(lambda x,s:(s,*divmod(x+t[1]-r[1],60)))(*divmod(t[2]-r[2],60))))(list(map(int,input().split(":"))),list(map(int,input().split(":")))))