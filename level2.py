from src.objects.checkpoint import CheckPoint
from src.objects.wall import Wall

checkpoints = []



walls = [Wall(7, 10, 232, 10),#outside walls start
Wall(232, 10, 327, 78),
Wall(327, 78, 392, 8),
Wall(392, 8, 613, 90),
Wall(613, 90, 639, 255),
Wall(639, 255, 565, 395),
Wall(565, 395, 644, 527),
Wall(644, 527, 581, 594),
Wall(581, 594, 332, 575),
Wall(332, 575, 218, 534),
Wall(218, 534, 352, 347),
Wall(352, 347, 350, 248),
Wall(350, 248, 410, 192),
Wall(410, 192, 283, 182),
Wall(283, 182, 265, 314),
Wall(265, 314, 282, 445),
Wall(218, 534, 175, 595),
Wall(175, 595, 9, 595),
Wall(9, 595, 7, 106),
Wall(7, 106, 7, 10), #outside walls end
Wall(50, 44, 231, 44), #inside walls start
Wall(231, 44, 306, 107),
Wall(306, 107, 509, 113),
Wall(509, 113, 571, 154),
Wall(571, 154, 580, 248),
Wall(580, 248, 504, 366),
Wall(504, 366, 543, 517),
Wall(543, 517, 343, 517),
Wall(343, 517, 426, 400),
Wall(426, 400, 434, 278),
Wall(434, 278, 491, 233),
Wall(491, 233, 509, 113),
Wall(254, 63, 153, 265),
Wall(153, 265, 184, 389),
Wall(184, 389, 114, 528),
Wall(114, 528, 128, 211),
Wall(128, 211, 50, 108),
Wall(50, 108, 50, 44), #inside walls end
Wall(381, 71, 417, 60), #obstacles start
Wall(417, 60, 410, 106),
Wall(410, 106, 390, 89),
Wall(390, 89, 381, 71),
Wall(460, 56, 485, 60),
Wall(485, 60, 495, 73),
Wall(495, 73, 475, 80),
Wall(475, 80, 460, 56),
Wall(45, 494, 23, 463),
Wall(23, 463, 56, 438),
Wall(56, 438, 61, 477),
Wall(61, 477, 45, 494),
Wall(23, 363, 55, 372),
Wall(55, 372, 50, 405),
Wall(50, 405, 22, 394),
Wall(22, 394, 23, 363),
Wall(74, 253, 98, 275),
Wall(98, 275, 80, 312),
Wall(80, 312, 62, 283),
Wall(62, 283, 74, 253)]

[x * 3 for x in walls]

checkpoints = [CheckPoint(52, 9, 52, 45),
CheckPoint(234, 9, 234, 48),
CheckPoint(328, 78, 304, 107),
CheckPoint(422, 17, 410, 111),
CheckPoint(498, 42, 493, 114),
CheckPoint(614, 90, 570, 154),
CheckPoint(576, 246, 639, 259),
CheckPoint(502, 365, 566, 395),
CheckPoint(541, 516, 612, 562),
CheckPoint(309, 565, 343, 516),
CheckPoint(428, 400, 350, 346),
CheckPoint(407, 194, 492, 228),
CheckPoint(304, 107, 283, 182),
CheckPoint(283, 182, 205, 155),
CheckPoint(150, 265, 266, 315),
CheckPoint(182, 388, 281, 445),
CheckPoint(114, 526, 112, 594),
CheckPoint(119, 445, 9, 436),
CheckPoint(121, 371, 8, 361),
CheckPoint(126, 250, 7, 250),
CheckPoint(7, 107, 51, 107)]

[x * 3 for x in checkpoints]