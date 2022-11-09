
readings = [
{
        'SSID':'amzn2',
        'RSSI': -24, 
},
{
        'SSID':'amzn3',  
        'RSSI': -25, 
},
{
        'SSID':'amzn1',
        'RSSI': -32,  
},
]

database_values = [
    {
        'SSID':'amzn3',
        'row': 2, 
        'column': 1,
        'zone' : 3
    },
    {
        'SSID':'amzn1',
        'row': 1,
        'column': 'null',
    },
    {
        'SSID':'amzn2',
        'row': 1, 
        'column': 2,
        'zone' : 4
    }
]


# Take the SSID from the first dictionary in the payload so I can determine the associated row

top_three_SSID = []
for reading in readings:
    top_three_SSID.append(reading['SSID'])


strongest = top_three_SSID[0]
second_strongest = top_three_SSID[1]
print(second_strongest)

def determine_row():
    for database_value in database_values:
        # Match the strongest RSSI with the database value and check to see if it's associated row is 2
        # If if is, print the zone associated with that router
        if strongest == database_value['SSID'] and database_value['row'] == 2:
            zone = database_value['zone']
            print(f'You are in zone {zone} ')
        elif strongest == database_value['SSID'] and database_value['row'] == 1:
            # If the strongest value is not in row 2, then it is in row 1
            # Now I need to figure out how to use the second strongest reading to differentiate the columns
            # and then use the column to determine the final zone
            print('the strongest value is in row 1')
            determine_column()


determine_row()

def determine_column():
    for database_value in database_values: 
        if second_strongest == database_value['SSID'] and database_value['column'] == 1:
            
            print(f'')


 




















        









