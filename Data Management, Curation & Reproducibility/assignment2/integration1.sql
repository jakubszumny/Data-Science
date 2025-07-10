INSERT INTO Integrated_Arrival
SELECT
    a.Airline,
    a.FlightNumber,
    a.ScheduledArrivalDate,
    a.ActualArrivalDate,
    a.ScheduledArrivalTime,
    a.ActualArrivalTime,
    a.GateTime,
    a.LandingTime,
    a.ArrivalGate
FROM Airline1 as a
JOIN Airport3_Arrivals AND Airport3_Departures 
AND Airline1_Schedule AND Airline1_Flights