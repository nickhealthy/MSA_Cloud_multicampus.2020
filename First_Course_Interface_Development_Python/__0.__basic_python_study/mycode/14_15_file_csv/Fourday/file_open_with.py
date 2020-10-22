# mode를 설정하지 않으면 default가 r(read)

myfile = open('i_have_a_dream.txt', 'r')
contents = myfile.read()
print(contents)
myfile.close()