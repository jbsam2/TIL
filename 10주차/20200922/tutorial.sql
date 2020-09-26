-- 테이블 생성
CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT Null
);

-- 테이블 삭제
DROP TABLE classmates;

-- 테이블 명 변경
ALTER TABLE classmates RENAME TO news;

-- 컬럼 추가
ALTER TABLE classmates ADD COLUMN created_at TEXT NOT NULL DEFAULT 1;

-- 데이터 생성
INSERT INTO classmates VALUES ('홍길동', 23, '유성구');


-- 데이터 조회

-- 모든 데이터
SELECT * FROM classmates;

-- 특정 컬럼만
SELECT name, age FROM classmates;

-- 개수 제한
SELECT name, age FROM classmates LIMIT 10;

-- 특정 위치에서부터 가져오기
SELECT name, age FROM classmates LIMIT 10 OFFSET 2;

-- 조건을 통해 가져오기
SELECT rowid, name FROM classmates WHERE address='유성구';

-- 중복 없이 가져오기
SELECT DISTINCT age FROM clasmates;

-- 데이터 삭제
DELETE FROM classmates WHERE rowid=4;

-- 데이터 수정
UPDATE classmates SET name='홍길동', address='제주' WHERE rowid=4;


-- WHERE 심화
-- WHERE 조건
SELECT * FROM users WHERE age>=30;
SELECT age, last_name FROM users WHERE age>=30 and last_name='김';

-- 갯수 세기
SELECT COUNT(*) FROM users;

-- 평균 구하기
SELECT AVG(age) FROM users WHERE age>=30;

-- 최소, 최대 : MIN, MAX

-- 와일드카드 LIKE
SELECT * FROM users WHERE age LIKE '2_';
SELECT * FROM users WHERE phone LIKE '02-%';

-- 정렬
SELECT * FROM users ORDER BY age ASC LIMIT 10;
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;

-- GROUP BY
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;


CREATE TABLE countries (
  room_num TEXT NOT NULL,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  grade TEXT NOT NULL,
  price INTEGER NOT NULL
);

INSERT INTO countries VALUES ('B203', '2019-12-31', '2020-01-03', 'suite', 900);
INSERT INTO countries VALUES ('1102', '2020-01-04', '2020-01-08', 'suite', 850);
INSERT INTO countries VALUES ('303', '2020-01-01', '2020-01-03', 'deluxe', 500);
INSERT INTO countries VALUES ('807', '2020-01-04', '2020-01-07', 'superior', 300);

ALTER TABLE countries RENAME TO hotels;

SELECT room_num, price FROM hotels 
ORDER BY price DESC LIMIT 2;

SELECT grade, COUNT(grade) FROM hotels
GROUP BY grade
ORDER BY COUNT(grade) DESC;

SELECT * FROM hotels
WHERE (room_num LIKE 'B%') or (grade='deluxe');

SELECT * FROM hotels
WHERE (room_num NOT LIKE 'B%') and (check_in='2020-01-04')
ORDER BY price;