x = str(input("Enter the type of vehicles:"))
if(x==bus):
    bus_fare = 100 * time
    print("Enter the parking time: ",time)
    print("Parking Amount:",bus_fare)
elif(x==car):
    car_fare = 50 * time
    print("Enter the parking time:",time)
    print("Parking Amount:",car_fare)
elif(x==motorcycle):
    motor_fare = 20 * time
    print("Enter the parking time:",time)
    print("Parking Amount:",motor_fare)
else:
        print("Invalid Input")