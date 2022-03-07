import numpy as np


EXAMPLE = [16,1,2,0,4,2,7,1,2,14]
DATA = [1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,40,1287,207,174,6,200,690,504,1589,211,52,280,1315,2,113,916,1265,14,298,1167,1132,251,176,1695,1229,38,800,612,22,1357,506,1021,716,41,1574,16,240,38,356,170,14,843,229,482,219,635,396,140,694,192,137,198,634,240,1205,712,850,1067,642,274,177,1428,107,46,1558,907,409,44,749,447,535,972,965,418,250,387,1002,60,623,169,43,694,1504,1561,547,481,546,314,309,411,458,1007,96,389,247,108,120,1153,172,939,276,250,53,126,545,560,98,589,887,53,95,42,313,789,6,1080,344,918,959,761,131,64,411,84,1194,450,104,805,1266,126,425,606,1166,649,204,593,398,1154,119,493,256,1344,374,1379,149,549,661,142,531,108,286,20,260,296,638,1246,82,274,23,712,240,330,671,813,101,155,914,426,342,364,846,227,1218,654,338,519,90,1148,210,859,557,692,307,1173,427,309,0,1116,385,312,318,113,309,547,1557,962,130,179,478,504,1723,476,20,227,928,835,343,603,377,517,1417,371,1402,6,243,48,904,1033,666,20,229,13,9,111,485,1283,0,423,428,169,39,380,9,1559,342,3,1816,391,459,91,191,1054,8,205,1745,493,0,1763,506,199,262,262,573,1666,1690,66,111,187,340,575,755,323,408,368,1162,426,156,6,557,871,385,1517,264,5,225,828,195,710,848,992,313,1139,751,544,521,856,172,203,125,520,75,1134,859,169,1,65,413,750,417,505,965,932,40,375,1173,11,758,751,1196,1850,965,770,758,1543,897,1506,172,353,227,212,15,0,231,448,7,3,131,1668,205,296,30,529,617,1158,114,682,412,160,141,55,971,155,550,207,242,812,699,657,182,649,927,270,274,1656,850,907,1030,366,518,188,206,382,685,554,208,811,921,160,18,1197,577,937,294,228,108,448,514,842,230,644,410,1385,203,1473,307,557,277,944,403,724,295,323,155,413,1777,48,66,207,677,269,170,301,840,115,122,660,113,6,1112,64,64,553,605,410,358,1060,160,770,551,159,765,143,1460,1295,687,200,328,56,146,211,661,517,132,90,314,1274,293,11,424,372,74,338,859,868,380,600,138,1133,1040,580,546,128,147,393,1032,1281,473,1002,134,0,253,566,142,239,636,747,23,1208,779,1331,166,23,498,956,332,460,894,68,1994,9,130,67,323,521,310,1,122,1005,273,1168,271,127,147,445,131,249,4,176,453,1334,296,172,113,152,297,693,420,1264,443,301,660,35,1302,500,604,936,770,1175,77,238,1,797,114,125,49,91,568,581,62,511,1088,32,73,508,452,325,11,366,87,347,709,990,12,288,105,561,796,31,1823,358,876,940,107,94,1363,301,709,23,1221,529,37,963,703,750,1149,133,772,718,1609,669,47,343,1093,434,47,916,600,149,353,199,300,384,577,667,1278,228,712,982,768,182,90,210,136,1472,810,493,342,1429,133,55,1715,540,123,12,356,244,266,336,373,56,317,249,216,147,17,45,417,1020,1428,488,79,325,104,259,475,1670,45,126,870,826,74,140,222,964,170,745,942,1469,533,283,93,294,18,783,1269,1181,1028,40,208,305,867,53,950,172,337,657,1577,1741,1139,27,397,15,105,71,1081,347,430,594,1740,195,1069,853,21,12,1452,545,153,294,229,983,145,187,1045,446,749,16,534,216,449,420,137,846,286,615,24,1362,1155,60,24,6,314,65,179,838,685,36,1018,748,680,1439,142,27,341,61,571,609,78,9,119,143,178,236,63,581,216,254,402,354,302,888,348,1277,1236,59,34,12,128,235,110,666,549,1190,492,1009,149,417,553,1091,567,985,605,693,72,787,118,439,421,204,308,320,506,464,510,507,1066,578,54,63,648,93,471,46,71,83,424,1561,236,112,274,610,1319,62,363,264,184,848,10,0,194,81,132,1215,191,456,163,275,39,434,725,0,215,99,726,929,551,509,1227,40,565,526,560,30,1124,1061,96,20,33,130,60,24,1482,1449,680,333,45,82,1164,275,162,610,446,1392,233,1052,218,130,22,23,1411,140,499,864,50,143,748,1463,375,1493,510,730,723,465,252,829,737,1603,261,28,839,702,320,612,101,329,567,67,328,936,857,142,596,341,1372,315,521,1250,279,59,1103,2,634,588,711,171,1659,772,166,560,130,472,114,103,41,75,89,34,182,285,264,349,24,1650,50,864,13,429,732,556,1188,532,42,162,1582,786,295,293,9,507,675,9,840,1277,1150,552,1746,437,63,1053,1456,1,675,266,666,12,1457]


def run(data):
    arr = np.array(data)
    maximum = np.max(arr)
    return np.min([np.sum(np.abs(arr - i)) for i in range(maximum)])


@np.vectorize
def compute_fuel(x):
    return sum(range(x+1))


def run_2(data):
    arr = np.array(data)
    maximum = np.max(arr)
    distances = np.array([np.abs(arr - i) for i in range(maximum)])
    return np.min(np.sum(compute_fuel(distances), axis=1))


def main():
    res = run(DATA)
    print(res)
    res = run_2(DATA)
    print(res)


if __name__ == '__main__':
    main()
