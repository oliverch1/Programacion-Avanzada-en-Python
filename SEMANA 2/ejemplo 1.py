#ELEVADOR
import os
import random
import time
os.system('cls')

class Edificio:
    def __init__(self, cantidad_pisos, cantidad_clientes, elevador):
        self.cantidad_pisos = cantidad_pisos
        self.cantidad_clientes = cantidad_clientes
        self.elevador = elevador
        self.lista_clientes = self.crear_clientes()
    
    def crear_clientes(self):
        clientes = []
        for id_cliente in range(1, self.cantidad_clientes + 1):
            piso_inicio = piso_destino = random.randint(1, self.cantidad_pisos)
            while piso_inicio == piso_destino:
                piso_destino = random.randint(1, self.cantidad_pisos)
            clientes.append(Cliente(piso_inicio=piso_inicio, piso_destino=piso_destino, id_cliente=id_cliente))
        return clientes

    def mostrar_piso(self, clientes_suben, clientes_bajan, elevador_en_piso, piso_actual):
        indicador_elevador = f"{'E':^10}" if elevador_en_piso else ''
        estado_piso = f"{str(piso_actual):^10}{clientes_suben:^15}{clientes_bajan:^15}{indicador_elevador}\n{'-' * 50}"
        print(estado_piso)

    def ejecutar(self):
        """Simulación del elevador"""
        while True:
            # Encabezado
            print(f"{'-' * 50}\n{'PISO':^10}{'SUBEN':^15}{'BAJAN':^15}{'ELEVADOR':^10}\n{'-' * 50}")

            for piso in range(self.cantidad_pisos, 0, -1):
                clientes_suben, clientes_bajan = "", ""
                for cliente in self.lista_clientes:
                    if self.elevador.direccion == 'subiendo':
                        if cliente.piso_inicio == piso and not cliente.en_elevador and not cliente.finalizado:
                            clientes_suben += f"{cliente.id_cliente} "

                        self.elevador.subir_cliente(cliente)
                        
                        if cliente.piso_destino == piso and not cliente.en_elevador and cliente.finalizado:
                            clientes_bajan += f"{cliente.id_cliente} "

                        elevador_en_piso = piso == (self.elevador.piso_actual if self.elevador.contar_clientes(cliente) > 0 else self.elevador.piso_actual - 1)

                    elif self.elevador.direccion == 'bajando':
                        self.elevador.subir_cliente(cliente)
                        
                        if cliente.piso_destino == piso and not cliente.en_elevador and cliente.finalizado:
                            clientes_bajan += f"{cliente.id_cliente} "

                        elevador_en_piso = piso == (self.elevador.piso_actual if self.elevador.contar_clientes(cliente) > 0 else self.elevador.piso_actual + 1)

                self.mostrar_piso(
                    clientes_suben=clientes_suben.rstrip(), 
                    clientes_bajan=clientes_bajan.rstrip(), 
                    elevador_en_piso=elevador_en_piso, 
                    piso_actual=piso
                )

            self.elevador.mover()
            time.sleep(1)
            os.system('cls')
            if all(cliente.finalizado for cliente in self.lista_clientes):
                break

class Ascensor:
    def __init__(self, total_pisos, max_clientes, piso_actual, direccion):
        self.total_pisos = total_pisos
        self.max_clientes = max_clientes
        self.piso_actual = piso_actual
        self.direccion = direccion

    def mover(self):
        self.piso_actual += 1 if self.direccion == 'subiendo' else -1

        if self.piso_actual > self.total_pisos:
            self.direccion = 'bajando'
            self.piso_actual = self.total_pisos - 1
        elif self.piso_actual < 1:
            self.direccion = 'subiendo'
            self.piso_actual = 2

    def subir_cliente(self, cliente):
        if cliente.en_elevador or cliente.finalizado:
            return

        if (self.direccion == 'subiendo' and cliente.piso_inicio == self.piso_actual - 1) or \
           (self.direccion == 'bajando' and cliente.piso_inicio == self.piso_actual + 1):
            cliente.en_elevador = True

    def contar_clientes(self, cliente):
        if cliente.en_elevador and not cliente.finalizado:
            if (self.direccion == 'subiendo' and cliente.piso_destino == self.piso_actual - 1) or \
               (self.direccion == 'bajando' and cliente.piso_destino == self.piso_actual + 1):
                cliente.en_elevador = False
                cliente.finalizado = True
                self.max_clientes -= 1

        return self.max_clientes

class Cliente:
    def __init__(self, piso_inicio, piso_destino, id_cliente, en_elevador=False, finalizado=False):
        self.piso_inicio = piso_inicio
        self.piso_destino = piso_destino
        self.id_cliente = id_cliente
        self.en_elevador = en_elevador
        self.finalizado = finalizado

# =================================== App =======================================

def entrada_valida(pregunta="", validar=lambda entrada: entrada, *args):
    while True:
        respuesta = input(pregunta)
        validacion = validar(respuesta, *args)
        if validacion['estado']:
            return validacion['valor']
        print(validacion['mensaje'])

def validar_numero(valor, min_valor, max_valor):
    try:
        valor = int(valor)
        if min_valor <= valor <= max_valor:
            return {'estado': True, 'valor': valor}
        raise ValueError()
    except ValueError:
        return {'estado': False, 'mensaje': f'Debe ingresar un valor entre {min_valor} y {max_valor}'}

def main():
    cantidad_pisos = entrada_valida('Ingrese el número de pisos [3-12]: ', validar_numero, 3, 12)
    os.system('cls')

    cantidad_clientes = entrada_valida('Ingrese el número de clientes [1-12]: ', validar_numero, 1, 12)
    os.system('cls')

    elevador = Ascensor(total_pisos=cantidad_pisos, max_clientes=cantidad_clientes, piso_actual=1, direccion='subiendo')

    edificio = Edificio(cantidad_pisos=cantidad_pisos, cantidad_clientes=cantidad_clientes, elevador=elevador)
    edificio.ejecutar()

if __name__ == '__main__':
    main()
