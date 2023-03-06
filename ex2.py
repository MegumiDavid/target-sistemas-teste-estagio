# 1

def make_fib(input_num: int):
    fib_list = [0,1]
    index = 0
    while True:
        new_num = fib_list[index] + fib_list[index+1]
        
        if (new_num == input_num):
            return True
        if (new_num > input_num):
            return False
            
        fib_list.append(new_num)
        index+=1
        
        
if __name__ == '__main__':
    input_num = int(input('Número: '))
    is_fib = make_fib(input_num)

    if (is_fib):
        print(f'O número {input_num} pertence a sequência de Fibonacci')
    else:
        print(f'O número {input_num} NÃO pertence a sequência de Fibonacci')