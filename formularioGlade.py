import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class ExemploFormulario(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Interface design")
        self.set_default_size(300, 200)
        self.set_border_width(10)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        etiqueta = Gtk.Label(label="First Label")
        cadro1 = Gtk.Frame(label="First Frame")
        cadro2 = Gtk.Frame(label="Second Frame")

        caixaV.pack_start(etiqueta, False, False, 2)
        caixaV.pack_start(cadro1, True, True, 20)
        caixaV.pack_start(cadro2, True, True, 20)

        self.add(caixaV)

        self.builder = Gtk.Builder()
        self.builder.add_from_file("formularioGlade.glade")
        test = self.builder.get_object("test")
        btnElixir = self.builder.get_object("btn")
        sinais = {"on_btnElixir_clicked": self.on_btnElixir_clicked}
        self.builder.connect_signals(sinais)

        cadro1.add(test)

        caixaV3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        caixaH3 = Gtk.Box(spacing=6)

        lblPromocion = Gtk.Label("Promoción")
        rbtNingun = Gtk.RadioButton(label="Ningún")
        rbtTransporte = Gtk.RadioButton(label="Transporte gratuito")
        rbtDesconto = Gtk.RadioButton(label="Desconto 5%")

        caixaV3.pack_start(caixaH3, False, False, 2)
        caixaV3.pack_start(lblPromocion, False, False, 2)
        caixaV3.pack_start(rbtNingun, False, False, 2)
        caixaV3.pack_start(rbtTransporte, False, False, 2)
        caixaV3.pack_start(rbtDesconto, False, False, 2)

        lblPrezo = Gtk.Label(label="Prezo")
        txtPrezo = Gtk.Entry()
        lblEuro = Gtk.Label(label="€")
        lblImpostos = Gtk.Label(label="Impostos")
        cmbImpostos = Gtk.ComboBoxText()
        cmbImpostos.append_text("4%")
        cmbImpostos.append_text("7%")
        cmbImpostos.append_text("14%")

        caixaH3.pack_start(lblPrezo, False, False, 2)
        caixaH3.pack_start(txtPrezo, False, False, 2)
        caixaH3.pack_start(lblEuro, False, False, 2)
        caixaH3.pack_start(lblImpostos, False, False, 2)
        caixaH3.pack_start(cmbImpostos, False, False, 2)

        cadro2.add(caixaV3)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_btnElixir_clicked(self, boton):
        print("Boton elixir pulsado")


if __name__ == "__main__":
    ExemploFormulario()
    Gtk.main()
