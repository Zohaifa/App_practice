import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class CustomerOrderApp(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical', padding = 10, spacing = 10)
        #Base:
        self.product_input = TextInput(hint_text = 'Which product would you like to buy')
        self.price_input = TextInput(hint_text = 'Enter product price', input_filter = 'float')
        self.quantity_slider = Slider(min = 0, max = 100, value = 1)
        self.quantity_label = Label(text = 'Quantity: 0')
        #display total cost:
        self.total_label = Label(text = 'Total price: $0.00')
        #confirm button:
        self.confirm_button = Button(text = 'Confirm Order')
        #Binding interactions
        #self.quantity_slider(value = self.on_quantity_change)
        #self.confirm_button.bind(on_press = self.on_confirm_order)
        #adding widgets
        layout.add_widget(Label(text = "Product Name:"))
        layout.add_widget(self.product_input)
        layout.add_widget(Label(text = "Product Price: "))
        layout.add_widget(self.price_input)
        layout.add_widget(Label(text = 'Select Quantity'))
        layout.add_widget(self.quantity_slider)
        layout.add_widget(self.quantity_label)
        layout.add_widget(self.total_label)
        layout.add_widget(self.confirm_button)

        return layout

if __name__ == '__main__':
    CustomerOrderApp().run()
