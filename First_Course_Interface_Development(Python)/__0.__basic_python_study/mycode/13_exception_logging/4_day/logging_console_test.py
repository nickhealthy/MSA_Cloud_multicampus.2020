# 여기는 콘솔에다가만 로그를 남김
import logging

def say_hello(msg):
    return 'Hello ' + msg

# logging 설정
# logging.basicConfig(level=logging.INFO(DEBUG)) # INFO 부분에 레벨 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of Program')
logging.debug(say_hello('디버그 모드'))

# info 라는 높은 레벨은 낮은 레벨 출력 불가
logging.info(say_hello('인포 모드'))
logging.debug('End of Program')