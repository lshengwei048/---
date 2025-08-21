# 暑期資料結構期末報告 學生:11224123羅聖幃 11224125吳泰安

## Python算法之希爾排序

### 希爾排序（Shell Sort）是由 Donald Shell 在 1959 年提出的一種 改進版插入排序。
它的核心思想是：

插入排序在資料「幾乎有序」時效率非常高。

所以先將資料分組，對分組內的資料進行插入排序。

逐步縮小分組的間隔（gap），直到間隔為 1，此時就相當於普通的插入排序，但因為數列已經大致有序，效率會比直接插入排序高很多。

## 圖例說明
![01](https://github.com/lshengwei048/---/blob/main/%E5%9C%96%E7%89%871.png)

## 代碼分析

### 初始化間隔（增量）
首先計算初始的間隔 gap，通常取數組長度的一半（gap = n // 2）。這個間隔決定了子序列的分割方式，後續會逐步縮小。

### 分組與插入排序

外層循環（間隔控制）：當 gap > 0，執行循環體。每次循環結束後將間隔縮小一半（gap = gap // 2）。

中層循環（遍歷每個子序列）：從 gap 開始遍歷到陣列末尾，每個元素 arr[i] 屬於不同的子序列。

內層循環（子序列插入排序）：儲存目前元素 arr[i] 到臨時變數 temp。在目前子序列中（間隔為 gap），從後往前比較元素。如果前一個元素 arr[j - gap] 大於 temp，則將其向後移動一個位置。重複上述比較和移動操作，直到找到正確的插入位置，然後將 temp 插入該位置。

### 縮小間隔
每次完成目前間隔的所有子序列排序後，將間隔縮小一半（例如，從 gap = 4 到 gap = 2，再到 gap = 1）。當間隔最終縮小到 1 時，整個數組就被視為一個子序列，此時執行的其實就是普通的插入排序，因為前面的多輪排序已經使數組趨近有序，插入排序的效率會更高。

### 終止條件
當間隔 gap 減少到 0 時，排序完成，此時排序後的陣列即為有序。

## 程式碼
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

## 執行結果
![01](https://github.com/lshengwei048/---/blob/main/%E5%9C%96%E7%89%871.png)
