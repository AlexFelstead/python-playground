# Implementing check against "Expecting" and "Result" for a print result would be ideal next step


hobby = "bouldering"
print(f"Expecting: g\nResult: {hobby[-1]}")

print("\n...\n")

hamlet = "To be, or not to be!"
print(f"Expecting: !\nResult: {hamlet[-1]}")

print("\n...\n")

macbeth = "Tomorrow, tomorrow and tomorrow, creeps in this petty pace from day to day to the last syllable of recorded time."
print(f"Expecting: Tomorrow\nResult: {macbeth[0:8]}")

print("\n...\n")

romeo = "What light through yonder window breaks?"
print(f"Expecting: WINDOW BREAKS\nResult: {romeo[-14:-1].upper()}")
