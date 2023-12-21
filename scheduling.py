import pandas as pd
from ortools.sat.python import cp_model
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle

def format_shift_time(shift_start, shift_end):
    start_time = datetime.strptime(str(shift_start), "%H%M").strftime("%I:%M %p")
    end_time = datetime.strptime(str(shift_end), "%H%M").strftime("%I:%M %p")
    return f"{start_time} - {end_time}"

def create_shift_scheduling_model():
    # Constants
    NUM_EMPLOYEES = 5

    # Shift times in minutes (converted to HHMM format for readability)
    SHIFT_TYPES = {
        "morning": (700, 1700, 45),   # 7:00 AM - 5:00 PM with 45 minutes break
        "afternoon": (1130, 1500, 0), # 11:30 AM - 3:00 PM with no break
        "evening": (1700, 2130, 0)    # 5:00 PM - 9:30 PM with no break
    }

    # Dates from January 1 to January 7
    start_date = datetime(2024, 1, 1)
    DAYS = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]

    # Model
    model = cp_model.CpModel()

    # Variables
    shifts = {(e, d, s): model.NewBoolVar(f'shift_e{e}d{d}s{s}')
              for e in range(NUM_EMPLOYEES)
              for d in DAYS
              for s in SHIFT_TYPES}

    # Constraints
    for d in DAYS:
        for s in SHIFT_TYPES:
            model.Add(sum(shifts[e, d, s] for e in range(NUM_EMPLOYEES)) == 1)

    for e in range(NUM_EMPLOYEES):
        for d in DAYS:
            model.Add(sum(shifts[e, d, s] for s in SHIFT_TYPES) <= 1)

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Creating a DataFrame for the schedule
    schedule_data = []
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for e in range(NUM_EMPLOYEES):
            for d in DAYS:
                day_of_week = datetime.strptime(d, '%Y-%m-%d').strftime('%A')
                for s in SHIFT_TYPES:
                    if solver.BooleanValue(shifts[(e, d, s)]):
                        shift_time = format_shift_time(SHIFT_TYPES[s][0], SHIFT_TYPES[s][1])
                        schedule_data.append({
                            'Date': d,
                            'Day': day_of_week,
                            'Employee': f'Employee {e + 1}',
                            'Shift Time': shift_time
                        })
    else:
        print("No feasible solution found.")

    schedule_df = pd.DataFrame(schedule_data)
    return schedule_df

# Run the model and print the schedule
schedule_df = create_shift_scheduling_model()
print(schedule_df)

def visualize_schedule(schedule_df):
    # Convert strings to datetime
    schedule_df['Start'] = pd.to_datetime(schedule_df['Date'] + ' ' + schedule_df['Shift Time'].str.split(' - ').str[0])
    schedule_df['End'] = pd.to_datetime(schedule_df['Date'] + ' ' + schedule_df['Shift Time'].str.split(' - ').str[1])

    # Create figure and plot space
    plt.figure(figsize=(15, 8))

    # Colors for different employees
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']

    for i, employee in enumerate(schedule_df['Employee'].unique()):
        employee_schedule = schedule_df[schedule_df['Employee'] == employee]
        for _, row in employee_schedule.iterrows():
            plt.plot([row['Start'], row['End']], [i, i], color=colors[i], linewidth=6, solid_capstyle='butt')

    # Formatting
    plt.yticks(range(len(schedule_df['Employee'].unique())), schedule_df['Employee'].unique())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()  # Rotate date labels
    plt.xlabel('Date and Time')
    plt.ylabel('Employee')
    plt.title('Employee Shift Schedule')
    plt.grid(True)
    plt.show()

# Visualize the schedule
visualize_schedule(schedule_df)
