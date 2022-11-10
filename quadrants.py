
readings = [
{
        'SSID':'amzn1',
        'RSSI': -21,  
},
{
        'SSID':'amzn2',
        'RSSI': -24, 
},
{
        'SSID':'amzn3',  
        'RSSI': -25, 
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
        'zone': 'null'
    },
    {
        'SSID':'amzn2',
        'row': 2, 
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



rows_cols = []

def determine_row():
    for database_value in database_values:
        # Match the strongest RSSI with the database value and check to see if it's associated row is 2
        # If if is, print the zone associated with that router
        if strongest == database_value['SSID'] and database_value['row'] == 2:
            zone = database_value['zone']
            print(f'You are in zone {zone} ')
            return zone
        # If the strongest value is in the second row, call the function to determine what column this value is in
        if strongest == database_value['SSID'] and database_value['row'] == 1:
            determine_column()


def determine_column():
        for database_value in database_values:
            if second_strongest == database_value['SSID']:
                column = database_value['column']
                # print(f'The second strongest value is in row 2 and is in column {column}')
                if column == 1:
                    print('You are in zone 1')
                    rows_cols.append((1,column))
                    return (1,column)
                if column == 2:
                    print('You are in zone 2')
                    rows_cols.append((1,column))








 




















        









