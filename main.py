class InvalidSeatNumberError(Exception):
    """Користувацький виняток для неправильного номера місця."""
    pass

class Ticket:
    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

    def display_info(self):
        return f"Фільм: {self.movie_title}, Місце: {self.seat_number}, Ціна: {self.price} грн"

class StandardTicket(Ticket):
    def __init__(self, movie_title, seat_number, price, discount=0):
        super().__init__(movie_title, seat_number, price)
        self.discount = discount

    def display_info(self):
        discount_info = f", Знижка: {self.discount}%" if self.discount else ""
        return f"{super().display_info()}{discount_info}"

class VIPticket(Ticket):
    def __init__(self, movie_title, seat_number, price, lounge_access=True, complimentary_drinks=1):
        super().__init__(movie_title, seat_number, price)
        self.lounge_access = lounge_access
        self.complimentary_drinks = complimentary_drinks

    def display_info(self):
        lounge_info = "Доступ до VIP-зони" if self.lounge_access else "Без доступу до VIP-зони"
        return f"{super().display_info()}, {lounge_info}, Безкоштовні напої: {self.complimentary_drinks}"

class Cinema:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        try:
            if not (1 <= ticket.seat_number <= 100):
                raise InvalidSeatNumberError(f"Невірний номер місця: {ticket.seat_number}. Повинен бути від 1 до 100.")
            self.tickets.append(ticket)
            print(f"Квиток додано: {ticket.display_info()}")
        except InvalidSeatNumberError as e:
            print(f"Помилка: {e}")
        except Exception as e:
            print("Сталася помилка при створенні квитка:", str(e))

    def display_all_tickets(self):
        if not self.tickets:
            print("Квитки відсутні.")
        for ticket in self.tickets:
            print(ticket.display_info())

# Приклад використання
cinema = Cinema()

# Створення стандартних та VIP квитків
standard_ticket = StandardTicket("Фільм A", 15, 120, discount=10)
vip_ticket = VIPticket("Фільм B", 5, 250, lounge_access=True, complimentary_drinks=2)

# Додавання квитків у кінотеатр
cinema.add_ticket(standard_ticket)
cinema.add_ticket(vip_ticket)

# Спроба додати квиток із неправильним номером місця
invalid_ticket = StandardTicket("Фільм C", 150, 100)
cinema.add_ticket(invalid_ticket)

# Відображення всіх квитків
print("\nСписок усіх виданих квитків:")
cinema.display_all_tickets()