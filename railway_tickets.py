# This program simulates booking train tickets. It has four classes: Train, Passenger, Ticket and Account.

# --------------------- PROJECT : RAILWAY TICKET BOOKING -----------------------

import random
from datetime import datetime


class Train():
    def __init__(self, train_num, source, destination, journey_datetime, seats_by_class):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.journey_datetime = journey_datetime
        # Dictionary storing available seats for each class: SL (S1), 3AC, 2AC, 1AC
        self.seats = seats_by_class
        # Waiting list counter for each class
        self.wl_count = {"SL": 0, "3AC": 0, "2AC": 0, "1AC": 0}

    def display_info(self):
        print(f"Train number: {self.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Journey Date & Time: {self.journey_datetime}")
        print(f"Available Seats -> SL (S1): {self.seats['SL']} | 3AC: {self.seats['3AC']} | 2AC: {self.seats['2AC']} | 1AC: {self.seats['1AC']}")
        print()

    def book_tickets(self, num_tickets, coach_class, passengers):
        booking_details = []
        coach_map = {"SL": "S1", "3AC": "B1", "2AC": "A1", "1AC": "H1"}
        coach_code = coach_map[coach_class]

        for passenger in passengers:
            pnr = random.randint(100000, 999999)
            
            # Check if confirmed seats are available in the selected class
            if self.seats[coach_class] > 0:
                seat_no = random.randint(1, 72)
                self.seats[coach_class] -= 1
                
                # Adjust berth if Middle (M) is chosen in 1AC or 2AC (since 1AC/2AC don't have middle berths)
                assigned_berth = passenger.berth_pref
                if coach_class in ["1AC", "2AC"] and assigned_berth == "M":
                    assigned_berth = random.choice(["L", "U"])
                
                status = f"CNF / {coach_code} / {seat_no} ({assigned_berth})"
            else:
                # Allocate Waiting List if seats are 0
                self.wl_count[coach_class] += 1
                status = f"WL{self.wl_count[coach_class]} ({coach_class})"

            booking_details.append((pnr, status))
        
        return booking_details


class Passenger:
    def __init__(self, name, age, gender, phone, berth_pref):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.berth_pref = berth_pref

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone Number: {self.phone}")
        print(f"Preferred Berth: {self.berth_pref}")


class Ticket:
    def __init__(self, train, source, destination, passengers, pnr, coach_class, status, booking_time):
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnr = pnr
        self.coach_class = coach_class
        self.status = status
        self.booking_time = booking_time

    def display_info(self):
        print(f"Train Number: {self.train.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Journey Date & Time: {self.train.journey_datetime}")
        print(f"Booked On: {self.booking_time}")
        print(f"Class: {self.coach_class}")
        print(f"PNR: {self.pnr}")
        print(f"Booking Status / Berth: {self.status}")
        for passenger in self.passengers:
            passenger.display_info()
        print()


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password


accounts = [
    Account("user1", "password1"),
    Account("user2", "password2")
]

logged_in_account = None

while True:
    print("\n1. Create an account\n2. Login\n")
    choice = input("Enter choice: ")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        accounts.append(Account(username, password))
        print("Account created successfully!")
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        for account in accounts:
            if account.username == username and account.check_password(password):
                logged_in_account = account
                break
        if logged_in_account is None:
            print("Invalid username or password.")
        else:
            print(f"\nLogged in as {logged_in_account.username}\n\n-----Available Train details-----\n")
            break
    else:
        print("Invalid choice.")

if logged_in_account is not None:
    trains = [
        Train("12737", "Tadepalligudem", "Secunderabad", "18-11-2026 20:15", {"SL": 40, "3AC": 15, "2AC": 8, "1AC": 2}),
        Train("12728", "Tadepalligudem", "Visakhapatnam", "19-11-2026 06:30", {"SL": 50, "3AC": 20, "2AC": 10, "1AC": 4}),
        # Train 22863 has 1 SL seat and 0 seats in other classes to test Waiting List (WL)
        Train("22863", "Vijayawada", "Bangalore", "20-11-2026 22:45", {"SL": 1, "3AC": 0, "2AC": 0, "1AC": 0}),
    ]

    # Display available trains
    for train in trains:
        train.display_info()

    # Get user input for booking
    while True:
        try:
            train_num = input("Enter Train Number: ")
            train = None
            for t in trains:
                if t.train_num == train_num:
                    train = t
                    break
            if train is None:
                raise ValueError("Invalid Train Number.")

            coach_class = input("Enter Coach Class (SL / 3AC / 2AC / 1AC): ").strip().upper()
            if coach_class == "S1":
                coach_class = "SL"
            if coach_class not in ["SL", "3AC", "2AC", "1AC"]:
                raise ValueError("Invalid Class. Choose from SL, 3AC, 2AC, or 1AC.")

            num_tickets = int(input("Enter Number of Tickets: "))
            if num_tickets <= 0:
                raise ValueError("Number of tickets should be greater than 0")

            # Inform user if booking goes into Waiting List
            if num_tickets > train.seats[coach_class]:
                print(f"Note: Only {train.seats[coach_class]} confirmed seat(s) left in {coach_class}. Remaining will be booked under Waiting List (WL).")

            break
        except ValueError as e:
            print(f"Invalid Input: {e}")

    passengers = []
    valid_berths = ["L", "M", "U", "SU", "SL"]

    for i in range(num_tickets):
        print(f"\nEnter details for Passenger {i + 1}:")
        while True:
            try:
                name = input("Name: ")
                if not name:
                    raise ValueError("Name cannot be empty")
                age = int(input("Age: "))
                if age <= 0 or age > 120:
                    raise ValueError("Invalid Age")
                gender = input("Gender: ")
                phone = input("Phone Number: ")
                if not phone or len(phone) != 10 or not phone.isdigit():
                    raise ValueError("Invalid Phone Number")
                berth_pref = input("Berth Preference (L / M / U / SU / SL): ").strip().upper()
                if berth_pref not in valid_berths:
                    raise ValueError("Invalid Berth. Choose L, M, U, SU, or SL.")

                passenger = Passenger(name, age, gender, phone, berth_pref)
                passengers.append(passenger)
                break
            except ValueError as e:
                print(f"Invalid Input: {e}")

    booking_results = train.book_tickets(num_tickets, coach_class, passengers)
    booking_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    print("\n--------------Booking Successful!------------\n\nYour Ticket Details: \n")

    for i in range(num_tickets):
        pnr, status = booking_results[i]
        ticket = Ticket(train, train.source, train.destination, [passengers[i]], pnr, coach_class, status, booking_time)
        ticket.display_info()
        print("\n--------Thank You------- \n-------Safe Journey------")