import typer
import re
from paket import lab7, lab8, lab9

app = typer.Typer()


@app.command()
def run():
    typer.echo(f"список модулей")
    typer.echo(f"calculate a recursive: 1")
    typer.echo(f"zamikanie: 2")
    typer.echo(f"generator: 3")
    func = typer.prompt("введите номер функции")
    funcs = {
        "1": lab7.calculate_a_recursive,
        "2": lab8.unique_values,
        "3": lab9.unique_combinations,
    }
    for i, f in funcs.items():
        typer.echo(f"{f}: {i}")
    args = typer.prompt("введите аргументы")

    if func == "1":
        typer.echo(
            funcs[func](args)
        )

    if func == "2":
        typer.echo(
            funcs[func](int(args))
        )

    if func == "3":
        exec(f"typer.echo(funcs[func]({args}))")


if __name__ == "__main__":
    app()