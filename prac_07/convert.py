from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKilometres(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert.kv')
        return self.root

    def handle_calculate(self):
        value = self.handle_invalid_inputs()
        result = value * 1.609344
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.handle_invalid_inputs() + change
        self.root.ids.text_input.text = str(value)
        self.handle_calculate()

    def handle_invalid_inputs(self):
        try:
             value = float(self.root.ids.text_input.text)
             return value
        except ValueError:
            return 0


ConvertMilesToKilometres().run()