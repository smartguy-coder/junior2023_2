import time

# print
# n = print
# n(55555)

# NO PARAMETERS
# def decorator_allow_only_str_args(func):
#     def wrapper(*args, **kwargs):
#         arguments = list(args) + list(kwargs.values())
#         for arg in arguments:
#             if not type(arg) == str:
#                 return ''
#
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
#
# @decorator_allow_only_str_args
# def my_function(value: str, value2: str) -> str:
#     return value + value2 + '!!!!'
#
# @decorator_allow_only_str_args
# def my_second_function(value: str) -> str:
#     return value * 3
#
# # func = decorator(my_function)('hhh')
# # print(func)
# # print(my_function.__name__)
# print(my_function(5, value2='6'))
# print(my_second_function(5))

# WITH PARAMETERS
# def auth(func):
#     def wrapper(*args, **kwargs):
#         user = input('Enter your name >>> ')
#         password = input('Enter your password >>> ')
#         if user == 'jj' and password == '1111':
#             result = func(*args, **kwargs)
#             return result
#         return 'You cannot provide the operation'
#     return wrapper
#
#
# def decorator_allow_only_str_args(check_args=False):
#     def inner_wrapper(func):
#
#         def wrapper(*args, **kwargs):
#             if check_args:
#                 arguments = list(args) + list(kwargs.values())
#                 for arg in arguments:
#                     if not type(arg) == str:
#                         return ''
#             result = func(*args, **kwargs)
#             return {'func_name': func.__name__, 'result': result}
#
#         return wrapper
#
#     return inner_wrapper
#
#
# @decorator_allow_only_str_args()
# def my_function(value: str, value2: str) -> str:
#     return value + value2 + '!!!!'
#
# @auth
# @decorator_allow_only_str_args(check_args=True)
# def my_second_function(value: str) -> str:
#     return value + 'fffffff'
#
# # func = decorator(my_function)('hhh')
# # print(func)
# # print(my_function.__name__)
# print(my_function('5', value2='6'))
# print(my_second_function('55555555'))
# print(my_second_function('9999999'))
# print(my_second_function('5'))

def returns_only_int(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return int(result)
    return wrapper


@returns_only_int
def calc_sphere_volume(radius: int):
    return (4/3) * 3.1416 * (radius ** 3)

@returns_only_int
def mult_to_two(length: int | float):
    return length * 2

print(calc_sphere_volume(5))
print(mult_to_two(5))