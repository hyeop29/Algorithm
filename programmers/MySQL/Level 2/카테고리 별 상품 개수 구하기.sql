SELECT LEFT(PRODUCT_CODE, 2) AS "CATEGORY", COUNT("CATEGORY") AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY
