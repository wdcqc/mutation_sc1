from eudplib import *
from datetime import datetime
from version import map_version

@EUDFunc
def onPluginStart():
    title = GetStringIndex("\x07Mutation \x06Warfare \x07v{}".format(map_version))
    desc = EncodeString("Team melee 3v3 with a twist of mutations.\r\n[AutoCom] Empty slots will become AI players.\r\n" + datetime.now().strftime("Build: %Y-%m-%d %H:%M:%S"))
    force3_name = GetStringIndex("Empty Slots = Computers")
    
    chkt = GetChkTokenized()
    chkt.setsection("SPRP", i2b2(title) + i2b2(desc))
    chkt.setsection("OWNR", b'\x06\x06\x06\x06\x06\x06\x05\x05\x00\x00\x00\x00')
    chkt.setsection("SIDE", b'\x05\x05\x05\x05\x05\x05\x01\x01\x07\x07\x07\x07')
    chkt.setsection("FORC", b'\x00\x00\x00\x01\x01\x01\x02\x02\x02\x00\x04\x00' + i2b2(force3_name) + b'\x06\x00\x0e\x0e\x0e\x0e')
