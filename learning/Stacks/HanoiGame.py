from StackHanoi import Stack

print("\n¡Vamos a jugar a las torres de Hanoi!")

#Crear las pilas
stacks = [Stack("Left"), Stack("Middle"), Stack("Right")]


# Crear las pilas
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.extend([left_stack, middle_stack, right_stack])

# Configurar el juego
num_disks = int(input("\n¿Con cuántos discos quieres jugar?\n"))
while num_disks < 3:
    num_disks = int(input("Ingresa un número mayor o igual a 3\n"))

# Agregar discos a la pila izquierda
for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

# Calcular la cantidad de movimientos óptimos
num_optimal_moves = (2 ** num_disks) - 1
print(f"\nLo más rápido que puedes resolver este juego es en {num_optimal_moves} movimientos")
#Obtener entrada del usuario


        
#Jugando el juego
