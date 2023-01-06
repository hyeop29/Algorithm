SELECT TABLE2.FOOD_TYPE, TABLE2.REST_ID, TABLE2.REST_NAME, TABLE2.FAVORITES
FROM (SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
      FROM REST_INFO
      GROUP BY FOOD_TYPE
      ) AS TABLE1
INNER JOIN REST_INFO AS TABLE2 
ON  TABLE1.FOOD_TYPE = TABLE2.FOOD_TYPE AND TABLE1.FAVORITES = TABLE2.FAVORITES
ORDER BY FOOD_TYPE DESC
