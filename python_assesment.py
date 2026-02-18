import random

class HotelReservation:
    def __init__(self):
        self.booking = None   # Stores active booking

    # Validate Contact Number
    def validate_contact(self, contact):
        return contact.isdigit() and len(contact) == 10

    # Generate Unique Booking ID
    def generate_booking_id(self):
        return "BK" + str(random.randint(1000, 9999))

    # Book Room
    def book_room(self):
        if self.booking is not None:
            print("⚠ You already have an active booking!")
            return

        name = input("Enter your name: ")
        contact = input("Enter your 10-digit contact number: ")

        if not self.validate_contact(contact):
            print(" Invalid contact number! Must be 10 digits.")
            return

        nights = int(input("Enter number of nights: "))

        print("\nRoom Types:")
        print("1. Standard - ₹2000/night")
        print("2. Deluxe   - ₹3500/night")
        print("3. Suite    - ₹5000/night")

        choice = int(input("Select room type (1/2/3): "))

        room_prices = {1: 2000, 2: 3500, 3: 5000}
        room_names = {1: "Standard", 2: "Deluxe", 3: "Suite"}

        if choice not in room_prices:
            print(" Invalid room selection!")
            return

        total_cost = room_prices[choice] * nights
        print(f"\nTotal Cost = ₹{total_cost}")

        confirm = input("Confirm booking? (yes/no): ")

        if confirm.lower() == "yes":
            booking_id = self.generate_booking_id()
            self.booking = {
                "Booking ID": booking_id,
                "Name": name,
                "Contact": contact,
                "Room Type": room_names[choice],
                "Nights": nights,
                "Total Cost": total_cost
            }
            print("Payment Successful!")
            print(f" Booking Confirmed! Your Booking ID: {booking_id}")
        else:
            print(" Booking Cancelled.")

    # View Booking
    def view_booking(self):
        if self.booking is None:
            print("No active booking found.")
        else:
            print("\n Booking Details:")
            for key, value in self.booking.items():
                print(f"{key}: {value}")

    # Cancel Booking
    def cancel_booking(self):
        if self.booking is None:
            print("No active booking to cancel.")
        else:
            confirm = input("Are you sure you want to cancel booking? (yes/no): ")
            if confirm.lower() == "yes":
                self.booking = None
                print(" Booking Cancelled Successfully.")
            else:
                print("Cancellation aborted.")

    # Menu
    def menu(self):
        while True:
            print("\n====== HOTEL RESERVATION MENU ======")
            print("1. Book Room")
            print("2. View Booking")
            print("3. Cancel Booking")
            print("4. Exit")

            choice_str = input("Enter choice: ").strip()

            try:
                choice = int(choice_str)
            except ValueError:
                print("Invalid choice! Please enter a number (1-4).")
                continue

            if choice == 1:
                self.book_room()
            elif choice == 2:
                self.view_booking()
            elif choice == 3:
                self.cancel_booking()
            elif choice == 4:
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice. Try again.")

reservation_system = HotelReservation()
reservation_system.menu()



