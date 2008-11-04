"""Spatial layouts of various electrophys (generally silicon polytrode) probe designs.
Spatial origin is at center top of each probe. Right now, spyke assumes that all
probe designs have contiguous channel indices starting from 0"""

# TODO: add pt16c, and pt16x layouts (with 16 to HS-27 adapter)


class Probe(object):
    """self.SiteLoc maps probe chan id to (x, y) position of site in um"""
    pass


class uMap54_1a(Probe):
    """uMap54_1a, 65um spacing, 3 column hexagonal"""
    def __init__(self):
        self.layout = '1a'
        self.name = 'uMap54_1a'
        self.nchans = 54
        self.ncols = 3
        SiteLoc = {}
        SiteLoc[0] = -56, 1170
        SiteLoc[1] = -56, 1105
        SiteLoc[2] = -56, 1040
        SiteLoc[3] = -56, 975
        SiteLoc[4] = -56, 910
        SiteLoc[5] = -56, 845
        SiteLoc[6] = -56, 585
        SiteLoc[7] = -56, 455
        SiteLoc[8] = -56, 325
        SiteLoc[9] = -56, 195
        SiteLoc[10] = -56, 65
        SiteLoc[11] = -56, 130
        SiteLoc[12] = -56, 260
        SiteLoc[13] = -56, 390
        SiteLoc[14] = -56, 520
        SiteLoc[15] = -56, 650
        SiteLoc[16] = -56, 715
        SiteLoc[17] = -56, 780
        SiteLoc[18] = 0, 1072
        SiteLoc[19] = 0, 942
        SiteLoc[20] = 0, 812
        SiteLoc[21] = 0, 682
        SiteLoc[22] = 0, 552
        SiteLoc[23] = 0, 422
        SiteLoc[24] = 0, 162
        SiteLoc[25] = 0, 97
        SiteLoc[26] = 0, 292
        SiteLoc[27] = 0, 227
        SiteLoc[28] = 0, 357
        SiteLoc[29] = 0, 487
        SiteLoc[30] = 0, 617
        SiteLoc[31] = 0, 747
        SiteLoc[32] = 0, 877
        SiteLoc[33] = 0, 1007
        SiteLoc[34] = 0, 1137
        SiteLoc[35] = 0, 1202
        SiteLoc[36] = 56, 780
        SiteLoc[37] = 56, 650
        SiteLoc[38] = 56, 520
        SiteLoc[39] = 56, 390
        SiteLoc[40] = 56, 260
        SiteLoc[41] = 56, 130
        SiteLoc[42] = 56, 65
        SiteLoc[43] = 56, 195
        SiteLoc[44] = 56, 325
        SiteLoc[45] = 56, 455
        SiteLoc[46] = 56, 585
        SiteLoc[47] = 56, 715
        SiteLoc[48] = 56, 845
        SiteLoc[49] = 56, 910
        SiteLoc[50] = 56, 975
        SiteLoc[51] = 56, 1105
        SiteLoc[52] = 56, 1170
        SiteLoc[53] = 56, 1040
        assert len(SiteLoc) == self.nchans
        self.SiteLoc = SiteLoc


class uMap54_1b(Probe):
    """uMap54_1b, 50um horizontal/46um vertical spacing, 3 column collinear"""
    def __init__(self):
        self.layout = '1b'
        self.name = 'uMap54_1b'
        self.nchans = 54
        self.ncols = 3
        SiteLoc = {}
        SiteLoc[0] = -43, 900
        SiteLoc[1] = -43, 850
        SiteLoc[2] = -43, 800
        SiteLoc[3] = -43, 750
        SiteLoc[4] = -43, 700
        SiteLoc[5] = -43, 650
        SiteLoc[6] = -43, 600
        SiteLoc[7] = -43, 550
        SiteLoc[8] = -43, 500
        SiteLoc[9] = -43, 450
        SiteLoc[10] = -43, 400
        SiteLoc[11] = -43, 350
        SiteLoc[12] = -43, 300
        SiteLoc[13] = -43, 250
        SiteLoc[14] = -43, 200
        SiteLoc[15] = -43, 150
        SiteLoc[16] = -43, 50
        SiteLoc[17] = -43, 100
        SiteLoc[18] = 0, 900
        SiteLoc[19] = 0, 800
        SiteLoc[20] = 0, 700
        SiteLoc[21] = 0, 600
        SiteLoc[22] = 0, 500
        SiteLoc[23] = 0, 400
        SiteLoc[24] = 0, 200
        SiteLoc[25] = 0, 100
        SiteLoc[26] = 0, 300
        SiteLoc[27] = 0, 50
        SiteLoc[28] = 0, 150
        SiteLoc[29] = 0, 250
        SiteLoc[30] = 0, 350
        SiteLoc[31] = 0, 450
        SiteLoc[32] = 0, 550
        SiteLoc[33] = 0, 650
        SiteLoc[34] = 0, 750
        SiteLoc[35] = 0, 850
        SiteLoc[36] = 43, 200
        SiteLoc[37] = 43, 100
        SiteLoc[38] = 43, 50
        SiteLoc[39] = 43, 150
        SiteLoc[40] = 43, 250
        SiteLoc[41] = 43, 300
        SiteLoc[42] = 43, 350
        SiteLoc[43] = 43, 400
        SiteLoc[44] = 43, 450
        SiteLoc[45] = 43, 500
        SiteLoc[46] = 43, 550
        SiteLoc[47] = 43, 600
        SiteLoc[48] = 43, 650
        SiteLoc[49] = 43, 700
        SiteLoc[50] = 43, 750
        SiteLoc[51] = 43, 850
        SiteLoc[52] = 43, 900
        SiteLoc[53] = 43, 800
        assert len(SiteLoc) == self.nchans
        self.SiteLoc = SiteLoc


class uMap54_1c(Probe):
    """uMap54_1c, 75um spacing, 3 column, hexagonal"""
    def __init__(self):
        self.layout = '1c'
        self.name = 'uMap54_1c'
        self.nchans = 54
        self.ncols = 3
        SiteLoc = {}
        SiteLoc[0] = -65, 1251
        SiteLoc[1] = -65, 1101
        SiteLoc[2] = -65, 951
        SiteLoc[3] = -65, 801
        SiteLoc[4] = -65, 651
        SiteLoc[5] = -65, 501
        SiteLoc[6] = -65, 351
        SiteLoc[7] = -65, 201
        SiteLoc[8] = -65, 51
        SiteLoc[9] = -65, 126
        SiteLoc[10] = -65, 276
        SiteLoc[11] = -65, 426
        SiteLoc[12] = -65, 576
        SiteLoc[13] = -65, 726
        SiteLoc[14] = -65, 876
        SiteLoc[15] = -65, 1026
        SiteLoc[16] = -65, 1176
        SiteLoc[17] = -65, 1326
        SiteLoc[18] = 0, 1364
        SiteLoc[19] = 0, 1214
        SiteLoc[20] = 0, 1064
        SiteLoc[21] = 0, 914
        SiteLoc[22] = 0, 764
        SiteLoc[23] = 0, 614
        SiteLoc[24] = 0, 314
        SiteLoc[25] = 0, 164
        SiteLoc[26] = 0, 464
        SiteLoc[27] = 0, 89
        SiteLoc[28] = 0, 239
        SiteLoc[29] = 0, 389
        SiteLoc[30] = 0, 539
        SiteLoc[31] = 0, 689
        SiteLoc[32] = 0, 839
        SiteLoc[33] = 0, 989
        SiteLoc[34] = 0, 1139
        SiteLoc[35] = 0, 1289
        SiteLoc[36] = 65, 1326
        SiteLoc[37] = 65, 1251
        SiteLoc[38] = 65, 1176
        SiteLoc[39] = 65, 1026
        SiteLoc[40] = 65, 876
        SiteLoc[41] = 65, 726
        SiteLoc[42] = 65, 576
        SiteLoc[43] = 65, 426
        SiteLoc[44] = 65, 276
        SiteLoc[45] = 65, 126
        SiteLoc[46] = 65, 51
        SiteLoc[47] = 65, 201
        SiteLoc[48] = 65, 351
        SiteLoc[49] = 65, 501
        SiteLoc[50] = 65, 651
        SiteLoc[51] = 65, 951
        SiteLoc[52] = 65, 1101
        SiteLoc[53] = 65, 801
        assert len(SiteLoc) == self.nchans
        self.SiteLoc = SiteLoc


class uMap54_2a(Probe):
    """uMap54_2a, 65um spacing, 2 column, staggered"""
    def __init__(self):
        self.layout = '2a'
        self.name = 'uMap54_2a'
        self.nchans = 54
        self.ncols = 2
        SiteLoc = {}
        SiteLoc[0] = -28, 1235
        SiteLoc[1] = -28, 1170
        SiteLoc[2] = -28, 1105
        SiteLoc[3] = -28, 1040
        SiteLoc[4] = -28, 975
        SiteLoc[5] = -28, 910
        SiteLoc[6] = -28, 845
        SiteLoc[7] = -28, 780
        SiteLoc[8] = -28, 715
        SiteLoc[9] = -28, 650
        SiteLoc[10] = -28, 585
        SiteLoc[11] = -28, 520
        SiteLoc[12] = -28, 455
        SiteLoc[13] = -28, 390
        SiteLoc[14] = -28, 325
        SiteLoc[15] = -28, 260
        SiteLoc[16] = -28, 195
        SiteLoc[17] = -28, 130
        SiteLoc[18] = -28, 65
        SiteLoc[19] = -28, 1300
        SiteLoc[20] = -28, 1365
        SiteLoc[21] = -28, 1430
        SiteLoc[22] = -28, 1495
        SiteLoc[23] = -28, 1560
        SiteLoc[24] = -28, 1690
        SiteLoc[25] = -28, 1755
        SiteLoc[26] = -28, 1625
        SiteLoc[27] = 28, 1722
        SiteLoc[28] = 28, 1657
        SiteLoc[29] = 28, 1592
        SiteLoc[30] = 28, 1527
        SiteLoc[31] = 28, 1462
        SiteLoc[32] = 28, 1397
        SiteLoc[33] = 28, 1332
        SiteLoc[34] = 28, 32
        SiteLoc[35] = 28, 97
        SiteLoc[36] = 28, 162
        SiteLoc[37] = 28, 227
        SiteLoc[38] = 28, 292
        SiteLoc[39] = 28, 357
        SiteLoc[40] = 28, 422
        SiteLoc[41] = 28, 487
        SiteLoc[42] = 28, 552
        SiteLoc[43] = 28, 617
        SiteLoc[44] = 28, 682
        SiteLoc[45] = 28, 747
        SiteLoc[46] = 28, 812
        SiteLoc[47] = 28, 877
        SiteLoc[48] = 28, 942
        SiteLoc[49] = 28, 1007
        SiteLoc[50] = 28, 1072
        SiteLoc[51] = 28, 1202
        SiteLoc[52] = 28, 1267
        SiteLoc[53] = 28, 1137
        assert len(SiteLoc) == self.nchans
        self.SiteLoc = SiteLoc


class uMap54_2b(Probe):
    """uMap54_2b, 50um spacing, 2 column, staggered"""
    def __init__(self):
        self.layout = '2b'
        self.name = 'uMap54_2b'
        self.nchans = 54
        self.ncols = 2
        SiteLoc = {}
        SiteLoc[0] = -25, 1275
        SiteLoc[1] = -25, 1175
        SiteLoc[2] = -25, 1075
        SiteLoc[3] = -25, 975
        SiteLoc[4] = -25, 875
        SiteLoc[5] = -25, 775
        SiteLoc[6] = -25, 725
        SiteLoc[7] = -25, 675
        SiteLoc[8] = -25, 625
        SiteLoc[9] = -25, 575
        SiteLoc[10] = -25, 525
        SiteLoc[11] = -25, 475
        SiteLoc[12] = -25, 425
        SiteLoc[13] = -25, 375
        SiteLoc[14] = -25, 325
        SiteLoc[15] = -25, 275
        SiteLoc[16] = -25, 225
        SiteLoc[17] = -25, 175
        SiteLoc[18] = -25, 125
        SiteLoc[19] = -25, 75
        SiteLoc[20] = -25, 25
        SiteLoc[21] = -25, 825
        SiteLoc[22] = -25, 925
        SiteLoc[23] = -25, 1025
        SiteLoc[24] = -25, 1225
        SiteLoc[25] = -25, 1325
        SiteLoc[26] = -25, 1125
        SiteLoc[27] = 25, 1300
        SiteLoc[28] = 25, 1200
        SiteLoc[29] = 25, 1100
        SiteLoc[30] = 25, 1000
        SiteLoc[31] = 25, 900
        SiteLoc[32] = 25, 0
        SiteLoc[33] = 25, 50
        SiteLoc[34] = 25, 100
        SiteLoc[35] = 25, 150
        SiteLoc[36] = 25, 200
        SiteLoc[37] = 25, 250
        SiteLoc[38] = 25, 300
        SiteLoc[39] = 25, 350
        SiteLoc[40] = 25, 400
        SiteLoc[41] = 25, 450
        SiteLoc[42] = 25, 500
        SiteLoc[43] = 25, 550
        SiteLoc[44] = 25, 600
        SiteLoc[45] = 25, 650
        SiteLoc[46] = 25, 700
        SiteLoc[47] = 25, 750
        SiteLoc[48] = 25, 800
        SiteLoc[49] = 25, 850
        SiteLoc[50] = 25, 950
        SiteLoc[51] = 25, 1150
        SiteLoc[52] = 25, 1250
        SiteLoc[53] = 25, 1050
        assert len(SiteLoc) == self.nchans
        self.SiteLoc = SiteLoc


class pt16a_HS27(Probe):
    """pt16a in DIP-16 to HS-27 adapter"""
    def __init__(self):
        self.layout = 'pt16a_HS27'
        self.name = 'pt16a_HS27'
        self.nchans = 20
        self.ncols = 2
        SiteLoc = {}
        SiteLoc[0] = -27, 279
        SiteLoc[1] = -27, 217
        SiteLoc[2] = -27, 155
        SiteLoc[3] = -27, 93
        SiteLoc[4] = -27, 31
        SiteLoc[5] = -27, 341
        SiteLoc[6] = -27, 403
        SiteLoc[7] = -27, 465
        # Gap of 4 (grounded) chans in the adapter, give them sites below the probe
        SiteLoc[8] = -27, 650
        SiteLoc[9] = -27, 700
        SiteLoc[10] = 27, 650
        SiteLoc[11] = 27, 700
        # Back to actual polytrode sites:
        SiteLoc[12] = 27, 434
        SiteLoc[13] = 27, 372
        SiteLoc[14] = 27, 310
        SiteLoc[15] = 27, 0
        SiteLoc[16] = 27, 62
        SiteLoc[17] = 27, 124
        SiteLoc[18] = 27, 186
        SiteLoc[19] = 27, 248
        assert len(SiteLoc) == self.nchans
        self.SiteLoc = SiteLoc


class pt16b_HS27(Probe):
    """pt16b in DIP-16 to HS-27 adapter"""
    def __init__(self):
        self.layout = 'pt16b_HS27'
        self.name = 'pt16b_HS27'
        self.nchans = 20
        self.ncols = 2
        SiteLoc = {}
        SiteLoc[0] = -27, 155
        SiteLoc[1] = -27, 93
        SiteLoc[2] = -27, 217
        SiteLoc[3] = -27, 341
        SiteLoc[4] = -27, 31
        SiteLoc[5] = -27, 279
        SiteLoc[6] = -27, 403
        SiteLoc[7] = -27, 465
        # Gap of 4 (grounded) chans in the adapter, give them sites below the probe
        SiteLoc[8] = -27, 650
        SiteLoc[9] = -27, 700
        SiteLoc[10] = 27, 650
        SiteLoc[11] = 27, 700
        # Back to actual polytrode sites:
        SiteLoc[12] = 27, 434
        SiteLoc[13] = 27, 372
        SiteLoc[14] = 27, 248
        SiteLoc[15] = 27, 0
        SiteLoc[16] = 27, 310
        SiteLoc[17] = 27, 186
        SiteLoc[18] = 27, 62
        SiteLoc[19] = 27, 124
        assert len(SiteLoc) == self.nchans
        self.SiteLoc = SiteLoc
