-- NAME: MUHAMMAD USAMA

select customers.customer_id, customers.name, 
concat('+', country_codes.country_code, customers.phone_number) from customers, country_codes
where customers.country = country_codes.country order by customers.customer_id;