from eudplib import *
from datetime import datetime
from version import map_version

@EUDFunc
def onPluginStart():
    title = GetStringIndex("\x07Mutation \x06AI Battles \x07v{}".format(map_version))
    desc = EncodeString("Watch AIs fight against each other, with a mutation twist.\r\n" + datetime.now().strftime("Build: %Y-%m-%d %H:%M:%S"))
    
    chkt = GetChkTokenized()
    chkt.setsection("SPRP", i2b2(title) + i2b2(desc))
    chkt.setsection("OWNR", b'\x05\x05\x05\x05\x05\x05\x05\x06\x00\x00\x00\x00')
    chkt.setsection("SIDE", b'\x01\x01\x01\x01\x01\x01\x01\x01\x07\x07\x07\x07')
    chkt.setsection("FORC", b'\x00\x00\x00\x01\x01\x01\x02\x03\x02\x00\x04\x00\x05\x00\x06\x00\x0e\x0e\x0e\x0e')
    chkt.setsection("COLR", b'\x00\x01\x02\x03\x04\x05\x06\x07')
    chkt.delsection("CRGB")
