def skladivanie(chislo):
    b = 0
    while True:
        print("Введите число. Для завершения оставьте пустую строку: \n")
        chislo = input()
        if chislo == '':
            break
        b = b + int(chislo)
        print(f'Сумма предыдущих чисел: {b}')

    return 'Подсчет окончен'

print(skladivanie(input('для того чтобы продолжить нажмите Enter\n')))
