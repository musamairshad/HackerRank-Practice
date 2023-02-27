-- NAME: MUHAMMAD USAMA
-- DIFFICULTY LEVEL: EASY                                              
-- Max Score: 10

select sum(city.population) from city, country where country.continent = 'Asia'
and city.countrycode = country.code;