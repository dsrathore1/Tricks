from prettytable import PrettyTable

myTable = PrettyTable(["Student", "Class", "Section", "Percentage"])

myTable.add_row (["Joe", "X", "A", "94.32%\n"])

myTable.add_row (["Raj", "X", "A", "91.29%\n"])

myTable.add_row (["Roy", "X", "A", "89.20%\n"])

myTable.add_row (["Mili", "X", "A", "92.80%\n"])

print (myTable)

