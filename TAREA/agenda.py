# -*- coding: utf-8 -*-
# python agenda.py --buscar NAME
# python agenda.py --agregar NAME
# python agenda.py --borrar NAME

import typer
from data_agenda import agenda
from rich.console import Console
from rich.table import Table

app = typer.Typer()

#print(agenda)

@app.command()
def buscar(name: str) -> list[str]:
    console = Console()
    table = Table("Nombre","Apellido","Email","Telefono")
    num_contactos = 0
    for item in agenda:
        if name.upper() in item.get('nombre','').upper():
            col1 = item['nombre']
            col2 = item['apellido']
            col3 = item['email']
            col4 = item['telefono']
            table.add_row(col1,col2,col3,col4)
            num_contactos +=1
    if num_contactos > 0:
        console.print(table)
    else:
        print("No hay contactos que coincidan con la búsqueda.")


@app.command()
def agregar(name: str) -> None:
    pass


@app.command()
def borrar(name: str) -> None:
    pass


if __name__ == "__main__":
    app()