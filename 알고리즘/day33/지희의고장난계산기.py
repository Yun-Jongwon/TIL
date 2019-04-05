def nboon(target,length):



    global min_len
    if target<=1:
        if length<min_len:
            min_len=length
        return


    for i in range(2,int(target**(1/2))+1):
        if target%i==0:
            str_target1=str(i)
            str_target2=str(target//i)
            str_len1=len(str_target1)
            str_len2=len(str_target2)

            flag=0
            new_flag=0
            for st in range(str_len1):
                if calcurator[int(str_target1[st])]!=1:
                    flag+=1
                    break
            if flag==0:

                nboon(target//i, length + str_len1 + 1)
            # else:
            #     nboon(i,length)

            for st in range(str_len2):
                if calcurator[int(str_target2[st])]!=1:
                    flag+=1
                    new_flag = 1
                    break

            if flag==0 :
                moment_length=length+2+str_len1+str_len2
                if moment_length< min_len:
                    min_len = moment_length
            if new_flag==0:
                nboon(i,length+str_len2+1)
            # else:
            #     nboon(target // i, length )


T=int(input())
for t in range(T):
    calcurator=list(map(int,input().split()))
    ttarget=int(input())
    min_len=987654321
    str_ttarget=str(ttarget)
    fflag=0
    for i in str_ttarget:
        if calcurator[int(i)]!=1:
            fflag=1
    if fflag==0:
        print("#{} {}".format(t+1,len(str_ttarget)+1))
    else:
        nboon(ttarget,0)
        if min_len==987654321:
            min_len=-1
        print("#{} {}".format(t+1,min_len))


