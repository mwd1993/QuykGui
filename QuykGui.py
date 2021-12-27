import tkinter as tk


class qgui:
    tk = tk

    def __init__(self):
        self.windows = []

    def new_window(self, window_name):
        if window_name:
            window = qgui.__window(window_name, _parent=self)
            self.windows.append(window)
            return window
        else:
            return False

    def set_main_window(self, window):
        window.object.mainloop()
        return self

    class __window:
        def __init__(self, window_name, _parent, window_size=[None, None]):
            if type(window_size) is not list:
                print('provided window size is not a list [size_x,size_y].\nDefaulting to size -> [600,600]')
                window_size = [600, 600]
            self.interface_objects = []
            self._ids = {}
            self.name = window_name
            self.parent = _parent
            self.tk = self.parent.tk
            self.object = tk.Tk()
            self.__background_color = None
            self.__global_padding = 5
            if window_size[0]:
                geo = str(window_size[0]) + 'x' + str(window_size[1])
                self.object.geometry(geo)
            self.object.title(window_name)

        def hide(self):
            self.object.withdraw()
            return self

        def show(self):
            self.object.deiconify()
            return self

        def resize(self):
            self.object.geometry("")

        def set_color(self, background_color=''):
            self.object.configure(bg=background_color)
            self.__background_color = background_color
            return self

        def get_color(self):
            return self.__background_color

        def set_global_padding(self, interface_object_padding):
            if type(interface_object_padding) is int:
                self.__global_padding = interface_object_padding
            else:
                print('set_global_padding only accepts integers.')

        def set_position(self, x_y: list):
            self.object.geometry('+' + str(x_y[0]) + '+' + str(x_y[1]))
            return self

        def get_position(self):
            g = self.object.geometry()
            g = str(g).replace('+', ' ').split(' ')
            return [g[1], g[2]]

        def get_by_id(self, str_id):
            if str_id in self._ids:
                return self._ids[str_id]
            else:
                return False

        def set_title(self, window_name):
            self.name = window_name
            self.object.title(window_name)
            return self

        def set_size(self, x_or_list, y=-1):
            if type(x_or_list) is list and y == -1:
                geo = str(x_or_list[0]) + 'x' + str(x_or_list[1])
            else:
                x = x_or_list
                geo = str(x) + 'x' + str(y)
            self.object.geometry(geo)
            return self

        # ------------------
        # Interface Objects
        # ------------------

        def new_btn(self, _text='ok', width_and_height=[20, 2], on_click_callback='', position=[None], id=''):
            btn = self.tk.Button(self.object, text=_text, width=width_and_height[0], height=width_and_height[1])
            btn.parent = self
            if on_click_callback:
                btn['command'] = on_click_callback

            btn.pack(pady=self.__global_padding)

            if len(position) >= 2:
                print('Position set ' + str(position))
                btn.place(x=position[0], y=position[1])

            io = self.__io_button(btn, 'button', _text, width_and_height=width_and_height, position=position, id=id, on_click_callback=on_click_callback)

            if id:
                self._ids[id] = io
            self.interface_objects.append(io)

            print('io button - > ' + str(io))
            return io

        def new_text(self, _text='Text', id='', width_and_height=[None, None], position=[None], font_size=None):
            # configure(font=('Ariel', i.get()))
            text = self.tk.Label(self.object, text=_text, width=width_and_height[0], height=width_and_height[1])
            text.parent = self
            if font_size:
                text.configure(font=(None, font_size))
            text.pack(pady=self.__global_padding)

            if len(position) >= 2:
                print('Position set ' + str(position))
                text.place(x=position[0], y=position[1])

            io = self.__io_text(text, 'text', _text, width_and_height=width_and_height, position=position, id=id)
            self.interface_objects.append(io)
            if id:
                self._ids[id] = io

            print('io text - > ' + str(io))
            return io

        def new_input(self, pre_text='', id='', position=[None], width_and_height=[None,None], on_enter_key='', on_value_change='',focus=False):
            _input = tk.Entry(self.object,width=width_and_height[0],borderwidth=2)
            _input.parent = self
            if pre_text:
                _input.insert(0, pre_text)
            _input.pack(pady=self.__global_padding)

            if len(position) >= 2:
                _input.place(x=position[0], y=position[1])

            if focus:
                _input.focus()

            io = self.__io_input(_input, 'input', pre_text, width_and_height=width_and_height, position=position, id=id, on_enter_key=on_enter_key,on_value_change=on_value_change)
            print('io input - > ' + str(io))
            self.interface_objects.append(io)
            if id:
                self._ids[id] = io
            return io

        def new_list(self, list_of_text_vals, position=[None], id='', width_and_height=[40, 8], on_click_callback=''):
            l_b = self.tk.Listbox(self.object, width=width_and_height[0], height=width_and_height[1],borderwidth=2)
            l_b.parent = self
            if on_click_callback:
                l_b.bind("<<ListboxSelect>>", on_click_callback)
            _index = 0
            for l in list_of_text_vals:
                _index += 1
                l_b.insert(_index, l)

            l_b.pack(pady=self.__global_padding)

            if len(position) >= 2:
                l_b.place(x=position[0], y=position[1])

            io = self.__io_list(l_b, 'list', list_of_text_vals, width_and_height=width_and_height, position=position, id=id, on_click_callback=on_click_callback)
            print('io list - > ' + str(io))
            self.interface_objects.append(io)
            if id:
                self._ids[id] = io

            return io

        def new_checkbox(self, text, on_click_callback='', id=''):
            var1 = False
            cb = self.tk.Checkbutton(self.object, text=text, variable=var1)
            cb.checked = var1
            if on_click_callback:
                cb['command'] = on_click_callback
            cb.pack()
            io = self.__io_check_box(cb)
            self.interface_objects.append(io)
            if id:
                # cb['id'] = id
                self._ids[id] = io

            return io

        # ------------------
        # Interface Objects End
        # ------------------

        class __io_text:
            def __init__(self, obj, _type, first='', width_and_height='', position=[None], id='', on_click_callback=''):
                self.tk = tk
                self.parent = obj.parent
                self.object = obj
                self.type = _type
                self.__background_color = None
                self.constructor_vals = {
                    'first': first,
                    'width_height': width_and_height,
                    'position': position,
                    'id': id,
                    'on_click_callback': on_click_callback
                }

                if self.parent.get_color() is not None:
                    self.set_color(self.parent.get_color())

            def set_color(self, background_color=''):
                self.object.configure(bg=background_color)
                self.__background_color = background_color
                return self

            def get_color(self):
                return self.__background_color

            def get_text(self):
                if self.type == 'text':
                    return self.object['text']

            def set_text(self, string):
                self.object.configure(text=string)
                return self

        class __io_input:
            def __init__(self, obj, _type, first='', width_and_height='', position=[None], id='', on_enter_key='',on_value_change=''):
                self.tk = tk
                self.object = obj
                self.type = _type
                self.parent = obj.parent
                self.__background_color = None
                if on_value_change:
                    self.object.bind('<KeyRelease>',on_value_change)
                if on_enter_key:
                    self.object.bind('<Return>', on_enter_key)

                self.constructor_vals = {
                    'first': first,
                    'width_height': width_and_height,
                    'position': position,
                    'id': id,
                }

                if self.parent.get_color() is not None:
                    self.set_color(self.parent.get_color())

            def set_color(self, background_color=''):
                self.object.configure(bg=background_color)
                self.__background_color = background_color
                return self

            def get_color(self):
                return self.__background_color

            def get_value(self):
                return self.object.get()

            def set_value(self, string):
                # self.clear_value()
                self.object.insert(0, string)
                return self

            def clear_value(self):
                self.object.delete(0, 'end')
                return self

            def disable(self, bool=True):
                pass

        class __io_button:
            def __init__(self, obj, _type, first='', width_and_height='', position=[None], id='', on_click_callback=''):
                self.tk = tk
                self.object = obj
                self.type = _type
                self.parent = obj.parent
                self.__background_color = None
                self.constructor_vals = {
                    'first': first,
                    'width_height': width_and_height,
                    'position': position,
                    'id': id,
                    'on_click_callback': on_click_callback
                }

                if self.parent.get_color() is not None:
                    self.set_color(self.parent.get_color())
                # print(str(self.constructor_vals))

            def set_color(self, background_color=''):
                self.object.configure(bg=background_color)
                self.__background_color = background_color
                return self

            def get_color(self):
                return self.__background_color

            def set_text(self, string):
                self.object.configure(text=string)
                return self

            def get_text(self):
                return self.object['text']

        class __io_list:
            def __init__(self, obj, _type, first='', width_and_height='', position=[None], id='', on_click_callback=''):
                self.tk = tk
                self.object = obj
                self.type = _type
                self.parent = obj.parent
                self.constructor_vals = {
                    'first': first,
                    'width_height': width_and_height,
                    'position': position,
                    'id': id,
                    'on_click_callback': on_click_callback
                }
                self.__list = first
                self.__background_color = None

                if self.parent.get_color() is not None:
                    # pass this for now for lists: self.set_color(self.parent.get_color())
                    pass


            def set_color(self, background_color=''):
                self.object.configure(bg=background_color)
                self.__background_color = background_color
                return self

            def get_color(self):
                return self.__background_color

            def get_selected(self):
                return self.object.get(self.tk.ANCHOR)

            def set_selected(self, index=0):

                self.object.selection_clear(0, 'end')
                if index == -1:
                    return self
                self.object.selection_set(index)
                return self

            def get_list(self):
                return self.__list

            def set_list(self, list_of_values):
                self.__list = list_of_values
                self.object.delete(0, self.tk.END)
                i = 0
                for v in list_of_values:
                    i = i + 1
                    self.object.insert(i, v)

                return self

        class __io_check_box:
            def __init__(self, obj, on_click_callback='', _id=''):
                self.tk = tk
                self.object = obj
                self.var = self.tk.BooleanVar()
                self.constructor_vals = {
                    'on_click_callback': on_click_callback,
                    'id': _id
                }

            def set_checked(self, checked: bool):
                print('state ' + str(self.object.checked))
                self.object.checked = checked
                if checked:
                    self.object.select()
                    self.var.set(True)
                else:
                    self.object.deselect()
                    self.var.set(False)
                return self

            def get_value(self):
                try:
                    print('- > ' + str(self.var.get()))
                    return self.var.get()
                except Exception as e:
                    print('error on checkbutton using get\n' + str(e))
                    return False
