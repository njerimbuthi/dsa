nums = [-1, 1, 0, -3, 3]
output = []

for i in range(len(nums)):
    product = 1
    for j in range(len(nums)):
        if i == j:
            continue
        product *= nums[j]
    output.append(product)
print(output)
