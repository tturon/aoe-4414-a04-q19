# ecef_to_eci.py
#
# Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km
#  Text explaining script usage
# Parameters:
# year: year of interest, integer
# month: month of interest, integer
# day: day of interest, integer
# hour: hour of interest, integer
# minute: minute of interest, integer
# second: second of interest, float
# ecef_x_km
# ecef_y_km
# ecef_z_km

# Output:
#  Code that coverts ECEF coords to ECI coordinates in kilometers
#
# Written by Thomas Turon
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module

import sys
import math

w_speed = 7.292115*10**-5 #rad/s

#input variables
year = ''
month = ''
day = ''
hour = ''
minute = ''
second = ''
ecef_x_km = ''
ecef_y_km = ''
ecef_z_km = ''

if len(sys.argv) == 10:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
    ecef_x_km = float(sys.argv[7])
    ecef_y_km = float(sys.argv[8])
    ecef_z_km = float(sys.argv[9])

else:
    print(\
        'Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'
        )
    exit()

jd = day - 32075 + 1461*(year + 4800 - (14 - month)//12)//4 + 367*(month - 2 + (14 - month)//12*12)//12 - 3*((year + 4900 - (14 - month)//12)//100)//4
jdmidnight = jd - 0.5
dfrac = (second + 60*(minute + 60*hour))/86400
jd_frac = jdmidnight + dfrac

tu = (jd_frac - 2451545.0)/36525
gmst_sec = 67310.54841 + (876600*60*60 + 8640184.812866)*tu + 0.093104*tu**2 - 6.2*10**-6*tu**3
gmst_rad = (gmst_sec%86400)*w_speed

#ecef components
eci_x_km = ecef_x_km * math.cos(gmst_rad) + ecef_y_km * -math.sin(gmst_rad)
eci_y_km = ecef_x_km * math.sin(gmst_rad) + ecef_y_km * math.cos(gmst_rad)
eci_z_km = ecef_z_km

# print results
print(eci_x_km)
print(eci_y_km)
print(eci_z_km)