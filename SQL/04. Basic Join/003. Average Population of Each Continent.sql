-- NAME: MUHAMMAD USAMA
-- DIFFICULTY LEVEL: EASY                                              
-- Max Score: 10

-- We use group by clause because it was given in the question that query the
-- continent names with respect to average city population.
-- We use floor because it was given in the question that avg city population
-- rounded down to the nearest integer.

select country.continent, floor(avg(city.population)) from country, city where
country.code = city.countrycode group by country.continent;