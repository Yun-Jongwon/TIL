T=int(input())
for t in range(T):
    R,N,K=map(int,input().split())
    point_data=[]
    for n in range(N):
        point=tuple(map(int,input().split()))
        point_data.append(point)

    second_question=[]
    result=[]
    for po1 in range(len(point_data)):
        gioolgi = []
        for po2 in range(len(point_data)):

            if po1!=po2:
                if point_data[po1][0]-point_data[po2][0]>0:
                    xs=1
                elif point_data[po1][0]-point_data[po2][0]==0:
                    xs=0
                else:
                    xs=-1
                if point_data[po1][1]-point_data[po2][1]>0:
                    ys=1
                elif point_data[po1][1]-point_data[po2][1]==0:
                    ys=0
                else:
                    ys=-1


                gioolgi.append(((point_data[po1][0]-point_data[po2][0])/(point_data[po1][1]-point_data[po2][1]) if not (point_data[po1][1]-point_data[po2][1])==0 else 0,(xs,ys)))

        result.append(N-1-(len(gioolgi)-len(set(gioolgi))))
    # print(sum(result))


    A = [0] + result[:] + [0] * N
    c = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            A[j] = (A[j] * K + j) % N + 1
            A[N + j] = (A[j] * j + K) % N + 1
        A.sort()
        B = [0] * (N * 2 + 1)
        B[0] = 1
        for j in range(1, N * 2 + 1):
            B[j] = (B[j - 1] * A[j] + j) % N + 1
        c[i] = B[2 * N]
    print('#%d %d %d' % (t + 1, sum(result), sum(c)))


