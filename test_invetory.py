from inventory import calculate_restock_order

print("Running Test 1 - normal item, low velocity")
result = calculate_restock_order(20, 30, 100, 10, False)
print("Obtained:", result, "expected: 80")
assert result == 80
print("done\n")

print("Running Test 2 - high velocity item")
result = calculate_restock_order(10, 20, 100, 10, True)
print("Obtained:", result, "expected: 110")
assert result == 110
print("done\n")

print("Running Test 3 - stock is still fine, no order needed")
result = calculate_restock_order(50, 30, 100, 10, False)
print("Obtained:", result, "expected: 0")
assert result == 0
print("done\n")

print("Running Test 4 - batch size of 0 should raise an error")
try:
    calculate_restock_order(10, 20, 100, 0, False)
    print("No error was raised!")
except ValueError as e:
    print("got the error we expected:", e)
print()

print("Running Test 5 - negative stock should raise an error")
try:
    calculate_restock_order(-5, 20, 100, 10, False)
    print("No error was raised!")
except ValueError as e:
    print("got the error we expected:", e)
print()

print("Running Test 6 - max_capacity not bigger than reorder_point should raise an error")

try:
    calculate_restock_order(10, 50, 40, 10, False)
    print("No error was raised")
except ValueError as e:
    print("got the error we expected:", e)
print()

print("All tests are done!")