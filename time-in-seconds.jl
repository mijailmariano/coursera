using Dates, Dates.TimeZones

# Prompt the user to enter their local date and hour
println("Enter your local date (YYYY-MM-DD):")
date_str = chomp(readline())

println("Enter your local hour (HH):")
hour_str = chomp(readline())

# Parse the user's input into a DateTime object
local_datetime = DateTime(date_str * "T" * hour_str * ":00:00", tz=TimeZone("local"))

# Calculate the total elapsed time in seconds since the start of the year
elapsed_seconds = floor(timeofday(local_datetime).value)

# Print the result
println("Total elapsed time in seconds since the start of the year: $elapsed_seconds")