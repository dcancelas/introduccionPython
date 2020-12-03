import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class FormularioGtk(Gtk.Window):
    saida_entry = Gtk.Entry()
    saida = ""

    def __init__(self):
        Gtk.Window.__init__(self, title="FormularioGtk")
        """self.set_size_request(500, 700)"""
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        info_label = Gtk.Label(label='Información sobre el producto')
        datbas_frame = Gtk.Frame(label='Datos básicos')
        datecon_frame = Gtk.Frame(label='Datos económicos')
        vbox.pack_start(info_label, False, False, 2)
        vbox.pack_start(datbas_frame, True, True, 20)
        vbox.pack_start(datecon_frame, True, True, 20)

        datbas_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        datbas_frame.add(datbas_box)
        nombre_label = Gtk.Label(label='Nombre')
        nombre_entry = Gtk.Entry()
        desc_label = Gtk.Label(label='Descripción')
        desc_textview = Gtk.TextView()
        foto_box = Gtk.Box(spacing=2)
        visitas_chkbutton = Gtk.CheckButton(label='Añadir contador de visitas')
        datbas_box.pack_start(nombre_label, False, False, 2)
        datbas_box.pack_start(nombre_entry, True, False, 2)
        datbas_box.pack_start(desc_label, False, False, 2)
        datbas_box.pack_start(desc_textview, True, True, 2)
        datbas_box.pack_start(foto_box, True, True, 10)
        datbas_box.pack_start(visitas_chkbutton, False, False, 2)

        foto_label = Gtk.Label(label='Foto')
        foto_entry = Gtk.Entry()
        foto_button = Gtk.Button(label="Elegir...")
        foto_box.pack_start(foto_label, False, False, 2)
        foto_box.pack_start(foto_entry, False, False, 2)
        foto_box.pack_start(foto_button, False, False, 2)

        datecon_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        datecon_frame.add(datecon_box)
        precio_box = Gtk.Box(spacing=6)
        promocion_label = Gtk.Label(label='Promoción')
        p1_radbutton = Gtk.RadioButton(label='Ninguno')
        p2_radbutton = Gtk.RadioButton(label='Transporte gratuito')
        p3_radbutton = Gtk.RadioButton(label='Descuento 5%')
        datecon_box.pack_start(precio_box, False, False, 2)
        datecon_box.pack_start(promocion_label, False, False, 2)
        datecon_box.pack_start(p1_radbutton, False, False, 2)
        datecon_box.pack_start(p2_radbutton, False, False, 2)
        datecon_box.pack_start(p3_radbutton, False, False, 2)

        precio_label = Gtk.Label(label='Precio')
        precio_entry = Gtk.Entry()
        euro_label = Gtk.Label(label='€')
        impuestos_label = Gtk.Label(label='Impuestos')
        impuestos_cbt = Gtk.ComboBoxText()
        impuestos_cbt.append_text('4%')
        impuestos_cbt.append_text('7%')
        impuestos_cbt.append_text('16%')
        impuestos_cbt.append_text('25%')
        precio_box.pack_start(precio_label, False, False, 2)
        precio_box.pack_start(precio_entry, False, False, 2)
        precio_box.pack_start(euro_label, False, False, 2)
        precio_box.pack_start(impuestos_label, False, False, 2)
        precio_box.pack_start(impuestos_cbt, False, False, 2)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == '__main__':
    FormularioGtk()
    Gtk.main()
