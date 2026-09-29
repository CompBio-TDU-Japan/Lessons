import random

FORTUNES = [
    "今日はいい日です。",
    "注意が必要な一日です。",
    "チャンスが訪れるでしょう。",
    "休息を大切にしてください。",
    "人との出会いがありそうです。",
]

def tell_fortune(name):
    fortune = random.choice(FORTUNES)
    print(f"{name}さんの今日の運勢: {fortune}")

name = input("名前を入力してください: ")
tell_fortune(name)
