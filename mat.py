import matplotlib.pyplot as plt

students = ["Arun", "Bala", "Charan", "David"]
marks = [80, 95, 70, 90]

plt.figure(figsize=(8,5))

plt.bar(students, marks, color="blue")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.grid(axis="y")

plt.show()