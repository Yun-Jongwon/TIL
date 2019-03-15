def merge(left,right):
    total_len=len(left)+len(right)
    new_result=[0]*total_len
    count=0
    left_len=len(left)
    right_len=len(right)
    i_left=0
    i_right=0
    while i_left<left_len and i_right<right_len:
        if right[i_right]>left[i_left]:
            new_result[count]=left[i_left]
            count+=1
            i_left+=1
        else:
            new_result[count]=right[i_right]
            count+=1
            i_right+=1



    if i_left<left_len:
        while i_left!=left_len:
            new_result[count]=left[i_left]
            i_left+=1
            count+=1
    elif i_right<right_len:
        while i_right!=right_len:
            new_result[count]=right[i_right]
            i_right+=1
            count+=1


    return new_result





def merge_sort(m):
    if len(m) <= 1 : # 사이즈가 0이거나 1인 경우, 바로 리턴
        return m
    
    # 1. DIVIDE 부분
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    
    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 2. CONQUER 부분 : 분할된 리스트들 병합
    return merge(left, right)
m=[9,5,5]
print(merge_sort(m))
result=0