class Engine:
    def __init__(self, mark: str, model: str, volume: float, power: int) -> None:
        self.mark = mark
        self.model = model
        self.volume = volume
        self.power = power


class Transport:
    def __init__(self, mark: str, model: str, year: int) -> None:
        self.mark = mark
        self.model = model
        self.year = year


class Car(Transport):
    def __init__(
        self, mark: str, model: str, year: int, color: str, price: int, engine: Engine
    ) -> None:
        super().__init__(mark, model, year)
        self.price = price
        self.color = color
        self.engine = engine

    def show_info(self) -> str:
        return f"Марка {self.mark}, модель {self.model} цвет {self.color} цена {self.price} руб. Двигатель {self.engine.model} мощностью {self.engine.power} л.с."


class Bike(Transport):
    def __init__(
        self, mark: str, model: str, year: int, color: str, price: int, engine: Engine
    ) -> None:
        super().__init__(mark, model, year)
        self.price = price
        self.color = color
        self.engine = engine

    def show_info(self) -> str:
        return f"Марка {self.mark}, модель {self.model} цвет {self.color} цена {self.price} руб. Двигатель {self.engine.model} мощностью {self.engine.power} л.с."


class Buyer:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance

    def transport_buying(self, transport: Transport):
        if self.balance < transport.price:
            not_enough_money = transport.price - self.balance
            print(f"У вас не хватает средств. Требуется ещё {not_enough_money} руб.")
        else:
            self.balance -= transport.price
            print(f"{self.name}, поздравляем с покупкой {transport.mark} {transport.model}!")
            print(f"Ваш баланс {self.balance}")


ej25 = Engine("Subaru", "EJ25", 2.5, 165)
ej20g = Engine("Subaru", "EJ20G", 2.0, 240)
moto_engine = Engine("Sizuki", "Bandit", 0.4, 50)
car01 = Car("Subaru", "Outback", 2007, "Blue", 650000, ej25)
car02 = Car("Subaru", "Forester", 1997, "Green", 270000, ej20g)
bike01 = Bike("Suzuki", "Bandit", 1991, "Black", 100000, moto_engine)
dmitry = Buyer("Дмитрий", 3000000)
dmitry.transport_buying(car01)
dmitry.transport_buying(bike01)
