# fastscore.schema.0: sch_input
# fastscore.schema.1: sch_output


# action gets called every time the model received data
def action(datum): # datum will match the sch_input, i.e. it will be a double
    x = datum
    y = datum*datum
    
    yield{'x': x, 'y':y}