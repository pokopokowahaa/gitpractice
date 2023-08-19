class OthelloPractice:
    def __init__(self):
        self.dires = [-10, -9, -8, -1, 1, 8, 9, 10]
        self.discs = ' - o x\n'
        self.bamed = [0 if i % 9 else 3 for i in range(91)]
        self.bamed[40] = self.bamed[50] = self.turn = 1
        self.bamed[41] = self.bamed[49] = 2

    def check_logic(self, bamed, move, flip=False):
        ret = False
        if not ret and not bamed[move]:
            for i in range(8):
                count = value = move + self.dires[i]
                while bamed[value] == 3 - self.turn:
                    value += self.dires[i]
                if count != value and bamed[value] == self.turn:
                    ret = value = move
                    while flip:
                        bamed[value] = self.turn
                        value += self.dires[i]
                        if bamed[value] == self.turn:
                            break
        return ret

    def play(self, com1=False, com2=True):
        end = False
        while not (move := 0):
            for i in range(9, 82):
                if self.check_logic(self.bamed, i, flip=False) and not move:
                    move = i
                print(self.discs[self.bamed[i]*2:][:2], end='')
            while move and not (end := False):
                if not com1 and self.turn == 1 or not com2 and self.turn == 2:
                    x, y = [int(i) for i in input().split()]
                    move = x + y * 9
                if self.check_logic(self.bamed, move, flip=True):
                    break
            else:
                if end:
                    break
                end, _ = True, print('pass')
            self.turn = 3 - self.turn


if __name__ == '__main__':
    OthelloPractice().play()
