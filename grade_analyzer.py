
# Task 1 — Process the Scores


def process_scores(students):
    averages = {}
    
    for name, scores in students.items():
        total = 0
        count = 0
        
        for score in scores:
            total += score
            count += 1
        
        avg = round(total / count, 2)
        averages[name] = avg
    
    return averages

# ==============================
# Task 2 — Classify the Grades
# ==============================

def classify_grades(averages):
    classified = {}
    
    # Grading thresholds (local variables, not global)
    A_grade = 90
    B_grade = 75
    C_grade = 60
    
    for name, avg in averages.items():
        if avg >= A_grade:
            grade = "A"
        elif avg >= B_grade:
            grade = "B"
        elif avg >= C_grade:
            grade = "C"
        else:
            grade = "F"
        
        classified[name] = (avg, grade)
    
    return classified



# Task 3 — Generate the Report


def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    
    total_students = len(classified)
    passed = 0
    
    for name, (avg, grade) in classified.items():
        if avg >= passing_avg:
            status = "PASS"
        else:
            status = "FAIL"
        
        if status == "PASS":
            passed += 1
        
        print(f"{name:<10} | Avg: {avg:<6} | Grade: {grade} | Status: {status}")
    
    failed = total_students - passed
    
    print("================================")
    print("Total Students :", total_students)
    print("Passed         :", passed)
    print("Failed         :", failed)
    
    return passed




students = {
        "Alice": [85, 90, 88, 82],
        "Bob": [60, 65, 63, 62],
        "Clara": [95, 98, 94, 98]
    }
    
averages = process_scores(students)
classified = classify_grades(averages)
generate_report(classified)