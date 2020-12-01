import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class FormularioGtk(Gtk.Window):
    saida_entry = Gtk.Entry()
    saida = ""

    def __init__(self):
        Gtk.Window.__init__(self, title="FormularioGtk")
        self.set_size_request(500, 700)
        self.set_border_width(10)

        datos_basicos = Gtk.Frame(label='Datos básicos')
        nombre = Gtk.Label(label='Nombre')
        datos_basicos.add(nombre)
        self.add(datos_basicos)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == '__main__':
    FormularioGtk()
    Gtk.main()
