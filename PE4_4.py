
grades = []


grades.append(92)
grades.append(51)
grades.append(83)
grades.append(37)
grades.append(72)


print("Current List:", grades)


total = grades[0] + grades[1] + grades[2] + grades[3] + grades[4]


average = total / len(grades)


print(f"Average: {average:.2f}")


grades.remove(51)  
grades.pop(grades.index(37))  


print("Updated list:", grades)


updated_average = sum(grades) / len(grades)
print(f"Updated Average: {updated_average:.3f}")
