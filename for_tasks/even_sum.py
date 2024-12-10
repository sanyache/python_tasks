"""
сума парних
"""
even_numbers = [int(x) for x in input().split() if not int(x) & 1]
print(sum(even_numbers))