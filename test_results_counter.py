results = ["PASS", "FAIL", "PASS", "PASS", "FAIL","PASS","SKIP", "FAIL", "PASS", "SKIP"]
pass_count = 0
fail_count = 0
skip_count = 0
for result in results:
    if result == "PASS":
        pass_count += 1
    elif result == "FAIL":
        fail_count += 1
    elif result == "SKIP":
        skip_count += 1

print("Total PASS:", pass_count)
print("Total FAIL:", fail_count)
print("Total SKIP:", skip_count)
print("Total results:", pass_count + fail_count + skip_count)