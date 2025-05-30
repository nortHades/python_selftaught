# Global variable
global_counter = 0


def increment_counter():
    # Local variable
    local_counter = 1
    print(f"Local counter: {local_counter}")


def increment_global_counter():
    global global_counter
    global_counter += 1
    print(f"Global counter: {global_counter}")


# Example
increment_counter()  # output local_counter = 1
increment_global_counter()
