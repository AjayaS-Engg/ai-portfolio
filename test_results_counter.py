results = ["PASS", "FAIL", "PASS", "PASS", "FAIL","PASS","SKIP", "FAIL", "PASS", "SKIP","BLOCKED"]
counts = {}

for result in results:
    if result in counts:
        counts[result] += 1
    else:
        counts[result] =0+ 1

print("Total PASS:", counts["PASS"])
print("Total FAIL:", counts["FAIL"])
print("Total SKIP:", counts["SKIP"])
print("Total results:", sum(counts.values()))