import merge_sort
import quick_sort
import generate_data
import performance_analysis
import seaborn as sns
import pandas as pd

# Generate datasets
sizes = [1000, 5000, 10000, 20000]
data_types = ["Sorted", "Reverse Sorted", "Random"]

results = []

for size in sizes:
    sorted_data = generate_data.create_sorted_data(size)
    reverse_sorted_data = generate_data.create_reverse_sorted_data(size)
    random_data = generate_data.create_random_data(size)

    datasets = {"Sorted": sorted_data, "Reverse Sorted": reverse_sorted_data, "Random": random_data}

    for data_type, data in datasets.items():
        merge_sort_result = performance_analysis.measure_performance(merge_sort.merge_sort, data.copy(), "Merge Sort")
        quick_sort_result = performance_analysis.measure_performance(quick_sort.quick_sort, data.copy(), "Quick Sort")

        results.append({"Algorithm": "Merge Sort", "Data Type": data_type, "Size": size, "Time (sec)": merge_sort_result["Time (sec)"], "Memory (MB)": merge_sort_result["Peak Memory Used (MB)"]})
        results.append({"Algorithm": "Quick Sort", "Data Type": data_type, "Size": size, "Time (sec)": quick_sort_result["Time (sec)"], "Memory (MB)": quick_sort_result["Peak Memory Used (MB)"]})

# Convert results into a DataFrame for Seaborn
df = pd.DataFrame(results)

# Plot Execution Time Comparison
sns.set(style="whitegrid")
sns.relplot(data=df, x="Size", y="Time (sec)", hue="Algorithm", style="Data Type", kind="line", markers=True)
sns.despine()
sns.plt.show()

# Plot Memory Usage Comparison
sns.relplot(data=df, x="Size", y="Memory (MB)", hue="Algorithm", style="Data Type", kind="line", markers=True)
sns.despine()
sns.plt.show()