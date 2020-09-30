import random
class GuessTheNumber:

    def __init__(self):
        self.secretNumber = random.randint(1, 100)

    def run(self):
        found_flag = False
        for i in range(1, 100):
            try:
                 guess = int (input('1から100までの数値を入力して下さい：'))
            except ValueError:
                print('数字意外が入力されました。数字を入力してください')
                continue

            if guess < self.secretNumber:
                print('あなたの推測した数字は小さいです。')
            elif guess > self.secretNumber:
                print('あなたの推測した数字は大きいです。')
            else:
                print('正解！推測した回数は、' + str(i) + ' です。')
                print(self.secretNumber)
                found_flag = True
                break

if __name__ == '__main__':
    g = GuessTheNumber()
    g.run()
