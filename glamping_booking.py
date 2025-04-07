import tkinter as tk
import json
import os
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from tkinter import messagebox
from pathlib import Path

window = tk.Tk()
window.title("booking Program")
window.geometry("800x600")

# getting paths
def get_data_path():
    base_dir = Path(__file__).parent
    data_dir = base_dir / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir / "reservations.json"


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


def view_reservations():

    data_file = get_data_path()
    
    try:
        # Check if file exists and has content
        if not data_file.exists():
            messagebox.showinfo("Info", "No reservations found. Create your first reservation.")
            return

        with open(data_file, "r") as f:
            content = f.read()
            reservations = json.loads(content) if content.strip() else []

        if not reservations:
            messagebox.showinfo("Info", "No reservations found")
            return

        # Create the view window
        view_window = tk.Toplevel(window)
        view_window.title("Manage Reservations")
        view_window.geometry("1000x550")  # Increased height for better button spacing

        # Create frame for treeview and scrollbar
        tree_frame = tk.Frame(view_window)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview with scrollbar
        columns = ("ID", "Guest", "Tent", "Check-In", "Check-Out", "Nights", "Platform")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        
        # Add vertical scrollbar
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)

        # Configure columns
        col_widths = [50, 150, 80, 100, 100, 60, 120]
        for col, width in zip(columns, col_widths):
            tree.heading(col, text=col)
            tree.column(col, width=width, anchor="center")

        # Add data to treeview
        for r in reservations:
            tree.insert("", "end", values=(
                r.get("id", ""),
                r.get("guest_name", ""),
                r.get("tent_number", ""),
                r.get("check_in_date", ""),
                r.get("check_out_date", ""),
                r.get("Number of nights", ""),  
                r.get("booking_platform", ""),
            ))

        # Create button frame at bottom
        button_frame = tk.Frame(view_window)
        button_frame.pack(fill="x", padx=10, pady=(0, 10))

        # Button styling
        btn_style = {"padx": 10, "pady": 5, "width": 15}

        def view_reservation_details():
            selected = tree.focus()
            if not selected:
                messagebox.showwarning("Warning", "Please select a reservation first.")
                return
            
            res_id = tree.item(selected)["values"][0]
            reservation = next((r for r in reservations if r.get("id") == res_id), None)
            
            if not reservation:
                messagebox.showerror("Error", "Reservation not found")
                return
            
            # Create detail window
            detail_window = tk.Toplevel(view_window)
            detail_window.title(f"Reservation Details - ID {res_id}")
            detail_window.geometry("600x800")

            # Create scrollable container
            main_frame = tk.Frame(detail_window)
            main_frame.pack(fill="both", expand=True, padx=10, pady=10)

            canvas = tk.Canvas(main_frame)
            scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # Display title
            tk.Label(scrollable_frame, 
                   text="FULL RESERVATION DETAILS", 
                   font=("Arial", 14, "bold")).pack(pady=10)
            


            # Section definitions
            sections = [
                ("Basic Information", [
                    ("Reservation ID", "id"),
                    ("Reservation Date", "reservation_date"),
                    ("Booking Platform", "booking_platform"),
                    ("Tent Number", "tent_number")
                ]),
                ("Guest Information", [
                    ("Guest Name", "guest_name"),
                    ("Guest Country", "guest_country"),
                    ("Number of Guests", "number_of_guests")
                ]),
                ("Dates", [
                    ("Check-In Date", "check_in_date"),
                    ("Check-Out Date", "check_out_date"),
                    ("Number of Nights", "Number_of_nights")  
                ]),
                ("Financial Information", [
                    ("Cleaning Cost", "cleaning"),
                    ("Extra Expenses", "extra_expenses"),
                    ("Calculation Results", "calculation_results"),
                    ("Profit Split", "profit_split")
                ])
            ]

        
            
            # Display sections
            for section_title, fields in sections:
                # Section header
                tk.Label(scrollable_frame, 
                        text=section_title, 
                        font=("Arial", 12, "bold"),
                        anchor="w").pack(fill="x", pady=(10, 5))
                
                # Section content frame
                frame = tk.Frame(scrollable_frame, bd=1, relief="solid", padx=5, pady=5)
                frame.pack(fill="x", padx=5, pady=5)
                
                # Display each field
                for label_text, field_key in fields:
                    value = reservation.get(field_key, "N/A")
                    if isinstance(value, dict):
                        value = "\n".join(f"{k}: {v}" for k, v in value.items())
                    
                    row_num = len(frame.winfo_children())//2  # Calculate row number
                    
                    tk.Label(frame, text=f"{label_text}:", 
                           font=("Arial", 10, "bold")).grid(
                           row=row_num, column=0, sticky="w", padx=5, pady=2)
                    tk.Label(frame, text=value, wraplength=400, 
                           justify="left").grid(
                           row=row_num, column=1, sticky="w", padx=5, pady=2)
            
            # Close button
            tk.Button(scrollable_frame, 
                     text="Close", 
                     command=detail_window.destroy).pack(pady=10)

        def delete_reservation():
            selected = tree.focus()
            if not selected:
                messagebox.showwarning("Warning", "Please select a reservation")
                return
            
            res_id = tree.item(selected)["values"][0]
            
            if messagebox.askyesno("Confirm", "Delete this reservation?"):
                try:
                    # Filter out the deleted reservation
                    updated_reservations = [r for r in reservations if r.get("id") != res_id]
                    
                    # Save to file
                    with open(data_file, "w") as f:
                        json.dump(updated_reservations, f, indent=4)
                    
                    # Update UI
                    tree.delete(selected)
                    messagebox.showinfo("Success", "Reservation deleted.")
                    
                    # Update our local reservations list
                    reservations[:] = updated_reservations
                    
                    # Close window if no reservations left
                    if not reservations:
                        view_window.destroy()
                        
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete: {e}")

        # Create action buttons
        view_btn = tk.Button(button_frame, 
                           text="View Details", 
                           command=view_reservation_details,
                           **btn_style)
        view_btn.pack(side="left", padx=5)

        delete_btn = tk.Button(button_frame, 
                             text="Delete", 
                             command=delete_reservation,
                             **btn_style)
        delete_btn.pack(side="left", padx=5)

        close_btn = tk.Button(button_frame, 
                            text="Close", 
                            command=view_window.destroy,
                            **btn_style)
        close_btn.pack(side="right", padx=5)

    except Exception as e:
        messagebox.showerror("Error", f"Cannot load reservations: {e}")



class ProfitCalculator:
            def __init__(self, reservations=None):
                self.glamping_net_profit = 0.0
                self.tent_owners_share = 0.0
                self.processed_reservations = 0
                if reservations:
                    self.process_reservations(reservations)

            def process_reservations(self, reservations):
                for r in reservations:
                    try:
                        profit_data = r.get("profit_split", {})
                        self.glamping_net_profit += float(profit_data.get("glamping_owner_share", 0))
                        self.tent_owners_share += float(profit_data.get("tent_owner_share", 0))
                        self.processed_reservations += 1
                    except (ValueError, TypeError, AttributeError) as e:
                        continue 

            def get_summary(self):
                return {
                    "total_glamping_profit": round(self.glamping_net_profit, 2),
                    "total_tent_owners_share": round(self.tent_owners_share, 2),
                    "combined_profit": round(self.glamping_net_profit + self.tent_owners_share, 2),
                    "processed_reservations": self.processed_reservations
                }

def show_profit_summary():
    data_file = get_data_path()
    
    try:
        # Check if file exists and has content
        if not data_file.exists():
            messagebox.showinfo("Info", "No reservations found. Create your first reservation.")
            return

        with open(data_file, "r") as f:
            content = f.read()
            reservations = json.loads(content) if content.strip() else []

        if not reservations:
            messagebox.showinfo("Info", "No reservations found")
            return
        
        
        calculator = ProfitCalculator(reservations) 
        summary = calculator.get_summary()
        
        profit_window = tk.Toplevel(window)
        profit_window.title("Profit Summary Report")
        profit_window.geometry("1000x550")

        # Create main frame with padding
        main_frame = tk.Frame(profit_window, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Title
        tk.Label(main_frame, 
                text="PROFIT SUMMARY REPORT", 
                font=("Arial", 16, "bold")).pack(pady=(0, 20))
        
        # Create frame for summary details
        summary_frame = tk.LabelFrame(main_frame, text="Summary", padx=10, pady=10)
        summary_frame.pack(fill="x", pady=10)
        
        # Display summary information
        summary_items = [
            ("Total Glamping Profit:", f"{summary['total_glamping_profit']}€"),
            ("Total Tent Owners Share:", f"{summary['total_tent_owners_share']}€"),
            ("Combined Profit:", f"{summary['combined_profit']}€"),
            ("Total Processed Reservations:", str(summary['processed_reservations']))
        ]
        
        for label, value in summary_items:
            item_frame = tk.Frame(summary_frame)
            item_frame.pack(fill="x", pady=5)
            
            tk.Label(item_frame, 
                    text=label, 
                    font=("Arial", 10, "bold")).pack(side="left")
            tk.Label(item_frame, 
                    text=value, 
                    font=("Arial", 10)).pack(side="right")
        
        # Add close button
        tk.Button(main_frame, 
                text="Close", 
                command=profit_window.destroy,
                width=15).pack(pady=20)

    except Exception as e:
        messagebox.showerror("Error", f"Error generating profit summary: {str(e)}")
             


button_frame = tk.Frame(window)
button_frame.pack(pady=10, anchor ='w')

settings_button = tk.Button(button_frame, text="Date settings", command=open_settings)
settings_button.pack(side=tk.LEFT, padx=5)

view_reservations_button = tk.Button(button_frame, text="View Reservations", 
                                   command=view_reservations)
view_reservations_button.pack(side=tk.LEFT, padx=5)

profit_view_window = tk.Button(button_frame, text="Profit Summary Report", command=show_profit_summary)
profit_view_window.pack(side=tk.LEFT, padx=5)

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
guest_country_name = tk.Frame(window)
guest_country_name.pack(pady=10, anchor="w")

label_guest_county = tk.Label(guest_country_name, text="Guest country:")
label_guest_county.pack(side=tk.LEFT)

entry_guest_county = tk.Entry(guest_country_name)
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
    global reservation_data
    # Pridobi vse podatke
    reservation_data = {
        "reservation_date": entry_reservation_date.get_date().strftime("%d.%m.%Y"),
        "booking_platform": entry_booking_platform.get(),
        "tent_number": entry_tent_number.get(),
        "guest_country": entry_guest_county.get(),
        "guest_name": entry_guest_name.get(),
        "number_of_guests": entry_number_of_guests.get(),
        "check_in_date": check_in_date.get_date().strftime("%d.%m.%Y"),
        "check_out_date": check_out_date.get_date().strftime("%d.%m.%Y"),
        "Number of nights": (check_out_date.get_date() - check_in_date.get_date()).days,  
        "cleaning": entry_cleaning_cost.get(),
        "extra_expenses": entry_extra_expenses.get(),
        "calculation_results": calculate_stay(),
        "profit_split": calculate_profit_split()
    }

    # Preveri podatke
    required_fields = {
        "reservation_date": "Reservation date is required!",
        "booking_platform": "Booking platform is required!",
        "tent_number": "Tent number is required!",
        "guest_country": "Guest country is required!",
        "guest_name": "Guest name is required!",
        "number_of_guests": "Number of guests is required!",
        "check_in_date": "Check-in date is required!",
        "check_out_date": "Check-out date is required!",
        "Number of nights": "Number of nights is required!",
        "cleaning": "Cleaning cost is required!",
        "extra_expenses": "Extra expenses are required!",
        "calculation_results": "Calculation results are required!",
        "profit_split": "Profit split is required!"
    }

    for field, error_message in required_fields.items():
        if not reservation_data.get(field):
            messagebox.showerror("Error", error_message)
            return False  # Vrnemo False, če validacija ni uspešna
    
    return True  # Vrnemo True, če je validacija uspešna

reservation_data = {}
def load_reservation():
    global reservation_data
    # Check if there is already this ID
    if 'id' in reservation_data:
        del reservation_data['id']  
    # Validate and prepare the data
    if not save_reservation():
        return  # Validation failed
    
    data_file = get_data_path()  # Get the proper file path
    
    try:
        # Try to read existing reservations
        try:
            if data_file.exists():
                with open(data_file, "r") as f:  
                    content = f.read()
                    reservations = json.loads(content) if content.strip() else []
            else:
                reservations = []
        except json.JSONDecodeError:
            reservations = []
            messagebox.showwarning("Warning", "Corrupted data file, creating new one")

        # Generate new ID (1 if empty, otherwise max + 1)
        new_id = 1 if not reservations else max(r.get('id', 0) for r in reservations) + 1
        reservation_data['id'] = new_id  # Add ID to current reservation

        # Add new reservation
        reservations.append(reservation_data)
        
        # Save back to file
        with open(data_file, "w") as f:  # Use data_file here too
            json.dump(reservations, f, indent=4, ensure_ascii=False)
            
        messagebox.showinfo("Success", f"Reservation saved with ID: {new_id}")
        
    except Exception as e:
        messagebox.showerror("Error", f"Could not save reservation: {str(e)}")



save_button = tk.Button(
    window, 
    text="Save reservation", 
    command=load_reservation  
)
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
