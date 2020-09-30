import random
class GuessTheNumber:

    def __init__(self):
        self.secretNumber = random.randint(1, 100)

    def run(self):
        found_flag = False
        for i in range(1, 7):  # loop 6 times from 1.
            print('数字を入力してください。')
            guess = int(input())

            if guess < self.secretNumber:
                print('あなたの推測した数字は小さいです。')
            elif guess > self.secretNumber:
                print('あなたの推測した数字は大きいです。')
            else:
                print('答えは ' + str(guess))
                print('正解！推測した回数は、' + str(i) + ' です。')
                found_flag = True
                break

        if not found_flag:
            print('コンピュータは、 ' + str(self.secretNumber) + 'を用意してました。')


if __name__ == '__main__':
    g = GuessTheNumber()
    g.run()
