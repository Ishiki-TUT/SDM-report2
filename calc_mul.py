#!/usr/bin/python3

import re
import sys
                
def calc(A,B):
        # 入力値を数値に変更(整数または浮動小数点数)
        try:
                a = int(A)
                b = int(B)
        except ValueError:
                return -1   # 数値に変換出来ないと場合はエラーとして扱う

        # 最大値はsys.maxsizeより大きい数には対応しない
        if a > sys.maxsize or b > sys.maxsize:
                return -1   # sys.maxsizeを超える数値はエラーとする
        
        # バリデーション：0 < A, B < 1000
        if a > 0 and b > 0:
                result =  a * b #計算結果を返す
                return result if result <= sys.maxsize else -1  # 結果がsys.maxsizeを超えないよう制限
        
        else:
                return -1 # 条件外の場合はエラーとして扱う
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                result = calc(A, B)
                if result == -1:
                        print('Invalid input or out of range (0 < A, B < 1000)')
                else:
                        print(f'input A * input B = {result}')
                matchstring = input("Enter 'end' to stop or press Enter to continue: ")

if __name__ == '__main__':
	main()
