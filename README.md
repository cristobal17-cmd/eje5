juegos = []

for i in range(2):
    print(f"\nVideojuego {i + 1}:")
    
    nombre = input("Nombre del videojuego: ").strip()
    while not nombre:
        print("Error: El nombre no puede estar vacío.")
        nombre = input("Nombre del videojuego: ").strip()
    
    while True:
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: Por favor ingresa un número válido (ejemplo: 29.99).")
    
    oferta = False
    
    videojuego = {
        "nombre": nombre,
        "precio": precio,
        "oferta": oferta
    }
    
    juegos.append(videojuego)

print("\n--- Lista completa de juegos ---")
for j in juegos:
    estado_oferta = "Sí" if j["oferta"] else "No"
    print(f"Juego: {j['nombre']} | Precio: ${j['precio']:.2f} | En oferta: {estado_oferta}")