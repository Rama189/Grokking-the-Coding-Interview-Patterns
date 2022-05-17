
#mycode 
def search_triplets(arr):
    arr.sort()
    result = []

    for k in range(len(arr)):
        if k > 0 and arr[k] ==  arr[k - 1]:
            continue
        
        i = k + 1
        j = len(arr) - 1

        target = 0 - arr[k] 

        while i < j:
            two_sum = arr[i] + arr[j]
            if two_sum == target:
                result.append([arr[k], arr[i], arr[j]])
                i += 1
                while arr[i] ==  arr[i - 1] and i < j:
                    i += 1
            elif two_sum > target:
                j = j - 1
            else:
                i = i + 1
    return result

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()
