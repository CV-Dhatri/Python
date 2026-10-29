# *Hospital Bill* 
# def hospital_bill(patient_name, disease, days=1, *tests, **details): 
# Requirements 
# Print patient details. 
# Print all medical tests. 
# Print doctor name and room type. 
# Calculate room charges. 
# Add test charges. 
# Print final hospital bill.

def hospital_bill(patient_name, disease, days=1, *tests, **details):
    print(f"Patient Name: {patient_name}")
    print(f"Disease: {disease}")
    print(f"Number of Days Admitted: {days}")

    if tests:
        print("Medical Tests:")
        for test in tests:
            print(f"- {test}")
    else:
        print("No medical tests conducted.")

    doctor_name = details.get('doctor_name', 'Not specified')
    room_type = details.get('room_type', 'Not specified')
    print(f"Doctor Name: {doctor_name}")
    print(f"Room Type: {room_type}")

    room_charges_per_day = 2000
    room_charges = days * room_charges_per_day
    test_charges = sum(details.get('test_charges', {}).get(test, 0) for test in tests)

    final_bill = room_charges + test_charges
    print(f"Room Charges: Rs.{room_charges}")
    print(f"Test Charges: Rs.{test_charges}")
    print(f"Final Hospital Bill: Rs.{final_bill}")