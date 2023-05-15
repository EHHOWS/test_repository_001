import random as rd

TURN = 10

class Compare():
    trust = "trust"
    betray = "betray"
    
    def add(self, mine, others) -> int:
        if mine + others == self.trust + self.betray:
            return 0
        elif mine + others == self.trust + self.trust:
            return 3
        elif mine + others == self.betray + self.trust:
            return 5
        elif mine + others == self.betray + self.betray:
            return 1
cp = Compare()

class Memory():
    def __init__(self):
        self.mine = []
        self.others = []
        self.result = []
    def memorize(self, mine, others):
        self.mine.append(mine)
        self.others.append(others)
        self.result.append(cp.add(mine, others))

class Character():
    def __init__(self, strategy=0):
        self.strategy = strategy
        self.memory = Memory()
    def scoring(self) -> int():
        score = 0
        for result in self.memory.result:
            score += result
        self.score = score
        return score
    def choice(self, turn):
        if self.strategy == 0: # 랜덤
            return rd.choice([cp.trust, cp.betray])
        elif self.strategy == 1: # 랜덤으로 선택 후, 고수
            if turn == 0:
                return rd.choice([cp.trust, cp.betray])
            else:
                return self.memory.mine[turn - 1]
        elif self.strategy == 2: # 일단 신뢰 후, 상대방 이전 선택 모방
            if turn == 0:
                return cp.trust
            else:
                return self.memory.others[turn - 1]
        elif self.strategy == 3: # 무조건 신뢰하다, 상대방이 3번 이상 배신하면 무조건 배신
            if len(self.memory.others) == len(set(self.memory.others)) + 2:
                return cp.betray
            else:
                return cp.trust
        elif self.strategy == 4: # 무조건 신뢰
            return cp.trust
        elif self.strategy == 5: # 무조건 배신
            return cp.betray
        


while True:
    ask = input("start?> ")
    if ask.lower() == "start" or ask.lower() == "s" or ask.lower() == "y" or ask.lower() == "yes" or ask.lower() == "start" or ask.lower == "strt" or ask == "네" or ask == "시작" or ask == "ㅇ" or ask == "ㅇㅇ" or ask.lower() == "o" or ask.lower() == "oo":
        rndm_strtg = rd.randint(0, 5)
    else:
        try:
            rndm_strtg = int(ask)
        except:
            print("END")
            break
    
    turn = 0
    me = Character()
    other = Character(rndm_strtg)
    print("START")
    while turn != TURN:
        mine = input("\ntrust or not> ")
        if mine.lower() == "trust" or mine.upper() == "Y" or mine.lower() == "yes" or mine.upper() == "T" or mine == "네" or mine == "신뢰" or mine == "tlsfhl" or ask == "ㅇ" or ask == "ㅇㅇ" or ask.lower() == "o" or ask.lower() == "oo":
            mine = cp.trust
        else:
            mine = cp.betray
        others = other.choice(turn)

        me.memory.memorize(mine, others)
        other.memory.memorize(others, mine)

        print(f"you give {mine.upper()} and other give {others.upper()},\nso you got {me.memory.result[turn]} score and other got {other.memory.result[turn]} ({turn + 1}/{TURN})")

        turn += 1

    print()
    if me.scoring() > other.scoring():
        print(f"WON({me.score} : {other.score})")
    elif me.scoring() == other.scoring():
        print(f"DRAW({me.score} : {other.score})")
    else:
        print(f"DEFEAT({me.score} : {other.score})")