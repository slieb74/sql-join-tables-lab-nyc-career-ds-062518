INSERT INTO powers (type, damage_points) VALUES
("works hard", 5),
("superstrength", 20),
("flight", 10),
("summons lightning", 10),
("ultra smart", 20),
("unlimited financing", 5),
("breaths underwater", 5),
("enhanced speed", 10),
("enhanced agility", 10),
("expert martial artist", 15),
("rage", 10),
("technorganic physiology", 10),
("enhanced flexibility", 10),
("magic ring", 1),
("advanced weaponry", 10),
("breaths in outer space", 10),
("x-ray vision", 10);


<!-- powers -->
id          type        damage_points
----------  ----------  -------------
1           works hard  5            
2           superstren  20           
3           flight      10           
4           summons li  10           
5           ultra smar  20           
6           unlimited   5            
7           breaths un  5            
8           enhanced s  10           
9           enhanced a  10           
10          expert mar  15           
11          rage        10           
12          technorgan  10           
13          enhanced f  10           
14          magic ring  1            
15          advanced w  10           
16          breaths in  10           
17          x-ray visi  10        

<!-- heroes -->
id          name        real_identity  weakness      squad_id  
----------  ----------  -------------  ------------  ----------
1           Batman      Bruce Wayne    mortal human  2         
2           Superman    Clark Kent     kryptonite    2         
3           Thor        Thor Odinson   ego           1         
4           Iron Man    Tony Stark     mortal human  1         
5           Wonder Wom  Diana Prince   broken brace  2         
6           Captain Am  Steve Rogers   mortal human  1         
7           Aquaman     Arthur Curry   needs water   2         
8           Black Pant  T'Challa       mortal human  1         
9           Black Wido  Natasha Roman  mortal human  1         
10          Hulk        Bruce Banner   rage          1         
11          Cyborg      Victor Stone   hackers       2         
12          Megaman                    hackers                 
13          StretcherF  Jean-Claude V  mortal human            
14          Goku        Kakarot        myopia                  
15          Green Lant  Alan Scott     the color ye  2     

INSERT INTO hero_powers (hero_id, power_id) VALUES
(1, 1),
(1, 6),
(1, 10),
(1, 15),
(2, 2),
(2, 3),
(2, 8),
(2, 9),
(2, 13),
(2, 16),
(2, 17),
(3, 4),
(3, 2),
(3, 16),
(4, 1),
(4, 5),
(4, 6),
(4, 15),
(5, 2),
(5, 8),
(5, 9),
(5, 15),
(6, 1),
(6, 2),
(6, 8),
(6, 9),
(6, 15),
(7, 7),
(8, 8),
(8, 9),
(8, 13),
(8, 15),
(9, 5),
(9, 10),
(9, 13),
(9, 9),
(10, 2),
(10, 11),
(11, 2),
(11, 15),
(11, 12),
(12, 7),
(12, 12),
(12, 17),
(13, 13),
(14, 1),
(14, 2),
(14, 3),
(14, 8),
(14, 9),
(14, 10),
(14, 16),
(15, 14);


name        total_damage
----------  ------------
Goku        80          
Superman    80          
Black Wido  55          
Captain Am  55          
Wonder Wom  50          
Black Pant  40          
Cyborg      40          
Iron Man    40          
Thor        40          
Batman      35          
Hulk        30          
Megaman     25          
StretcherF  10          
Aquaman     5           
Green Lant  1           
