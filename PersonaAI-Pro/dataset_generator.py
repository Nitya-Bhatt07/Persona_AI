import csv
import random

# 5 personality classes
personalities = ["Calm", "Leader", "Analytical", "Creative", "Emotional"]

# number of rows
ROWS = 200
QUESTIONS = 15

def generate_answer(personality):
    """
    Generate MCQ answers (1–5) based on personality type
    """
    if personality == "Calm":
        return [random.randint(1, 3) for _ in range(QUESTIONS)]

    elif personality == "Leader":
        return [random.randint(3, 5) for _ in range(QUESTIONS)]

    elif personality == "Analytical":
        return [random.choice([2, 3, 4, 5]) for _ in range(QUESTIONS)]

    elif personality == "Creative":
        return [random.randint(1, 5) for _ in range(QUESTIONS)]

    elif personality == "Emotional":
        return [random.choice([2, 3, 4]) for _ in range(QUESTIONS)]

# Create CSV
with open("dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # header
    header = [f"q{i}" for i in range(1, QUESTIONS + 1)]
    header.append("personality")
    writer.writerow(header)

    for i in range(ROWS):
        personality = random.choice(personalities)
        answers = generate_answer(personality)

        writer.writerow(answers + [personality])

print("✅ dataset.csv generated successfully with 200 rows!")