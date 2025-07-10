INSERT INTO Integrated_Arrival
SELECT
    a.FlightNumber,
    a.ArrivalAirport,
    a.ScheduledArrivalDate,
    a.ScheduledArrivalTime,
    a.ActualArrivalTime,
    a.DepartureAirport,
    a.ScheduledDepartureDate,
    a.ScheduledDepartureTime,
    a.ActualDepartureTime
FROM Airline2_Flight as a
JOIN Airport3_Arrivals
