"""
сума парних
"""
even_numbers = [x for x in map(int, input().split()) if not x & 1]
print(sum(even_numbers))