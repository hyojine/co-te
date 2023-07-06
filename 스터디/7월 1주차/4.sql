# delete from person 
# where id not in (select pp.id 
#                  from (select email, min(id) as id
#                        from person 
#                        group by email
#                        having count(*)>1) p, person pp
#                  where p.email=pp.email and p.id=pp.id)

# DELETE FROM person
# WHERE id IN (SELECT id
#              FROM ( 
#                  SELECT id, ROW_NUMBER() OVER (PARTITION BY email) as row_num
#                  FROM person
#                  ) tmp
#              WHERE row_num > 1);

DELETE FROM Person WHERE Id NOT IN 
(SELECT * FROM( SELECT MIN(Id) FROM Person GROUP BY Email) as p);
