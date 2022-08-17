try:
    raise ValueError()
except ValueError:
    print("Do something.")
    raise