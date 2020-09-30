import random
answer = random.randint(1,100)

while True:
    try:
         number = int (input('1から100までの数値を入力して下さい：'))
    except ValueError:
        print('数字意外が入力されました。数字を入力してください')
        continue
    if 0 < number < 101:
         if answer < number:
             print('もっと小さな数字です')
         elif answer > number:
             print('もっと大きな数字です')
         else:
             break
    else:
        print('1から100以外の数値が入力されました')

print('正解',+answer)
