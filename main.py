def test_function():
    # nonlocal inner_function
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
# inner_function()    # ошибка: NameError: name 'inner_function' is not defined.
                    # Did you mean: 'test_function'?
#  Я не могу вызвать её вне функции test_function, т.к они в разных пространствах
# test_function()   # выводит на печать строку: 'Я в области видимости функции test_function'
