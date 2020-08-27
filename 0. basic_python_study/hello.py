import sys

print('sys파일 길이', len(sys.argv))

for val in sys.argv:
    print("val = ", val)

def say_hello(msg):
    return 'Hello ' + msg

def main():
    msg = sys.argv[1]
    print(msg)
    if msg is None:
        print('enter msg')
    else:
        print(say_hello(msg))

# 직접 실행했을때 실행
if __name__ == '__main__':
    print("직접실행")
    main()
# import 됬을때만 실행
else:
    print('import 되어 실행됨')