from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class CalculatorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input_text = ''
    
    def build(self):
        self.output_label = Label(size_hint_y=0.75, font_size=40)
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',   
                          '7', '8', '9', '*',
                          '0', '.', '=', '/')
        
        root_widget = BoxLayout(orientation='vertical')
        root_widget.add_widget(self.output_label)
        
        # Number and operator buttons in 4x4 grid
        button_grid = GridLayout(cols=4, size_hint_y=2)
        for symbol in button_symbols:
            btn = Button(text=symbol, font_size=32)
            btn.bind(on_press=self.on_button_press)
            button_grid.add_widget(btn)
        
        root_widget.add_widget(button_grid)
        
        # C button in its own full-width row
        clear_button = Button(text='C', font_size=32, size_hint_y=0.5)
        clear_button.bind(on_press=self.on_clear_press)
        root_widget.add_widget(clear_button)
        
        self.output_label.bind(height=self.resize_label_text)
        self.update_display()
        
        return root_widget
    
    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                result = str(eval(self.input_text))
                self.output_label.text = f"Input: {self.input_text}\nResult: {result}"
                self.input_text = result
            except:
                self.output_label.text = "Error"
                self.input_text = ''
        else:
            self.input_text += instance.text
            self.update_display()
    
    def on_clear_press(self, instance):
        self.input_text = ''
        self.update_display()
    
    def update_display(self):
        if self.input_text:
            self.output_label.text = f"Input: {self.input_text}"
        else:
            self.output_label.text = "0"
    
    def resize_label_text(self, label, new_height):
        label.font_size = 0.4 * label.height


if __name__ == '__main__':
    CalculatorApp().run()