-- NAME: MUHAMMAD USAMA
-- DIFFICULTY LEVEL: EASY                                              
-- Max Score: 15

select round(sum(lat_n), 2) as lat, round(sum(long_w), 2) as lon from station;