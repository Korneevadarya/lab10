
import typer
from my_packege.module1 import calculate_a_recursive
from my_packege.module2 import get_values
from my_packege.module3 import unique_combinations

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
    result = get_values()
    typer.echo(f"Result: {result}")

@app.command()
def module3_command():
    result = unique_combinations()
    typer.echo(f"Result: {result}")

if __name__ == "__main__":
    if i == 1:
        typer.run(module1_command)
    if i == 2:
        typer.run(module2_command)
    if i == 3:
        typer.run(module3_command)
