monthConversions = {
    #Key    #Value
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Nov": "November",
    "Dec": "December",
} #to access specific key or value

#print(monthConversions["Nov"]) #or
#print(monthConversion.get("Dec")) #or
print(monthConversions.get("Luv", "Not a valid key"))