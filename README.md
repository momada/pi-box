# pi-box

# Display screen <-> Raspberry Pi
# +--------------+---------------+
# |   LCD1602    |  RaspberryPi  |
# +--------------+---------------+
# | Yellow(GND)  |	     6       |
# | Orange(VCC)	 |		   2       |
# |  Red (SDA)	 |		   3       |
# | Brown(SCL)	 |		   5       |
# +--------------+---------------+

# Encoder <-> Raspberry Pi
# +--------------+---------------+
# |RotaryEncoder |  Raspberry Pi |
# +--------------+---------------+
# |   Purple	   |		  11       |
# |    Blue  	   |		  13       |
# |    White  	 |		  17       |
# |    Grey   	 |		  15       |
# |    Black  	 |		  14       |
# +--------------+---------------+


# Raspberry Pi GPIO
# +----------+-Rev2-+------+--------+------+-------+
# | wiringPi | GPIO | Phys | Name   | Mode | Value |
# +----------+------+------+--------+------+-------+
# |      0   |  17  |  11  | GPIO 0 | IN   | Low   |
# |      1   |  18  |  12  | GPIO 1 | IN   | Low   |
# |      2   |  27  |  13  | GPIO 2 | IN   | Low   |
# |      3   |  22  |  15  | GPIO 3 | IN   | Low   |
# |      4   |  23  |  16  | GPIO 4 | IN   | Low   |
# |      5   |  24  |  18  | GPIO 5 | IN   | Low   |
# |      6   |  25  |  22  | GPIO 6 | IN   | Low   |
# |      7   |   4  |   7  | GPIO 7 | IN   | Low   |
# |      8   |   2  |   3  | SDA    | IN   | High  |
# |      9   |   3  |   5  | SCL    | IN   | High  |
# |     10   |   8  |  24  | CE0    | ALT0 | High  |
# |     11   |   7  |  26  | CE1    | ALT0 | High  |
# |     12   |  10  |  19  | MOSI   | ALT0 | Low   |
# |     13   |   9  |  21  | MISO   | ALT0 | Low   |
# |     14   |  11  |  23  | SCLK   | ALT0 | High  |
# |     15   |  14  |   8  | TxD    | ALT0 | High  |
# |     16   |  15  |  10  | RxD    | ALT0 | High  |
# |     17   |  28  |   3  | GPIO 8 | IN   | Low   |
# |     18   |  29  |   4  | GPIO 9 | IN   | Low   |
# |     19   |  30  |   5  | GPIO10 | IN   | Low   |
# |     20   |  31  |   6  | GPIO11 | IN   | Low   |
# +----------+------+------+--------+------+-------+
