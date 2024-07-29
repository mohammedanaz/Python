import traceback

try:
    x = 1/0
except ZeroDivisionError:
    # traceback.print_exc()
    print('error')