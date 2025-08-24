from nicegui import ui

def open_url(url):
    ui.run_javascript(f'window.open("{url}")')

@ui.page('/')
def main_page():
    ui.button('Buy me a coffee', icon='coffee', on_click=open_url("https://www.openai.com")).style(
        'background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;'
    )

    with ui.element("div").classes('absolute top-0 right-0 p-4'):
        ui.button('Playlist Randomizer', icon='verified', on_click=open_url("http://127.0.0.1:8080"), color='green').classes(
            'bg-green-500 text-white py-2 px-4 rounded hover:bg-green-700 no-underline'
        ).style(
            'background-color: green; color: white;'
        )
        
    with ui.element("div").classes("gap-8"):
        ui.chip("Why?", icon='ads_click', on_click=lambda: open_url("http://127.0.0.1:8080")).classes('mr-6')
        ui.link('Math_solver', 'https://www.symbolab.com/worksheets/Calculus').classes('mr-6')
        ui.link('Japanese', 'https://knowt.com/flashcards/28669fe4-cd36-4a20-8faf-f22fc0d0237c/edit').classes('mr-6')
        ui.link('Spanish', 'https://spanish.wlingua.com').classes('mr-6')
        ui.link('Math_questions', 'https://mathkangaroo.org/mks/practice/free-question-samples/').classes('mr-6')
        ui.link('Myhtology', 'https://www.theoi.com').classes('mr-6')
        ui.link('Clouds', 'https://cloudatlas.wmo.int/en/home.html').classes('mr-6')
    ui.textarea(label='How are you feeling?', placeholder='Speak your mind.').props('clearable').style("width: 700px; height: 200px;")
    
    # Background customization
    ui.add_head_html("""
    <style>
        body {
            background: url('https://i.pinimg.com/originals/3a/20/3e/3a203ee6bbbcae273938ca7e4e7257f2.gif') no-repeat center center fixed;
            background-size: cover;
            margin: 0;
        }
    </style>
    """)
    
    with ui.row():
        c1 = ui.checkbox(on_change=lambda e: ui.notify(str(e.value)))
        ui.button('Are you gay?', on_click=lambda: c1.set_value(not c1.value))
    
    with ui.row():
        c2 = ui.checkbox().on('click', lambda e: ui.notify(str(e.sender.value)))
        ui.button('set value', on_click=lambda: c2.set_value(not c2.value))
    
    # Corrected button for internal navigation
    ui.button('Videos', on_click=lambda: ui.run_javascript("window.location.href = '/page2'"))

    switch = ui.switch('Switch me')
    ui.label('You are black now. Congrats!').bind_visibility_from(switch, 'value')

@ui.page('/page2')
def second_page():
    with ui.column(): 
        ui.label('Page 2')
        ui.button('Go Back to Main Page', on_click=lambda: ui.run_javascript("window.location.href = '/'"))

def open_external_site():
    ui.run_javascript("window.open('https://example.com', '_blank')")

ui.run(on_air=True)
