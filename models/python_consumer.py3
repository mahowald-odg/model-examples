# fastscore.schema.0: sch_output
# fastscore.schema.1: python_output


def action(datum):
    s = str(datum) + " from Python!"
    yield s