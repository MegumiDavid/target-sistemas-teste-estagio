# 5
def reverse_str(str_input: str):
    str_list = [*str_input]
    reversed_str = ['_' for char in str_list]
    
    for i in range (0, len(str_list)):
        if (i == 0):
            reversed_str[len(str_list) - 1] = str_list[i]
        else:
            reversed_str[len(str_list) - i - 1] = str_list[i]
    return reversed_str
        
if __name__ == '__main__':
    str_input = input('String: ')
    a = reverse_str(str_input)
    print(a)