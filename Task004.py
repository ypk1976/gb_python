# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

S = int(input("How many paper cranes did children make? "))
boy = S/6
katya = boy * 4
print(f"Each boy created {int(boy)} cranes")
print(f"Katya created {int(katya)} cranes")

