# 1. %formating: C언어 style
# 2. String format 함수: {} 에 대응하는 값을 format() 의 인자로 전달
# 3. f-string:  python 3.6 이상에서만 사용


temperature = 36
print('온도 값은 %d %.2f' % (temperature, temperature))

print('온도 값은 {0:.2f}'.format(temperature))

print(f'온도 값은 {temperature} ')

#print("Art: %5d, price per Unit: %8.2f" % (453, 59.058))
#print("Art: {0:5d}, price per Unit: {1:5.2f}" .format(453, 59.058))

# padding
print('product {0:10s}, Price per unit {1:10.3f}'.format('apple', 5.243))
print('product {0:>10s}, Price per unit {1:10.3f}'.format('apple', 5.243))
