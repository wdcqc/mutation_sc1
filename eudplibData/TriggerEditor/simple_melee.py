from eudplib import *
from datetime import datetime
from version import map_version

@EUDFunc
def onPluginStart():
    title = GetStringIndex("\x07Mutation \x063v3 \x07v{}".format(map_version))
    desc = EncodeString("Team melee 3v3 with a twist of mutations.\r\n" + datetime.now().strftime("Build: %Y-%m-%d %H:%M:%S"))
    
    chkt = GetChkTokenized()
    chkt.setsection("SPRP", i2b2(title) + i2b2(desc))
    