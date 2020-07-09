# 1주일 내용 10문제로 끝내기

# 1. 파이썬 조건문을 활용하여 장발장은 빵을 못먹게 하기
# - 실행 예시 : "장발장 차례 입니다, 빵을 드릴 수 없습니다."
# - 실행 예시 : "홍길동 차례 입니다, 빵을 하나 드리겠습니다."

people = ['홍길동', '성진', '심청이', '장발장', '심봉사']
for name in people:
    if name == '장발장':
        print("장발장 차례 입니다, 빵을 드릴 수 없습니다.")
    else:
        print(f"{name} 차례 입니다, 빵을 하나 드리겠습니다.")

# --------------------------------------------------------

# 2. 1번 문제의 구현된 부분을 함수로 바꾸기
# - 조건 : 입력값(사람 한 명씩) 을 받아서 빵을 먹으면 안되는 사람이면 0을, 먹어도 되면 1을 반환하기
# - 실행 예시 : "홍길동은 빵을 먹을 수 있는 사람 입니다."
# - 실행 예시 : "장발장은 빵을 먹을 수 있는 사람 입니다."
# 반복문을 활용하여 5 명 전원 다 출력 할 것

def eating_bread(name):
    return 0 if name == '장발장' else 1


for name in people:
    if eating_bread(name):
        print(f"{name}은 빵을 먹을 수 없는 사람 입니다.")
    else:
        print("장발장은 빵을 먹을 수 있는 사람 입니다.")

# --------------------------------------------------------

# 3. 지역변수와 전역변수 이해하기

# 아래의 코드는 num_stamp 라는 전역변수를 함수 내에서 global 명령을 통해 수정가능하게 억지로 만든상태이다.
# 하지만, 함수의 기능과 본질을 생각하면 아래의 예시는 굉장히 바람직하지 못하다!
# global 명령은 안쓰는 것이 좋다!
# 그렇다면, global 명령을 사용하지 않고 아래의 로직을 함수의 입력값과 반환값을 활용하여 수정해보기!

num_stamp = 0  # 쿠폰 스탬프가 찍힌 횟수 (전역변수)


def stamp(pl_stamp):
    """쿠폰 스탬프가 찍힌 횟수를 증가시키고, 화면에 출력한다."""
    pl_stamp += 1
    print(pl_stamp)
    return pl_stamp


num_stamp = stamp(num_stamp)  # 화면에 1이 출력된다
num_stamp = stamp(num_stamp)  # 화면에 2가 출력된다


# --------------------------------------------------------

# 4. 클래스 이용하기
# 요구사항
# - 교통수단 클래스 만들기 (속성 : 이름, 가격, 출발시간, 도착시간 / 기능 : 출발시간, 도착시간 보기)
# - 비행기 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 수하물 가능여부
# 기능 : 출발시간, 도착시간 보기, 수하물 맡기기(수하물이 가능하면 "수하물을 맡겼습니다!"출력, 불가능하면 "이 비행기는 수하물을 못맡깁니다!" 출력)
# - 기차 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 좌석등급
# 기능 : 출발시간, 도착시간 보기, 좌석등급 보기

# 클래스를 상속을 활용해서 효율적으로 만들어 볼것! (메소드 오버라이딩)
# 두 개 이상의 인스턴스를 비행기, 기차 각각 만들어 볼것

class transport :
    def __init__(self, name, price, de_time, arr_time):
        self.name = name
        self.price = price
        self.de_time = de_time
        self.arr_time = arr_time

    def departure_time(self):
        print(f"출발시간은 {self.de_time}입니다.")

    def arrival_time(self):
        print(f"도착시간은 {self.de_arr}입니다.")


class airplane(transport):
    def __init__(self, name, price, de_time, arr_time, baggage):
        super().__init__(name, price, de_time, arr_time)
        self.baggage = baggage

    def fin_baggaged(self):
        if self.baggage:
            print("수하물을 맡곁습니다!")
        else:
            print("이 비행기는 수하물을 못 맡깁니다!")


class train(transport):
    def __init__(self, name, price, de_time, arr_time, seat):
        super().__init__(name, price, de_time, arr_time)
        self.seat = seat

    def show_seat_grade(self):
        print(f"좌석 등급은 {self.seat}입니다.")


KA147 = airplane('아시아나147', 2000000, '07:40', '18:30', True)
CN258 = airplane('남방항공258', 180000, '10:00', '14:00', False)

for airplane in [KA147, CN258] :
    print(
        airplane.name()
        airplane.de_time()
        airplane.arr_time()
        airplane.fin_baggaged())

ktx = Train('KTX', 46000, '11:00', '14:00', '특실')
srt = Train('STX', 40000, '16:00', '19:00', '일반석')

for train in [ktx, stx]:
    print(
        train.name()
        train.de_time()
        train.arr_time()
        train.show_seat_grade())

# --------------------------------------------------------

# 5. 문자열 이용하기


# 파이썬 io 하는거 2 문제
