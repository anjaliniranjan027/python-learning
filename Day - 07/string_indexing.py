# indexing = accesing elements of a sequence using [] (indexing operator)
#            [start:stop:step] (slicing operator)

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # 1
print(credit_number[5]) # 5
print(credit_number[-1]) # 6
print(credit_number[:4]) # 1234
print(credit_number[5:9]) # 5678
print(credit_number[::2]) # 135790246

# Masking all but last 4 digits of credit card number
last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}") # xxxx-xxxx-xxxx-3456

# Reversing a string
credit_number = credit_number[::-1]
print(credit_number) # 1234-5678-9012-3456