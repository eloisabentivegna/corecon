dictionary_tag = "Palanque-Delabrouille et al. 2013 (Fourier transform method)"

reference   = "Palanque-Delabrouille, Yeche, Borde, Le Goff, Rossi, Viel, et al.; A&A 559, A85 (2013)"

description = \
"""
1D Lyman-alpha power spectrum estimated from 13821 BOSS QSOs using the Fourier transform.
"""

data_structure         = "grid" #grid or points

ndim                   = 2

dimensions_descriptors = ["redshift", "ks (h/Mpc)"]

axes                   = [[2.2, 2.4, 2.6, 2.8, 3. , 3.2, 3.4, 3.6, 3.8, 4., 4.2, 4.4],
                          [0.001084, 0.001626, 0.002168, 0.00271 , 0.003252, 0.003794,
                           0.004336, 0.004878, 0.00542 , 0.005962, 0.006504, 0.007046,
                           0.007588, 0.00813 , 0.008672, 0.009214, 0.009756, 0.010298,
                           0.01084 , 0.011382, 0.011924, 0.012466, 0.013008, 0.01355 ,
                           0.014092, 0.014634, 0.015176, 0.015718, 0.01626 , 0.016802,
                           0.017344, 0.017886, 0.018428, 0.01897 , 0.019512]
                         ]

values      = [[18.14740, 16.82860, 17.33220, 17.65820, 15.95860, 13.90080,  \
                13.39390, 14.34260, 14.03330, 13.14740, 12.83220, 11.55600,  \
                11.04740, 11.40290, 11.19240, 10.16030, 9.72887, 10.19740,  \
                9.94076, 9.13371, 8.45841, 8.13738, 8.16634, 7.58319,  \
                7.69209, 7.82870, 7.09658, 6.74426, 7.79677, 8.51479,  \
                9.19975, 6.26875, 6.12212, 7.77703, 4.67218 \
               ], \
               [24.49190, 20.75420, 21.61260, 22.17610, 20.81430, 17.37650,  \
                16.63150, 16.77750, 16.94030, 16.86060, 14.61570, 13.79200,  \
                13.96800, 14.15990, 12.73340, 12.37040, 11.54550, 11.12070,  \
                11.17760, 11.74540, 10.31240, 10.11830, 9.70098, 9.55087,  \
                9.73476, 9.04571, 8.21397, 8.04387, 8.59117, 7.93963,  \
                8.05913, 7.12668, 6.70061, 6.29888, 6.51759 \
               ], \
               [30.10690, 26.42360, 28.13660, 27.00180, 24.96180, 21.39650,  \
                20.31550, 20.38620, 20.74300, 19.72340, 17.86700, 16.67620,  \
                16.87480, 16.61540, 16.02540, 15.14180, 13.94430, 14.17730,  \
                14.04100, 13.40410, 12.76650, 11.90370, 12.13640, 11.77530,  \
                10.88120, 10.66310, 9.89215, 10.76790, 10.91110, 10.52990,  \
                8.70338, 9.11874, 8.66423, 8.25528, 6.63576 \
               ], \
               [37.31690, 32.72750, 33.77350, 33.66920, 30.82730, 26.27020,  \
                24.10680, 24.79290, 25.18050, 24.81860, 21.50130, 19.82800,  \
                20.13520, 20.00490, 18.94500, 18.58940, 17.33180, 17.22070,  \
                16.77030, 16.63980, 15.66180, 14.71150, 14.07370, 13.38580,  \
                13.59880, 12.99550, 12.22270, 11.59600, 11.26940, 11.38050,  \
                12.04750, 10.94550, 11.49410, 11.03420, 10.10130 \
               ], \
               [47.39860, 39.12320, 41.86870, 40.80430, 37.45730, 30.70730,  \
                30.36430, 29.96290, 30.70520, 28.49630, 25.95000, 24.24240,  \
                24.75310, 24.22920, 21.41040, 20.62060, 21.46020, 20.61920,  \
                20.12620, 18.32040, 17.93180, 18.16690, 17.17260, 16.31850,  \
                16.55530, 14.79060, 15.26360, 14.98340, 14.61320, 13.49860,  \
                13.55270, 13.68910, 12.15190, 12.48680, 14.16660 \
               ], \
               [56.41690, 49.10420, 50.25750, 49.28710, 44.19260, 38.69920,  \
                35.32780, 36.86990, 36.53820, 33.54080, 31.45040, 30.04810,  \
                29.30130, 28.93750, 26.85290, 27.02840, 24.57270, 23.24440,  \
                24.02820, 24.08880, 21.91470, 21.71090, 20.08790, 20.21460,  \
                19.70970, 19.42410, 19.52540, 18.72090, 16.92220, 17.20160,  \
                16.32160, 15.63220, 15.82610, 16.55190, 16.74190 \
               ], \
               [62.63390, 63.51260, 58.88310, 54.20650, 49.77810, 48.16230,  \
                44.56990, 47.22880, 42.28170, 40.71470, 36.67070, 36.17470,  \
                35.27340, 35.31130, 35.56150, 30.89830, 28.06730, 29.79120,  \
                28.58530, 26.36250, 27.95590, 24.49640, 26.00520, 25.58810,  \
                27.04740, 23.69610, 22.28030, 20.37690, 21.10480, 19.87370,  \
                19.66780, 20.27570, 17.00700, 16.66600, 19.75850 \
               ], \
               [74.43840, 68.44420, 69.86260, 65.41410, 62.51850, 56.05490,  \
                52.89360, 48.93610, 50.62780, 44.80660, 45.29740, 38.55370,  \
                39.28180, 40.62880, 42.51730, 38.66330, 39.32670, 36.15850,  \
                33.41960, 36.64910, 32.05260, 26.28390, 28.56920, 29.30660,  \
                28.01930, 25.42550, 28.05890, 25.85320, 26.31210, 26.58800,  \
                24.21200, 24.51990, 24.41350, 22.17460, 21.74370 \
               ], \
               [87.75660, 87.30570, 98.28820, 82.46920, 74.70830, 64.15350,  \
                72.74030, 62.50860, 54.87180, 60.23710, 58.27740, 53.19250,  \
                49.85220, 46.29700, 48.14960, 41.09970, 47.16370, 51.36800,  \
                41.06460, 44.78140, 41.51960, 37.93240, 41.41820, 36.42710,  \
                40.36220, 33.24780, 33.45940, 38.72400, 34.77260, 33.00620,  \
                32.35960, 35.25210, 34.33060, 34.44170, 35.14160 \
               ], \
               [118.03600, 122.27000, 125.18300, 101.16100, 104.44700, 81.52000,  \
                71.83810, 64.36880, 76.55500, 67.06640, 73.13690, 56.85300,  \
                58.47940, 65.33080, 61.83160, 48.41980, 47.73890, 50.49350,  \
                50.42910, 40.41810, 49.83020, 55.39840, 63.78120, 47.48800,  \
                40.77480, 48.27300, 55.40480, 56.26160, 55.04060, 45.56000,  \
                48.89230, 59.07360, 58.40840, 33.09510, 44.77760 \
               ], \
               [139.74700, 116.94200, 126.66600, 138.76400, 92.15970, 109.79100,  \
                86.42300, 105.18600, 96.05880, 68.53290, 82.94520, 78.46810,  \
                74.08370, 62.42830, 79.24270, 74.87790, 64.01850, 58.57400,  \
                65.26440, 59.18020, 68.17060, 70.92940, 62.53540, 51.53680,  \
                57.50190, 57.31060, 68.89000, 51.56220, 36.08930, 31.71930,  \
                41.66260, 51.20460, 50.92360, 46.87560, 59.47980 \
               ], \
               [134.68500, 133.04700, 112.64200, 128.67600, 126.63400, 103.18800,  \
                106.85100, 129.66600, 81.66660, 87.49800, 101.46900, 93.14290,  \
                80.66750, 86.86000, 87.97140, 71.50080, 80.03090, 48.18330,  \
                79.82300, 101.56500, 105.66300, 88.87780, 63.43760, 46.98410,  \
                68.72850, 53.33310, 48.93350, 53.97000, 47.66760, 56.11470,  \
                86.51950, 72.36440, 64.43040, 72.31310, 99.26430 \
               ], \
              ]

err_up      = [[1.05431, 0.92911, 0.90117, 0.84133, 0.74259, 0.64049,  \
                0.60410, 0.62293, 0.61487, 0.58568, 0.56387, 0.55229,  \
                0.53478, 0.58243, 0.57783, 0.58307, 0.60321, 0.62912,  \
                0.67411, 0.67731, 0.71475, 0.70454, 0.78249, 0.81362,  \
                0.89607, 1.01415, 1.04309, 1.10532, 1.28931, 1.45791,  \
                1.65688, 1.66635, 1.82689, 2.16296, 2.37003 \
               ], \
               [0.77273, 0.62770, 0.63283, 0.61430, 0.58300, 0.49106,  \
                0.46448, 0.46388, 0.46588, 0.49154, 0.44016, 0.43127,  \
                0.45072, 0.47168, 0.45721, 0.47170, 0.48413, 0.49126,  \
                0.52070, 0.57264, 0.56812, 0.61346, 0.63549, 0.65810,  \
                0.74167, 0.77576, 0.79315, 0.87218, 0.97081, 0.99844,  \
                1.14166, 1.23565, 1.35760, 1.47909, 1.66224 \
               ], \
               [1.00344, 0.84771, 0.87703, 0.81340, 0.74016, 0.64667,  \
                0.62172, 0.60050, 0.60454, 0.58056, 0.54630, 0.52618,  \
                0.53816, 0.55342, 0.56254, 0.55610, 0.54308, 0.57242,  \
                0.58958, 0.61203, 0.61743, 0.61761, 0.69559, 0.70589,  \
                0.72233, 0.77253, 0.80671, 0.87584, 0.99254, 1.04584,  \
                1.00263, 1.15445, 1.24512, 1.38002, 1.39157 \
               ], \
               [0.71429, 0.61690, 0.64060, 0.63968, 0.60433, 0.53575,  \
                0.51535, 0.52227, 0.55101, 0.58278, 0.53179, 0.51530,  \
                0.53273, 0.56069, 0.55974, 0.57940, 0.58530, 0.60821,  \
                0.63199, 0.66874, 0.67789, 0.70027, 0.69379, 0.74577,  \
                0.79029, 0.83225, 0.85844, 0.88552, 0.91167, 1.00469,  \
                1.20830, 1.21152, 1.35041, 1.36425, 1.58002 \
               ], \
               [1.04994, 0.89224, 0.94476, 0.93822, 0.90331, 0.77827,  \
                0.76034, 0.74673, 0.81381, 0.76542, 0.72313, 0.69051,  \
                0.73969, 0.74601, 0.71928, 0.72554, 0.78317, 0.76627,  \
                0.79957, 0.81121, 0.80714, 0.88254, 0.87198, 0.91604,  \
                1.07326, 0.95289, 1.08787, 1.07362, 1.14812, 1.16965,  \
                1.26771, 1.39407, 1.37786, 1.53337, 1.81030 \
               ], \
               [1.59066, 1.39606, 1.42556, 1.40566, 1.33353, 1.12013,  \
                1.03241, 1.16380, 1.16276, 1.09076, 1.05690, 1.05267,  \
                1.03407, 1.06407, 1.04641, 1.09773, 1.03501, 1.03344,  \
                1.05078, 1.14108, 1.07542, 1.17741, 1.14155, 1.17279,  \
                1.22091, 1.29518, 1.32690, 1.44282, 1.32007, 1.40369,  \
                1.49478, 1.58037, 1.75331, 1.99247, 2.01161 \
               ], \
               [2.56710, 2.62162, 2.39671, 2.15394, 2.05450, 1.87234,  \
                1.65274, 2.13280, 1.62325, 1.63775, 1.51349, 1.58151,  \
                1.54055, 1.63895, 1.59811, 1.46712, 1.41041, 1.50527,  \
                1.54401, 1.46002, 1.52331, 1.47604, 1.63253, 1.70740,  \
                1.75466, 1.66490, 1.69902, 1.71770, 1.75000, 1.87686,  \
                1.89055, 2.00874, 2.10082, 2.19577, 2.28540 \
               ], \
               [7.01419, 6.20278, 6.06493, 5.49456, 5.31910, 4.56628,  \
                4.31161, 3.87746, 4.01235, 3.76146, 3.46537, 3.00060,  \
                3.04175, 3.20766, 3.32685, 3.09700, 3.16080, 2.94430,  \
                2.82923, 3.10460, 2.69154, 2.35804, 2.52682, 2.59581,  \
                2.98827, 2.55574, 2.54898, 2.39953, 2.51869, 2.81348,  \
                2.94531, 2.89238, 2.83894, 2.73156, 3.00405 \
               ], \
               [8.74206, 9.03578, 9.21913, 8.73917, 6.94900, 5.54583,  \
                7.52887, 5.81498, 5.41103, 5.58487, 5.24907, 5.73655,  \
                4.53499, 4.33798, 4.26192, 3.77447, 4.34408, 5.51545,  \
                3.85138, 4.40565, 4.11871, 3.87519, 4.42309, 3.61361,  \
                4.54331, 4.02951, 4.16600, 4.38442, 4.22827, 5.47036,  \
                4.26788, 4.60871, 4.72180, 5.63055, 5.11321 \
               ], \
               [13.94392, 12.56465, 13.92834, 11.16990, 10.95302, 8.76699,  \
                7.29038, 6.90138, 7.77648, 6.72099, 8.18254, 6.93645,  \
                7.49287, 7.52543, 7.57280, 6.06953, 6.03851, 6.48977,  \
                5.73209, 4.89756, 7.27028, 8.32598, 7.85075, 6.90087,  \
                6.44234, 6.75313, 9.76638, 8.35148, 9.59598, 8.61921,  \
                8.90341, 11.01865, 11.57151, 7.79483, 11.25068 \
               ], \
               [27.72469, 21.09319, 21.97533, 22.50198, 16.19222, 21.11222,  \
                16.05992, 17.29048, 17.93531, 10.54487, 12.73688, 12.70018,  \
                12.64219, 11.41546, 13.28638, 11.13764, 11.27847, 10.53096,  \
                12.15508, 11.09168, 10.68483, 13.01724, 11.49772, 9.65058,  \
                11.27909, 12.37282, 14.89102, 10.90613, 9.91564, 10.35910,  \
                10.26533, 10.69887, 13.42710, 10.51291, 13.06279 \
               ], \
               [31.99788, 20.54201, 24.24986, 24.92818, 24.69674, 16.14727,  \
                26.91205, 26.66991, 15.19148, 16.50694, 19.33833, 16.65110,  \
                15.23958, 15.83812, 13.93344, 10.95404, 16.66409, 10.30775,  \
                21.71051, 18.54386, 22.75397, 18.53114, 14.67771, 11.51589,  \
                15.57881, 12.29335, 10.98704, 16.92341, 13.80406, 15.22739,  \
                24.68206, 24.38592, 22.57838, 20.29706, 24.06798 \
               ], \
              ]

err_down    = [[1.05431, 0.92911, 0.90117, 0.84133, 0.74259, 0.64049,  \
                0.60410, 0.62293, 0.61487, 0.58568, 0.56387, 0.55229,  \
                0.53478, 0.58243, 0.57783, 0.58307, 0.60321, 0.62912,  \
                0.67411, 0.67731, 0.71475, 0.70454, 0.78249, 0.81362,  \
                0.89607, 1.01415, 1.04309, 1.10532, 1.28931, 1.45791,  \
                1.65688, 1.66635, 1.82689, 2.16296, 2.37003 \
               ], \
               [0.77273, 0.62770, 0.63283, 0.61430, 0.58300, 0.49106,  \
                0.46448, 0.46388, 0.46588, 0.49154, 0.44016, 0.43127,  \
                0.45072, 0.47168, 0.45721, 0.47170, 0.48413, 0.49126,  \
                0.52070, 0.57264, 0.56812, 0.61346, 0.63549, 0.65810,  \
                0.74167, 0.77576, 0.79315, 0.87218, 0.97081, 0.99844,  \
                1.14166, 1.23565, 1.35760, 1.47909, 1.66224 \
               ], \
               [1.00344, 0.84771, 0.87703, 0.81340, 0.74016, 0.64667,  \
                0.62172, 0.60050, 0.60454, 0.58056, 0.54630, 0.52618,  \
                0.53816, 0.55342, 0.56254, 0.55610, 0.54308, 0.57242,  \
                0.58958, 0.61203, 0.61743, 0.61761, 0.69559, 0.70589,  \
                0.72233, 0.77253, 0.80671, 0.87584, 0.99254, 1.04584,  \
                1.00263, 1.15445, 1.24512, 1.38002, 1.39157 \
               ], \
               [0.71429, 0.61690, 0.64060, 0.63968, 0.60433, 0.53575,  \
                0.51535, 0.52227, 0.55101, 0.58278, 0.53179, 0.51530,  \
                0.53273, 0.56069, 0.55974, 0.57940, 0.58530, 0.60821,  \
                0.63199, 0.66874, 0.67789, 0.70027, 0.69379, 0.74577,  \
                0.79029, 0.83225, 0.85844, 0.88552, 0.91167, 1.00469,  \
                1.20830, 1.21152, 1.35041, 1.36425, 1.58002 \
               ], \
               [1.04994, 0.89224, 0.94476, 0.93822, 0.90331, 0.77827,  \
                0.76034, 0.74673, 0.81381, 0.76542, 0.72313, 0.69051,  \
                0.73969, 0.74601, 0.71928, 0.72554, 0.78317, 0.76627,  \
                0.79957, 0.81121, 0.80714, 0.88254, 0.87198, 0.91604,  \
                1.07326, 0.95289, 1.08787, 1.07362, 1.14812, 1.16965,  \
                1.26771, 1.39407, 1.37786, 1.53337, 1.81030 \
               ], \
               [1.59066, 1.39606, 1.42556, 1.40566, 1.33353, 1.12013,  \
                1.03241, 1.16380, 1.16276, 1.09076, 1.05690, 1.05267,  \
                1.03407, 1.06407, 1.04641, 1.09773, 1.03501, 1.03344,  \
                1.05078, 1.14108, 1.07542, 1.17741, 1.14155, 1.17279,  \
                1.22091, 1.29518, 1.32690, 1.44282, 1.32007, 1.40369,  \
                1.49478, 1.58037, 1.75331, 1.99247, 2.01161 \
               ], \
               [2.56710, 2.62162, 2.39671, 2.15394, 2.05450, 1.87234,  \
                1.65274, 2.13280, 1.62325, 1.63775, 1.51349, 1.58151,  \
                1.54055, 1.63895, 1.59811, 1.46712, 1.41041, 1.50527,  \
                1.54401, 1.46002, 1.52331, 1.47604, 1.63253, 1.70740,  \
                1.75466, 1.66490, 1.69902, 1.71770, 1.75000, 1.87686,  \
                1.89055, 2.00874, 2.10082, 2.19577, 2.28540 \
               ], \
               [7.01419, 6.20278, 6.06493, 5.49456, 5.31910, 4.56628,  \
                4.31161, 3.87746, 4.01235, 3.76146, 3.46537, 3.00060,  \
                3.04175, 3.20766, 3.32685, 3.09700, 3.16080, 2.94430,  \
                2.82923, 3.10460, 2.69154, 2.35804, 2.52682, 2.59581,  \
                2.98827, 2.55574, 2.54898, 2.39953, 2.51869, 2.81348,  \
                2.94531, 2.89238, 2.83894, 2.73156, 3.00405 \
               ], \
               [8.74206, 9.03578, 9.21913, 8.73917, 6.94900, 5.54583,  \
                7.52887, 5.81498, 5.41103, 5.58487, 5.24907, 5.73655,  \
                4.53499, 4.33798, 4.26192, 3.77447, 4.34408, 5.51545,  \
                3.85138, 4.40565, 4.11871, 3.87519, 4.42309, 3.61361,  \
                4.54331, 4.02951, 4.16600, 4.38442, 4.22827, 5.47036,  \
                4.26788, 4.60871, 4.72180, 5.63055, 5.11321 \
               ], \
               [13.94392, 12.56465, 13.92834, 11.16990, 10.95302, 8.76699,  \
                7.29038, 6.90138, 7.77648, 6.72099, 8.18254, 6.93645,  \
                7.49287, 7.52543, 7.57280, 6.06953, 6.03851, 6.48977,  \
                5.73209, 4.89756, 7.27028, 8.32598, 7.85075, 6.90087,  \
                6.44234, 6.75313, 9.76638, 8.35148, 9.59598, 8.61921,  \
                8.90341, 11.01865, 11.57151, 7.79483, 11.25068 \
               ], \
               [27.72469, 21.09319, 21.97533, 22.50198, 16.19222, 21.11222,  \
                16.05992, 17.29048, 17.93531, 10.54487, 12.73688, 12.70018,  \
                12.64219, 11.41546, 13.28638, 11.13764, 11.27847, 10.53096,  \
                12.15508, 11.09168, 10.68483, 13.01724, 11.49772, 9.65058,  \
                11.27909, 12.37282, 14.89102, 10.90613, 9.91564, 10.35910,  \
                10.26533, 10.69887, 13.42710, 10.51291, 13.06279 \
               ], \
               [31.99788, 20.54201, 24.24986, 24.92818, 24.69674, 16.14727,  \
                26.91205, 26.66991, 15.19148, 16.50694, 19.33833, 16.65110,  \
                15.23958, 15.83812, 13.93344, 10.95404, 16.66409, 10.30775,  \
                21.71051, 18.54386, 22.75397, 18.53114, 14.67771, 11.51589,  \
                15.57881, 12.29335, 10.98704, 16.92341, 13.80406, 15.22739,  \
                24.68206, 24.38592, 22.57838, 20.29706, 24.06798 \
               ], \
              ]

err_up2     = None

err_down2   = None

upper_lim   = [[False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
              ]

lower_lim   = [[False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
               [False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False, False,  \
                False, False, False, False, False \
               ], \
              ]