def shell_sort_step(arr):
    n = len(arr)
    gap = n // 2  # 初始 gap
    step = 1      # 計數步驟用
    
    while gap > 0:
        print(f"\n=== gap = {gap} ===")
        # 對每個子序列做插入排序
        for i in range(gap, n):
            temp = arr[i]
            j = i
            print(f"\n步驟 {step}: 處理元素 arr[{i}] = {temp}")
            
            # 插入排序過程
            while j >= gap and arr[j - gap] > temp:
                print(f"  arr[{j-gap}] = {arr[j-gap]} > {temp} → 向右移動")
                arr[j] = arr[j - gap]
                j -= gap
                print(f"  當前狀態: {arr}")
            
            arr[j] = temp
            print(f"  插入完成，陣列狀態: {arr}")
            step += 1
        
        gap //= 2  # 縮小 gap
    
    print("\n=== 排序完成 ===")
    return arr


# 測試
data = [8, 9, 3, 2, 4, 1, 1, 5]
print("排序前:", data)
sorted_data = shell_sort_step(data)
print("排序後:", sorted_data)
