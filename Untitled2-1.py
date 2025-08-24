from nicegui import ui
import random

def redirect_to_patreon():
    ui.run_javascript('window.open("https://www.openai.com", "_blank")')

def redirect_to_site():
    ui.run_javascript('window.open("http://127.0.0.1:8080", "_blank")')

# Create a visually styled button that redirects
ui.button('Buy me a coffe', icon='coffee', on_click=redirect_to_patreon).style(
    'background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;'
)

with ui.element("div").classes('absolute top-0 right-0 p-4'):
    ui.button('Playlist Randomizer', icon='verified', on_click=redirect_to_site, color='green').classes(
        'bg-green-500 text-white py-2 px-4 rounded hover:bg-green-700 no-underline'
    ).style(
        'background-color: green; color: white;'
    )

def go_to_page2():
    ui.open_url('/page2')

# Define the first page
@ui.page('/')
def main_page():
    with ui.column():
        ui.label('This is the Main Page')
        ui.button('Go to Page 2', on_click=go_to_page2)

# Define the second page
@ui.page('/page2')
def second_page():
    with ui.column():
        ui.label('This is Page 2')
        ui.button('Go to Main Page', on_click=lambda: ui.open('/'))


with ui.element("div").classes(
    "w-full h-full flex justify-center items-center"
).style("background-color: transparent;"): 
    ui.textarea(label='Text', placeholder='Start writing!').props('clearable')
    

ui.textarea(label='Doggo', placeholder='Write bro!').props('clearable').style("width: 700px; height: 200px;")
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

ui.run()
