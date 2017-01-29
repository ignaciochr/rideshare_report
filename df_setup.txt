SELECT user_id_r
      ,MIN(request_time) AS first_request_time
      ,MIN(pickup_time) AS first_pickup_time
FROM
    (SELECT *
    FROM 
        (SELECT user_id AS user_id_r
              ,request_time
        FROM (SELECT user_id
              ,CASE event_name
                  WHEN 'login' THEN 'request'
                  WHEN 'send_message' THEN 'pickup'
                  ELSE NULL END AS event_type
              ,cast(occurred_at AS time) AS request_time
        FROM tutorial.yammer_events
        WHERE extract(month FROM occurred_at) = 7
        AND extract(day FROM occurred_at) = 18
        AND event_name = 'login'
        ) AS requests 
        ) AS request_table 
    LEFT JOIN 
        (SELECT user_id AS user_id_p
              ,pickup_time
        FROM (SELECT user_id
              ,CASE event_name
                  WHEN 'login' THEN 'request'
                  WHEN 'send_message' THEN 'pickup'
                  ELSE NULL END AS event_type
              ,cast(occurred_at AS time) AS pickup_time
        FROM tutorial.yammer_events
        WHERE extract(month FROM occurred_at) = 7
        AND extract(day FROM occurred_at) = 18
        AND event_name = 'send_message'
        ) AS pickups 
        ) AS pickup_table 
    ON pickup_table.user_id_p = request_table.user_id_r) AS df
WHERE user_id_p IS NOT NULL
AND pickup_time > request_time
GROUP BY df.user_id_r
ORDER BY df.user_id_r
