



DECLARE @number INT = 4
DECLARE @isprime INT = 0
DECLARE @counter INT
DECLARE @result VARCHAR(MAX) = '2&3&'

WHILE (@number <= 1000)
BEGIN
    SET @counter = 2
    WHILE (@counter <= CAST(SQRT(@number) as INT))
    BEGIN
        IF (@number % @counter = 0)
        BEGIN
            SET @isprime = 0
            Break
        END
        ELSE
        BEGIN
            SET @isprime = 1
            SET @counter += 1
        END        
    END
    IF @isprime = 1
    SET @result += CAST(@number as VARCHAR(6)) + '&'
    SET @number += 1
END

PRINT(LEFT(@result, len(@result)-1))


