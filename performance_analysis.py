import time
import tracemalloc

def measure_performance(sort_function, data, function_name):
    """Measures execution time and peak memory usage of a sorting function."""
    
    tracemalloc.start()  # Start memory tracking
    start_time = time.time()
    
    sort_function(data)
    
    end_time = time.time()
    current, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()  # Stop memory tracking
    
    time_taken = end_time - start_time
    memory_used = peak_memory / (1024 * 1024)  # Convert from bytes to MB
    
    result = {
        "Algorithm": function_name,
        "Time (sec)": round(time_taken, 4),
        "Peak Memory Used (MB)": round(memory_used, 4)
    }
    
    return result