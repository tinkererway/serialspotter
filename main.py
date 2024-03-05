# SerialSpotter v1_0_0

from kivy.config import Config
Config.set('graphics', 'resizable', '1') 
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
Config.set('graphics', 'minimum_width', '800')
Config.set('graphics', 'minimum_height', '480')

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons

from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.core.window import Window

from kivy.core.text import LabelBase, DEFAULT_FONT
LabelBase.register(DEFAULT_FONT, "SpaceMono-Regular.ttf")

import serial.tools.list_ports
import keyboard


# The following code snippet is adapted from a GitHub Gist by terminak:
# https://gist.github.com/terminak/ef3c34922a1fced048b1db8e0ec6837b#file-hover_highlight_refs-py
# Used for highlighting the website on hover.

class HighlightLabel(Label):
    def __init__(self, **kwargs):
        super(HighlightLabel, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)
        self._instructions = []
        
    def on_mouse_pos(self, *largs):
        pos = self.to_widget(*largs[1])
        if self.collide_point(*pos):
            tx, ty = pos
            tx -= self.center_x - self.texture_size[0] / 2.
            ty -= self.center_y - self.texture_size[1] / 2.
            ty = self.texture_size[1] - ty
            for uid, zones in self.refs.items():
                for zone in zones:
                    x, y, w, h = zone
                    if x <= tx <= w and y <= ty <= h:
                        self._highlight_ref(uid)
                        return
        if self._instructions:
            self._clear_instructions()
        
    def _highlight_ref(self, name):
        if self._instructions:
            return
        store = self._instructions.append
        with self.canvas:
            store(Color(0, 1, 0, 0.25))
        self.text = '[color=#839496]!(c) [ref=https://tinkererway.dev/serialspotter][u]Tinkererway[/u][/ref] . No rights reserved . Made with love in opensource[/color]'
      
    def _clear_instructions(self):
        rm = self.canvas.remove
        for instr in self._instructions:
            rm(instr)
        self._instructions = []
        self.text = '[color=#839496]!(c) [ref=https://tinkererway.dev/serialspotter]Tinkererway[/ref] . No rights reserved . Made with love in opensource[/color]'
        
        
class SerialSpotterApp(MDApp):

    icon = 'icon_serialspotter.png'
   
    def build(self):
        keyboard.hook(self.on_key_event)
        
    def on_start(self):
        self.root.ids.ports_list.text = ' '
        self.list_serial_ports_minimal()
        
    def on_key_event(self, event):
        key = event.name
        if event.event_type == keyboard.KEY_DOWN:
            if key == 'esc':
                print("Exiting...")
                SerialSpotterApp().stop()
            elif key == 'space':
                self.list_serial_ports()
            else:
                self.list_serial_ports_minimal()
                
    def list_serial_ports(self):
        ports = serial.tools.list_ports.comports()
        if not ports:
            self.root.ids.ports_list.text = "[color=#839496][size=13sp]No serial ports found.[/size][/color]"
            return
            
        port_info = ""
        for port in ports:
            port_info += '[color=#839496][size=13sp] \u2022 ' +f" {port.device}: {port.description}, {port.hwid}  , {port.manufacturer}, {port.serial_number}, {port.product}, {port.interface} [/size][/color]\n"
        port_info += '[color=#839496][size=25sp]---------------------------------------------[/size][/color]\n'
        port_info += '[color=#839496][size=13sp]Press any  key to refresh the list, or hit \'Esc\' to exit![/size][/color]\n'
        self.root.ids.ports_list.text = port_info
                
    def list_serial_ports_minimal(self):
        ports = serial.tools.list_ports.comports()
        if not ports:
            self.root.ids.ports_list.text = "[color=#839496][size=13sp]No serial ports found.[/size][/color]"
            return

        port_info = ""
        for port in ports:
            port_info += '[color=#839496][size=13sp] \u2022 ' +f" {port.device}: {port.description}   [/size][/color]\n"
        port_info += '[color=#839496][size=25sp]---------------------------------------------[/size][/color]\n'
        port_info += '[color=#839496][size=16sp]Press any  key to refresh the list, or hit \'Esc\' to exit![/size][/color]\n'
        self.root.ids.ports_list.text = port_info
                
if __name__ == '__main__':
    SerialSpotterApp().run()
    

    
    
    
    

