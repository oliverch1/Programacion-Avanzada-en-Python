#realizamos importaciones
import os
import random
import time

class Customer:
    def __init__(self, num_floors, customer_number):
        self.cur_floor = random.randint(2, num_floors)  # Piso inicial aleatorio (excluyendo el piso 1)
        self.dst_floor = random.randint(1, num_floors)  # Piso destino aleatorio
        while self.dst_floor == self.cur_floor:
            self.dst_floor = random.randint(1, num_floors)  # Asegura que el destino sea diferente al piso actual
        self.name = str(customer_number)  # Nombre secuencial del cliente como número
        self.in_elevator = False  
        self.finished = False 

class Elevator:
    #creamos variables y definimos sus estados
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.register_list = [] 
        self.cur_floor = 1  
        self.direction = 1  

    def move(self):
        # Mueve el elevador un piso en la dirección actual
        self.cur_floor += self.direction

        # Cambia la dirección si llega al piso más alto o al piso 1
        if self.cur_floor == self.num_floors:
            self.direction = -1
        elif self.cur_floor == 1:
            self.direction = 1

    def register_customer(self, customer):
        # Agrega un cliente al elevador
        self.register_list.append(customer)
        customer.in_elevator = True

    def cancel_customer(self, customer):
        # Elimina un cliente del elevador
        self.register_list.remove(customer)
        customer.in_elevator = False
        customer.finished = True

class Building:
    def __init__(self):
        self.num_floors = self.get_valid_input("Número de pisos (entre 3 y 12): ", 3, 12)
        self.customer_list = []
        self.elevator = Elevator(self.num_floors)
        self.generate_customers()

    def get_valid_input(self, prompt, min_val, max_val):
        # Solicita al usuario un valor dentro de un rango válido
        while True:
            try:
                value = int(input(prompt))
                if min_val <= value <= max_val:
                    return value
                else:
                    print(f"Por favor, ingrese un valor entre {min_val} y {max_val}.")
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")

    def generate_customers(self):
        # Genera clientes con nombres secuenciales y los agrega a la lista de clientes del edificio
        num_customers = self.get_valid_input("Número de clientes (entre 3 y 12): ", 3, 12)
        for customer_number in range(1, num_customers + 1):
            customer = Customer(self.num_floors, customer_number)
            self.customer_list.append(customer)

    def run(self):
        while self.customer_list or self.elevator.register_list:
            os.system("cls")
            self.output()
            time.sleep(1)

            # Mover el ascensor antes de recoger a los clientes
            self.elevator.move()

            # Recoger a los clientes en el mismo piso antes de subir
            for customer in self.customer_list:
                if not customer.in_elevator and customer.cur_floor == self.elevator.cur_floor and self.elevator.cur_floor != 1:
                    self.elevator.register_customer(customer)
                    self.customer_list.remove(customer)  # Eliminar de la lista de clientes que esperan

            # Eliminar clientes del elevador y marcarlos como terminados
            for customer in self.elevator.register_list[:]:  # Usamos [:] para evitar problemas al modificar la lista
                if customer.dst_floor == self.elevator.cur_floor:
                    self.elevator.cancel_customer(customer)

    def output(self):
    # Imprime el estado del edificio y el elevador en la consola
        print("Edificio de", self.num_floors, "pisos")
        print("Piso | Suben   | Bajan   | Elevador")

        # Crear una lista de pisos en orden descendente
        reversed_floors = list(range(self.num_floors, 0, -1))

        for floor in reversed_floors:
            # Filtrar clientes en el piso actual que se están bajando del elevador
            customers_down = [customer for customer in self.elevator.register_list if customer.dst_floor == floor]

            # Obtener los nombres de los clientes que suben en este piso
            names_up = [customer.name for customer in self.customer_list if customer.cur_floor == floor]

            # Obtener los nombres de los clientes que bajan en este piso
            names_down = [customer.name for customer in customers_down]

            # Construir una cadena con los nombres de los clientes que suben en el piso actual
            names_up_str = ", ".join(names_up) if names_up else " "

            # Construir una cadena con los nombres de los clientes que bajan en el piso actual
            names_down_str = ", ".join(names_down) if names_down else " "

            elevator_indicator = "X" if self.elevator.cur_floor == floor else " "

            print(f"{floor:^4} | {names_up_str:^7} | {names_down_str:^5} | {elevator_indicator:^8}")
#definimos la funcion main 
def main():
    building = Building()
    building.run()

if __name__ == "__main__":
    main()

