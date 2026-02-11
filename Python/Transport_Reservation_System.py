class TransportReservation:
    def __init__(self):
        self.routes = {"Mumbai to Pune": 500,
                       "delhi to jaipur": 600
                       }
        self.ticket = {}

        self.seats = {routes:0 for routes in self.routes}

        self.next_ticket_id = 10001     # auto-generated ticket Id
        self.max_seats = 40

# ____________________SHOW ROUTES ______________________
    def show_routes(self):
        print("\n Available routes:")
        for route, price in self.routes.items():
            available = self.max_seats - self.seats[route]
            print(f"{route}: - {price} | Seats Available: {available}")

# ____________________BOOK TICKET ________________________
    def book_ticket(self):
        name = input("Enter ticket name: ")

        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Age must be a number.")
            return

        mobile = input("Enter mobile number: ")
        if not(mobile.isdigit() and len(mobile) == 10):
            print("mobile number must be 10 digits.")
            return

        self.show_routes()
        route = input("Enter route exactly as shown:")

        if route not in self.routes:
            print("Invalid route selection")
            return

        if self.seats[route] >= self.max_seats:
            print("Transport is full for this route")
            return

        # Assign seat number
        seat_number = self.seats[route] + 1
        self.seats[route] += 1

        # Generate ticket ID
        ticket_id = self.next_ticket_id
        self.next_ticket_id += 1

        # Store ticket details
        self.ticket[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "seats": seat_number,
            "price": self.routes[route],
            "route": route
        }

        print("\n Ticket Booked Successfully")
        print(f"Ticket ID: {ticket_id}")
        print(f"seat No  : {seat_number}")
        print(f"Fare     : {self.routes[route]}")

#__________________VIEW TICKET _________________________
    def view_ticket(self):
        try:
            ticket_id = int(input("Enter ticket ID: "))
        except ValueError:
            print("Invalid ticket ID")
            return

        if ticket_id not in self.ticket:
            print("Ticket nit found")
            return

        ticket = self.ticket[ticket_id]
        print("\n Ticket Details:")
        print(f"Ticket ID: {ticket_id}")
        print(f"Name: {ticket['name']}")
        print(f"Age: {ticket['age']}")
        print(f"Mobile: {ticket['mobile']}")
        print(f"Seats: {ticket['seats']}")
        print(f"Price: {ticket['price']}")
        print(f"Route: {ticket['route']}")
        print(f"Fare: {ticket['price']}")

#_________________ CANCEL TICKET ___________________
    def cancel_ticket(self):
        try:
            ticket_id = int(input("Enter ticket ID to cancel: "))
        except ValueError:
            print("Invalid ticket ID")
            return

        if ticket_id not in self.ticket:
            print("Ticket not found")
            return

        route = self.ticket[ticket_id]["route"]
        self.seats[route] -= 1
        del self.ticket[ticket_id]

        print("\n Ticket Cancelled Successfully")

# ____________________ MAIN PROGRAM ________________
bus= TransportReservation()

while True:
        print("\n Transport Reservation System:")
        print("1. show Available Routes")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bus.show_routes()
        elif choice == "2":
            bus.book_ticket()
        elif choice == "3":
            bus.view_ticket()
        elif choice == "4":
            bus.cancel_ticket()

