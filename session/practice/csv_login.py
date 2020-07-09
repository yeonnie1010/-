# TODO_0 : csv 모듈 불러오기
import csv

information_file_path = 'information.csv'

def read_info_csv():
    with open(information_file_path, "r") as f:
        info_csv_data = csv.reader(f)

    return info_csv_data

def write_info_csv(info_csv_data):
    with open(information_file_path, 'w') as f:
        wr_info_csv_data = csv.writer(f)
        wr_info_csv_data.writerow(['id', 'pw'])
        wr_info_csv_data.writerow(['kuy7970', 'a123456789'])

#####################################################3
        
def user_input():
    try:
        id, pw = map(str, input("아이디와 비밀번호를 차례로 입력해주세요 : ").split())
        return id, pw
    except:
        print("올바르지 않은 입력입니다!")
        id, pw = user_input()
        return id, pw
# Q. 여기서 'map'은 뭐지?


# TODO_1 : signin 함수를 구현해서 로그인 시키기
# 1. csv 파일에서 존재하는 아이디인지 확인하기
# 2. 존재하면 비밀번호 맞는지 체크
# 3. 비밀번호도 맞으면 로그인성공 출력하기

def id_right() :

    for line in info_csv_data :
        if(line[0] == 'id') :
            continue
        if(line[0] == 'id') :
            return True
    return False


def pw_right() :

    for line in list(info_csv_data)[1:] :
        if(line[1] == 'pw') :
            continue
        if(line[0] == 'pw') :
            return True
    return False


def signin(id, pw):
    if(id_right(id)):
        if(pw_right(pw)) :
            print("성공적으로 로그인하셨습니다.")
            return True
    print("로그인이 실패하였습니다. 다시 시도해주세요.")
    return False


# TODO_2 : csvfile 에 유저가 존재하는지 확인하는 함수 구현해서 호출하기
# 1. 아이디를 기준으로 존재하는 유저인지 확인
# 2. 존재한다면 다시 아이디를 입력받고,
# 3. 존재하지 않는다면 다음 단계로 넘겨주기

def user_right(id):
    if(id_right(id)):
        id = input("이미 존재하는 ID입니다. 다시 입력해주세요.")
        id = user_right(id)
    return


# TODO_3 : csvfile 에 등록되어있는 형태로 유저 등록하는 함수 구현하기
# 1. 아이디와 비밀번호를 그냥 데이터로 받아서 추가해보기
# 2. 아이디와 비밀번호를 '딕셔너리' 형태로 받아서 추가해보기 (프로그래밍 실력의 기본은 구글링! 최대한 구글링 해보세요!!)
# Q. 'w'으로 받아야 할듯??

def join(id,pw) :
    with open('information_file_path','a', newline='') as f :
        wr_info_csv_data = csv.writer(f)
        wr_info_csv_data.writerow(['id', 'pw'])

def join(dictionary):
    with open('information_file_path','a', newline='') as f :
        wr = csv.writer(f)
        wr.wrtierow(dictionary.values())

# TODO_4 : csvfile 에서 현재 가입되어 있는 유저 전부 출력하기
def userlist():
    print("현재 존재하는 유저 :")
    with open(information_file_path, "r") as f:
        info_csv_data = csv.reader(f)
        for information in list(info_csv_data)[1:]:
            print(inforamtion[0])


def exitcheck():
    stop = int(input("\n계속하시려면 0, 종료하시려면 1을 눌러주세요. : "))
    if stop == 0:
        start()
    elif stop == 1:
        exit()


def start():
##여기 이렇게 하는 거 맞나?
    path = "C:\\Users\\user\\Desktop\\ai_school\\session\\information.csv"
    print('csv 로 데이터 다루기 로그인 예제')
    signup_or_login = input('1 - 로그인 / 2 - 회원가입 : \n')

    if signup_or_login ==1 :
        id, pw = user_input()
        # TODO_5 : 위의 TODO1 참고 후 signin 함수 실행하기
        signin(id, pw)
    elif signup_or_login ==2 :
        id = input("ID : ")
        id = is_user_right(id)
        pw = input("PW : ")
      # TODO_6 : 회원가입을 아이디와 비밀번호만 받아서 진행할 것
      # 1. 존재하는지 확인 (위의 TODO_2의 함수 활용)
      # 2. 문제 없으면 회원가입 완료 후 userlist() 함수 구현

        dict_user = {
            "id": id,
            "pw": pw
        }
        # signup(id, pw)
        signup(dict_user)
        userlist()
    else:
        print("올바른 숫자를 입력하세요!")

    exitcheck()


start()

# TODO_7 : 깃헙에 업로드하고 깃헙 주소 제출!
