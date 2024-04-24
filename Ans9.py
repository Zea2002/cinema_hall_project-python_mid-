class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()

        Star_Cinema.entry_hall(self)

    def _initialize_seats(self):
        for row in range(1, self._rows + 1):
            self._seats[row] = ['O' for _ in range(self._cols)]

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)

    def book_seats(self, show_id, seats_to_book):
        for row, col in seats_to_book:
            if row not in self._seats or col not in range(1, self._cols + 1):
                raise ValueError("Invalid seat")

            if self._seats[row][col - 1] == 'X':
                raise ValueError("Seat already booked")

            self._seats[row][col - 1] = 'X'

    def view_show_list(self):
        print("Shows running today:")
        for show in self._show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        print("Available seats for the show:")
        for row, seats in self._seats.items():
            for col, status in enumerate(seats, start=1):
                if status == 'O':
                    print(f"Row {row}, Col {col}")

hall1 = Hall(5, 5, 1)
hall1.entry_show("101", "The Avengers", "10:00 AM")
hall1.entry_show("102", "Avatar", "2:00 PM")

while True:
    print("\nOptions:")
    print("1. View all shows today")
    print("2. View available seats in a show")
    print("3. Book tickets")
    print("4. Exit")
   
    choice = input("Enter your choice: ")

    if choice == '1':
        hall1.view_show_list()
    elif choice == '2':
        show_id = input("Enter the ID of the show: ")
        hall1.view_available_seats(show_id)
    elif choice == '3':
        show_id = input("Enter the ID of the show: ")
        try:
            num_seats = int(input("Enter the number of seats to book: "))
            seats_to_book = []
            for _ in range(num_seats):
                seat = input("Enter seat to book (format: row,col): ").split(',')
                row, col = map(int, seat)
                seats_to_book.append((row, col))
            hall1.book_seats(show_id, seats_to_book)
            print("Booking successful!")
        except ValueError:
            print("Invalid number of seats. Please enter a valid number.")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
