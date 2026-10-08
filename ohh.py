def average(numbers):
    return sum(numbers) / len(numbers)

students = {
    "Asha": [85, 90, 78],
    "Ravi": [92, 88, 95],
    "Mina": [70, 65, 80],
}

for name, scores in students.items():
    avg = average(scores)
    status = "Pass" if avg >= 75 else "Needs work"
    print(f"{name}: {avg:.1f} ({status})")