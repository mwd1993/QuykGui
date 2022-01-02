# QuykGui
A way to quickly create GUI elements, while also providing easy to add custom functionality.  
Also, if need be, you can directly access the tkinter object by reference: `QuykGuiObject.object`.  
This means, you can always do anything tkinter allows for, if you need to do things QuykGui does not allow.  
Think of QuykGui as a higher level way to make interfaces while still allowing for lower level (tkinter objects) access.


### Basic Example | add easy search filtering

![](https://github.com/mwd1993/QuykGui/blob/main/quykgui%20example.gif)

### The code behind the GIF Example

```python
from QuykGui import qgui

# Define methods to be used when we interact
# with the interface elements
# ------------------------------------------
def list_click_show_item(e=''):
    global window
    main_list = window['main'].get_by_id('main-list')
    selected = main_list.get_selected()
    print(selected)
    window['ok'].get_by_id('ok-text').set_text('You clicked on ' + str(selected))
    window['ok'].show()


def input_sort_gui_list(a=''):
    global window
    main_list = window['main'].get_by_id('main-list')
    main_input = window['main'].get_by_id('main-input')
    _show = []
    for li in main_list.get_list():
        if main_input.get_value().lower() in li.lower():
            _show.append(li)
    if len(_show) == 0:
        main_list.set_list(fruit_list)
        return fruit_list
    main_list.set_list(_show)
    return _show


def ok_close():
    global window
    window['ok'].hide()


def button_exit_program():
    exit()
# ------------------------------------------
# ------------------------------------------

# Initialize QuykGui
q = qgui()

# Create a few windows we will be using
# for our Graphical Interface
window = {
    'main': q.new_window('Main Window'),
    'ok': q.new_window('Ok').hide()
}

# Easily Customize/Edit our Ok window
window['ok'].set_size([300, 100])
window['ok'].new_text('some text here', id='ok-text')
window['ok'].new_btn('Ok', on_click_callback=ok_close)

# Easily Customize/Edit our Main window
window['main'].set_size([600, 300])
window['main'].new_text('Type part of a substring below to search through the list (press enter to search)')
window['main'].new_input(on_value_change=input_sort_gui_list, id='main-input')
fruit_list = open('fruit list.txt','r').readlines()
window['main'].new_list(fruit_list, on_click_callback=list_click_show_item,id='main-list')
window['main'].new_btn('Exit Program', on_click_callback=button_exit_program,id='main-button')

# Set our main window, to the Main Window
q.set_main_window(window['main'])

```

### Example: Accessing a tkinter object
```python
from QuykGui import qgui

# Initialize QuykGui
q = qgui()

# Create a main window
window = {
    'main': q.new_window('Main Window'),
}

# Option 1 - storing to local variable
text_element = window['main'].new_text('this is some text on the interface.')
tkinter_obj = text_element.object

# Option 2 - finding by Id
window['main'].new_text('this is some text on the interface.', id='text_element')
tkinter_obj = window['main'].get_by_id('text_element').object

# Set our main window, to the Main Window
q.set_main_window(window['main'])
```
