import random
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpVariableBinary, LpStatus, value

# Sample data
employees = ["Manager_431", "AsstManager_876", "Employee_765", "Employee_654", "Employee_273"]
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
min_hours_per_shift = 3
max_hours_per_shift = 9
hours_per_week = {"Manager_431": 40, "AsstManager_876": 40, "Employee_765": 20, "Employee_654": 30, "Employee_273": 35}

# Create a list of tuples representing all possible shifts
shifts = [(emp, day) for emp in employees for day in days_of_week]

# Create a binary variable for each shift
shift_assignments = LpVariable.dicts("ShiftAssignment", shifts, 0, 1, LpVariableBinary)

# Create the LP problem
model = LpProblem("ShiftAssignmentProblem", LpMinimize)

# Objective function: minimize the total difference in assigned shifts
model += lpSum([shift_assignments[emp, day] for emp, day in shifts]), "TotalDifference"

# Constraints
for emp in employees:
    # Weekly hours constraint
    model += lpSum([shift_assignments[emp, day] * random.randint(min_hours_per_shift, max_hours_per_shift) for day in days_of_week]) == hours_per_week[emp]

# Solve the problem
model.solve()

# Check the status of the solution
if LpStatus[model.status] == "Optimal":
    # Print the results
    for emp, day in shifts:
        if value(shift_assignments[emp, day]) == 1:
            print(f"{emp} assigned to {day} for {random.randint(min_hours_per_shift, max_hours_per_shift)} hours")
else:
    print("No optimal solution found. Check your constraints.")