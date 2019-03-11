from src.objects.checkpoint import CheckPoint
from src.objects.wall import Wall

walls = [Wall(46, 24, 423, 18), # Outer walls 
Wall(423, 18, 435, 552),
Wall(435, 552, 48, 556),
Wall(48, 556, 46, 24),
Wall(104, 78, 366, 76), # Inner walls
Wall(104 , 78, 104, 490),
Wall(173, 555, 169, 142),
Wall(240, 78, 240, 490),
Wall(316, 555, 316, 142),
Wall(366, 78, 370, 490)]

[x * 3 for x in walls]

checkpoints = [CheckPoint(103, 24, 104, 78),
CheckPoint(237, 22, 239, 77),
CheckPoint(363, 20, 364, 75),
CheckPoint(367, 76, 424, 76),
CheckPoint(427, 174, 368, 174),
CheckPoint(429, 300, 370, 300),
CheckPoint(433, 489, 372, 489),
CheckPoint(371, 490, 372, 552),
CheckPoint(370, 485, 316, 485),
CheckPoint(367, 281, 313, 281),
CheckPoint(366, 139, 311, 139),
CheckPoint(308, 77, 308, 138),
CheckPoint(308, 140, 242, 140),
CheckPoint(311, 311, 245, 311),
CheckPoint(314, 485, 248, 485),
CheckPoint(247, 489, 247, 553),
CheckPoint(245, 487, 174, 487),
CheckPoint(242, 278, 172, 278),
CheckPoint(240, 142, 171, 142),
CheckPoint(168, 80, 168, 141),
CheckPoint(167, 142, 106, 142),
CheckPoint(170, 307, 106, 307),
CheckPoint(171, 492, 108, 492),
CheckPoint(106, 494, 106, 554),
CheckPoint(104, 491, 50, 491),
CheckPoint(104, 235, 48, 235),
CheckPoint(104, 111, 48, 111)]

[x * 3 for x in checkpoints]