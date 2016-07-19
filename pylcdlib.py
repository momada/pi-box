#!/usr/bin/python
#-*-coding:utf-8-*-
import smbus
import time

# General i2c device class so that other devices can be added easily
class i2c_device:
    def __init__(self, addr, port):
        self.addr = addr
        self.bus = smbus.SMBus(port)

    def write(self, byte):
        self.bus.write_byte(self.addr, byte)

    def read(self):
        return self.bus.read_byte(self.addr)

    def read_nbytes_data(self, data, n): # For sequential reads > 1 byte
        return self.bus.read_i2c_block_data(self.addr, data, n)


class lcd:
    def __init__(self, addr, port):
        self.lcd_device = i2c_device(addr, port)
        self.lcd_device.write(0x30)
        self.lcd_strobe()
        time.sleep(0.008)
        self.lcd_device.write(0x30)
        self.lcd_strobe()
        time.sleep(0.001)
        self.lcd_strobe()
        time.sleep(0.0005)
        self.lcd_device.write(0x20)
        self.lcd_strobe()
        time.sleep(0.01)

        self.lcd_write(0x28) #Function set:4 digits data bus, 2 lines,5x7 dots/character
        self.lcd_write(0x08) #Display switch:display off,cursor off,blink off
        self.lcd_write(0x01) #Screen clear
        self.lcd_write(0x06) #Input set:Set moving direction of cursor
        self.lcd_write(0x0C) #Display switch:display on,cursor off,blink off

# clocks EN to latch command
    def lcd_strobe(self):
        self.lcd_device.write(self.lcd_device.read() | 0x0C) #Set 'E' to 1, keep 'PD#' as 1
        self.lcd_device.write(self.lcd_device.read() & 0xFB) #Set 'E' to 0, keep 'PD#' as 1

# write a command to lcd
    def lcd_write(self, cmd):
        self.lcd_device.write(((cmd >> 4)<< 4) | 0x08) #Write cmd: high 4 digits first
        self.lcd_strobe()
        self.lcd_device.write(((cmd & 0x0F)<< 4) | 0x08)#Write cmd: low 4 digits
        self.lcd_strobe()
        self.lcd_device.write(0x08)

# write a character to lcd (or character rom)
    def lcd_write_char(self, charvalue):
        self.lcd_device.write((0x01 | (charvalue >> 4)<< 4) |0x08) #Write data: high 4 digits first
        self.lcd_strobe()
        self.lcd_device.write((0x01 | (charvalue & 0x0F)<< 4) | 0x08) #Write data: low 4 digits
        self.lcd_strobe()
        self.lcd_device.write(0x08)

# put char function
    def lcd_putc(self, char):
        self.lcd_write_char(ord(char))

# put string function
    def lcd_puts(self, string, line):
        if line == 1:
            self.lcd_write(0x80)
        if line == 2:
            self.lcd_write(0xC0)

        for char in string:
            self.lcd_putc(char)
#        self.lcd_device.write(0x08)
	self.lcd_write(0x2)

# clear lcd and set to home
    def lcd_clear(self):
        self.lcd_write(0x1)  #Screen clear
        self.lcd_write(0x2)  #Reset cursor

# add custom characters (0 - 7)
    def lcd_load_custon_chars(self, fontdata):
        self.lcd_device.bus.write(0x40)
        for char in fontdata:
            for line in char:
                self.lcd_write_char(line)
