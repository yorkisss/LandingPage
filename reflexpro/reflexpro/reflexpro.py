import reflex as rx

class State(rx.State):
    pass

def navbar():
    logo_size = "55px"

    return rx.hstack(
        
        rx.image(
            src="/logo.png", 
            width="auto",
            height=logo_size,
            border_radius="md",
            object_fit="contain"
        ),
        rx.spacer(), 

        
        rx.hstack(
            rx.text("Life & News", href="#", font_family="Helvetica", font_size="sm", margin_x="0.5em", color="#26201c"),
            rx.text("About", href="#", font_family="Helvetica", font_size="sm", margin_x="0.5em", color="#26201c"),
            rx.text("Store", href="#", font_family="Helvetica", font_size="sm", margin_x="0.5em", color="#26201c"),
            rx.text("Recipes", href="#", font_family="Helvetica", font_size="sm", margin_x="0.5em", color="#26201c"),
            spacing="1",
        ),
        rx.spacer(), 



        rx.image(
            src="/logo2.png", 
            width="auto",
            height=logo_size,
            border_radius="md",
            object_fit="contain"
        ),
        
        
        justify="between",
        padding="0.5em 1em",
        bg="#e5e9de", 
        width="100%",
        align_items="center",
    ), 
    rx.image( 
        src="/logo2.png",
        width=logo_size,
        height="auto",
        border_radius="md",
        object_fit="contain"
    ),
    rx.spacer(),
def hero():
    return rx.hstack(
        rx.box(
            rx.image(src="/foto1.png", height="1000"), 
            rx.vstack(
                
            ),
            flex="1", 
            align_items="flex-start",
            
            
        ),
        
    )

def top_picks():
    return rx.box(
        rx.image(
            src="/foto4.png",
            height="auto",
            border_radius="md",
            object_fit="contain"
        )
    )

def school_section():
    return rx.box(
        rx.image(
            src="/foto2.png",
            height="auto",
            border_radius="md",
            object_fit="contain",
            style={"margin-left": "-210px"}
        )
    )

def everyday_section():
    return rx.box(
        rx.image(
            src="/foto3.png",
            height="auto",
            border_radius="md",
            object_fit="contain",
            style={"margin-left": "-210px"} 
        )
    )

def index():
    return rx.vstack(
        navbar(),
        rx.hstack(
            rx.vstack(
                hero(),
                top_picks(),
                align_items="flex-start",
                flex="2",
            ),
            rx.vstack(
                school_section(),
                everyday_section(),
                align_items="stretch",
                flex="1",
                spacing="1",
            ),
            spacing="2",
            padding="1",
            align_items="flex-start",
        ),
        bg="#e5e9de",
        min_h="100vh",
        align_items="stretch",
        style={"width": "1100px", "margin": "0 auto"}, # Añadimos un ancho máximo y centramos
    )
app = rx.App()
app.add_page(index)