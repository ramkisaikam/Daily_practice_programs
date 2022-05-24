
def binary_search(nums, target) :
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1

List = [-1,0,1,2,6,7,9,15,22]
target = 9
index = binary_search(nums=List,target=target)
print(index)
