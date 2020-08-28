# 여기는 파일도 만들어서 로그를 남기고 콘솔에도 로그를 남김

# 1. logger 생성
# 2. level 설정
# 3. 파일 핸들러에 '파일 이름, 기능(r,w,a..), 인코딩 설정
# 4. 포맷팅 설정으로 저장을 원하는 값들을 설정
# 5.


import logging

def say_hello(msg):
    return 'Hello ' + msg

# logger 생성
root_logger = logging.getLogger()
# log level 설정
root_logger.setLevel(logging.DEBUG) # logging.DEBUG 변수로 상수값 <> 밑에 .debug는 함수
# logger file Handler 생성
fileHandler = logging.FileHandler('test.log', 'w', 'utf-8') # log 파일명, 쓰기, UTF-8 인코딩
# logger console Handler 생성
streamHandler = logging.StreamHandler()

# 무엇을 나타낼지 Formatter(포맷팅) 설정
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s: %(filename)s:%(lineno)s - %(message)s')

# File Handler에 file_formatter 설정, 지정함
fileHandler.setFormatter(file_formatter)
streamHandler.setFormatter(formatter)

# logger 객체에 file_handler 와 stream_handler를 등록
root_logger.addHandler(fileHandler)
root_logger.addHandler(streamHandler)

root_logger.debug('Start of Program')
root_logger.debug(say_hello('debug 모드'))
root_logger.info(say_hello('info 모드'))
# root_logger.warn(say_hello('warn 모드')) DeprecationWarning : 버전이 없음
root_logger.error(say_hello('error 모드'))
root_logger.debug('End of Program')