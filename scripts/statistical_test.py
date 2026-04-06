from scipy.stats import mannwhitneyu

hotspot = [0.91, 1.0, 0.91, 1.0, 1.0, 0.91]
non_hotspot = [0.78, 0.75, 0.80, 0.76]

stat, p = mannwhitneyu(hotspot, non_hotspot)

print("p-value:", p)
