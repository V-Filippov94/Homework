# Написать декоратор `count_runs`,
# который считает количество вызовов функции,
# сохраняет это значение в атрибуте объета функции:
#
# Пример:
#
# ```python
# @count_runs
# def sum2(a: int, b: int) -> int:
#     print(a + b)
#
#
# print(sum2.run_count)
# sum2(1, 2)
# print(sum2.run_count)
# sum2(1, 2)
# print(sum2.run_count)
# ```
#
# ```
# 0
# 3
# 1
# 3
# 2
# ```

count = 0


def count_run(func):
    def fake(*args, **kwargs):
        global count
        result = func(*args, **kwargs)
        count += 1
        fake.run_count = count
        return result
    return fake


@count_run
def sum2(a: int, b: int) -> int:
    return a + b


def main():
    sum2(1, 2)
    print(sum2.run_count)
    sum2(1, 5)
    print(sum2.run_count)
    sum2(1, 5)
    print(sum2.run_count)


if __name__ == '__main__':
    main()