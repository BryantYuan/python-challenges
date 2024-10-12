from memory_profiler import memory_usage


def calculate_memory_usage(file_path):
    # Define a function to execute the Python file
    with open(file_path) as f:
        code = f.read()  # Read the Python file content
        mem_before = memory_usage()[0]
        exec(code)  # Dynamically execute the file content
        mem_after = memory_usage()[0]

    # Measure memory usage of executing the Python file
    mem_usage = mem_after - mem_before

    # Return the memory usage information
    return mem_usage