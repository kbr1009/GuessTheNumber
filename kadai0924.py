import random as rd

questionNumber = []
for i in range(2):
    questionNumber.append(rd.randint(1,5))

print("数当てゲームになります。\n二つの数字を当ててください。\n")
num1 = input("1つ目の数字を入力してください:")
num2 = input("2つ目の数字を入力してください:")

while questionNumber[0] != int(num1) or questionNumber[1] != int(num2):
    if questionNumber[0] == int(num1) or questionNumber[1] == int(num2):
        print("どちらかは合ってます！")
    else:
        print("間違い！ もう一度入力してください。\n")

    num1 = input("1つ目の数字を入力してください:")
    num2 = input("2つ目の数字を入力してください:")

print("正解です！終了！")
