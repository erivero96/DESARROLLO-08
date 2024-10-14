import reflex as rx

class State(rx.State):
    contador: int = 0

    # Función para incrementar el conteo
    def incrementar(self):
        self.contador += 1

    # Función para disminuir el conteo
    def disminuir(self):
        self.contador -= 1


def Contador() -> rx.Component:
    return rx.vstack(
        rx.heading(State.contador),
        rx.button("Incrementar", on_click=State.incrementar),
        rx.button("Disminuir", on_click=State.disminuir),
    )
    

# Configuración de la app y página principal
app = rx.App()
app.add_page(Contador)  # Página del contador

