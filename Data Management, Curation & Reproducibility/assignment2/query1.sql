SELECT 'A1' as s.FlightNumber,
        s.ArrivalAirport,
        f.ArrivalGate
FROM Airline1_Schedule as s, Airline1_Flight as f
WHERE s.FlightId = f.FlightId