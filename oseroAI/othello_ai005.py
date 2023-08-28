class OthelloPractice:
    def __init__(self):
        self.dires = [-10, -9, -8, -1, 1, 8, 9, 10]
        self.discs = ' - o x\n'
        self.bamed = [0 if i % 9 else 3 for i in range(91)]
        self.bamed[40] = self.bamed[50] = self.turn = 1
        self.bamed[41] = self.bamed[49] = 2

        self.evalu = [0 for i in range(91)]

        self.evalu[10] = 10
        self.evalu[17] = 10
        self.evalu[73] = 10
        self.evalu[80] = 10

        self.evalu[11] = -5
        self.evalu[16] = -5
        self.evalu[19] = -5
        self.evalu[20] = -5
        self.evalu[25] = -5
        self.evalu[26] = -5
        self.evalu[64] = -5
        self.evalu[65] = -5
        self.evalu[70] = -5
        self.evalu[71] = -5
        self.evalu[74] = -5
        self.evalu[79] = -5

        self.evalu[12] = 1
        self.evalu[15] = 1
        self.evalu[28] = 1
        self.evalu[30] = 1
        self.evalu[33] = 1
        self.evalu[35] = 1
        self.evalu[55] = 1
        self.evalu[57] = 1
        self.evalu[60] = 1
        self.evalu[62] = 1
        self.evalu[75] = 1
        self.evalu[78] = 1


 
    def loop(self, bamed, move, depth, turn, move1):
        next_bamed = bamed.copy()
        next_depth = depth - 1
        next_turn = 3 - turn
        evalu = -5
        tmp_evalu = 0
        self.check_logic(next_bamed, turn,  move, flip=True)

        if next_depth == 0:
            print("self.evalu",self.evalu[move],"move",move)
            evalu = 3*self.evalu[move] 
            print("evalu ",evalu)
        elif next_turn == 2:

            for i in range(9, 82):
                if self.check_logic(next_bamed, turn, i, flip=False):
                    tmp_evalu = self.loop(next_bamed, i, next_depth, next_turn, move1)
                if tmp_evalu >= evalu:
                    evalu = tmp_evalu
                    move1 = i
                

        else:

            for i in range(9, 82):
                if self.check_logic(next_bamed, turn, i, flip=False):
                    tmp_evalu = self.loop(next_bamed, i, next_depth, next_turn, move1)
                if tmp_evalu <= evalu:
                    evalu = tmp_evalu

        return evalu


    

    def check_logic(self, bamed, turn,  move, flip=False):
        ret = False
        if not ret and not bamed[move]:
            for i in range(8):
                count = value = move + self.dires[i]
                while bamed[value] == 3 - turn:
                    value += self.dires[i]
                if count != value and bamed[value] == turn:
                    ret = value = move
                    while flip:
                        bamed[value] = turn
                        value += self.dires[i]
                        if bamed[value] == turn:
                            break
        return ret

    def play(self, com1=False, com2=True):
        end = False
        move1 = 0
        while not (move := 0):
            score = -5
            for i in range(9, 82):
                tmp_score = self.loop(self.bamed, i, 2, self.turn, move1)
                if tmp_score >= score:
                    score = tmp_score
                    move = i
                print("score ",score," move ",move)

            for i in range(9, 82):
                print(self.discs[self.bamed[i]*2:][:2], end='')
            print(move)
            while move and not (end := False):
                if not com1 and self.turn == 1 or not com2 and self.turn == 2:
                    x, y = [int(i) for i in input().split()]
                    move = x + y * 9
                if self.check_logic(self.bamed, self.turn,  move, flip=True):
                    break
            else:
                if end:
                    break
                end, _ = True, print('pass')
            self.turn = 3 - self.turn


if __name__ == '__main__':
    OthelloPractice().play()
