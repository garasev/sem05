import psutil
import main


def memory_peak(function, length=5):
    p = psutil.Process()
    mem1 = p.memory_info().peak_wset

    s1 = main.random_string(length)
    s2 = main.random_string(length)
    function(s1, s2, False)

    mem2 = p.memory_info().peak_wset
    print(mem2 - mem1)


if __name__ == '__main__':
    memory_peak(main.calc_func[0], 1)
    memory_peak(main.calc_func[0], 2)
    memory_peak(main.calc_func[0], 3)
    memory_peak(main.calc_func[0], 4)
    memory_peak(main.calc_func[0], 5)
