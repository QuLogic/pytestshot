import threading
import time
import unittest

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import pytestshot


class TestBasicWin(unittest.TestCase):
    def setUp(self):
        self.pil_img = None

        self.window = Gtk.Window()
        self.button = Gtk.Button.new_with_label("pouet")
        self.window.add(self.button)
        self.window.show_all()
        self.window.set_size_request(640, 480)
        self.window.connect('destroy', Gtk.main_quit)
        self.window.connect_after('draw', self.save_screenshot)

    def save_screenshot(self, widget, cr):
        assert widget == self.window
        self.pil_img = pytestshot.screenshot(widget.get_window())
        widget.destroy()

    def test_screenshot(self):
        Gtk.main()

        self.assertNotEqual(self.pil_img, None)

    def test_ref(self):
        Gtk.main()

        self.assertNotEqual(self.pil_img, None)
        pytestshot.assertScreenshot(self, "test_basic", self.pil_img)
