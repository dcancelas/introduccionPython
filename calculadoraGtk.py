import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class CalculadoraGtk(Gtk.Window):
    saida_entry = Gtk.Entry()
    saida = ""

    def __init__(self):
        Gtk.Window.__init__(self, title="CalculadoraGtk")
        self.set_size_request(300, 300)

        # Propiedades do Grid
        grid = Gtk.Grid()
        self.add(grid)
        grid.set_row_homogeneous(5)
        grid.set_column_homogeneous(3)
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)
        grid.set_margin_top(10)
        grid.set_margin_bottom(10)
        grid.set_margin_start(10)
        grid.set_margin_end(10)

        # Propiedades do Entry
        self.saida_entry.set_text("")
        self.saida_entry.set_editable(False)
        self.saida_entry.set_margin_bottom(5)

        # Botóns da aplicación
        botonC = Gtk.Button(label="C")
        botonC.connect("clicked", self.on_btn_clicked, "C")
        botonAC = Gtk.Button(label="AC")
        botonAC.connect("clicked", self.on_btn_clicked, "AC")

        boton1 = Gtk.Button(label="1")
        boton1.connect("clicked", self.on_btn_clicked, "1")
        boton2 = Gtk.Button(label="2")
        boton2.connect("clicked", self.on_btn_clicked, "2")
        boton3 = Gtk.Button(label="3")
        boton3.connect("clicked", self.on_btn_clicked, "3")
        boton4 = Gtk.Button(label="4")
        boton4.connect("clicked", self.on_btn_clicked, "4")
        boton5 = Gtk.Button(label="5")
        boton5.connect("clicked", self.on_btn_clicked, "5")
        boton6 = Gtk.Button(label="6")
        boton6.connect("clicked", self.on_btn_clicked, "6")
        boton7 = Gtk.Button(label="7")
        boton7.connect("clicked", self.on_btn_clicked, "7")
        boton8 = Gtk.Button(label="8")
        boton8.connect("clicked", self.on_btn_clicked, "8")
        boton9 = Gtk.Button(label="9")
        boton9.connect("clicked", self.on_btn_clicked, "9")
        boton0 = Gtk.Button(label="0")
        boton0.connect("clicked", self.on_btn_clicked, "0")

        boton_sumar = Gtk.Button(label="+")
        boton_sumar.connect("clicked", self.on_btn_clicked, "+")
        boton_restar = Gtk.Button(label="-")
        boton_restar.connect("clicked", self.on_btn_clicked, "-")
        boton_multi = Gtk.Button(label="×")
        boton_multi.connect("clicked", self.on_btn_clicked, "×")
        boton_dividir = Gtk.Button(label="÷")
        boton_dividir.connect("clicked", self.on_btn_clicked, "÷")
        boton_punto = Gtk.Button(label=".")
        boton_punto.connect("clicked", self.on_btn_clicked, ".")
        boton_igual = Gtk.Button(label="=")
        boton_igual.connect("clicked", self.on_btn_clicked, "igual")

        # Posición no Grid
        grid.attach(self.saida_entry, 0, 0, 4, 1)
        grid.attach(botonC, 2, 1, 1, 1)
        grid.attach(botonAC, 3, 1, 1, 1)
        grid.attach(boton1, 0, 2, 1, 1)
        grid.attach(boton2, 1, 2, 1, 1)
        grid.attach(boton3, 2, 2, 1, 1)
        grid.attach(boton4, 0, 3, 1, 1)
        grid.attach(boton5, 1, 3, 1, 1)
        grid.attach(boton6, 2, 3, 1, 1)
        grid.attach(boton7, 0, 4, 1, 1)
        grid.attach(boton8, 1, 4, 1, 1)
        grid.attach(boton9, 2, 4, 1, 1)
        grid.attach(boton0, 0, 5, 1, 1)
        grid.attach(boton_punto, 1, 5, 1, 1)
        grid.attach(boton_igual, 2, 5, 1, 1)
        grid.attach(boton_dividir, 3, 2, 1, 1)
        grid.attach(boton_multi, 3, 3, 1, 1)
        grid.attach(boton_restar, 3, 4, 1, 1)
        grid.attach(boton_sumar, 3, 5, 1, 1)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btn_clicked(self, boton, valor):
        if valor == "C" or valor == "AC" or valor == "igual":
            if valor == "C":
                self.saida = self.saida[:-1]
            if valor == "AC":
                self.saida = ""
            if valor == "igual":
                self.saida = ""
        else:
            self.saida = self.saida + valor

        if valor != "igual":
            self.saida_entry.set_text(self.saida)


if __name__ == '__main__':
    CalculadoraGtk()
    Gtk.main()
