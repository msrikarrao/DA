from datetime import *
dt1 = "2025-7-30"
dt2 = "8-14-2025"
dt3 = "2025, 8, 19"
dt4 = "10 30 - 20, 4, and 2026"
dt5 = "Meet me on 8th of 1st month in 2027, at 11 hours, 35 minutes"
dt6 = "9/30/2018 @ 7 hours and 30 minutes 45 seconds"
print(datetime.strptime(dt1, "%Y-%m-%d"))
print(datetime.strptime(dt2, "%m-%d-%Y"))
print(datetime.strptime(dt3, "%Y, %m, %d"))
print(datetime.strptime(dt4, "%H %M - %d, %m, and %Y"))
print(datetime.strptime(dt5, "Meet me on %dth of %mst month in %Y, at %H hours, %M minutes"))
print(datetime.strptime(dt6, "%m/%d/%Y @ %H hours and %M minutes %S seconds"))