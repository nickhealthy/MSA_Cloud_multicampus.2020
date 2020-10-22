cities = ["서울","부산","인천", \
        "대구","대전","광주","울산","수원"]
print(cities[0:6]) #0~5
print(cities[0:6:2]) #2개 단위로 건너뜀
print(cities[::-1]) #역순
print(cities[:]) #전체
print(cities[-50:50]) #전체
print(cities[::2], "AND", cities[::-1])