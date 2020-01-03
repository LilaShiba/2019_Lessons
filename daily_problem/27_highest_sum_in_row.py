'''
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.

'''
# gives sequence and highest sum
def highSum(arr):
  highest = 0
  length = len(arr)
  ans = []
  for x in range(length):
    temp_sum = sum(arr[x:])
    if temp_sum > highest:
      highest = temp_sum
      ans = arr[x:]
  if len(ans) > 0:
    return highest, ans
  return highest


# This algorithm is known as Kadane's algorithm, and it runs in O(N) time and O(1) space.
def kadens(arr):
  max_ending_here = max_so_far = 0
  for x in arr:
    # ensures positive
    max_ending_here = max(x, max_ending_here + x)
    # ensures highest sum
    max_so_far = max(max_so_far, max_ending_here)
  return max_so_far

if __name__ == '__main__':
  arr =  [34, -50, 42, 14, -5, 86]
  # 42, 14, -5, 86
  print(highSum(arr))
  arr2 = [-5, -1, -8, -9]
  print(highSum(arr2))
  print(kadens(arr))
  print(kadens(arr2))
