# data_user = list(input("Enter you string: "))
# shift = int(input("How many to shift the string: "))
# for x in data_user:
#     # получаем значение ASCII
#     a = int(ord(x))
#     b = a-shift
#     # декодируем символ обратно через функцию chr
#     print(str(chr(b)), end='')


def select_method():
    while True:
        question = input('\nSelect method coding (c) or decoding (d): ')
        question = question.lower()
        if question == 'c':
            coding(question)
        elif question == 'd':
            decoding(question)
        else:
            print('Invalid choice!')


def coding(question):
    if question == "c":
        data_user = list(input("Enter you string: "))
        shift = int(input("How many to shift the string: "))
        for x in data_user:
            a = int(ord(x))
            b = a+shift
            print(str(chr(b)), end='')


def decoding(question):
    if question == "d":
        data_user = list(input("Enter you string: "))
        shift = int(input("How many to shift the string: "))
        for x in data_user:
            a = int(ord(x))
            b = a - shift
            print(str(chr(b)), end='')


select_method()

