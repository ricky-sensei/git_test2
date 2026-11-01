times = int(input("何杯目ですか？: "))

drinks = ["ビール", "ビール", "ビール", "レモンサワー", "レモンサワー"]

# ユーザーが入力した数字をインデックスに変換
key = times - 1

if key < 0 or key > len(drinks) - 1:
    print("範囲外です")
elif key == 0:
    print(drinks[key])
    print("乾杯")
elif key == len(drinks) - 1:
    print(drinks[len(drinks) - 1])
    print("お疲れ様でした")
else:
    print(drinks[key])
    print("おいしいなー")
