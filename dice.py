#!/usr/bin/python3

# サイコロの目を表示させる関数
def cat(file_name):
    try:
        with open(file_name, 'rb') as file:
            content = file.read().decode('utf-8')  # もしエンコーディングがutf-8でない場合は適切なエンコーディングを指定
            print(content)
    except FileNotFoundError:
        print(f"ファイル '{file_name}' が見つかりません。")

# loop 1000
count=1
while count <= 10:
    # 完全なランダム(module機能的random)
    # https://magazine.techacademy.jp/magazine/15821
    import random
    dice_value = random.randint(1, 6)

    # result.logへの記録
    # 14.1.7 WITHによるファイルの自動的なクローズ
    with open('result.log', mode='a') as f: # mode=aは追記できる
        f.write(str(dice_value) + '\n')

    # valueをfile名に変換する(case文)
    # https://x-tech.pasona.co.jp/media/detail.html?p=2635
    value = int(dice_value)
    if value == 1:
        value = 'one.txt'
    elif value == 2:
        value = 'two.txt'
    elif value == 3:
        value = 'three.txt'
    elif value == 4:
        value = 'four.txt'
    elif value == 5:
        value = 'five.txt'
    elif value == 6:
        value = 'six.txt'

    # output
    cat(value)

    # increment
    count += 1

    # sleep
    import time
    time.sleep(2)