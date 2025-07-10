SELECT 'A3' as a.Airline,
        a.FlightNumber,
FROM Airport3_Arrivals as a
WHERE a.Scheduled != a.Actual