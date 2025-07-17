# series sum

start = 1
end = 99
numerator = start
result = 0

while numerator < end:
    denominator = numerator + 2
    result += numerator / denominator
    print (numerator, "/", denominator, "=", numerator / denominator)
    numerator += 2

print (result)