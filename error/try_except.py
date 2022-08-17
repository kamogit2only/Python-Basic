def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print("0で割ることは出来ません、正しい値を入力してください。")
        print(e)
    except ValueError:
        print("数字を入力してください。")
    else:    
        print(f"一人 {each}円です。")
    finally:
        print("ご利用ありがとうございます。")
    
    
if __name__ == "__main__":
    split_bill(10000)