import gradio as gr

def unit_converter(category, value, from_unit, to_unit):
    try:
        if category == "Length":
            factors = {
                "meters": 1,
                "kilometers": 1000,
                "miles": 1609.34,
                "feet": 0.3048
            }
            result = value * factors[from_unit] / factors[to_unit]

        elif category == "Weight":
            factors = {
                "grams": 1,
                "kilograms": 1000,
                "pounds": 453.592,
                "ounces": 28.3495
            }
            result = value * factors[from_unit] / factors[to_unit]

        elif category == "Temperature":
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    result = (value * 9/5) + 32
                elif to_unit == "Kelvin":
                    result = value + 273.15
                else:
                    result = value
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    result = (value - 32) * 5/9
                elif to_unit == "Kelvin":
                    result = (value - 32) * 5/9 + 273.15
                else:
                    result = value
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    result = value - 273.15
                elif to_unit == "Fahrenheit":
                    result = (value - 273.15) * 9/5 + 32
                else:
                    result = value

        elif category == "Time":
            factors = {
                "seconds": 1,
                "minutes": 60,
                "hours": 3600,
                "days": 86400
            }
            result = value * factors[from_unit] / factors[to_unit]
        else:
            return "Invalid category"

        return f"{value} {from_unit} = {result:.4f} {to_unit}"

    except Exception as e:
        return f"Error: {e}"

# Unit options
categories = {
    "Length": ["meters", "kilometers", "miles", "feet"],
    "Weight": ["grams", "kilograms", "pounds", "ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["seconds", "minutes", "hours", "days"]
}

with gr.Blocks() as demo:
    gr.Markdown("## 🔄 Unit Converter App")

    category = gr.Dropdown(choices=list(categories.keys()), value="Length", label="Category")
    value = gr.Number(label="Value", value=1.0)
    from_unit = gr.Dropdown(choices=categories["Length"], value="meters", label="From")
    to_unit = gr.Dropdown(choices=categories["Length"], value="kilometers", label="To")

    output = gr.Textbox(label="Result")

    def update_units(cat):
        return gr.update(choices=categories[cat], value=categories[cat][0]), \
               gr.update(choices=categories[cat], value=categories[cat][1])

    category.change(update_units, category, [from_unit, to_unit])
    gr.Button("Convert").click(unit_converter, [category, value, from_unit, to_unit], output)

demo.launch()
