import json
import sqlite3

students_file_path = './students.json'

# print(students_json_data['students'])


def read_students_json():
    with open(students_file_path, "r") as json_file:
        students_json_data = json.load(json_file)

    return students_json_data


def write_students_json(students_json_data):
    with open(students_file_path, 'w') as outfile:
        json.dump(students_json_data, outfile, ensure_ascii=False, indent=4)


conn = sqlite3.connect('students_list.db')
cur = conn.cursor()


cur.execute(
    CREATE TABLE students_list (
        "이름" TEXT, "나이" INT, "직업" TEXT, "ID" TEXT NOT NULL, "PW" TEXT);
    INSERT INTO students_list("이름", "나이", "직업", "ID", "PW") VALUES (students_json_data);
    INSERT INTO students_list() VALUES('순돌이', '4', '반려견', 'gosundol', 'abcde');
)


conn.commit()

conn.close()

cur.execute("SELECT * FROM students_list")


