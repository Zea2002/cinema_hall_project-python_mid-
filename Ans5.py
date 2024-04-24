class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.initialize_seats()

        Star_Cinema.entry_hall(self)

    def initialize_seats(self):
        for row in range(1, self.rows + 1):
            self.seats[row] = ['O' for _ in range(self.cols)]

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

    def book_seats(self, show_id, seats_to_book):
        for row, col in seats_to_book:
            if row not in self.seats or col not in range(1, self.cols + 1):
                raise ValueError("Invalid seat")

            if self.seats[row][col - 1] == 'X':
                raise ValueError("Seat already booked")

            self.seats[row][col - 1] = 'X'

    def view_show_list(self):
        print("Shows running today:")
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")