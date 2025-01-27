import sys,os,tabulate,csv

Times_List = [] # list of tuples to store the data from the file
Drivers_Info = [] # list of tuples to store the driver info from the file

def main():
    if len(sys.argv) < 2: # makes sure that the user provides a file name as an argument
        print("Please provide a file name as an argument")
        sys.exit(1)
    filein = sys.argv[1]

    if not os.path.exists(filein): # checks if the file exists
        print(f"Error: File '{filein}' not found")
        sys.exit(1)

    with open(filein) as f: # opens the lap times file 
        Race_Location = f.readline().strip() # takes the name of the location from the file then proceeds
        for line in f:
            driver = line[:3]
            time = float(line[3:])
            Times_List.append((driver, time))
    Times_List.sort(key=lambda x: x[1])  # sorts the list by the time field in ascending order

    with open("f1_drivers.txt") as f:  # opens the driver info file and stores the data in a list of tuples
        reader = csv.reader(f)
        for row in reader:
            Driver_Number = row[0]
            Driver_Tag = row[1]
            Driver_Name = row[2]
            Drivers_Team = row[3]
            Drivers_Info.append((Driver_Tag, Driver_Number, Driver_Name, Drivers_Team))

    #-------PASS CRITERIA-------#
    print(f"Racetrack: {Race_Location}")

    print(f"The Fastest time was: {Times_List[0][1]} by driver {Times_List[0][0]}")

    #-------IMPROVE CRITERIA-------#
    Times_List.sort(key=lambda x: x[0]) # Sorts by the driver tag
    Driver_Race_Times = {}  # dictionary to store all the times for each driver
    for driver, time in Times_List:
        if driver not in Driver_Race_Times:
            Driver_Race_Times[driver] = []
        Driver_Race_Times[driver].append(time)

    Complete_Times = []  # stores the driver tag, fastest time and their average time
    # Calculate the fastest time and average time for each driver and store in Complete_Times
    for driver in Driver_Race_Times:
        fastest_time = min(Driver_Race_Times[driver])
        average_time = sum(Driver_Race_Times[driver]) / len(Driver_Race_Times[driver])
        Complete_Times.append((driver, fastest_time, average_time))

    print(tabulate.tabulate(Complete_Times, headers=["Driver", "Fastest Time", "Average Time"], tablefmt="fancy_grid"))

    total_time = sum(time[1] for time in Times_List)
    average_time = total_time / len(Times_List)

    print(f"The average time for all racers was {average_time}")

    #-------TOP MARKS CRITERIA-------#
    Full_List = []  # stores the driver tag and their time
    for driver, time in Times_List:
        for driver_info in Drivers_Info:
            if driver == driver_info[0]:
                Full_List.append((driver_info[2], driver_info[3], time))
    Full_List.sort(key=lambda x: x[2])  # sorts by the time field in descending order
    print(tabulate.tabulate(Full_List, headers=["Driver", "Time"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()