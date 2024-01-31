select name AS results  from (
    select name,u1.user_id,count(rating) as greatestmovies from MovieRating l1
join Users u1 on l1.user_id=u1.user_id
group by user_id      
order by greatestmovies desc, name ASC limit 1
) t1

union ALL
select tmp.title AS results  from
(
    SELECT m1.movie_id, m2.title, AVG(m1.rating) AS avg_rating 
FROM MovieRating m1
JOIN Movies m2 ON m1.movie_id = m2.movie_id 
WHERE m1.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY m1.movie_id, m2.title
ORDER BY avg_rating DESC,M2.title ASC
LIMIT 1
)tmp 

