from eudplib import *
from datetime import datetime
from version import map_version

@EUDFunc
def onPluginStart():
    title = GetStringIndex("\x07Mutation \x06AI Observation \x07v{}".format(map_version))
    desc = EncodeString("Watch AIs fight against each other, with a mutation twist.\r\n[Type2] Please leave player slot empty and use an observer slot.\r\n" + datetime.now().strftime("Build: %Y-%m-%d %H:%M:%S"))
    
    force1_name = GetStringIndex("AI Observation")
    force2_name = GetStringIndex("Use an Observer slot!")
    force3_name = GetStringIndex("Leave this slot empty!")

    chkt = GetChkTokenized()
    chkt.setsection("SPRP", i2b2(title) + i2b2(desc))
    chkt.setsection("OWNR", b'\x05\x05\x05\x05\x05\x05\x06\x02\x00\x00\x00\x00')
    chkt.setsection("SIDE", b'\x01\x01\x01\x01\x01\x01\x01\x01\x07\x07\x07\x07')
    chkt.setsection("FORC", b'\x00\x00\x00\x01\x01\x01\x02\x03' + i2b2(force1_name) + i2b2(force2_name) + i2b2(force3_name) + b'\x06\x00\x0e\x0e\x0e\x0e')
    chkt.setsection("COLR", b'\x00\x01\x02\x03\x04\x05\x06\x07')
    chkt.delsection("CRGB")

    mbrf = chkt.getsection("MBRF")
    for index in range(2393, len(mbrf), 2400): # Force4 player execution flag
        if mbrf[index] == 1:
            mbrf = mbrf[:index - 4] + b'\x01\x00\x00\x00\x00' + mbrf[index + 1:] # add AllPlayers
    assert len(mbrf) % 2400 == 0
    
    chkt.setsection("MBRF", mbrf)
