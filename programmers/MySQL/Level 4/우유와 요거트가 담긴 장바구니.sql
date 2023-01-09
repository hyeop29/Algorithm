SELECT CP1.CART_ID
FROM
    (SELECT CART_ID, COUNT(CART_ID) AS AMOUNT
    FROM CART_PRODUCTS
    WHERE NAME = "Yogurt"
    GROUP BY CART_ID, NAME)
    AS CP1
    INNER JOIN
    (SELECT CART_ID, COUNT(CART_ID) AS AMOUNT
    FROM CART_PRODUCTS
    WHERE NAME = "Milk"
    GROUP BY CART_ID, NAME)
    AS CP2
    ON CP1.CART_ID = CP2.CART_ID
ORDER BY CART_ID
