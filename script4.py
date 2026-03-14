import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='your user',
    password='your password',
    autocommit=True )

def get_airport_by_icao(icao_code):

    sql = f"SELECT name, iso_country FROM airport WHERE ident='{icao_code}'"
    print(sql)

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport: {row[0]}")
            print(f"Location: {row[1]}")
    else:
        print(f"No airport found with ICAO code: {icao_code}")




icao_code = input("Enter ICAO code: ")
get_airport_by_icao(icao_code)

connection.close()



def get_airports_by_country(area_code):

    sql = f"""
    SELECT type, COUNT(*) as count 
    FROM airport 
    WHERE iso_country='{area_code}' 
    GROUP BY type 
    ORDER BY type
    """
    print(sql)

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        print(f"\nAirports in {area_code}:")
        for row in result:
            print(f"{row[0]}: {row[1]} airports")
    else:
        print(f"No airports found for country code: {area_code}")




area_code = input("Enter area code (e.g., FI): ")
get_airports_by_country(area_code)

connection.close()


from geopy.distance import geodesic


def get_airport_coordinates(icao_code):

    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao_code}'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    if result:
        return (result[0], result[1])
    else:
        return None


def calculate_distance_between_airports(icao_code1, icao_code2):

    coords1 = get_airport_coordinates(icao_code1)
    coords2 = get_airport_coordinates(icao_code2)

    if coords1 is None:
        print(f"Airport with ICAO code {icao_code1} not found")
        return

    if coords2 is None:
        print(f"Airport with ICAO code {icao_code2} not found")
        return


    distance_km = geodesic(coords1, coords2).kilometers

    print(f"Distance between {icao_code1} and {icao_code2}: {distance_km:.2f} km")




icao_code1 = input("Enter first airport ICAO code: ")
icao_code2 = input("Enter second airport ICAO code: ")
calculate_distance_between_airports(icao_code1, icao_code2)

connection.close()
