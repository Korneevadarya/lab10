# Лабораторная работа 10.
## Пакеты и модули
### Задание
Создайте пакет, содержащий 3 модуля на основе лабораторных работ №№ 7-9
Напишите запускающий модуль на основе Typer, который позволит выбирать и настраивать параметры запуска логики из пакета.
### Программа
```python

import typer
from my_package.module1 import calculate_a_recursive
from my_package.module2 import get_values
from my_package.module3 import unique_combinations

app = typer.Typer()
typer.echo(f"список модулей")
typer.echo(f"calculate a recursive: 1")
typer.echo(f"zamikanie: 2")
typer.echo(f"generator: 3")
i = int(input("Введите номер модуля какой хотите запустить: "))

@app.command()
def module1_command():
    i = int(input("Введите число которое нужно преобразовать по формуле: "))
    result = calculate_a_recursive(i)
    typer.echo(f"Result: {result}")

@app.command()
def module2_command():
    a=[]
    b = int (input ("Введите размер массива:"))
    for i in range (b):
        a.append (int (input ()))
    
    result = get_values(a)
    typer.echo(f"Result: {result}")

@app.command()
def module3_command():
    seq1 = [1, 2]
    seq2 = [3, 4]
    seq3 = [5 ,6]
    for combination in unique_combinations(seq1, seq2, seq3):
        print(combination)
    result = unique_combinations()
    typer.echo(f"Result: {result}")

if __name__ == "__main__":
    if i == 1:
        typer.run(module1_command)
    if i == 2:
        typer.run(module2_command)
    if i == 3:
        typer.run(module3_command)

```