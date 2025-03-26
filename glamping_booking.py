import tkinter as tk
import json
import os
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from tkinter import messagebox



# Price zones
price_zones_direct = [
    {"zone": "A", 
     "price": 150,
     "start": "01.06.2025",
     "end": "20.06.2025"},
    
    {"zone": "B", 
     "price": 200,
     "start": "21.06.2025",
     "end": "15.07.2025"},
    
    {"zone": "C", 
     "price": 250,
     "start": "16.07.2025",
     "end": "15.08.2025"},
    
    {"zone": "D", 
     "price": 150,
     "start": "16.08.2025",
     "end": "30.09.2025"},
     ]

price_zones_airbnb = [
    {"zone": "A", 
     "price": 175,
     "start": "01.06.2025",
     "end": "20.06.2025"},

    {"zone": "B", 
     "price": 225,
     "start": "21.06.2025",
     "end": "15.07.2025"},

    {"zone": "C", 
     "price": 275,
     "start": "16.07.2025",
     "end": "15.08.2025"},

    {"zone": "D", 
     "price": 175,
     "start": "16.08.2025",
     "end": "30.09.2025"},
     ]

price_zones_booking = [
    {"zone": "A", 
     "price": 170,
     "start": "01.06.2025",
     "end": "20.06.2025"},

    {"zone": "B", 
     "price": 220,
     "start": "21.06.2025",
     "end": "15.07.2025"},

    {"zone": "C", 
     "price": 270,
     "start": "16.07.2025",
     "end": "15.08.2025"},

    {"zone": "D", 
     "price": 170,
     "start": "16.08.2025",
     "end": "30.09.2025"},
     ]

platform_prices = {
    "direct": price_zones_direct,
    "airbnb": price_zones_airbnb,
    "booking": price_zones_booking
}

#save and load settings
def save_to_file():
    with open("zones_settings.json", "w") as f:
        json.dump(platform_prices, f, indent=4)

def load_from_file():
    global price_zones_direct, price_zones_airbnb, price_zones_booking
    try:
        with open("zones_settings.json", "r") as f:
            data = json.load(f)
            price_zones_direct = data["direct"]
            price_zones_airbnb = data["airbnb"]
            price_zones_booking = data["booking"]
    except FileNotFoundError:
        pass

load_from_file()

window = tk.Tk()
window.title("booking Program")
window.geometry("1600x1200")


#date settings
def open_settings():
    global price_entries, settings_window
    global zone_a_start, zone_b_start, zone_c_start, zone_d_start
    global zone_a_end, zone_b_end, zone_c_end, zone_d_end

    settings_window = tk.Toplevel(window)
    settings_window.title("date settings")
    settings_window.geometry("1150x1000")

    tk.Label(settings_window, text="Date settings", font=("Arial", 16, "bold")).pack(pady=10)

    main_frame = tk.Frame(settings_window)
    main_frame.pack(pady=10, padx=20)

    #Zone date settings
    dates_frame = tk.LabelFrame(main_frame, text="Zone dates", font=("Arial", 11, "bold"))
    dates_frame.pack(fill="x", pady=10)

    # Zone A
    tk.Label(dates_frame, text="Zone A:", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(dates_frame, text="Start:").grid(row=0, column=1) 
    zone_a_start = DateEntry(dates_frame, width=12, date_pattern='dd.mm.yyyy')
    zone_a_start.set_date(datetime.strptime(price_zones_direct[0]["start"], "%d.%m.%Y").date())
    zone_a_start.grid(row=0, column=2, padx=5)
    tk.Label(dates_frame, text="End:").grid(row=0, column=3)
    zone_a_end = DateEntry(dates_frame, width=12, date_pattern='dd.mm.yyyy')
    zone_a_end.set_date(datetime.strptime(price_zones_direct[0]["end"], "%d.%m.%Y").date())
    zone_a_end.grid(row=0, column=4, padx=5)

    # Zone B
    tk.Label(dates_frame, text="Zone B:", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
    tk.Label(dates_frame, text="Start:").grid(row=1, column=1)
    zone_b_start = DateEntry(dates_frame, width=12, date_pattern='dd.mm.yyyy')
    zone_b_start.set_date(datetime.strptime(price_zones_direct[1]["start"], "%d.%m.%Y").date())
    zone_b_start.grid(row=1, column=2, padx=5)
    tk.Label(dates_frame, text="End:").grid(row=1, column=3)
    zone_b_end = DateEntry(dates_frame, width=12, date_pattern='dd.mm.yyyy')
    zone_b_end.set_date(datetime.strptime(price_zones_direct[1]["end"], "%d.%m.%Y").date())
    zone_b_end.grid(row=1, column=4, padx=5) 
    
    # Zone C
    tk.Label(dates_frame, text="Zone C:", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=5, pady=5)
    tk.Label(dates_frame, text="Start:").grid(row=2, column=1)
    zone_c_start = DateEntry(dates_frame, width=12, date_pattern='dd.mm.yyyy')
    zone_c_start.set_date(datetime.strptime(price_zones_direct[2]["start"], "%d.%m.%Y").date())
    zone_c_start.grid(row=2, column=2, padx=5)
    tk.Label(dates_frame, text="End:").grid(row=2, column=3)
    zone_c_end = DateEntry(dates_frame, width=12, date_pattern='dd.mm.yyyy')
    zone_c_end.set_date(datetime.strptime(price_zones_direct[2]["end"], "%d.%m.%Y").date())
    zone_c_end.grid(row=2, column=4, padx=5)

    # Zone D        
    tk.Label(dates_frame, text="Zone D:", font=("Arial", 10, "bold")).grid(row=3, column=0, padx=5, pady=5)
    tk.Label(dates_frame, text="Start:").grid(row=3, column=1)
    zone_d_start = DateEntry(dates_frame, width=12, date_pattern='dd.mm.yyyy')
    zone_d_start.set_date(datetime.strptime(price_zones_direct[3]["start"], "%d.%m.%Y").date())
    zone_d_start.grid(row=3, column=2, padx=5)
    tk.Label(dates_frame, text="End:").grid(row=3, column=3)
    zone_d_end = DateEntry(dates_frame, width=12, date_pattern='dd.mm.yyyy')
    zone_d_end.set_date(datetime.strptime(price_zones_direct[3]["end"], "%d.%m.%Y").date())
    zone_d_end.grid(row=3, column=4, padx=5)

    # Price settings
    price_frame = tk.LabelFrame(main_frame, text="Zone price settings", font=("Arial", 11, "bold"))
    price_frame.pack(fill="x", pady=10)

    # Column headers for prices
    tk.Label(price_frame, text="Zone", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(price_frame, text="Direct", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(price_frame, text="Airbnb", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)
    tk.Label(price_frame, text="Booking", font=("Arial", 10, "bold")).grid(row=0, column=3, padx=5, pady=5)

   # Price entries for each zone
    zones = ["A", "B", "C", "D"]
    price_entries = {
        "direct": {},
        "airbnb": {},
        "booking": {}
    }

    for idx, zone in enumerate(zones, 1):
        tk.Label(price_frame, text=f"Zone {zone}:").grid(row=idx, column=0, padx=5, pady=5)
        
        price_entries["direct"][zone] = tk.Entry(price_frame, width=10)
        price_entries["direct"][zone].grid(row=idx, column=1, padx=5, pady=5)
        price_entries["direct"][zone].insert(0, str(next((z["price"] for z in price_zones_direct if z["zone"] == zone), "")))

        price_entries["airbnb"][zone] = tk.Entry(price_frame, width=10)
        price_entries["airbnb"][zone].grid(row=idx, column=2, padx=5, pady=5)
        price_entries["airbnb"][zone].insert(0, str(next((z["price"] for z in price_zones_airbnb if z["zone"] == zone), "")))

        price_entries["booking"][zone] = tk.Entry(price_frame, width=10)
        price_entries["booking"][zone].grid(row=idx, column=3, padx=5, pady=5)
        price_entries["booking"][zone].insert(0, str(next((z["price"] for z in price_zones_booking if z["zone"] == zone), "")))
    # Save button
    save_button = tk.Button(settings_window, 
                            text="Save", 
                            command=save_zone_settings,
                            width=20,
                            height=2,
                            bg="green",
                            fg="white",
                            font=("Arial", 10, "bold"))
    save_button.pack(pady=20)


def save_zone_settings():
    zone_dates = {
        "A": {
            "start": zone_a_start.get_date(),
            "end": zone_a_end.get_date()
        },
        "B": {
            "start": zone_b_start.get_date(),
            "end": zone_b_end.get_date()
        },
        "C": {
            "start": zone_c_start.get_date(),
            "end": zone_c_end.get_date()
        },
        "D": {
            "start": zone_d_start.get_date(),
            "end": zone_d_end.get_date()
        }
    }

    #Validate each zone's start is before its end
    for zone, dates in zone_dates.items():
        if dates["end"] <= dates["start"]:
            messagebox.showwarning("Invalid date", f"Zone {zone} end date must be after start date\n"
                                   f"Start: {dates['start']}\n"
                                   f"End: {dates['end']}")
                
            return

    #Validate zones are in sequential order
    if (zone_dates["B"]["start"] <= zone_dates["A"]["start"] or
        zone_dates["C"]["start"] <= zone_dates["B"]["start"] or
        zone_dates["D"]["start"] <= zone_dates["C"]["start"]):
        messagebox.showwarning("Invalid date", "Zones must be in sequential order without overlapping")
        return

    formatted_dates = {
        zone: {
            "start": zone_dates[zone]["start"].strftime("%d.%m.%Y"),
            "end": zone_dates[zone]["end"].strftime("%d.%m.%Y")
        }
        for zone, dates in zone_dates.items()
    }

    global price_zones_direct, price_zones_airbnb, price_zones_booking

    #update the zones prices
    for platform in ["direct", "airbnb", "booking"]:
        for zone in ["A", "B", "C", "D"]:
            try:
                price = float(price_entries[platform][zone].get())
                
                for zone_data in platform_prices[platform]:
                    if zone_data["zone"] == zone:
                        zone_data["price"] = price
                        zone_data["start"] = formatted_dates[zone]["start"]
                        zone_data["end"] = formatted_dates[zone]["end"]
                        break
            except ValueError:
                messagebox.showwarning("Invalid price", f"Please enter a valid price for zone {zone} on {platform}")
                return
            
    price_zones_direct = platform_prices["direct"]
    price_zones_airbnb = platform_prices["airbnb"]
    price_zones_booking = platform_prices["booking"]

    settings_window.destroy()

    save_to_file()

    #update the min and max date
    min_date, max_date = get_booking_date_range()
    check_in_date.config(mindate=min_date, maxdate=max_date)
    check_out_date.config(mindate=min_date, maxdate=max_date)



def open_saved_reservation():
    saved_window = tk.Toplevel(window)
    saved_window.title("Saved Reservations")
    saved_window.geometry("1200x600")


    columns = ("Reservation Date", "Platform")
    tree = ttk.Treeview(saved_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(fill="both", expand=True)
    
    
button_frame = tk.Frame(window)
button_frame.pack(pady=10, anchor ='w')

settings_button = tk.Button(button_frame, text="Date settings", command=open_settings)
settings_button.pack(side=tk.LEFT, padx=5)

saved_reservation_button = tk.Button(button_frame, text="Saved reservations", command=open_saved_reservation)
saved_reservation_button.pack(side=tk.LEFT, padx=5)



#get the booking date range
def get_booking_date_range():
    all_dates = []
    for platform in platform_prices.values():
        for zone in platform:
            start_date = datetime.strptime(zone["start"], "%d.%m.%Y").date()
            end_date = datetime.strptime(zone["end"], "%d.%m.%Y").date()
            all_dates.extend([start_date, end_date])
    return min(all_dates), max(all_dates)

min_date, max_date = get_booking_date_range()


label = tk.Label(window, text="Welcome to the booking program!")
label.pack()

#booking platform used 
booking_platform_container = tk.Frame(window)
booking_platform_container.pack(pady=10, anchor="w")

booking_platform_frame = tk.Frame(booking_platform_container)
booking_platform_frame.pack(pady=10, anchor="w")

label_booking_platform = tk.Label(booking_platform_frame, text="Booking platform:")
label_booking_platform.pack(side=tk.LEFT)

entry_booking_platform = ttk.Combobox(booking_platform_frame, values=["direct", "airbnb", "booking", "manual"], 
                                      width=22, 
                                      state="readonly")
entry_booking_platform.pack(side=tk.LEFT)
entry_booking_platform.set("Select booking platform")

# Global variables for platform-specific frames and entries
price_per_night_frame = None
price_per_night_entry = None
booking_fee_in_percentage_frame = None
booking_fee_in_percentage_entry = None
airbnb_fee_in_percentage_frame = None
airbnb_fee_in_percentage_entry = None

#handle platform selection
def handle_platform_selection(event=None):
    global price_per_night_frame, price_per_night_entry
    global booking_fee_in_percentage_frame, booking_fee_in_percentage_entry
    global airbnb_fee_in_percentage_frame, airbnb_fee_in_percentage_entry

    # Clear all existing platform-specific frames
    for frame in [price_per_night_frame, booking_fee_in_percentage_frame, airbnb_fee_in_percentage_frame]:
        if frame:
            frame.destroy()

    selected_platform = entry_booking_platform.get()

    if selected_platform == "manual":
        price_per_night_frame = tk.Frame(booking_platform_container)
        price_per_night_frame.pack(pady=10, anchor="w")

        price_per_night_label = tk.Label(price_per_night_frame, text="Price per night:")
        price_per_night_label.pack(side=tk.LEFT)

        price_per_night_entry = tk.Entry(price_per_night_frame)
        price_per_night_entry.pack(side=tk.LEFT)

    elif selected_platform == "booking":
        booking_fee_in_percentage_frame = tk.Frame(booking_platform_container)
        booking_fee_in_percentage_frame.pack(pady=10, anchor="w")

        booking_fee_in_percentage_label = tk.Label(booking_fee_in_percentage_frame, text="Booking fee in percentage:")
        booking_fee_in_percentage_label.pack(side=tk.LEFT)

        booking_fee_in_percentage_entry = tk.Entry(booking_fee_in_percentage_frame)
        booking_fee_in_percentage_entry.pack(side=tk.LEFT)

    elif selected_platform == "airbnb":
        airbnb_fee_in_percentage_frame = tk.Frame(booking_platform_container)
        airbnb_fee_in_percentage_frame.pack(pady=10, anchor="w")

        airbnb_fee_in_percentage_label = tk.Label(airbnb_fee_in_percentage_frame, text="Airbnb fee in percentage:")
        airbnb_fee_in_percentage_label.pack(side=tk.LEFT)

        airbnb_fee_in_percentage_entry = tk.Entry(airbnb_fee_in_percentage_frame)
        airbnb_fee_in_percentage_entry.pack(side=tk.LEFT)

entry_booking_platform.bind("<<ComboboxSelected>>", handle_platform_selection)

# Reservation creation date
reservation_date_frame = tk.Frame(window)
reservation_date_frame.pack(pady=10, anchor="w")

label_reservation_date = tk.Label(reservation_date_frame, text="Reservation creation date:")
label_reservation_date.pack(side=tk.LEFT)

entry_reservation_date = DateEntry(reservation_date_frame, width=12,
                                  background='darkblue',
                                  foreground='white',
                                  borderwidth=2,
                                  date_pattern='dd.mm.yyyy')
entry_reservation_date.pack(side=tk.LEFT)


# Tent number
tent_number_frame = tk.Frame(window)
tent_number_frame.pack(pady=10, anchor="w")

label_tent_number = tk.Label(tent_number_frame, text="Tent number:")
label_tent_number.pack(side=tk.LEFT)

entry_tent_number = ttk.Combobox(tent_number_frame, values=["tent 1(far left)", "tent 2", "tent 3", "tent 4", "tent 5(far right)"], width=20, state="readonly")
entry_tent_number.pack(side=tk.LEFT)
entry_tent_number.set("Select tent number")

# Guest Country
gueast_country_name = tk.Frame(window)
gueast_country_name.pack(pady=10, anchor="w")

label_guest_county = tk.Label(gueast_country_name, text="Guest country:")
label_guest_county.pack(side=tk.LEFT)

entry_guest_county = tk.Entry(gueast_country_name)
entry_guest_county.pack(side=tk.LEFT)

# Guest name
guest_name = tk.Frame(window)
guest_name.pack(pady=10, anchor="w")

label_guest_name = tk.Label(guest_name, text="Guest name:")
label_guest_name.pack(side=tk.LEFT)

entry_guest_name = tk.Entry(guest_name)
entry_guest_name.pack(side=tk.LEFT)

# Number of guests
number_of_guests_frame = tk.Frame(window)
number_of_guests_frame.pack(pady=10, anchor="w")

label_number_of_guests = tk.Label(number_of_guests_frame, text="Number of guests:")
label_number_of_guests.pack(side=tk.LEFT)

entry_number_of_guests = tk.Entry(number_of_guests_frame)
entry_number_of_guests.pack(side=tk.LEFT)

def validate_checkout_date(event=None):
    check_in = check_in_date.get_date()
    check_out = check_out_date.get_date()
    if check_out <= check_in:
        check_out_date.set_date(check_in + timedelta(days=1))

        messagebox.showwarning("Invalid date", "Check-out date must be after check-in date")

# Dates
dates_frame = tk.Frame(window)
dates_frame.pack(pady=10, anchor="w")

check_in_label = tk.Label(dates_frame, text="Check-in date:")
check_in_label.grid(row=0, column=0, padx=5)

check_in_date = DateEntry(dates_frame, width=12,
                          background='darkblue',
                          foreground='white',
                          borderwidth=2,
                          date_pattern='dd.mm.yyyy',
                          mindate=min_date,
                          maxdate=max_date)
check_in_date.grid(row=0, column=1, padx=5)
check_in_date.bind("<<DateEntrySelected>>", validate_checkout_date)

#check out date
check_out_label = tk.Label(dates_frame, text="Check-out date:")
check_out_label.grid(row=1, column=0, padx=5)

check_out_date = DateEntry(dates_frame, width=12,
                           background='darkblue',
                           foreground='white',
                           borderwidth=2,
                           date_pattern='dd.mm.yyyy',
                           mindate=min_date,
                           maxdate=max_date)
check_out_date.grid(row=1, column=1, padx=5, pady=5)
check_out_date.bind("<<DateEntrySelected>>", validate_checkout_date)

#extra expenses
extra_expenses_frame = tk.Frame(window)
extra_expenses_frame.pack(pady=10, anchor="w")

label_extra_expenses = tk.Label(extra_expenses_frame, text="Extra expenses:")
label_extra_expenses.pack(side=tk.LEFT)

entry_extra_expenses = tk.Entry(extra_expenses_frame)
entry_extra_expenses.pack(side=tk.LEFT)

# Calculate the total price of the stay
def calculate_stay():
    check_in = check_in_date.get_date()
    check_out = check_out_date.get_date()
    nights_count = (check_out - check_in).days

    extra_expenses = entry_extra_expenses.get()
    try:
        extra_expenses = float(extra_expenses) if extra_expenses else 0
    except ValueError:
        extra_expenses = 0
    
    platform_fee_in_percentage = 0
    total_price = 0
    original_price = 0
    platform_fee = 0
    selected_platform = entry_booking_platform.get()

    if selected_platform == "manual":
        try:
            price_per_night = float(price_per_night_entry.get())
            total_price = round(price_per_night * nights_count, 2)
            original_price = total_price
        except (ValueError, AttributeError):
            total_price = 0

    else:
        current_date = check_in
        price_zones = platform_prices[selected_platform]

        while current_date < check_out:
            date_str = current_date.strftime("%d.%m.%Y")

            price_per_night = None
            for zone in price_zones:
                zone_start = datetime.strptime(zone["start"], "%d.%m.%Y").date()
                zone_end = datetime.strptime(zone["end"], "%d.%m.%Y").date()
                if zone_start <= current_date <= zone_end:
                    price_per_night = zone["price"]
                    original_price += price_per_night

            current_date += timedelta(days=1)
                    
                    
        if selected_platform == "booking":
            platform_fee_in_percentage = booking_fee_in_percentage_entry.get()
            platform_fee = float(booking_fee_in_percentage_entry.get()) / 100 * original_price
            total_price = original_price - platform_fee

        elif selected_platform == "airbnb":
            platform_fee_in_percentage = airbnb_fee_in_percentage_entry.get()
            platform_fee = float(airbnb_fee_in_percentage_entry.get()) / 100 * original_price
            total_price = original_price - platform_fee

        else:
            total_price = original_price
            
    return {
        "total_price": total_price,
        "original_price": original_price,
        "platform_fee": platform_fee,
        "extra_expenses": extra_expenses,
        "platform_fee_in_percentage": platform_fee_in_percentage
    }

# Calculate profit split
def calculate_profit_split():
    stay_details = calculate_stay()
    total_price = stay_details["total_price"]
    cleaning_cost = 0

    cleaning = entry_cleaning_cost.get()
    extra_expenses = entry_extra_expenses.get()

    tent_owner_share = round(total_price * 0.65, 2)

    glamping_owner_share = round(total_price * 0.35, 2)

    if cleaning == "yes":
        cleaning_cost = 30
        tent_owner_share -= cleaning_cost / 2
        glamping_owner_share -= cleaning_cost / 2
    
    if extra_expenses:
        extra_expenses = float(extra_expenses)
        tent_owner_share -= extra_expenses / 2
        glamping_owner_share -= extra_expenses / 2

    return {
        "tent_owner_share": tent_owner_share,
        "glamping_owner_share": glamping_owner_share,
        "cleaning_cost": cleaning_cost,
        "total_price": total_price
    }


# cleaning cost
cleaning_cost_frame = tk.Frame(window)
cleaning_cost_frame.pack(pady=10, anchor="w")

label_cleaning_cost = tk.Label(cleaning_cost_frame, text="Cleaning cost(30€):")
label_cleaning_cost.pack(side=tk.LEFT)

entry_cleaning_cost = ttk.Combobox(cleaning_cost_frame, values=["yes", "no"], width=20, state="readonly")
entry_cleaning_cost.pack(side=tk.LEFT)
entry_cleaning_cost.set("Select yes or no")

def display_calculation_results():
    stay_details = calculate_stay()
    profit_split = calculate_profit_split()

    total_before_cleaning = stay_details['total_price']
    tent_share_before = round(total_before_cleaning * 0.65, 2)
    glamping_share_before = round(total_before_cleaning * 0.35, 2)
    

    # Format the results string
    results = f"""
Booking Details:
---------------
Platform: {entry_booking_platform.get()}
Number of nights: {(check_out_date.get_date() - check_in_date.get_date()).days}
Reservation date: {entry_reservation_date.get_date().strftime("%d.%m.%Y")}
Guest country: {entry_guest_county.get()}
Average price per night: {stay_details['original_price'] / (check_out_date.get_date() - check_in_date.get_date()).days:.2f}€
Original price per stay: {stay_details['original_price']:.2f}€

Fees and Expenses:
----------------
Platform fee: {stay_details['platform_fee']:.2f}€ ({stay_details['platform_fee_in_percentage']}%)
Extra expenses: {stay_details['extra_expenses']:.2f}€
Cleaning cost: {profit_split.get('cleaning_cost', 0):.2f}€

Profit Split Before Cleaning and Extra Expenses. (After Platform Fee):
-----------------------------------------------
Tent owner share(65%): {tent_share_before:.2f}€
Glamping owner share(35%): {glamping_share_before:.2f}€

Final Split After Cleaning and Extra Expenses:
---------------------------------------
Tent owner share(65%): {profit_split['tent_owner_share']:.2f}€
Glamping owner share(35%): {profit_split['glamping_owner_share']:.2f}€
"""
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, results)
    result_text.config(state=tk.DISABLED)

# Calculate button
calculate_button = tk.Button(window, text="Calculate profit split:", command=display_calculation_results)
calculate_button.pack(pady=10)



def save_reservation():
    # Get all the important data
    reservation_data = {
        "reservation_date": entry_reservation_date.get_date().strftime("%d.%m.%Y"),
        "booking_platform": entry_booking_platform.get(),
        "tent_number": entry_tent_number.get(),
        "guest_country": entry_guest_county.get(),
        "guest_name": entry_guest_name.get(),
        "number_of_guests": entry_number_of_guests.get(),
        "check_in_date": check_in_date.get_date().strftime("%d.%m.%Y"),
        "check_out_date": check_out_date.get_date().strftime("%d.%m.%Y"),
        "cleaning": entry_cleaning_cost.get(),
        "extra_expenses": entry_extra_expenses.get(),
        "calculation_results": calculate_stay(),
        "profit_split": calculate_profit_split()
    }

    try:
        # Try to load existing reservations
        try:
            with open("reservations.json", "r") as f:
                reservations = json.load(f)
        except FileNotFoundError:
            reservations = []  # If file doesn't exist, start with empty list
        
        # Add new reservation
        reservations.append(reservation_data)
        
        # Save all reservations back to file
        with open("reservations.json", "w") as f:
            json.dump(reservations, f, indent=4)
            
        messagebox.showinfo("Success", "Reservation saved!")
        
    except Exception as e:
        messagebox.showerror("Error", f"Could not save reservation: {str(e)}")

# Update your save button to use this function
save_button = tk.Button(window, text="Save reservation", command=save_reservation)        
save_button.pack(pady=10)


result_frame = tk.Frame(window, bg="SystemButtonFace")
result_frame.pack(pady=10, fill=tk.BOTH, expand=True)

result_text = tk.Text(result_frame, 
                      width=70, 
                      height=15, 
                      font=("Courier", 10), 
                      state="disabled",
                      bg="SystemButtonFace",
                      relief="flat",
                      padx=10,
                      pady=10)
scrollbar = ttk.Scrollbar(
    result_frame,
    orient=tk.VERTICAL,
    command=result_text.yview,
    style="Vertical.TScrollbar")

result_text.config(yscrollcommand=scrollbar.set)

result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


window.mainloop()
