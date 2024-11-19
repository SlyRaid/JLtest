from inspect import signature


def strict(func):
    def wrapper(*args, **kwargs):
        func_signature = signature(func)

        for i, arg_value in enumerate(args):
            arg_name = list(func_signature.parameters.keys())[i]
            arg_type = func.__annotations__.get(arg_name)
            if arg_type is not None and not isinstance(arg_value, arg_type):
                raise TypeError()

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # 3
print(sum_two(1, 2.4))  # TypeError
