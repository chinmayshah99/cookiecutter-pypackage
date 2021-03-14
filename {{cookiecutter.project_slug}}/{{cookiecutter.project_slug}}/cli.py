"""Console script for {{cookiecutter.project_slug}}."""
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    typer.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli")
    typer.echo("See click documentation at https://typer.tiangolo.com/")
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    app()