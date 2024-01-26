import mysql.connector
import random

cnx = mysql.connector.connect(
    host='localhost',
    user='andy',
    password='Andydy212003*',
    database='churchdoc'
)
cursor = cnx.cursor()

def check_credentials():
    # Get username and password from user input
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")

    try:
        query = "SELECT Username, Password FROM admin WHERE Username = %s"
        cursor.execute(query, (Username,))
        user = cursor.fetchone()

        if user:
            login, stored_password = user
            if stored_password == Password:
                print("Success")
                HomePage()
                
            else:
                print('Incorrect password')
        else:
            print('Username not found')

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()

def request():
    def generate_random_numbers(length):
        random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(length))
        return random_numbers

    # Generate RequestCode
    TransactionCode = generate_random_numbers(10)
    print("Transaction Code:", TransactionCode)

    # Take user input for values
    Name = input("Enter Name: ")
    Birthdate = input("Enter Birthdate: ")
    RequestedMaterials = input("Enter Requested Materials: ")

    try:
        # Insert RequestCode into one table
        query_request_code = "INSERT INTO status (RequestStatus, RequestCode) VALUES (%s, %s)"
        cursor.execute(query_request_code, ("Processing", TransactionCode,))
        cnx.commit()

        # Get the auto-generated primary key (PK) of the inserted row
        request_code_pk = cursor.lastrowid

        # Insert other values along with the reference to RequestCode PK into another table
        query_data = "INSERT INTO request (RequestCode, Name, Birthdate, RequestedMaterials, Status) VALUES (%s, %s, %s, %s, %s)"
        values_data = (TransactionCode, Name, Birthdate, RequestedMaterials, "Processing")
        cursor.execute(query_data, values_data)
        cnx.commit()

        print("Values inserted successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()

def schedule():
    def generate_random_numbers(length):
        random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(length))
        return random_numbers

    # Generate RequestCode
    ScheduleCode = generate_random_numbers(10)
    print("Transaction Code:", ScheduleCode)

    # Take user input for values
    # Pa-radio button nito ha
    Name = input("Enter Name: ")
    AppointmentDate = input("Enter Date: ")
    Appointment = input("Enter Requested Materials: ")

    try:
        # Insert RequestCode into one table
        query_request_code = "INSERT INTO status (RequestCode, RequestStatus) VALUES (%s, %s)"
        cursor.execute(query_request_code, (ScheduleCode, "For Approval"))
        cnx.commit()
        
        # Get the auto-generated primary key (PK) of the inserted row
        request_code_pk = cursor.lastrowid
        
        # Insert other values along with the reference to RequestCode PK into another table
        query_data = "INSERT INTO scheduledappointment (RequestCode, Name, Date, Appointment, Status) VALUES (%s, %s, %s, %s, %s)"
        values_data = (ScheduleCode, Name, AppointmentDate, Appointment, "For Approval")
        cursor.execute(query_data, values_data)
        cnx.commit()

        print("Values inserted successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()
        

#Log in 
def login():
        print("Log in as Admin - 1")
        print("Log in as User - 2")
        login = input("Select: ")
        print("\n")

        try:
            login = int(login)  # Convert input to integer
            if login == 1:
                check_credentials()
            elif login == 2:
                HomePage()
            else:
                print("Invalid selection!")
        except ValueError:
            print("Invalid input! Please enter a number.")



# HomePage
def HomePage():
    print("\n")
    print("How can we help you today?")
    print("1 - Request Materials")
    print("2 - Schedule an Appointment")
    Prompt = input("Select: ")
    print("\n")
    try:
        Prompt = int(Prompt)  # Convert input to integer
        if Prompt == 1:
            request()
        elif Prompt == 2:
            schedule()
        else:
            print("Invalid selection!")
    except ValueError:
        print("Invalid input! Please enter a number.")

login()



