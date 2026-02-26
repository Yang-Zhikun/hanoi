steps = 1

def hanoi(A: str, B: str, C: str, n: int) -> None:
    global steps
    # 如果只有一个，直接将A柱的圆盘移到C柱
    if n == 1:
        print(f"{steps}: 将{A}柱最上面的圆盘移到{C}柱")
        steps += 1
        return
    
    # 如果有n个圆盘，先将n-1个移到B
    hanoi(A, C, B, n-1)
    # 再将A柱剩下的一个圆盘移到C
    print(f"{steps}: 将{A}柱最上面的圆盘移到{C}柱")
    steps += 1
    # 最后将B柱的n－1个圆盘移到C柱
    hanoi(B, A, C, n-1)


print("输入初始圆盘数：", end = '')
n = int(input())
hanoi('A', 'B', 'C', n)
#print(steps)
