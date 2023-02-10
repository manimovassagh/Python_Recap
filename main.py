def main():
    print('Hi Mani from main func')
    secondary_function()
    my_input = input('Give me some items mani! \n')
    print('Nice to meet you ', my_input)


def secondary_function():
    print('Hi from secondary function')


seconds = 12
minutes = seconds / 60
print(minutes)
# sample comment

if __name__ == '__main__':
    main()
