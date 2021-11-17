class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []


    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty(self):
        for person in self.passengers:
            self.passengers.remove(person)
        # OR:
        # self.passengers.clear()

    def pick_up_from_stop(self, b_stop):
        for person in b_stop.queue:
            self.pick_up(person)
    # OR:
    # def pick_up_from_stop(self, b_stop):
    #     for person in b_stop.queue:
    #         self.passengers.append(person)
    #     return len(self.passengers)