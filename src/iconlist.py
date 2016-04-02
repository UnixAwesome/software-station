#!/usr/bin/python3

from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf
import glob
import os
import sys

found = glob.glob('/usr/local/share/icons/mate/24x24/*/*png')

icons = [ ]

for f in found:
    base = os.path.basename(f)
    icons.append(os.path.splitext(base)[0])


class IconViewWindow(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self)
        self.set_title("%d icon%c - %s" % (len(icons), '' if len(icons) < 2 else 's', 'usr/local/share/icons/mate/24x24/'))
        self.set_default_size(660, 400)

        liststore = Gtk.ListStore(Pixbuf, str)
        iconview = Gtk.IconView.new()
        iconview.set_model(liststore)
        iconview.set_pixbuf_column(0)
        iconview.set_text_column(1)

        for icon in sorted(icons):
            try:
                pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 64, 0)
                liststore.append([pixbuf, icon])
            except Exception as inst:
                print(inst)

        swnd = Gtk.ScrolledWindow()
        swnd.add(iconview)
        self.add(swnd)


win = IconViewWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
