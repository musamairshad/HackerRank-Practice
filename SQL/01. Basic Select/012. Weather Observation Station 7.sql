-- NAME: MUHAMMAD USAMA
-- DIFFICULTY LEVEL: EASY                                              
-- Max Score: 10

select distinct city from station 
where  city  like '%a' or  
       city  like '%e' or 
       city  like '%i' or 
       city  like '%o' or 
       city  like '%u';