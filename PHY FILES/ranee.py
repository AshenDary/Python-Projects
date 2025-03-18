import tkinter as tk
from tkinter import ttk, messagebox
import time

lrt1_stations = ["Baclaran", "EDSA", "Libertad", "Gil Puyat", "Vito Cruz", "Quirino", "Pedro Gil",
                "UN Avenue", "Central Terminal", "Carriedo", "Doroteo Jose", "Bambang", 
                "Tayuman", "Blumentritt", "Abad Santos", "R. Papa", "5th Avenue", 
                "Monumento", "Balintawak", "Roosevelt"]


lrt2_stations = ["Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore", "Betty Go-Belmonte", 
                "Araneta Center-Cubao", "Anonas", "Katipunan", "Santolan", "Marikina-Pasig", "Antipolo"]


mrt3_stations = ["North Avenue", "Quezon Avenue", "GMA Kamuning", "Araneta Center Cubao",
                 "Santolan-Annapolis", "Ortigas", "Shaw Boulevard", "Boni", "Guadalupe",
                 "Buendia", "Ayala", "Magallanes", "Taft Avenue"]

# Transfer stations
transfer_stations = {
    ("LRT 1", "Doroteo Jose"): ("LRT 2", "Recto"),
    ("LRT 2", "Recto"): ("LRT 1", "Doroteo Jose"),
    ("LRT 2", "Araneta Center-Cubao"): ("MRT 3", "Araneta Center Cubao"),
    ("MRT 3", "Araneta Center Cubao"): ("LRT 2", "Araneta Center-Cubao"),
    ("MRT 3", "Taft Avenue"): ("LRT 1", "EDSA"),
    ("LRT 1", "EDSA"): ("MRT 3", "Taft Avenue")
}

# Fare Matrix
lrt1_beep_card = [
    [13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 23, 24, 25, 26, 27, 28, 29, 30, 33, 35],
    [14, 13, 15, 15, 17, 18, 19, 20, 21, 22, 23, 24, 24, 25, 26, 27, 28, 29, 32, 34],
    [15, 15, 13, 14, 15, 16, 17, 18, 20, 21, 22, 22, 23, 24, 25, 26, 27, 28, 31, 33],
    [16, 15, 14, 13, 15, 16, 17, 17, 19, 20, 21, 21, 22, 23, 24, 25, 26, 27, 30, 32],
    [17, 17, 15, 15, 13, 14, 15, 16, 18, 19, 19, 20, 21, 22, 23, 24, 25, 26, 29, 31],
    [18, 18, 16, 16, 14, 13, 14, 15, 17, 18, 18, 19, 20, 21, 22, 23, 24, 25, 28, 30],
    [19, 19, 17, 17, 15, 14, 13, 14, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 27, 29],
    [20, 20, 18, 17, 16, 15, 14, 13, 15, 16, 16, 17, 18, 19, 20, 21, 22, 23, 26, 28],
    [22, 21, 20, 19, 18, 17, 16, 15, 13, 14, 15, 16, 17, 17, 18, 19, 20, 22, 24, 27],
    [23, 22, 21, 20, 19, 18, 17, 16, 14, 13, 14, 15, 16, 16, 18, 18, 20, 21, 24, 26],
    [23, 23, 22, 21, 19, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 19, 20, 23, 25],
    [24, 24, 22, 21, 20, 19 ,18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 19, 22, 24],
    [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 21, 23],
    [26, 25, 24, 23, 22, 21, 20, 19, 17, 16, 16, 15, 14, 13, 14, 15, 16, 18, 20, 23],
    [27, 26, 25, 24, 23, 22, 21, 20, 18, 18, 17, 16, 15, 14, 13, 14, 15, 17, 19, 22],
    [28, 27, 26, 25, 24, 23, 22, 21, 19, 18, 18, 17, 16, 15, 14, 13, 14, 16, 18, 21],
    [29, 28, 27, 26, 25, 24, 23, 22, 20, 20, 19, 18, 17, 16, 15, 14, 13, 15, 17, 20],
    [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 18, 17, 16, 15, 13, 16, 18],
    [33, 32, 31, 30, 29, 28, 27, 26, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16, 13, 16],
    [35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 23, 22, 21, 20, 18, 16, 13]
]

lrt1_sjt = [
    [0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 35, 35],
    [15, 0, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 30, 35, 35],
    [15, 15, 0, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 35, 35],
    [20, 15, 15, 0, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 35],
    [20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 35],
    [20, 20, 20, 20, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30],
    [20, 20, 20, 20, 15, 15, 0, 15, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 30, 30],
    [20, 20, 20, 20, 20, 15, 15, 0, 15, 20, 20, 20, 20, 20, 20, 25, 25, 25, 30, 30],
    [25, 25, 20, 20, 20, 20, 20, 15, 0, 15, 15, 20, 20, 20, 20, 20, 20, 25, 25, 30],
    [25, 25, 25, 20, 20, 20, 20, 20, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 30],
    [25, 25, 25, 25, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25],
    [25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 20, 25, 25],
    [25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 25, 25],
    [30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 25],
    [30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 25],
    [30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 20, 20, 25],
    [30, 30, 30, 30, 25, 25, 25, 25, 20, 20, 20, 20, 20, 20, 15, 15, 0, 15, 20, 20],
    [30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 20, 15, 0, 20, 20],
    [35, 35, 35, 30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 0, 20],
    [35, 35, 35, 35, 35, 30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 25, 20, 20, 20, 0]
]

lrt2_beep_card = [
    [13, 15, 16, 18, 19, 21, 22, 23, 25, 26, 28, 31, 33],
    [15, 13, 15, 17, 18, 19, 21, 22, 24, 25, 27, 29, 32],
    [16, 15, 13, 15, 16, 18, 19, 20, 22, 23, 26, 28, 30],
    [18, 17, 15, 13, 15, 16, 17, 19, 20, 22, 24, 26, 29],
    [19, 18, 16, 15, 13, 14, 16, 17, 19, 20, 22, 24, 27],
    [21, 19, 18, 16, 14, 13, 15, 16, 18, 19, 21, 23, 26],
    [22, 21, 19, 17, 16, 15, 13, 15, 16, 18, 20, 22, 25],
    [23, 22, 20, 19, 17, 16, 15, 13, 15, 16, 19, 21, 23],
    [25, 24, 22, 20, 19, 18, 16, 15, 13, 14, 17, 19, 22],
    [26, 25, 23, 22, 20, 19, 18, 16, 14, 13, 16, 18, 21],
    [28, 27, 26, 24, 22, 21, 20, 19, 17, 16, 13, 15, 18],
    [31, 29, 28, 26, 24, 23, 22, 21, 19, 18, 15, 13, 16],
    [33, 32, 30, 29, 27, 26, 25, 23, 22, 21, 18, 16, 13]
]

lrt2_sjt = [
    [0, 15, 20, 20, 20, 25, 25, 25, 25, 30, 30, 35, 35],
    [15, 0, 15, 20, 20, 20, 25, 25, 25, 25, 30, 30, 35],
    [20, 15, 0, 15, 20, 20, 20, 20, 25, 25, 30, 30, 30],
    [20, 20, 15, 0, 15, 20, 20, 20, 20, 25, 25, 30, 30],
    [20, 20, 20, 15, 0, 15, 20, 20, 20, 20, 25, 25, 30],
    [25, 20, 20, 20, 15, 0, 15, 20, 20, 20, 25, 25, 30],
    [25, 25, 20, 20, 20, 15, 0, 15, 20, 20, 20, 25, 25],
    [25, 25, 20, 20, 20, 20, 15, 0, 15, 20, 20, 25, 25],
    [25, 25, 25, 20, 20, 20, 20, 15, 0, 15, 20, 20, 25],
    [30, 25, 25, 25, 20, 20, 20, 20, 15, 0, 20, 20, 25],
    [30, 30, 30, 25, 25, 25, 20, 20, 20, 20, 0, 15, 20],
    [35, 30, 30, 30, 25, 25, 25, 25, 20, 20, 15, 0, 20],
    [35, 35, 30, 30, 30, 30, 25, 25, 25, 25, 20, 20, 0]
]

mrt3_fares = [
    [0, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24, 28, 28],
    [13, 0, 13, 13, 13, 16, 20, 20, 20, 24, 24, 24, 28],
    [13, 13, 0, 13, 13, 16, 16, 20, 20, 20, 24, 24, 28],
    [16, 13, 13, 0, 13, 16, 16, 20, 20, 20, 24, 24, 24],
    [16, 16, 13, 13, 0, 13, 16, 16, 20, 20, 20, 24, 24],
    [20, 16, 16, 16, 13, 0, 13, 13, 16, 16, 20, 24, 24],
    [20, 20, 16, 16, 16, 13, 0, 13, 13, 16, 16, 20, 24],
    [20, 20, 20, 16, 16, 13, 13, 0, 13, 13, 16, 16, 20],
    [24, 20, 20, 20, 16, 16, 13, 13, 0, 13, 13, 16, 16],
    [24, 24, 20, 20, 20, 16, 16, 13, 13, 0, 13, 13, 16],
    [24, 24, 24, 24, 20, 20, 16, 16, 13, 13, 0, 13, 13],
    [28, 24, 24, 24, 24, 20, 20, 16, 16, 13, 13, 0, 13],
    [28, 28, 28, 24, 24, 24, 24, 20, 16, 16, 13, 13, 0]
]

lrt1_distances = [
    0.0, 0.59, 1.01, 0.73, 1.06, 0.83, 0.79, 0.75, 1.21, 0.73, 
    0.69, 0.65, 0.62, 0.67, 0.93, 0.66, 0.95, 1.09, 2.25, 1.87
]
lrt2_distances = [
    0.0, 1.05, 1.389, 1.357, 1.234, 0.928, 1.075, 1.164, 1.438, 0.955, 
    1.97, 0.9, 0.7
]
mrt3_distances = [
    0.0, 1.7, 1.3, 1.8, 1.5, 1.6, 1.3, 1.4, 1.7, 2.2, 1.0, 1.2, 1.4
]

# Fine settings
fine_amount = 30.00
fine_interval = 5  # Fine every 5 seconds delay

# Initialize GUI
root = tk.Tk()
root.title("LRT Fare Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Global variables to manage balance and fare state
initial_balance = 1000
current_balance = initial_balance
selected_line = None
stations = []
fare_matrix = None
distance_matrix = None
start_time = None
fine_applied = False
timer_paused = False
accumulated_fines = 0  # Track total fines across all trips
total_distance = 0.0  # Total distance traveled in kilometers
total_stations_passed = 0  # Total number of stations passed
last_fine_time = None
station_error_active = False
timer_stopped = False  # New variable to track if timer should be stopped
timer_running = False
timer_id = None


is_locked = {"card_type": False, "line": False, "start_station": False, "passenger_type": False, "end_station": False}

# GUI Elements
tk.Label(root, text="Select Card Type:").grid(row=0, column=0, padx=10, pady=5)
card_type_selector = ttk.Combobox(root, values=["Beep Card", "Single Journey Ticket"], state="readonly")
card_type_selector.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Select Line:").grid(row=1, column=0, padx=10, pady=5)
line_selector = ttk.Combobox(root, values=["LRT 1", "LRT 2", "MRT 3"], state="readonly")
line_selector.grid(row=1, column=1, padx=10, pady=5)
line_selector.bind("<<ComboboxSelected>>", lambda event: update_stations())

tk.Label(root, text="Select Passenger Type:").grid(row=2, column=0, padx=10, pady=5)
passenger_type_selector = ttk.Combobox(root, values=["Regular", "Student", "PWD/Senior"], state="readonly")
passenger_type_selector.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Select Starting Station:").grid(row=3, column=0, padx=10, pady=5)
start_station = ttk.Combobox(root, values=stations, state="readonly")
start_station.grid(row=3, column=1, padx=10, pady=5)
start_station.bind("<<ComboboxSelected>>", lambda event: lock_required_fields())

tk.Label(root, text="Select Destination Station:").grid(row=4, column=0, padx=10, pady=5)
end_station = ttk.Combobox(root, values=stations, state="readonly")
end_station.grid(row=4, column=1, padx=10, pady=5)
end_station.bind("<<ComboboxSelected>>", lambda event: None)  # Remove pause_timer call here

# LabelFrame for timer and fines labels, creating a bordered box
info_frame = tk.LabelFrame(root, text="Information", padx=10, pady=5)
info_frame.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
warning_label = tk.Label(info_frame, text="", fg="red")
warning_label.pack(side="top", pady=(0, 10))  # Place it at the top with a small padding below

# Timer label inside the frame
timer_label = tk.Label(info_frame, text="Timer: 0.00s")
timer_label.pack(side="left", padx=(0, 20))  # Add small space to the right

# Total fines label inside the frame
total_fines_label = tk.Label(info_frame, text="Total fines: ₱0.00", fg="red")
total_fines_label.pack(side="left")


# LabelFrame for Fare with Discount, creating a bordered box
fare_discount_frame = tk.LabelFrame(root, text="Fare with Discount", padx=10, pady=5)
fare_discount_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Fare with discount label inside the fare discount frame
fare_with_discount_label = tk.Label(fare_discount_frame, text="Fare w/ discount:")
fare_with_discount_label.pack(side="left", padx=5)


# Travel Data Section
# LabelFrame for Travel Data section, creating a bordered box
travel_data_frame = tk.LabelFrame(root, text="Travel Data", padx=10, pady=5)
travel_data_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

# Total fare label inside the travel data frame
total_fare_label = tk.Label(travel_data_frame, text="Total fare of all travels (including fines):")
total_fare_label.grid(row=0, column=0, sticky="w")

# Total distance traveled label inside the travel data frame
distance_label = tk.Label(travel_data_frame, text="Total distance traveled: 0.00 km")
distance_label.grid(row=1, column=0, sticky="w")

# Total stations passed label inside the travel data frame
stations_passed_label = tk.Label(travel_data_frame, text="Total stations passed: 0")
stations_passed_label.grid(row=2, column=0, sticky="w")

# Balance label inside the travel data frame
balance_label = tk.Label(travel_data_frame, text=f"Balance: PHP {current_balance:.2f}")
balance_label.grid(row=3, column=0, sticky="w")


reset_program_btn = tk.Button(root, text="Reset Program", command=lambda: reset_program())
reset_program_btn.grid(row=13, column=1, columnspan=1, pady=10)

# Transfer Buttons (Initially hidden)
# Place transfer buttons frame at a dedicated position, above the fare section
transfer_frame = tk.Frame(root)
transfer_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Transfer buttons within the frame
transfer_yes_btn = tk.Button(transfer_frame, text="Yes, Transfer", command=lambda: handle_transfer(True))
transfer_continue_btn = tk.Button(transfer_frame, text="Continue on this Line", command=lambda: handle_transfer(False))
transfer_yes_btn.grid(row=0, column=0, padx=5)
transfer_continue_btn.grid(row=0, column=1, padx=5)

# Hide the transfer buttons initially
transfer_yes_btn.grid_remove()
transfer_continue_btn.grid_remove()
# Functions 

# Function to show transfer buttons if transfer is available
def show_transfer_buttons():
    transfer_yes_btn.grid()  # Show "Yes, Transfer" button
    transfer_continue_btn.grid()  # Show "Continue on this Line" button

# Function to hide transfer buttons
def hide_transfer_buttons():
    transfer_yes_btn.grid_remove()
    transfer_continue_btn.grid_remove()

# Transfer handling function

def handle_transfer(transfer):
    """Handle user's choice to transfer or continue riding on the current line."""
    if transfer:
        # Get the current line and selected end station
        current_line = line_selector.get()
        end_station_name = end_station.get()
        transfer_key = (current_line, end_station_name)

        # Check if a valid transfer is available
        if transfer_key in transfer_stations:
            # Retrieve the new line and transfer station from the dictionary
            new_line, transfer_station = transfer_stations[transfer_key]
            line_selector.set(new_line)  # Set the new line
            update_stations()  # Refresh station list for the new line
            start_station.set(transfer_station)  # Set start station to transfer station on new line
            end_station.set('')  # Clear end station to prompt for new destination
        else:
            messagebox.showerror("Transfer Error", "Transfer station not available.")
    # Hide transfer buttons after handling
    hide_transfer_buttons()

# LabelFrame for Fare with Discount, creating a bordered box
fare_discount_frame = tk.LabelFrame(root, text="Fare with Discount", padx=10, pady=5)
fare_discount_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Fare with discount label inside the fare discount frame
fare_with_discount_label = tk.Label(fare_discount_frame, text="Fare w/ discount:")
fare_with_discount_label.pack(side="left", padx=5)

# Frame for Transfer Buttons (Initially hidden)
# Place transfer buttons frame at a dedicated position, below the fare section
transfer_frame = tk.Frame(root, padx=10, pady=20)  # Add padding to avoid overlap
transfer_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

transfer_yes_btn = tk.Button(transfer_frame, text="Yes, Transfer", command=lambda: handle_transfer(True))
transfer_continue_btn = tk.Button(transfer_frame, text="Continue on this Line", command=lambda: handle_transfer(False))
transfer_yes_btn.grid(row=0, column=0, padx=5)
transfer_continue_btn.grid(row=0, column=1, padx=5)

# Initially hide the transfer buttons
hide_transfer_buttons()

def update_stations():
    """Update stations and fare matrix based on selected line and card type."""
    global selected_line, stations, fare_matrix, distance_matrix
    selected_line = line_selector.get()
    card_type = card_type_selector.get()

    if selected_line == "LRT 1":
        stations = lrt1_stations
        fare_matrix = lrt1_beep_card if card_type == "Beep Card" else lrt1_sjt
        distance_matrix = lrt1_distances
    elif selected_line == "LRT 2":
        stations = lrt2_stations
        fare_matrix = lrt2_beep_card if card_type == "Beep Card" else lrt2_sjt
        distance_matrix = lrt2_distances
    elif selected_line == "MRT 3":
        stations = mrt3_stations
        fare_matrix = mrt3_fares
        distance_matrix = mrt3_distances
    else:
        stations = []
        fare_matrix = None
        distance_matrix = None

    start_station['values'] = stations
    end_station['values'] = stations
    start_station.set('')
    end_station.set('')

def calculate_distance(start_index, end_index, distances):
    if start_index < end_index:
        return sum(distances[start_index:end_index])
    else:
        return sum(distances[end_index:start_index])

def calculate_stations_passed(start_index, end_index):
    return abs(end_index - start_index)

def start_timer():
    """Initialize the timer for calculating fines and warnings."""
    global start_time, fine_applied, timer_paused
    fine_applied = False
    timer_paused = False
    start_time = time.time()
    update_timer_display()

def stop_timer():
    global timer_running
    timer_running = False
    if timer_id:
        root.after_cancel(timer_id)

def lock_required_fields():
    """Lock fields and start the timer after setting the start station."""
    if start_station.get():
        for field in ["card_type", "line", "start_station", "passenger_type"]:
            lock_field(field)
        start_timer()

def lock_field(field_name):
    """Lock specified field."""
    if not is_locked[field_name]:
        is_locked[field_name] = True
        if field_name == "card_type":
            card_type_selector.config(state="disabled")
        elif field_name == "line":
            line_selector.config(state="disabled")
        elif field_name == "start_station":
            start_station.config(state="disabled")
        elif field_name == "passenger_type":
            passenger_type_selector.config(state="disabled")
        elif field_name == "end_station":
            end_station.config(state="disabled")

def pause_timer():
    """Pause the timer when a valid destination station is selected."""
    global timer_paused
    # Only pause if a start and valid end station are set, and they are different
    if start_station.get() and end_station.get() and start_station.get() != end_station.get():
        timer_paused = True
    else:
        timer_paused = False  # Keep timer active if conditions are not met


def reset_program():
    """Reset all selections and calculations."""
    global current_balance, fine_applied, start_time, accumulated_fines, total_distance, total_stations_passed, is_locked, timer_paused
    current_balance = initial_balance
    fine_applied = False
    accumulated_fines = 0
    total_distance = 0.0
    total_stations_passed = 0
    start_time = None
    timer_paused = False

    # Reset all fields and clear displays
    for widget, config in [(line_selector, 'readonly'), (card_type_selector, 'readonly'),
                           (passenger_type_selector, 'readonly'), (start_station, 'readonly'), (end_station, 'readonly')]:
        widget.set('')
        widget.config(state=config)

    timer_label.config(text="Timer: 0.00s")
    total_fines_label.config(text="Total fines: ₱0.00")
    fare_with_discount_label.config(text="Fare w/ discount:")
    total_fare_label.config(text="Total fare of all travels (including fines):")
    distance_label.config(text="Total distance traveled: 0.00 km")
    stations_passed_label.config(text="Total stations passed: 0")
    balance_label.config(text=f"Balance: PHP {initial_balance:.2f}")
    calculate_btn.config(state="normal")

    # Reset field lock statuses
    for key in is_locked:
        is_locked[key] = False


def apply_fine():
    """Apply a fine and update relevant labels and balance."""
    global current_balance, accumulated_fines, timer_stopped
    if current_balance >= fine_amount:
        current_balance -= fine_amount
        accumulated_fines += fine_amount
        total_fines_label.config(text=f"Total fines: ₱{accumulated_fines:.2f}")
        balance_label.config(text=f"Balance: PHP {current_balance:.2f}")
    else:
        # Stop the timer if balance is insufficient for further fines
        timer_stopped = True  # Set timer_stopped to True to stop the timer updates
        lock_all_selections()
        calculate_btn.config(state="disabled")  # Disable Calculate button
        total_fines_label.config(text="Insufficient balance for fine.")

def update_timer_display():
    """Update the timer display and alternate between fine and warning messages."""
    global start_time, fine_applied, accumulated_fines, timer_paused, last_fine_time, timer_stopped

    # Stop timer updates if timer_stopped is True
    if timer_stopped:
        return  # Exit the function if the timer is stopped due to insufficient balance

    # Continue updating the timer even if balance is insufficient or inputs are locked
    if start_time:
        elapsed = time.time() - start_time
        remaining_time = fine_interval - (elapsed % fine_interval)
        timer_label.config(text=f"Timer: {remaining_time:.2f}s")

        # Show a persistent warning message unless a fine has just been applied
        if not fine_applied:
            warning_label.config(text="Warning! A fine will be applied every delay.")

        # Apply fine every 5 seconds as needed
        if int(elapsed) >= fine_interval and (last_fine_time is None or elapsed - last_fine_time >= fine_interval):
            apply_fine()
            fine_applied = True
            last_fine_time = elapsed  # Update last fine time
            warning_label.config(text="A fine of PHP 30.00 applied due to delay.")

            # Schedule the warning to reappear after 1 second
            root.after(1000, lambda: warning_label.config(text="Warning! A fine will be applied every delay."))

        # Reset fine_applied to allow a new fine in the next interval
        elif int(elapsed) % fine_interval != 0:
            fine_applied = False

        # Schedule the next timer update
        root.after(100, update_timer_display)


def lock_all_selections():
    """Locks all selectors and only enables the reset button."""
    for field_name in ["card_type", "line", "start_station", "passenger_type", "end_station"]:
        lock_field(field_name)
    reset_program_btn.config(state="normal")  # Enable reset button
    calculate_btn.config(state="disabled")  # Disable Calculate button

# Define continue_riding_label
continue_riding_label = tk.Label(root, text="")
continue_riding_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

def hide_continue_buttons():
    yes_button.grid_remove()
    no_button.grid_remove()

def continue_ride():
    """Enable selection of a new destination after selecting 'Yes' to continue riding."""
    global ride_continuing
    ride_continuing = True
    end_station.set('')  # Clear end station for a new selection
    continue_riding_label.config(text="")  # Hide continue riding message
    hide_continue_buttons()

def end_ride():
    """End ride and display final travel data."""
    continue_riding_label.config(text="Final Travel Data:")
    # Display final travel data in the label
    fare_with_discount_label.config(text=f"Total fare w/ discount: PHP {accumulated_fines:.2f}")
    total_fare_label.config(text=f"Total fare of all travels: PHP {accumulated_fines:.2f}")
    distance_label.config(text=f"Total distance traveled: {total_distance:.2f} km")
    stations_passed_label.config(text=f"Total stations passed: {total_stations_passed}")
    hide_continue_buttons()
    lock_all_selections()
    stop_timer()

# Define yes_button and no_button for the continue ride prompt
yes_button = tk.Button(root, text="Yes", command=continue_ride)
no_button = tk.Button(root, text="No", command=end_ride)
yes_button.grid(row=10, column=0, padx=5)
no_button.grid(row=10, column=1, padx=5)

# Initially hide the continue buttons
hide_continue_buttons()

def calculate_fare():
    """Calculate fare including transfer options, discount handling, and balance checks."""
    global total_distance, total_stations_passed, current_balance, accumulated_fines, timer_paused, station_error_active
    stop_timer()
    # Check that both start and end stations are selected
    if not start_station.get() or not end_station.get():
        return  # Wait until both stations are selected

    # Handle invalid same station selection
    if start_station.get() == end_station.get():
        station_error_active = True
        messagebox.showerror("Input Error", "Starting and destination stations cannot be the same.")
        end_station.set('')  # Clear end station
        start_timer()  # Restart the timer to continue counting
        return
    else:
        station_error_active = False  # Clear error flag if stations are valid

    # Detect if the end station is a transfer point
    current_line = line_selector.get()
    end_station_name = end_station.get()
    transfer_key = (current_line, end_station_name)

    # Check if end station qualifies as a transfer station
    if transfer_key in transfer_stations:
        # Prompt user with transfer options
        show_transfer_buttons()
        return  # Exit early to await user's transfer decision

    # Calculate fare and display data
    start_index = stations.index(start_station.get())
    end_index = stations.index(end_station_name)
    segment_fare = fare_matrix[start_index][end_index]

    # Apply discount based on passenger type
    passenger_type = passenger_type_selector.get()
    discount = 0.2 if passenger_type == "Student" else 0.3 if passenger_type == "PWD/Senior" else 0
    segment_fare *= (1 - discount)

    # Calculate total fare with fines
    total_fare = segment_fare + accumulated_fines

    #distance
    if current_line == "LRT 1":
        segment_distance = calculate_distance(start_index, end_index, lrt1_distances)
    elif current_line == "LRT 2":
        segment_distance = calculate_distance(start_index, end_index, lrt2_distances)
    elif current_line == "MRT 3":
        segment_distance = calculate_distance(start_index, end_index, mrt3_distances)
    total_distance += segment_distance

    segment_stations_passed = calculate_stations_passed(start_index, end_index)
    total_stations_passed += segment_stations_passed

    # Display travel data
    fare_with_discount_label.config(text=f"Fare w/ discount: PHP {segment_fare:.2f}")
    total_fare_label.config(text=f"Total fare of all travels (including fines): PHP {total_fare:.2f}")

    # Check balance for Beep Card or notify for Single Journey Ticket
    card_type = card_type_selector.get()
    if card_type == "Beep Card":
        if current_balance >= total_fare:
            current_balance -= total_fare
            balance_label.config(text=f"Balance: PHP {current_balance:.2f}")
            start_timer()  # Reset the timer for the next trip
        else:
            # Lock all selections if balance is insufficient
            messagebox.showerror("Insufficient Balance", "Not enough balance for fare. Please reset the program.")
            lock_all_selections()
            calculate_btn.config(state="disabled")  # Disable Calculate button
            return
    else:  # Single Journey Ticket
        if total_fare > segment_fare:
            messagebox.showinfo("Additional Payment Required", "Additional payment is required due to extra time spent.")
        start_timer()  # Reset the timer for the next trip

    # Prepare for the next segment
    start_station.set(end_station.get())
    end_station.set('')  # Reset end station
    hide_transfer_buttons()  # Hide transfer buttons if transfer is not needed

    # Prompt user to continue or stop the ride
    if messagebox.askyesno("Continue Ride", "Do you want to continue riding?"):
        continue_ride()  # Set start station to previous end station and clear end station
    else:
        end_ride()  # End the ride and display final travel data

# Bind Calculate button
calculate_btn = tk.Button(root, text="Calculate Fare", command=calculate_fare)
calculate_btn.grid(row=13, column=0, columnspan=1, pady=10)

# Run GUI
root.mainloop()