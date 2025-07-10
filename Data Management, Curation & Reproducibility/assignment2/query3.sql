SELECT 'A3' as a.Airline,
        a.FlightNumber,
        s.ArrivalAirport,
        a.ArrivalGate
FROM Airline1_Schedule as s, Airport3_Arrivals as a
WHERE s.FlightNumber = a.FlightNumber