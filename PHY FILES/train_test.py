import tkinter as tk
from tkinter import ttk, messagebox
import time

lrt1_single_journey_fares = [
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

lrt1_stored_value_fares = [
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

lrt2_single_journey_fares = [
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

lrt2_stored_value_fares = [
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
    0.59, 1.01, 0.73, 1.06,
    0.83, 0.79, 0.75, 1.21,
    0.73, 0.69, 0.65, 0.62,
    0.67, 0.93, 0.66, 0.95,
    1.09, 2.25, 1.87
]

lrt2_distances = [
    1.11, 1.22, 1.27, 1.04,
    1.21, 1.25, 1.18, 1.25,
    1.10, 1.35, 1.20
]

mrt3_distances = [
    1.7, 1.3, 1.8, 1.5, 1.6,
    1.3, 1.4, 1.7, 2.2, 1.0,
    1.2, 1.4
]

lrt1_stations = [
    "Roosevelt", "Balintawak", "Monumento", "5th Avenue", "R. Papa",
    "Abad Santos", "Blumentritt", "Tayuman", "Bambang", "Doroteo Jose",
    "Carriedo", "Central Terminal", "United Nations", "Pedro Gil",
    "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", "EDSA", "Baclaran"
]

lrt2_stations = [
    "Recto", "Legarda", "Pureza", "V-Mapa", "J-Ruiz","Gilmore", "Betty-Go-Belmonte",
    "Cubao", "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo"
]

mrt3_stations = [
    "North Ave", "Quezon Ave", "GMA Kamuning", "Cubao Araneta",
    "Santolan Annapolis", "Ortigas", "Shaw Blvd", "Boni Ave",
    "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft Ave"
]

def calculate_discounted_fare(fare, discount_type):
    discount = 0
    if discount_type == 'student':
        discount = 0.20
    elif discount_type == 'pwd' or discount_type == 'senior':
        discount = 0.30
    return fare * (1 - discount)

def calculate_fare(start_station, end_station, ticket_type, discount_type=None, line='LRT1'):
    if line == 'LRT1' and start_station in lrt1_stations and end_station in lrt1_stations:
        start_index = lrt1_stations.index(start_station)
        end_index = lrt1_stations.index(end_station)

        if ticket_type == 'single journey':
            fare = lrt1_single_journey_fares[start_index][end_index]
        elif ticket_type == 'beep card':
            fare = lrt1_stored_value_fares[start_index][end_index]
        else:
            return None

    elif line == 'LRT2' and start_station in lrt2_stations and end_station in lrt2_stations:
        start_index = lrt2_stations.index(start_station)
        end_index = lrt2_stations.index(end_station)

        if ticket_type == 'single journey':
            fare = lrt2_single_journey_fares[start_index][end_index]
        elif ticket_type == 'beep card':
            fare = lrt2_stored_value_fares[start_index][end_index]
        else:
            return None

    elif line == 'MRT3' and start_station in mrt3_stations and end_station in mrt3_stations:
        start_index = mrt3_stations.index(start_station)
        end_index = mrt3_stations.index(end_station)

        if ticket_type == 'single journey':
            fare = mrt3_fares[start_index][end_index]
        elif ticket_type == 'beep card':
            fare = mrt3_fares[start_index][end_index]
        else:
            return None

    else:
        return "Invalid station choice, please select valid stations for the chosen line."

    if start_index == end_index:
        return 0.0

    if discount_type:
        fare = calculate_discounted_fare(fare, discount_type)

    return fare

class TrainFareCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("LRT AND MRT STATIONS")
        root.resizable(False, False)
        self.root.geometry("1000x800")
        self.root.config(bg="#2c3e50")
        self.balance = 0
        self.total_fare = 0
        self.total_distance = 0
        self.total_stations_passed = 0
        self.previous_end_station = None
        self.train_line = None
        self.start_time = None
        self.timer_running = False

        self.create_widgets()

    def reset_inputs(self):
        self.card_type_var.set('')
        self.passenger_type_var.set('')
        self.terminal_var.set('')
        self.start_station_var.set('')
        self.end_station_var.set('')
        self.balance = 0
        self.total_fare = 0
        self.total_distance = 0
        self.total_stations_passed = 0
        self.previous_end_station = None
        self.train_line = None
        self.start_time = None
        self.timer_running = False
        self.fine_amount = 0
        self.timer_label.config(text="Time left: 5 seconds")
        self.fine_notification_label.config(text="")
        self.result_label.config(text="")
        self.transfer_prompt_label.config(text="")
        self.transfer_button_frame.pack_forget()

    def create_widgets(self):
        font = ("Lucida Console", 16)
        button_font = ("Lucida Console", 16, "bold")

        main_frame = tk.Frame(self.root, bg="#34495e", bd=5)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        title_label = tk.Label(main_frame, text="𓇼 LRT AND MRT 𓇼", font=("Lucida Console", 24, "bold"), fg="white", bg="#34495e")
        title_label.pack(pady=(0, 20))

        self.card_type_var = tk.StringVar()
        self.passenger_type_var = tk.StringVar()
        self.terminal_var = tk.StringVar()
        self.start_station_var = tk.StringVar()
        self.end_station_var = tk.StringVar()

        card_type_frame = tk.Frame(main_frame, bg="#34495e")
        card_type_frame.pack(pady=5)
        ttk.Label(card_type_frame, text="Select Card Type:", font=font, background="#34495e", foreground="white").pack(side=tk.LEFT, padx=10)
        self.card_type_menu = ttk.Combobox(card_type_frame, textvariable=self.card_type_var, values=["Beep Card", "Single Journey"], font=font)
        self.card_type_menu.pack(side=tk.LEFT, padx=10)
        self.card_type_menu.bind("<<ComboboxSelected>>", self.update_balance)

        passenger_type_frame = tk.Frame(main_frame, bg="#34495e")
        passenger_type_frame.pack(pady=5)
        ttk.Label(passenger_type_frame, text="Select Passenger Type:", font=font, background="#34495e", foreground="white").pack(side=tk.LEFT, padx=10)
        self.passenger_type_menu = ttk.Combobox(passenger_type_frame, textvariable=self.passenger_type_var, values=["Regular", "Student", "PWD", "Senior"], font=font)
        self.passenger_type_menu.pack(side=tk.LEFT, padx=10)

        terminal_frame = tk.Frame(main_frame, bg="#34495e")
        terminal_frame.pack(pady=5)
        ttk.Label(terminal_frame, text="Select Terminal:", font=font, background="#34495e", foreground="white").pack(side=tk.LEFT, padx=10)
        self.terminal_menu = ttk.Combobox(terminal_frame, textvariable=self.terminal_var, values=["LRT1", "LRT2", "MRT3"], font=font)
        self.terminal_menu.pack(side=tk.LEFT, padx=10)
        self.terminal_menu.bind("<<ComboboxSelected>>", self.update_stations)

        start_station_frame = tk.Frame(main_frame, bg="#34495e")
        start_station_frame.pack(pady=5)
        ttk.Label(start_station_frame, text="Select Start Station:", font=font, background="#34495e", foreground="white").pack(side=tk.LEFT, padx=10)
        self.start_station_menu = ttk.Combobox(start_station_frame, textvariable=self.start_station_var, font=font)
        self.start_station_menu.pack(side=tk.LEFT, padx=10)
        self.start_station_menu.bind("<<ComboboxSelected>>", self.track_time)

        end_station_frame = tk.Frame(main_frame, bg="#34495e")
        end_station_frame.pack(pady=5)
        ttk.Label(end_station_frame, text="Select End Station:", font=font, background="#34495e", foreground="white").pack(side=tk.LEFT, padx=10)
        self.end_station_menu = ttk.Combobox(end_station_frame, textvariable=self.end_station_var, font=font)
        self.end_station_menu.pack(side=tk.LEFT, padx=10)

        # Timer Label
        self.timer_label = ttk.Label(main_frame, text="Time left: 5 seconds", font=font, background="#34495e", foreground="white")
        self.timer_label.pack(pady=5)

        # Fine Notification Label
        self.fine_notification_label = ttk.Label(main_frame, text="", foreground="red", font=font, background="#34495e")
        self.fine_notification_label.pack(pady=5)

        # Calculate Fare Button
        self.calculate_button = tk.Button(main_frame, text="Calculate Fare", command=self.calculate_fare_gui, font=button_font, bg="#e74c3c", fg="white")
        self.calculate_button.pack(pady=10)

        # Result and Transfer Prompt
        self.result_label = ttk.Label(main_frame, text="", wraplength=300, font=font, background="#34495e", foreground="white")
        self.result_label.pack(pady=5)

        self.transfer_prompt_label = ttk.Label(main_frame, text="", wraplength=300, font=font, background="#34495e", foreground="white")
        self.transfer_prompt_label.pack(pady=5)

        self.transfer_button_frame = tk.Frame(main_frame, bg="#34495e")
        self.transfer_button_frame.pack(pady=5, fill=tk.X, expand=True)

        self.button_container = tk.Frame(self.transfer_button_frame, bg="#34495e")
        self.button_container.pack(anchor=tk.CENTER)

        self.yes_button = tk.Button(self.button_container, text="Transfer", command=self.switch_lines, font=button_font, bg="#3498db", fg="white")
        self.continue_button = tk.Button(self.button_container, text="Continue", command=self.continue_travel, font=button_font, bg="#3498db", fg="white")
        self.no_button = tk.Button(self.button_container, text="No", command=self.end_travel, font=button_font, bg="#3498db", fg="white")

        self.yes_button.pack(side=tk.LEFT, padx=10, pady=5)
        self.continue_button.pack(side=tk.LEFT, padx=10, pady=5)
        self.no_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.transfer_button_frame.pack_forget()

        # Restart Button
        self.restart_button = tk.Button(main_frame, text="Restart", command=self.reset_inputs, font=button_font, bg="#2ecc71", fg="white")
        self.restart_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    def update_balance(self, event):
        card_type = self.card_type_var.get()
        if card_type == "Beep Card":
            self.balance = 1000
        else:
            self.balance = float('inf')

    def update_stations(self, event):
        terminal = self.terminal_var.get()
        if terminal == "LRT1":
            stations = lrt1_stations
        elif terminal == "LRT2":
            stations = lrt2_stations
        elif terminal == "MRT3":
            stations = mrt3_stations
        else:
            stations = []

        self.start_station_menu['values'] = stations
        self.end_station_menu['values'] = stations

    def track_time(self, event):
        self.start_time = time.time()
        self.timer_running = True
        self.fine_amount = 0
        self.timer_label.config(text="Time left: 5 seconds")
        self.update_timer()

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            time_left = max(0, 5 - int(elapsed_time) % 5)

            new_fine_amount = (int(elapsed_time) // 5) * 30
            if new_fine_amount > self.fine_amount:
                self.fine_amount = new_fine_amount
                self.show_fine_notification()

            if self.fine_amount > self.balance:
                messagebox.showerror("Error", "Your fine exceeds your balance. You cannot continue.")
                return

            self.timer_label.config(text=f"Time left: {time_left} seconds | Fine: ₱{self.fine_amount}")
            self.root.after(1000, self.update_timer)

    def show_fine_notification(self):
        self.fine_notification_label.config(text="You have been just fined!")

    def calculate_fare_gui(self):
        self.timer_running = False
        start_station = self.start_station_var.get()
        end_station = self.end_station_var.get()
        card_type = self.card_type_var.get()
        passenger_type = self.passenger_type_var.get().lower()

        if not start_station or not end_station or not card_type or not passenger_type:
            messagebox.showerror("Error", "Please fill all fields")
            return

        if start_station == end_station:
            messagebox.showerror("Error", "Start and end stations cannot be the same")
            return

        fare = calculate_fare(start_station, end_station, card_type.lower(), passenger_type, self.terminal_var.get())
        if isinstance(fare, str):
            messagebox.showerror("Error", fare)
            return

        self.total_fare += fare
        self.balance -= fare

        if card_type == "Beep Card" and self.balance < 0:
            messagebox.showwarning("Insufficient Balance", "Your balance is insufficient to cover the fare. Additional payment is required for the extra time spent.")
            self.balance += fare
            self.total_fare -= fare
            return

        fine = self.apply_fine(card_type)

        self.result_label.config(text=f"The fare from {start_station} to {end_station} is: ₱{fare:.2f}\nFine applied for delay: ₱{fine:.2f}\nRemaining balance: ₱{self.balance:.2f}")

        # Calculate distance traveled
        start_index = self.start_station_menu['values'].index(start_station)
        end_index = self.end_station_menu['values'].index(end_station)
        if self.terminal_var.get() == "LRT1":
            distance_traveled = sum(lrt1_distances[min(start_index, end_index):max(start_index, end_index)])
        elif self.terminal_var.get() == "LRT2":
            distance_traveled = sum(lrt2_distances[min(start_index, end_index):max(start_index, end_index)])
        elif self.terminal_var.get() == "MRT3":
            distance_traveled = sum(mrt3_distances[min(start_index, end_index):max(start_index, end_index)])
        self.total_distance += distance_traveled

        self.previous_end_station = end_station
        self.handle_transfer()

    def apply_fine(self, card_type):
        fine = 0
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            fine = (elapsed_time // 5) * 30.0
            if fine > 0:
                self.total_fare += fine
                if card_type == "Beep Card":
                    self.balance -= fine
                    if self.balance < 0:
                        messagebox.showwarning("Insufficient Balance", "Your balance is insufficient to cover the fines")
                        self.balance += fine
                        self.total_fare -= fine
                        return fine
        return fine

    def handle_transfer(self):
        if self.previous_end_station in ["Recto", "Doroteo Jose", "Taft Ave", "EDSA", "Cubao", "Cubao Araneta"]:
            self.transfer_prompt_label.config(text="You have reached a transfer station. Do you want to switch lines or continue traveling?")
            self.yes_button.pack(side=tk.LEFT, padx=5)
        else:
            self.transfer_prompt_label.config(text="Do you want to continue traveling?")
            self.yes_button.pack_forget()
        self.transfer_button_frame.pack()

    def switch_lines(self):
        self.fine_notification_label.config(text="")
        if self.terminal_var.get() == 'LRT1':
            if self.previous_end_station == "Doroteo Jose":
                self.terminal_var.set('LRT2')
                self.previous_end_station = "Recto"
            elif self.previous_end_station == "EDSA":
                self.terminal_var.set('MRT3')
                self.previous_end_station = "Taft Ave"
        elif self.terminal_var.get() == 'LRT2':
            if self.previous_end_station == "Recto":
                self.terminal_var.set('LRT1')
                self.previous_end_station = "Doroteo Jose"
            elif self.previous_end_station == "Cubao":
                self.terminal_var.set('MRT3')
                self.previous_end_station = "Cubao Araneta"
        elif self.terminal_var.get() == 'MRT3':
            if self.previous_end_station == "Taft Ave":
                self.terminal_var.set('LRT1')
                self.previous_end_station = "EDSA"
            elif self.previous_end_station == "Cubao Araneta":
                self.terminal_var.set('LRT2')
                self.previous_end_station = "Cubao"

        self.update_stations(None)
        self.start_station_var.set(self.previous_end_station)
        self.end_station_var.set('')
        self.track_time(None)
        self.transfer_prompt_label.config(text="")
        self.transfer_button_frame.pack_forget()

    def continue_on_same_line(self):
        self.transfer_prompt_label.config(text="")
        self.transfer_button_frame.pack_forget()

    def continue_travel(self):
        self.fine_notification_label.config(text="")
        self.result_label.config(text="")  # Clear the result label
        self.start_station_var.set(self.previous_end_station)
        self.end_station_var.set('')
        self.track_time(None)
        self.transfer_prompt_label.config(text="")
        self.transfer_button_frame.pack_forget()

    def end_travel(self):
        self.fine_notification_label.config(text="")
        self.result_label.config(text=f"Total distance: {self.total_distance:.2f} km\nTotal fare: ₱{self.total_fare:.2f}")
        self.transfer_prompt_label.config(text="")
        self.transfer_button_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = TrainFareCalculator(root)
    root.mainloop()