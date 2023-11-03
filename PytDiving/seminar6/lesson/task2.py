import guess
import sys
init_numbers = list(map(int, [i for i in sys.argv][1:]))
guess.guess_f(*init_numbers)

# запуск через терминал командой: python hw_task2.py 1 10 3