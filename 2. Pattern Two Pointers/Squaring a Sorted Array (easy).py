#mycode , huh, wrote some spaghetti code, alas fail, failed to consider in between elements! it's negative dude
#may 16, 2022, Crying! Why can't I code for the life of me!!!
def make_squares(arr):
    result = []
    left, right = 0, 0

    for x in arr:
        squared = x * x
        if not result:
            result.append(squared)
            continue

        if len(result) == 1:
            if squared  < result[right]:
                result.insert(right, squared )
                left = right
            else:
                result.insert(right + 1, squared )
            right += 1
        else:
            if squared  < result[right] and squared  > result[left]:
                result.insert(right, squared )
                left = right
            elif squared  >= result[right]:
                result.insert(right + 1, squared )
            elif squared  <= result[left]:
                result.insert(left, squared )
                
            right += 1
    return result

#answer
def make_squares(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  highestSquareIdx = n - 1
  left, right = 0, n - 1
  while left <= right:
    leftSquare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      left += 1
    else:
      squares[highestSquareIdx] = rightSquare
      right -= 1
    highestSquareIdx -= 1

  return squares

def main():
  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-4,-1,0,3,10])))
main()