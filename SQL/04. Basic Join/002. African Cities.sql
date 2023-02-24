-- NAME: MUHAMMAD USAMA
-- DIFFICULTY LEVEL: EASY                                              
-- Max Score: 10

select city.name from city, country where country.continent = 'Africa' and 
city.countrycode = country.code;