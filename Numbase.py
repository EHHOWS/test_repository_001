import random as rd

# 최대 횟수, 숫자 개수 설정정
ROUND = 9
NUMBER = 3

while True:
    # 겹치지 않는 숫자 리스트 생성
    numbers = set()
    while len(numbers) != NUMBER:
        numbers.add(str(rd.randint(0, 9)))
    numbers = list(numbers)

    # Round 초기화
    Round = 0
    while True:
        # 세자리 겹치지 않는 정수 입력받기
        while True:
            try:
                user_numbers = []
                user_number = input(f"서로 다른 숫자를 {NUMBER}개 입력하시오>")
                # 숫자 3개(str) -> 리스트에 옮기기
                for i in user_number:
                    user_numbers.append(i)

                int(user_number)
                if len(user_numbers) != NUMBER:
                    raise
                elif len(set(user_numbers)) != NUMBER:
                    raise
                    
                break
            except:
                pass
        
        # ball, strike, out 개수 세기
        ball_cnt = 0
        strike_cnt = 0
        out_cnt = 0
        
        for i in range(NUMBER):
            if user_numbers[i] == numbers[i]:
                strike_cnt += 1
        for i in range(NUMBER):
            if user_numbers[i] in numbers:
                ball_cnt += 1

        ball_cnt = ball_cnt - strike_cnt
        out_cnt = NUMBER - ball_cnt - strike_cnt
        Round += 1
        
        # 결과 발표
        print(f"{strike_cnt} strike {ball_cnt} ball {out_cnt} out ({Round}/{ROUND})")

        # 끝 발표
        if strike_cnt == NUMBER:
            print("YOU WON")
            print(f"NUMBER WAS {numbers[0]}{numbers[1]}{numbers[2]}")
            break
        if Round == ROUND:
            print("YOU DEFEAT")
            print(f"NUMBER WAS {numbers[0]}{numbers[1]}{numbers[2]}")
            break
    
    # 계속?
    will_continue = input("계속하시겠습니까?(Y/N)> ")
    if will_continue.upper() == "Y":
        print("\n" * 2)
        pass
    else:
        break
