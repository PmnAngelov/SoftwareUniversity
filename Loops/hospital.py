period_of_days = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
for day in range(1, period_of_days + 1):
    if day % 3 == 0 and untreated_patients > treated_patients:
            doctors += 1

    patients_for_the_day = int(input())
    if patients_for_the_day <= doctors:
        treated_patients += patients_for_the_day
    else:
        untreated_patients += patients_for_the_day - doctors
        treated_patients += abs(patients_for_the_day - untreated_patients)


print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")










