import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class CalculadoraGtk(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="CalculadoraGtk")

        grid = Gtk.Grid()
        self.add(grid)
        boton1 = Gtk.Button(label="1")
        boton2 = Gtk.Button(label="2")
        boton3 = Gtk.Button(label="3")
        boton4 = Gtk.Button(label="4")
        boton5 = Gtk.Button(label="5")
        boton6 = Gtk.Button(label="6")
        boton7 = Gtk.Button(label="7")
        boton8 = Gtk.Button(label="8")
        boton9 = Gtk.Button(label="9")
        boton_sumar = Gtk.Button(label="+")
        boton_restar = Gtk.Button(label="-")
        boton_multi = Gtk.Button(label="×")
        boton_dividir = Gtk.Button(label="÷")

        grid.attach(boton1, 0, 0, 2, 4)
        grid.attach_next_to(boton2, boton1, Gtk.PositionType.RIGHT, 2, 4)
        grid.attach_next_to(boton3, boton2, Gtk.PositionType.RIGHT, 2, 4)
        grid.attach_next_to(boton4, boton1, Gtk.PositionType.BOTTOM, 2, 4)
        grid.attach_next_to(boton5, boton4, Gtk.PositionType.RIGHT, 2, 4)
        grid.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 2, 4)
        grid.attach_next_to(boton7, boton4, Gtk.PositionType.BOTTOM, 2, 4)
        grid.attach_next_to(boton8, boton7, Gtk.PositionType.RIGHT, 2, 4)
        grid.attach_next_to(boton9, boton8, Gtk.PositionType.RIGHT, 2, 4)
        grid.attach_next_to(boton_sumar, boton3, Gtk.PositionType.RIGHT, 2, 4)
        grid.attach_next_to(boton_restar, boton_sumar, Gtk.PositionType.BOTTOM, 2, 4)
        grid.attach_next_to(boton_multi, boton_sumar, Gtk.PositionType.RIGHT, 2, 4)
        grid.attach_next_to(boton_dividir, boton_multi, Gtk.PositionType.BOTTOM, 2, 2)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == '__main__':
    CalculadoraGtk()
    Gtk.main()
