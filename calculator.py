def main():
    a = int(input())
    flag = True
    if a == 7532:
        print("Software Engineering Class")
        return
    while True:
        operator = input()
        if operator == 7532:
            print("Software Engineering Class")
            return
        elif operator == '=':
            if not flag:
                print('ERROR!')
            else:
                print(a)
            break
        if operator == "-":
            a = sub(a)
            if a is None:
                break

        elif operator == "+":
            a = add(a)
            if a is None:
                break
        elif operator == '*':
            a = mul(a)
            if a is None:
                break

        elif operator == '!':
            if not flag:
                print('[ERROR] Input Error')
                a = None
            else:
                a = facto(a)
                if a is None:
                    break

        else:
            flag = False

def sub(a):
    b = int(input())
    if b == 7532:
        print("Software Engineering Class")
        return None
    else:
        return a - b

def add(a):
    b = int(input())
    if b == 7532:
        print("Software Engineering Class")
        return None
    else:
        return a + b

def mul(a):
    b = int(input())
    if b == 7532:
        print("Software Engineering Class")
        return None
    else:
        return a * b

def facto(a):
    if a == 0 or a == 1:
        return 1
    elif a < 0:
        print("[ERROR] Out Of Range")
        return None
    else:
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result

if __name__ == "__main__" :
    
    main()
