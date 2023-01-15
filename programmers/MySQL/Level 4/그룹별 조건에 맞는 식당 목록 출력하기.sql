SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_PROFILE AS MP INNER JOIN REST_REVIEW AS RR ON MP.MEMBER_ID = RR.MEMBER_ID
WHERE MP.MEMBER_ID = (SELECT MEMBER_ID
                     FROM REST_REVIEW
                     GROUP BY MEMBER_ID
                     ORDER BY COUNT(*) DESC LIMIT 1)
ORDER BY REVIEW_DATE, REVIEW_TEXT
