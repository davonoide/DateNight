import flet as ft
import random

# Definir los topics
topics = [
    {
        "What to eat?": {
            "options": [
                        "Pizza",
                        "Elotes",
                        "Hamburguesas",
                        "Tacos",
                        "Chilaquiles",
                        "Bola de arroz",
                        "Comida china",
                        "Tamales",
                        "Crepas",
                        "Sushi",
                        "Enchiladas",
                        "Pasta",
                        "Sandwiches",
                        "Quesadillas",
                        "Empanadas",
                        "Hot dogs",
                        "Ensalada",
                        "Ramen",
                        "Burritos",
                        "Nachos",
                        "Sopa",
                        "Pollo frito",
                        "Panqueques",
                        "Fajitas",
                        "Ceviche",
                        "Arepas",
                        "Waffles",
                        "Churros",
                        "Donas",
                        "Helado"
                    ]
        },
        "What to do?": {
            "options": ["Ver pelicula", 
                        "Salir al parque", 
                        "Ir al Cine", 
                        "Ver series", 
                        "Ver MAX", 
                        "Ver Prime", 
                        "Ver Disney", 
                        "Jugar juegos de mesa", 
                        "Just dance en pareja", 
                        "Ir al parque", 
                        "Ir a la presa", 
                        "Jugar VideoJuegos", 
                        "Pintar", 
                        "Cena romántica",
                        "Noche de cine",
                        "Paseo al aire libre",
                        "Caminata en la naturaleza",
                        "Ver documentales",
                        "Cita en un café",
                        "Ver nueva serie",
                        ]
        },
        "What to do after?": {
            "options": ["Ir por un helado", 
                        "Ir por malteada", 
                        "Blizzard", 
                        "Ir por papitas", 
                        "Cucharear", 
                        "Ducha juntos",
                        "Ver un episodio",
                        "Beber té o café",
                        "Paseo corto",
                        "Contar historias",
                        "Compartir un snack",
                        "Mirar estrellas",
                        "Abrazarse y conversar"]
        },
        "Sexy Time": {
            "options": ["De perrito",
                        "De frente",
                        "El arriba",
                        "Ella arriba",
                        "La cucharita",
                        "69",
                        "La vaquera",
                        "El misionero",
                        "El puente",
                        "El molinillo",
                        "La carretilla",
                        "El espiral",
                        "El tornillo",
                        "La amazona",
                        "El cangrejo",
                        "El loto",
                        "El martillo",
                        "El abrazo del koala",
                        "El columpio",
                        "El gatito",
                        "La tijera",
                        "El helicóptero",
                        "El dragón",
                        "La hamaca",
                        "La fusión",
                        "El trapecio",
                        "El camaleón",
                        "La estrella",
                        "El beso profundo",
                        "El ancla",
                        "El rincón del placer",
                        "La ola",
                        "El faro",
                        "El corazón valiente",
                        "El arco",
                        "El fluir",
                        "La mariposa",
                        "El zigzag",
                        "El ascensor",
                        "El colibrí",
                        "El balancín",
                        "El puente de amor",
                        "El cohete",
                        "La estrella fugaz",
                        "El tsunami",
                        "El vals",
                        "El barco",
                        "El tren",
                        "El auto",
                        "El delfín"
                    ]
        },
    }
]

def main(page: ft.Page):
    page.title = "DateNigth"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    Title1 = ft.Text(value="DATE", size=30)
    image = ft.Image(src="heart.png", width=70, height=70)  # Reemplaza con la URL de tu imagen o una ruta local
    Title2 = ft.Text(value="NIGHT", size=30)

    Title_row = ft.Row(controls=[Title1, image, Title2], alignment=ft.MainAxisAlignment.CENTER)
    Title_container = ft.Container(content=Title_row, bgcolor=ft.colors.BLACK45, padding=10, width=1050, height=100, border_radius=8)

    # Usar Column para centrar el Container
    centered_title = ft.Column(
        controls=[Title_container],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    page.add(centered_title)
    
    row = ft.ResponsiveRow(spacing=20, alignment=ft.MainAxisAlignment.CENTER,)

    # Function to handle button click
    def select_option(e):
        topic_name = e.control.data
        topic_options = topics[0][topic_name]["options"]
        selected_option = random.choice(topic_options)
        
        # Update the corresponding result Text
        for item in row.controls:
            if isinstance(item, ft.Container):
                col = item.content
                if isinstance(col, ft.Column):
                    for sub_item in col.controls:
                        if isinstance(sub_item, ft.Container) and sub_item.data == topic_name:
                            result_text = sub_item.content
                            if isinstance(result_text, ft.Text):
                                result_text.value = selected_option
        
        # Update the page to reflect changes
        page.update()
    
    # Function to handle reset button click
    def reset_all(e):
        # Reset all result Text to empty
        for item in row.controls:
            if isinstance(item, ft.Container):
                col = item.content
                if isinstance(col, ft.Column):
                    for sub_item in col.controls:
                        if isinstance(sub_item, ft.Container):
                            result_text = sub_item.content
                            if isinstance(result_text, ft.Text):
                                result_text.value = ""
        
        # Update the page to reflect changes
        page.update()

    # Create the UI elements
    for topic_name in topics[0].keys():
        topic_text = ft.Text(value=topic_name, data=topic_name, size=20)
        select_button = ft.ElevatedButton(text="Escojer", data=topic_name, on_click=select_option)
        result_text = ft.Text(value="", size=20, text_align=ft.TextAlign.CENTER)
        
        result_container = ft.Container(content=result_text, data=topic_name, bgcolor=ft.colors.GREY_900, padding=5, alignment=ft.alignment.center)
        
        col = ft.Column(controls=[topic_text, select_button, result_container], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
        container = ft.Container(content=col, bgcolor=ft.colors.BLACK45, padding=10, border_radius=8, col={"sm": 12, "md": 6, "xl": 3})

        row.controls.append(container)
    
    # Create a Column with scrolling enabled
    scrollable_column = ft.Column(
        controls=[row],
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    # Add the Scrollable Column to the page
    page.add(scrollable_column)
    
    # Create and add the reset button
    reset_button = ft.ElevatedButton(text="Reiniciar", on_click=reset_all)
    reset_button_row = ft.Row(controls=[reset_button], alignment=ft.MainAxisAlignment.CENTER)
    page.add(reset_button_row)

    page.update()

# Run the Flet app
ft.app(target=main)
