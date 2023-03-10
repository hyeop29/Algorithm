SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER, COUNT(DISTINCT OS.USER_ID) AS USERS
FROM USER_INFO AS UI INNER JOIN ONLINE_SALE AS OS ON UI.GENDER IS NOT NULL AND UI.USER_ID = OS.USER_ID
GROUP BY DATE_FORMAT(SALES_DATE,"%Y-%m"),GENDER
ORDER BY YEAR, MONTH, GENDER
