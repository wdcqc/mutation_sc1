from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x663DE0, Add, -1536),# units:Rank/Sublabel  index:17    from 13 To 7
        SetMemory(0x663DE4, Add, -184549376),# units:Rank/Sublabel  index:23    from 19 To 8
        SetMemory(0x663DE8, Add, -2816),# units:Rank/Sublabel  index:25    from 19 To 8
        SetMemory(0x661740, Add, 655360),# units:Air Weapon  index:98    from 100 To 110
        SetMemory(0x6640C4, Add, -64),# units:Special Ability Flags  index:17    from 1476395072 To 1476395008
        SetMemory(0x6640DC, Add, -64),# units:Special Ability Flags  index:23    from 1509949504 To 1509949440
        SetMemory(0x6640E4, Add, -64),# units:Special Ability Flags  index:25    from 1107296320 To 1107296256
        SetMemory(0x661FEC, Add, 20709376),# units:Ready Sound  index:23    from 0 To 316
        SetMemory(0x661FF0, Add, 20709376),# units:Ready Sound  index:25    from 0 To 316
        SetMemory(0x65FFDC, Add, -7340032),# units:What Sound Start  index:23    from 436 To 324
        SetMemory(0x65FFE0, Add, -7340032),# units:What Sound Start  index:25    from 436 To 324
        SetMemory(0x662C1C, Add, -7340032),# units:What Sound End  index:23    from 439 To 327
        SetMemory(0x662C20, Add, -7340032),# units:What Sound End  index:25    from 439 To 327
        SetMemory(0x663B64, Add, -7274496),# units:Piss Sound Start  index:23    from 431 To 320
        SetMemory(0x663B68, Add, -7274496),# units:Piss Sound Start  index:25    from 431 To 320
        SetMemory(0x661F14, Add, -7340032),# units:Piss Sound End  index:23    from 435 To 323
        SetMemory(0x661F18, Add, -7340032),# units:Piss Sound End  index:25    from 435 To 323
        SetMemory(0x663C3C, Add, -7340032),# units:Yes Sound Start  index:23    from 440 To 328
        SetMemory(0x663C40, Add, -7340032),# units:Yes Sound Start  index:25    from 440 To 328
        SetMemory(0x66146C, Add, -7340032),# units:Yes Sound End  index:23    from 443 To 331
        SetMemory(0x661470, Add, -7340032),# units:Yes Sound End  index:25    from 443 To 331
        SetMemory(0x662FB4, Add, -524288),# units:Portrait  index:23    from 14 To 6
        SetMemory(0x662FB8, Add, -524288),# units:Portrait  index:25    from 14 To 6
        SetMemory(0x66384C, Add, -4096),# units:Staredit Group Flags  index:173    from 20 To 4
        SetMemory(0x661558, Add, 131072),# units:Staredit Availability Flags  index:33    from 0 To 2
        SetMemory(0x6615DC, Add, 2),# units:Staredit Availability Flags  index:98    from 4 To 6
        SetMemory(0x6616B8, Add, 131072),# units:Staredit Availability Flags  index:209    from 32 To 34
        SetMemory(0x657324, Add, -22),# weapons:Label  index:34    from 342 To 320
        SetMemory(0x657350, Add, -17),# weapons:Label  index:56    from 377 To 360
        SetMemory(0x657350, Add, -1114112),# weapons:Label  index:57    from 375 To 358
        SetMemory(0x657354, Add, -18),# weapons:Label  index:58    from 381 To 363
        SetMemory(0x657354, Add, -1114112),# weapons:Label  index:59    from 376 To 359
        SetMemory(0x657358, Add, -17),# weapons:Label  index:60    from 378 To 361
        SetMemory(0x657358, Add, -1114112),# weapons:Label  index:61    from 379 To 362
        SetMemory(0x657384, Add, -655360),# weapons:Label  index:83    from 403 To 393
        SetMemory(0x657388, Add, -10),# weapons:Label  index:84    from 400 To 390
        SetMemory(0x6573A8, Add, -655360),# weapons:Label  index:101    from 1265 To 1255
        SetMemory(0x6573AC, Add, -5),# weapons:Label  index:102    from 1248 To 1243
        SetMemory(0x6573B4, Add, -9),# weapons:Label  index:106    from 1267 To 1258
        SetMemory(0x6573B4, Add, -327680),# weapons:Label  index:107    from 1249 To 1244
        SetMemory(0x6573BC, Add, 1011),# weapons:Label  index:110    from 229 To 1240
        SetMemory(0x656E18, Add, 12),# weapons:Graphics  index:92    from 148 To 160
        SetMemory(0x656E60, Add, 64),# weapons:Graphics  index:110    from 142 To 206
        SetMemory(0x657A50, Add, 2),# weapons:Target Flags  index:92    from 1 To 3
        SetMemory(0x657A74, Add, -2),# weapons:Target Flags  index:110    from 3 To 1
        SetMemory(0x6575E0, Add, 32),# weapons:Maximum Range  index:92    from 224 To 256
        SetMemory(0x657628, Add, 32),# weapons:Maximum Range  index:110    from 128 To 160
        SetMemory(0x6571EC, Add, -256),# weapons:Damage Upgrade  index:29    from 60 To 59
        SetMemory(0x657204, Add, -1),# weapons:Damage Upgrade  index:52    from 60 To 59
        SetMemory(0x657204, Add, -256),# weapons:Damage Upgrade  index:53    from 60 To 59
        SetMemory(0x657220, Add, -1),# weapons:Damage Upgrade  index:80    from 60 To 59
        SetMemory(0x657220, Add, -256),# weapons:Damage Upgrade  index:81    from 60 To 59
        SetMemory(0x65723C, Add, 458752),# weapons:Damage Upgrade  index:110    from 7 To 14
        SetMemory(0x6572B4, Add, -2),# weapons:Weapon Type  index:92    from 3 To 1
        SetMemory(0x6572C4, Add, -131072),# weapons:Weapon Type  index:110    from 3 To 1
        SetMemory(0x656764, Add, 1507328),# weapons:Explosion Type  index:110    from 1 To 24
        SetMemory(0x656964, Add, 5),# weapons:Inner Splash Range  index:110    from 0 To 5
        SetMemory(0x6571A4, Add, 50),# weapons:Medium Splash Range  index:110    from 0 To 50
        SetMemory(0x65785C, Add, 100),# weapons:Outer Splash Range  index:110    from 0 To 100
        SetMemory(0x656F68, Add, 253),# weapons:Damage Amount  index:92    from 7 To 260
        SetMemory(0x656F8C, Add, 9),# weapons:Damage Amount  index:110    from 6 To 15
        SetMemory(0x6576B0, Add, 1310720),# weapons:Damage Bonus  index:29    from 0 To 20
        SetMemory(0x6576E0, Add, 15),# weapons:Damage Bonus  index:52    from 0 To 15
        SetMemory(0x6576E0, Add, 2621440),# weapons:Damage Bonus  index:53    from 0 To 40
        SetMemory(0x657718, Add, 20),# weapons:Damage Bonus  index:80    from 0 To 20
        SetMemory(0x657718, Add, 1310720),# weapons:Damage Bonus  index:81    from 0 To 20
        SetMemory(0x657730, Add, -1),# weapons:Damage Bonus  index:92    from 1 To 0
        SetMemory(0x657014, Add, 44),# weapons:Weapon Cooldown  index:92    from 22 To 66
        SetMemory(0x657024, Add, -458752),# weapons:Weapon Cooldown  index:110    from 15 To 8
        SetMemory(0x657028, Add, -5),# weapons:Weapon Cooldown  index:112    from 22 To 17
        SetMemory(0x65797C, Add, 1310720),# weapons:Forward Offset  index:110    from 0 To 20
        SetMemory(0x6567C4, Add, 1),# weapons:Icon  index:34    from 241 To 242
        SetMemory(0x6567F8, Add, 2424832),# weapons:Icon  index:61    from 265 To 302
        SetMemory(0x656828, Add, -3),# weapons:Icon  index:84    from 278 To 275
        SetMemory(0x656838, Add, 349),# weapons:Icon  index:92    from 0 To 349
        SetMemory(0x656848, Add, 589824),# weapons:Icon  index:101    from 359 To 368
        SetMemory(0x65684C, Add, 125),# weapons:Icon  index:102    from 241 To 366
        SetMemory(0x656850, Add, 2555904),# weapons:Icon  index:105    from 332 To 371
        SetMemory(0x656854, Add, 40),# weapons:Icon  index:106    from 332 To 372
        SetMemory(0x656854, Add, 2686976),# weapons:Icon  index:107    from 332 To 373
        SetMemory(0x656858, Add, 141),# weapons:Icon  index:108    from 240 To 381
        SetMemory(0x65685C, Add, 9),# weapons:Icon  index:110    from 323 To 332
        SetMemory(0x666318, Add, 547),# sprites:Image File  index:220    from 207 To 754
        SetMemory(0x66C440, Add, 65536),# images:Clickable  index:754    from 0 To 1
        SetMemory(0x66F1E8, Add, -1),# images:Iscript ID  index:360    from 244 To 243
        SetMemory(0x66F810, Add, -161),# images:Iscript ID  index:754    from 340 To 179
        SetMemory(0x66FAEC, Add, -233),# images:Iscript ID  index:937    from 410 To 177
        SetMemory(0x66FB14, Add, -305),# images:Iscript ID  index:947    from 407 To 102
        SetMemory(0x655B2C, Add, 2424832),# upgrades:Icon  index:55    from 0 To 37
        SetMemory(0x655B30, Add, 38),# upgrades:Icon  index:56    from 0 To 38
        SetMemory(0x655B30, Add, 2555904),# upgrades:Icon  index:57    from 0 To 39
        SetMemory(0x655AAC, Add, 2490368),# upgrades:Label  index:55    from 0 To 38
        SetMemory(0x655AB0, Add, 39),# upgrades:Label  index:56    from 0 To 39
        SetMemory(0x655AB0, Add, 2621440),# upgrades:Label  index:57    from 0 To 40
        SetMemory(0x655734, Add, 16777216),# upgrades:Max. Repeats  index:55    from 0 To 1
        SetMemory(0x655738, Add, 1),# upgrades:Max. Repeats  index:56    from 0 To 1
        SetMemory(0x655738, Add, 256),# upgrades:Max. Repeats  index:57    from 0 To 1
    ])

