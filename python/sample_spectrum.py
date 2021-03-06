"""
file: sample_spectrum.py
brief:
author: S. V. Paulauskas
date: December 19, 2020
"""

cs137_spectrum = [(1, 143), (2, 169), (3, 179), (4, 192), (5, 200), (6, 245), (7, 284),
                  (8, 316), (9, 360), (10, 406), (11, 482), (12, 514), (13, 552), (14, 648),
                  (15, 761), (16, 853), (17, 936), (18, 1123), (19, 1227), (20, 1429), (21, 1513),
                  (22, 1767), (23, 1987), (24, 2183), (25, 2257), (26, 2447), (27, 2754),
                  (28, 3053), (29, 3252), (30, 3309), (31, 3561), (32, 3603), (33, 3833),
                  (34, 3933), (35, 4031), (36, 4202), (37, 4187), (38, 4149), (39, 4001),
                  (40, 4123), (41, 4002), (42, 3901), (43, 3819), (44, 3723), (45, 3460),
                  (46, 3434), (47, 3245), (48, 3123), (49, 2977), (50, 2839), (51, 2682),
                  (52, 2564), (53, 2361), (54, 2227), (55, 2108), (56, 2112), (57, 1886),
                  (58, 1825), (59, 1706), (60, 1653), (61, 1610), (62, 1521), (63, 1413),
                  (64, 1391), (65, 1360), (66, 1245), (67, 1333), (68, 1246), (69, 1213),
                  (70, 1174), (71, 1197), (72, 1159), (73, 1119), (74, 1179), (75, 1132), (76, 997),
                  (77, 1080), (78, 1156), (79, 1148), (80, 1067), (81, 1118), (82, 1107),
                  (83, 1114), (84, 1104), (85, 1049), (86, 1143), (87, 1082), (88, 1002),
                  (89, 1098), (90, 1063), (91, 1074), (92, 1069), (93, 1135), (94, 1071),
                  (95, 1051), (96, 1101), (97, 1028), (98, 1053), (99, 1014), (100, 1033),
                  (101, 986), (102, 1071), (103, 1107), (104, 1037), (105, 1052), (106, 1093),
                  (107, 1077), (108, 1074), (109, 1016), (110, 1090), (111, 1035), (112, 1086),
                  (113, 1167), (114, 1178), (115, 1206), (116, 1144), (117, 1218), (118, 1143),
                  (119, 1209), (120, 1188), (121, 1181), (122, 1230), (123, 1272), (124, 1343),
                  (125, 1323), (126, 1345), (127, 1367), (128, 1354), (129, 1390), (130, 1428),
                  (131, 1503), (132, 1498), (133, 1550), (134, 1500), (135, 1540), (136, 1522),
                  (137, 1617), (138, 1553), (139, 1647), (140, 1653), (141, 1643), (142, 1570),
                  (143, 1589), (144, 1651), (145, 1654), (146, 1593), (147, 1626), (148, 1611),
                  (149, 1673), (150, 1580), (151, 1557), (152, 1520), (153, 1617), (154, 1559),
                  (155, 1519), (156, 1541), (157, 1475), (158, 1472), (159, 1415), (160, 1478),
                  (161, 1433), (162, 1481), (163, 1484), (164, 1450), (165, 1364), (166, 1344),
                  (167, 1335), (168, 1330), (169, 1304), (170, 1285), (171, 1313), (172, 1230),
                  (173, 1279), (174, 1173), (175, 1226), (176, 1264), (177, 1303), (178, 1213),
                  (179, 1151), (180, 1128), (181, 1151), (182, 1126), (183, 1174), (184, 1117),
                  (185, 1109), (186, 1127), (187, 1039), (188, 1096), (189, 1053), (190, 1092),
                  (191, 1030), (192, 1132), (193, 1074), (194, 1019), (195, 1065), (196, 990),
                  (197, 1043), (198, 1036), (199, 1067), (200, 1049), (201, 1060), (202, 1056),
                  (203, 978), (204, 1056), (205, 1006), (206, 979), (207, 997), (208, 1000),
                  (209, 1009), (210, 987), (211, 935), (212, 1021), (213, 984), (214, 989),
                  (215, 1049), (216, 968), (217, 996), (218, 998), (219, 1015), (220, 1032),
                  (221, 1012), (222, 1012), (223, 1006), (224, 1045), (225, 1056), (226, 1009),
                  (227, 1036), (228, 970), (229, 1011), (230, 1014), (231, 1058), (232, 992),
                  (233, 1056), (234, 983), (235, 1028), (236, 1014), (237, 1039), (238, 1091),
                  (239, 1009), (240, 1028), (241, 1057), (242, 1036), (243, 1066), (244, 1048),
                  (245, 1089), (246, 1040), (247, 1050), (248, 1043), (249, 1073), (250, 1030),
                  (251, 1050), (252, 1016), (253, 1075), (254, 1086), (255, 1072), (256, 1064),
                  (257, 1028), (258, 1060), (259, 1057), (260, 1103), (261, 1063), (262, 1030),
                  (263, 1099), (264, 1062), (265, 1046), (266, 1110), (267, 1181), (268, 1051),
                  (269, 1053), (270, 1031), (271, 1125), (272, 1121), (273, 1105), (274, 1083),
                  (275, 1101), (276, 1129), (277, 1044), (278, 1081), (279, 1069), (280, 1099),
                  (281, 1108), (282, 1132), (283, 1091), (284, 1059), (285, 1145), (286, 1092),
                  (287, 1173), (288, 1101), (289, 1064), (290, 1076), (291, 1115), (292, 1168),
                  (293, 1171), (294, 1145), (295, 1110), (296, 1136), (297, 1186), (298, 1078),
                  (299, 1165), (300, 1151), (301, 1108), (302, 1165), (303, 1175), (304, 1209),
                  (305, 1160), (306, 1099), (307, 1166), (308, 1196), (309, 1192), (310, 1183),
                  (311, 1214), (312, 1112), (313, 1230), (314, 1199), (315, 1222), (316, 1178),
                  (317, 1184), (318, 1197), (319, 1189), (320, 1243), (321, 1232), (322, 1258),
                  (323, 1265), (324, 1253), (325, 1264), (326, 1272), (327, 1293), (328, 1256),
                  (329, 1259), (330, 1276), (331, 1270), (332, 1302), (333, 1264), (334, 1336),
                  (335, 1245), (336, 1319), (337, 1341), (338, 1335), (339, 1335), (340, 1328),
                  (341, 1416), (342, 1338), (343, 1396), (344, 1443), (345, 1384), (346, 1392),
                  (347, 1356), (348, 1359), (349, 1314), (350, 1342), (351, 1437), (352, 1426),
                  (353, 1426), (354, 1413), (355, 1428), (356, 1499), (357, 1561), (358, 1508),
                  (359, 1501), (360, 1493), (361, 1560), (362, 1585), (363, 1498), (364, 1519),
                  (365, 1594), (366, 1563), (367, 1683), (368, 1627), (369, 1626), (370, 1630),
                  (371, 1711), (372, 1602), (373, 1731), (374, 1684), (375, 1725), (376, 1760),
                  (377, 1739), (378, 1755), (379, 1797), (380, 1704), (381, 1792), (382, 1777),
                  (383, 1834), (384, 1804), (385, 1837), (386, 1798), (387, 1800), (388, 1748),
                  (389, 1827), (390, 1850), (391, 1876), (392, 1911), (393, 1846), (394, 1865),
                  (395, 1801), (396, 1925), (397, 1829), (398, 1891), (399, 1900), (400, 1914),
                  (401, 1886), (402, 1898), (403, 1844), (404, 1960), (405, 1765), (406, 1818),
                  (407, 1899), (408, 1865), (409, 1874), (410, 1891), (411, 1875), (412, 1851),
                  (413, 1897), (414, 1853), (415, 1860), (416, 1826), (417, 1712), (418, 1732),
                  (419, 1809), (420, 1832), (421, 1850), (422, 1813), (423, 1751), (424, 1810),
                  (425, 1746), (426, 1768), (427, 1801), (428, 1779), (429, 1780), (430, 1707),
                  (431, 1698), (432, 1780), (433, 1776), (434, 1769), (435, 1750), (436, 1730),
                  (437, 1706), (438, 1784), (439, 1747), (440, 1674), (441, 1699), (442, 1702),
                  (443, 1655), (444, 1619), (445, 1720), (446, 1708), (447, 1723), (448, 1721),
                  (449, 1691), (450, 1623), (451, 1677), (452, 1633), (453, 1650), (454, 1672),
                  (455, 1705), (456, 1659), (457, 1665), (458, 1671), (459, 1614), (460, 1665),
                  (461, 1623), (462, 1639), (463, 1705), (464, 1651), (465, 1622), (466, 1633),
                  (467, 1625), (468, 1636), (469, 1623), (470, 1578), (471, 1604), (472, 1597),
                  (473, 1624), (474, 1692), (475, 1571), (476, 1583), (477, 1547), (478, 1510),
                  (479, 1588), (480, 1684), (481, 1612), (482, 1571), (483, 1573), (484, 1636),
                  (485, 1672), (486, 1618), (487, 1578), (488, 1628), (489, 1608), (490, 1575),
                  (491, 1639), (492, 1529), (493, 1510), (494, 1678), (495, 1583), (496, 1575),
                  (497, 1577), (498, 1576), (499, 1545), (500, 1500), (501, 1545), (502, 1532),
                  (503, 1573), (504, 1578), (505, 1576), (506, 1570), (507, 1500), (508, 1561),
                  (509, 1577), (510, 1551), (511, 1570), (512, 1542), (513, 1573), (514, 1517),
                  (515, 1548), (516, 1491), (517, 1490), (518, 1551), (519, 1567), (520, 1547),
                  (521, 1483), (522, 1508), (523, 1530), (524, 1559), (525, 1555), (526, 1549),
                  (527, 1495), (528, 1486), (529, 1548), (530, 1472), (531, 1442), (532, 1438),
                  (533, 1511), (534, 1486), (535, 1507), (536, 1577), (537, 1501), (538, 1526),
                  (539, 1530), (540, 1533), (541, 1477), (542, 1419), (543, 1514), (544, 1463),
                  (545, 1509), (546, 1467), (547, 1412), (548, 1424), (549, 1429), (550, 1446),
                  (551, 1456), (552, 1507), (553, 1506), (554, 1436), (555, 1410), (556, 1463),
                  (557, 1429), (558, 1396), (559, 1410), (560, 1516), (561, 1457), (562, 1437),
                  (563, 1429), (564, 1505), (565, 1412), (566, 1472), (567, 1451), (568, 1437),
                  (569, 1344), (570, 1492), (571, 1451), (572, 1433), (573, 1468), (574, 1452),
                  (575, 1445), (576, 1491), (577, 1461), (578, 1436), (579, 1390), (580, 1320),
                  (581, 1371), (582, 1504), (583, 1431), (584, 1489), (585, 1522), (586, 1423),
                  (587, 1401), (588, 1405), (589, 1394), (590, 1442), (591, 1443), (592, 1381),
                  (593, 1340), (594, 1372), (595, 1420), (596, 1406), (597, 1407), (598, 1453),
                  (599, 1450), (600, 1367), (601, 1383), (602, 1444), (603, 1407), (604, 1397),
                  (605, 1322), (606, 1366), (607, 1413), (608, 1389), (609, 1421), (610, 1298),
                  (611, 1306), (612, 1304), (613, 1292), (614, 1357), (615, 1295), (616, 1320),
                  (617, 1351), (618, 1320), (619, 1384), (620, 1402), (621, 1337), (622, 1269),
                  (623, 1328), (624, 1386), (625, 1357), (626, 1328), (627, 1297), (628, 1269),
                  (629, 1391), (630, 1243), (631, 1286), (632, 1319), (633, 1366), (634, 1341),
                  (635, 1343), (636, 1332), (637, 1324), (638, 1269), (639, 1290), (640, 1299),
                  (641, 1316), (642, 1316), (643, 1283), (644, 1269), (645, 1348), (646, 1243),
                  (647, 1298), (648, 1290), (649, 1361), (650, 1256), (651, 1370), (652, 1302),
                  (653, 1260), (654, 1313), (655, 1392), (656, 1207), (657, 1295), (658, 1274),
                  (659, 1323), (660, 1282), (661, 1318), (662, 1250), (663, 1256), (664, 1275),
                  (665, 1260), (666, 1290), (667, 1311), (668, 1244), (669, 1272), (670, 1300),
                  (671, 1284), (672, 1265), (673, 1268), (674, 1202), (675, 1271), (676, 1313),
                  (677, 1233), (678, 1281), (679, 1289), (680, 1261), (681, 1298), (682, 1250),
                  (683, 1213), (684, 1179), (685, 1252), (686, 1264), (687, 1192), (688, 1333),
                  (689, 1275), (690, 1258), (691, 1284), (692, 1335), (693, 1333), (694, 1219),
                  (695, 1186), (696, 1288), (697, 1281), (698, 1276), (699, 1203), (700, 1222),
                  (701, 1235), (702, 1300), (703, 1281), (704, 1225), (705, 1264), (706, 1227),
                  (707, 1273), (708, 1264), (709, 1218), (710, 1234), (711, 1263), (712, 1190),
                  (713, 1293), (714, 1246), (715, 1247), (716, 1249), (717, 1228), (718, 1272),
                  (719, 1220), (720, 1230), (721, 1215), (722, 1225), (723, 1202), (724, 1180),
                  (725, 1204), (726, 1281), (727, 1210), (728, 1217), (729, 1185), (730, 1232),
                  (731, 1237), (732, 1287), (733, 1265), (734, 1264), (735, 1217), (736, 1212),
                  (737, 1209), (738, 1268), (739, 1225), (740, 1188), (741, 1241), (742, 1208),
                  (743, 1245), (744, 1216), (745, 1183), (746, 1160), (747, 1325), (748, 1224),
                  (749, 1230), (750, 1232), (751, 1190), (752, 1218), (753, 1237), (754, 1135),
                  (755, 1186), (756, 1163), (757, 1247), (758, 1245), (759, 1199), (760, 1257),
                  (761, 1184), (762, 1236), (763, 1181), (764, 1150), (765, 1224), (766, 1169),
                  (767, 1205), (768, 1185), (769, 1154), (770, 1247), (771, 1186), (772, 1194),
                  (773, 1168), (774, 1252), (775, 1186), (776, 1226), (777, 1175), (778, 1198),
                  (779, 1260), (780, 1289), (781, 1137), (782, 1246), (783, 1225), (784, 1165),
                  (785, 1187), (786, 1230), (787, 1232), (788, 1160), (789, 1195), (790, 1179),
                  (791, 1202), (792, 1240), (793, 1199), (794, 1209), (795, 1250), (796, 1138),
                  (797, 1207), (798, 1196), (799, 1203), (800, 1220), (801, 1165), (802, 1150),
                  (803, 1189), (804, 1135), (805, 1099), (806, 1200), (807, 1201), (808, 1233),
                  (809, 1269), (810, 1179), (811, 1139), (812, 1136), (813, 1196), (814, 1204),
                  (815, 1093), (816, 1132), (817, 1094), (818, 1163), (819, 1191), (820, 1185),
                  (821, 1197), (822, 1198), (823, 1218), (824, 1108), (825, 1106), (826, 1180),
                  (827, 1123), (828, 1124), (829, 1094), (830, 1143), (831, 1075), (832, 1181),
                  (833, 1138), (834, 1157), (835, 1145), (836, 1137), (837, 1057), (838, 1144),
                  (839, 1164), (840, 1102), (841, 1049), (842, 1133), (843, 1122), (844, 1107),
                  (845, 1162), (846, 1132), (847, 1123), (848, 1062), (849, 1118), (850, 1119),
                  (851, 1136), (852, 1030), (853, 1012), (854, 1118), (855, 1086), (856, 1023),
                  (857, 1134), (858, 1043), (859, 1090), (860, 1065), (861, 1017), (862, 1083),
                  (863, 1036), (864, 1034), (865, 1038), (866, 1035), (867, 969), (868, 1029),
                  (869, 1078), (870, 1061), (871, 989), (872, 990), (873, 1049), (874, 1013),
                  (875, 1018), (876, 1065), (877, 962), (878, 1031), (879, 1055), (880, 978),
                  (881, 998), (882, 965), (883, 941), (884, 974), (885, 982), (886, 980),
                  (887, 949), (888, 969), (889, 929), (890, 983), (891, 944), (892, 881),
                  (893, 896), (894, 957), (895, 952), (896, 900), (897, 892), (898, 945),
                  (899, 917), (900, 919), (901, 885), (902, 854), (903, 872), (904, 858),
                  (905, 810), (906, 900), (907, 869), (908, 842), (909, 838), (910, 830),
                  (911, 827), (912, 844), (913, 797), (914, 789), (915, 852), (916, 789),
                  (917, 759), (918, 840), (919, 821), (920, 739), (921, 740), (922, 777),
                  (923, 741), (924, 762), (925, 766), (926, 777), (927, 749), (928, 735),
                  (929, 701), (930, 721), (931, 703), (932, 700), (933, 752), (934, 687),
                  (935, 672), (936, 724), (937, 677), (938, 698), (939, 677), (940, 705),
                  (941, 675), (942, 654), (943, 655), (944, 588), (945, 597), (946, 626),
                  (947, 628), (948, 586), (949, 574), (950, 626), (951, 632), (952, 584),
                  (953, 575), (954, 540), (955, 595), (956, 529), (957, 587), (958, 536),
                  (959, 583), (960, 579), (961, 521), (962, 547), (963, 538), (964, 529),
                  (965, 530), (966, 523), (967, 538), (968, 518), (969, 478), (970, 523),
                  (971, 480), (972, 458), (973, 493), (974, 468), (975, 442), (976, 452),
                  (977, 489), (978, 463), (979, 464), (980, 420), (981, 524), (982, 476),
                  (983, 463), (984, 400), (985, 432), (986, 425), (987, 436), (988, 422),
                  (989, 414), (990, 429), (991, 423), (992, 398), (993, 395), (994, 469),
                  (995, 402), (996, 426), (997, 387), (998, 390), (999, 370), (1000, 398),
                  (1001, 379), (1002, 417), (1003, 371), (1004, 378), (1005, 366), (1006, 352),
                  (1007, 331), (1008, 367), (1009, 341), (1010, 369), (1011, 405), (1012, 356),
                  (1013, 352), (1014, 340), (1015, 360), (1016, 347), (1017, 332), (1018, 386),
                  (1019, 347), (1020, 354), (1021, 293), (1022, 341), (1023, 335), (1024, 321),
                  (1025, 331), (1026, 331), (1027, 320), (1028, 361), (1029, 324), (1030, 309),
                  (1031, 349), (1032, 340), (1033, 349), (1034, 275), (1035, 298), (1036, 327),
                  (1037, 311), (1038, 298), (1039, 333), (1040, 316), (1041, 286), (1042, 302),
                  (1043, 262), (1044, 289), (1045, 318), (1046, 335), (1047, 308), (1048, 298),
                  (1049, 285), (1050, 282), (1051, 316), (1052, 344), (1053, 276), (1054, 289),
                  (1055, 289), (1056, 284), (1057, 301), (1058, 311), (1059, 301), (1060, 313),
                  (1061, 291), (1062, 237), (1063, 282), (1064, 294), (1065, 277), (1066, 274),
                  (1067, 286), (1068, 293), (1069, 274), (1070, 299), (1071, 281), (1072, 300),
                  (1073, 279), (1074, 303), (1075, 277), (1076, 293), (1077, 290), (1078, 287),
                  (1079, 282), (1080, 262), (1081, 248), (1082, 271), (1083, 247), (1084, 298),
                  (1085, 264), (1086, 276), (1087, 295), (1088, 255), (1089, 267), (1090, 283),
                  (1091, 281), (1092, 279), (1093, 283), (1094, 274), (1095, 266), (1096, 271),
                  (1097, 273), (1098, 304), (1099, 273), (1100, 297), (1101, 296), (1102, 278),
                  (1103, 281), (1104, 302), (1105, 288), (1106, 284), (1107, 302), (1108, 289),
                  (1109, 266), (1110, 306), (1111, 294), (1112, 282), (1113, 271), (1114, 268),
                  (1115, 291), (1116, 317), (1117, 327), (1118, 294), (1119, 298), (1120, 301),
                  (1121, 283), (1122, 324), (1123, 325), (1124, 309), (1125, 334), (1126, 364),
                  (1127, 312), (1128, 316), (1129, 339), (1130, 325), (1131, 356), (1132, 347),
                  (1133, 332), (1134, 338), (1135, 340), (1136, 371), (1137, 355), (1138, 341),
                  (1139, 346), (1140, 371), (1141, 372), (1142, 371), (1143, 368), (1144, 381),
                  (1145, 391), (1146, 417), (1147, 397), (1148, 370), (1149, 405), (1150, 421),
                  (1151, 419), (1152, 421), (1153, 413), (1154, 391), (1155, 470), (1156, 433),
                  (1157, 488), (1158, 479), (1159, 410), (1160, 486), (1161, 480), (1162, 508),
                  (1163, 483), (1164, 500), (1165, 531), (1166, 502), (1167, 525), (1168, 540),
                  (1169, 581), (1170, 525), (1171, 563), (1172, 601), (1173, 615), (1174, 624),
                  (1175, 576), (1176, 688), (1177, 610), (1178, 668), (1179, 642), (1180, 685),
                  (1181, 685), (1182, 725), (1183, 704), (1184, 682), (1185, 753), (1186, 764),
                  (1187, 770), (1188, 796), (1189, 764), (1190, 746), (1191, 874), (1192, 861),
                  (1193, 908), (1194, 896), (1195, 922), (1196, 1005), (1197, 1052), (1198, 1002),
                  (1199, 985), (1200, 1106), (1201, 1061), (1202, 1063), (1203, 1117), (1204, 1066),
                  (1205, 1180), (1206, 1198), (1207, 1212), (1208, 1252), (1209, 1338),
                  (1210, 1421), (1211, 1343), (1212, 1480), (1213, 1447), (1214, 1436),
                  (1215, 1529), (1216, 1557), (1217, 1567), (1218, 1628), (1219, 1665),
                  (1220, 1771), (1221, 1734), (1222, 1780), (1223, 1971), (1224, 1995),
                  (1225, 1978), (1226, 1992), (1227, 2071), (1228, 2157), (1229, 2165),
                  (1230, 2235), (1231, 2202), (1232, 2271), (1233, 2342), (1234, 2483),
                  (1235, 2465), (1236, 2637), (1237, 2731), (1238, 2575), (1239, 2750),
                  (1240, 2870), (1241, 2828), (1242, 3064), (1243, 3080), (1244, 3143),
                  (1245, 3167), (1246, 3304), (1247, 3428), (1248, 3533), (1249, 3460),
                  (1250, 3620), (1251, 3632), (1252, 3778), (1253, 3825), (1254, 3883),
                  (1255, 4060), (1256, 4152), (1257, 4234), (1258, 4286), (1259, 4350),
                  (1260, 4441), (1261, 4526), (1262, 4599), (1263, 4809), (1264, 4818),
                  (1265, 4826), (1266, 4961), (1267, 5058), (1268, 5275), (1269, 5267),
                  (1270, 5298), (1271, 5507), (1272, 5678), (1273, 5534), (1274, 5730),
                  (1275, 5724), (1276, 5757), (1277, 6004), (1278, 5946), (1279, 6064),
                  (1280, 6230), (1281, 6293), (1282, 6314), (1283, 6464), (1284, 6698),
                  (1285, 6550), (1286, 6684), (1287, 6835), (1288, 6738), (1289, 6978),
                  (1290, 7030), (1291, 7171), (1292, 7152), (1293, 7258), (1294, 7274),
                  (1295, 7375), (1296, 7564), (1297, 7653), (1298, 7708), (1299, 7844),
                  (1300, 7736), (1301, 7603), (1302, 7844), (1303, 7952), (1304, 7963),
                  (1305, 7988), (1306, 8050), (1307, 8054), (1308, 8201), (1309, 8211),
                  (1310, 8203), (1311, 8356), (1312, 8439), (1313, 8300), (1314, 8246),
                  (1315, 8524), (1316, 8402), (1317, 8404), (1318, 8298), (1319, 8381),
                  (1320, 8369), (1321, 8389), (1322, 8714), (1323, 8491), (1324, 8361),
                  (1325, 8442), (1326, 8374), (1327, 8539), (1328, 8354), (1329, 8486),
                  (1330, 8435), (1331, 8342), (1332, 8464), (1333, 8271), (1334, 8089),
                  (1335, 8234), (1336, 8041), (1337, 8022), (1338, 8081), (1339, 7999),
                  (1340, 7990), (1341, 7965), (1342, 7815), (1343, 7897), (1344, 7843),
                  (1345, 7693), (1346, 7904), (1347, 7605), (1348, 7476), (1349, 7452),
                  (1350, 7331), (1351, 7076), (1352, 7105), (1353, 7067), (1354, 7141),
                  (1355, 7020), (1356, 6846), (1357, 6742), (1358, 6787), (1359, 6583),
                  (1360, 6509), (1361, 6551), (1362, 6340), (1363, 6123), (1364, 6049),
                  (1365, 6223), (1366, 6126), (1367, 5957), (1368, 5841), (1369, 5884),
                  (1370, 5735), (1371, 5564), (1372, 5603), (1373, 5411), (1374, 5306),
                  (1375, 5248), (1376, 5199), (1377, 5103), (1378, 4920), (1379, 4783),
                  (1380, 4752), (1381, 4616), (1382, 4601), (1383, 4481), (1384, 4442),
                  (1385, 4350), (1386, 4132), (1387, 3896), (1388, 4032), (1389, 3870),
                  (1390, 3836), (1391, 3781), (1392, 3654), (1393, 3526), (1394, 3545),
                  (1395, 3402), (1396, 3286), (1397, 3279), (1398, 3147), (1399, 3081),
                  (1400, 2904), (1401, 2872), (1402, 2789), (1403, 2767), (1404, 2661),
                  (1405, 2576), (1406, 2526), (1407, 2455), (1408, 2371), (1409, 2279),
                  (1410, 2243), (1411, 2175), (1412, 2111), (1413, 2046), (1414, 2072),
                  (1415, 1923), (1416, 1847), (1417, 1837), (1418, 1774), (1419, 1730),
                  (1420, 1692), (1421, 1573), (1422, 1546), (1423, 1546), (1424, 1490),
                  (1425, 1413), (1426, 1381), (1427, 1267), (1428, 1285), (1429, 1219),
                  (1430, 1072), (1431, 1149), (1432, 1097), (1433, 1038), (1434, 937), (1435, 991),
                  (1436, 968), (1437, 939), (1438, 893), (1439, 882), (1440, 833), (1441, 763),
                  (1442, 700), (1443, 724), (1444, 695), (1445, 674), (1446, 680), (1447, 628),
                  (1448, 656), (1449, 583), (1450, 574), (1451, 507), (1452, 486), (1453, 491),
                  (1454, 444), (1455, 488), (1456, 433), (1457, 396), (1458, 386), (1459, 400),
                  (1460, 391), (1461, 370), (1462, 317), (1463, 314), (1464, 338), (1465, 318),
                  (1466, 280), (1467, 277), (1468, 263), (1469, 262), (1470, 246), (1471, 228),
                  (1472, 227), (1473, 223), (1474, 218), (1475, 167), (1476, 177), (1477, 177),
                  (1478, 188), (1479, 154), (1480, 151), (1481, 155), (1482, 127), (1483, 131),
                  (1484, 150), (1485, 134), (1486, 109), (1487, 105), (1488, 114), (1489, 99),
                  (1490, 92), (1491, 94), (1492, 108), (1493, 98), (1494, 96), (1495, 85),
                  (1496, 65), (1497, 83), (1498, 71), (1499, 71), (1500, 72), (1501, 59),
                  (1502, 59), (1503, 63), (1504, 52), (1505, 57), (1506, 53), (1507, 52),
                  (1508, 45), (1509, 49), (1510, 46), (1511, 39), (1512, 54), (1513, 50),
                  (1514, 42), (1515, 39), (1516, 44), (1517, 41), (1518, 39), (1519, 41),
                  (1520, 46), (1521, 31), (1522, 24), (1523, 34), (1524, 35), (1525, 23),
                  (1526, 24), (1527, 21), (1528, 25), (1529, 27), (1530, 26), (1531, 21),
                  (1532, 27), (1533, 23), (1534, 38), (1535, 21), (1536, 20), (1537, 17),
                  (1538, 29), (1539, 28), (1540, 19), (1541, 27), (1542, 20), (1543, 12),
                  (1544, 20), (1545, 22), (1546, 24), (1547, 23), (1548, 22), (1549, 20),
                  (1550, 17), (1551, 19), (1552, 17), (1553, 18), (1554, 15), (1555, 14),
                  (1556, 17), (1557, 12), (1558, 25), (1559, 14), (1560, 20), (1561, 17),
                  (1562, 14), (1563, 12), (1564, 15), (1565, 9), (1566, 15), (1567, 21), (1568, 13),
                  (1569, 12), (1570, 14), (1571, 14), (1572, 9), (1573, 27), (1574, 13), (1575, 12),
                  (1576, 17), (1577, 11), (1578, 11), (1579, 20), (1580, 10), (1581, 12),
                  (1582, 12), (1583, 8), (1584, 6), (1585, 13), (1586, 14), (1587, 19), (1588, 12),
                  (1589, 13), (1590, 17), (1591, 12), (1592, 10), (1593, 12), (1594, 7), (1595, 11),
                  (1596, 8), (1597, 14), (1598, 11), (1599, 16), (1600, 11), (1601, 16), (1602, 15),
                  (1603, 13), (1604, 12), (1605, 20), (1606, 12), (1607, 12), (1608, 8), (1609, 13),
                  (1610, 12), (1611, 27), (1612, 12), (1613, 11), (1614, 18), (1615, 16),
                  (1616, 12), (1617, 14), (1618, 14), (1619, 11), (1620, 7), (1621, 17), (1622, 13),
                  (1623, 14), (1624, 12), (1625, 12), (1626, 10), (1627, 21), (1628, 10),
                  (1629, 10), (1630, 10), (1631, 13), (1632, 11), (1633, 12), (1634, 11),
                  (1635, 11), (1636, 19), (1637, 10), (1638, 8), (1639, 7), (1640, 18), (1641, 20),
                  (1642, 14), (1643, 22), (1644, 9), (1645, 11), (1646, 16), (1647, 20), (1648, 9),
                  (1649, 11), (1650, 12), (1651, 8), (1652, 16), (1653, 9), (1654, 8), (1655, 16),
                  (1656, 16), (1657, 13), (1658, 11), (1659, 13), (1660, 16), (1661, 10),
                  (1662, 10), (1663, 9), (1664, 10), (1665, 7), (1666, 14), (1667, 13), (1668, 9),
                  (1669, 10), (1670, 22), (1671, 11), (1672, 14), (1673, 9), (1674, 8), (1675, 13),
                  (1676, 12), (1677, 17), (1678, 9), (1679, 12), (1680, 10), (1681, 9), (1682, 21),
                  (1683, 17), (1684, 7), (1685, 15), (1686, 12), (1687, 9), (1688, 14), (1689, 14),
                  (1690, 15), (1691, 10), (1692, 11), (1693, 9), (1694, 13), (1695, 9), (1696, 13),
                  (1697, 15), (1698, 14), (1699, 8), (1700, 12), (1701, 13), (1702, 11), (1703, 17),
                  (1704, 14), (1705, 17), (1706, 18), (1707, 8), (1708, 16), (1709, 15), (1710, 15),
                  (1711, 13), (1712, 13), (1713, 7), (1714, 9), (1715, 14), (1716, 11), (1717, 16),
                  (1718, 8), (1719, 17), (1720, 8), (1721, 8), (1722, 9), (1723, 22), (1724, 16),
                  (1725, 9), (1726, 12), (1727, 13), (1728, 13), (1729, 21), (1730, 21), (1731, 16),
                  (1732, 15), (1733, 12), (1734, 17), (1735, 11), (1736, 15), (1737, 9), (1738, 14),
                  (1739, 8), (1740, 13), (1741, 15), (1742, 14), (1743, 9), (1744, 24), (1745, 14),
                  (1746, 14), (1747, 11), (1748, 9), (1749, 10), (1750, 14), (1751, 22), (1752, 20),
                  (1753, 17), (1754, 15), (1755, 16), (1756, 15), (1757, 10), (1758, 12),
                  (1759, 20), (1760, 9), (1761, 11), (1762, 11), (1763, 13), (1764, 15), (1765, 15),
                  (1766, 11), (1767, 14), (1768, 12), (1769, 12), (1770, 15), (1771, 17),
                  (1772, 13), (1773, 11), (1774, 13), (1775, 14), (1776, 21), (1777, 15), (1778, 6),
                  (1779, 12), (1780, 17), (1781, 18), (1782, 10), (1783, 14), (1784, 13),
                  (1785, 10), (1786, 12), (1787, 10), (1788, 17), (1789, 18), (1790, 19), (1791, 6),
                  (1792, 9), (1793, 20), (1794, 20), (1795, 18), (1796, 19), (1797, 13), (1798, 12),
                  (1799, 15), (1800, 13), (1801, 24), (1802, 19), (1803, 19), (1804, 22),
                  (1805, 15), (1806, 9), (1807, 14), (1808, 16), (1809, 12), (1810, 7), (1811, 13),
                  (1812, 4), (1813, 20), (1814, 8), (1815, 8), (1816, 13), (1817, 13), (1818, 9),
                  (1819, 9), (1820, 9), (1821, 11), (1822, 15), (1823, 9), (1824, 11), (1825, 10),
                  (1826, 11), (1827, 18), (1828, 12), (1829, 16), (1830, 8), (1831, 15), (1832, 23),
                  (1833, 11), (1834, 13), (1835, 19), (1836, 22), (1837, 17), (1838, 11),
                  (1839, 17), (1840, 18), (1841, 9), (1842, 15), (1843, 18), (1844, 17), (1845, 26),
                  (1846, 8), (1847, 16), (1848, 12), (1849, 16), (1850, 12), (1851, 9), (1852, 13),
                  (1853, 6), (1854, 15), (1855, 20), (1856, 16), (1857, 15), (1858, 11), (1859, 16),
                  (1860, 12), (1861, 11), (1862, 10), (1863, 11), (1864, 13), (1865, 16),
                  (1866, 11), (1867, 13), (1868, 13), (1869, 10), (1870, 8), (1871, 16), (1872, 17),
                  (1873, 12), (1874, 7), (1875, 11), (1876, 16), (1877, 13), (1878, 17), (1879, 9),
                  (1880, 13), (1881, 11), (1882, 17), (1883, 10), (1884, 16), (1885, 21), (1886, 8),
                  (1887, 17), (1888, 13), (1889, 19), (1890, 15), (1891, 18), (1892, 16),
                  (1893, 12), (1894, 18), (1895, 13), (1896, 11), (1897, 13), (1898, 13),
                  (1899, 15), (1900, 12), (1901, 13), (1902, 18), (1903, 15), (1904, 11),
                  (1905, 18), (1906, 11), (1907, 10), (1908, 11), (1909, 11), (1910, 9), (1911, 6),
                  (1912, 6), (1913, 9), (1914, 11), (1915, 12), (1916, 12), (1917, 13), (1918, 19),
                  (1919, 11), (1920, 9), (1921, 8), (1922, 8), (1923, 14), (1924, 13), (1925, 11),
                  (1926, 12), (1927, 10), (1928, 8), (1929, 13), (1930, 16), (1931, 10), (1932, 10),
                  (1933, 8), (1934, 10), (1935, 11), (1936, 12), (1937, 11), (1938, 14), (1939, 12),
                  (1940, 11), (1941, 12), (1942, 11), (1943, 8), (1944, 17), (1945, 8), (1946, 12),
                  (1947, 16), (1948, 10), (1949, 10), (1950, 17), (1951, 12), (1952, 5), (1953, 6),
                  (1954, 11), (1955, 11), (1956, 10), (1957, 11), (1958, 16), (1959, 13),
                  (1960, 10), (1961, 12), (1962, 6), (1963, 7), (1964, 8), (1965, 14), (1966, 13),
                  (1967, 12), (1968, 8), (1969, 7), (1970, 16), (1971, 8), (1972, 14), (1973, 14),
                  (1974, 11), (1975, 13), (1976, 16), (1977, 14), (1978, 17), (1979, 9), (1980, 14),
                  (1981, 10), (1982, 13), (1983, 12), (1984, 11), (1985, 10), (1986, 9), (1987, 14),
                  (1988, 15), (1989, 9), (1990, 7), (1991, 9), (1992, 12), (1993, 10), (1994, 4),
                  (1995, 10), (1996, 9), (1997, 19), (1998, 15), (1999, 10), (2000, 13)]
