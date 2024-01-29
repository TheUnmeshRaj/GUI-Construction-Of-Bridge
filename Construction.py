import tkinter as tk
from tkinter import ttk


def calculate_reinforcement_area():
    try:
        b = float(deck_width_entry.get())
        d = float(effective_depth_entry.get())
        fc = float(fc_entry.get())
        fy = float(fy_entry.get())
    except ValueError:
        reinforcement_result_label.config(
            text="Invalid input. Please enter numeric values."
        )
        return

    As_min = 0.0025 * b * d * (fc / fy)
    reinforcement_result_label.config(
        text=f"Minimum Area of Reinforcement (As): {As_min} mm²"
    )


def calculate_pile_bearing_capacity():
    try:
        pile_base_area = float(pile_base_area_entry.get())
        ultimate_soil_capacity = float(ultimate_soil_capacity_entry.get())
        pile_side_area = float(pile_side_area_entry.get())
        ultimate_side_resistance = float(ultimate_side_resistance_entry.get())
    except ValueError:
        pile_bearing_capacity_result_label.config(
            text="Invalid input. Please enter numeric values."
        )
        return

    pile_bearing_capacity = (
        pile_base_area * ultimate_soil_capacity
        + pile_side_area * ultimate_side_resistance
    )
    pile_bearing_capacity_result_label.config(
        text=f"Bearing Capacity of Pile Foundation: {pile_bearing_capacity} units"
    )


def calculate_max_deflection():
    try:
        load = float(load_entry.get())
        length = float(length_entry.get())
        elasticity = float(elasticity_entry.get())
        inertia = float(inertia_entry.get())
    except ValueError:
        max_deflection_result_label.config(
            text="Invalid input. Please enter numeric values."
        )
        return

    max_deflection = (load * length**3) / (48 * elasticity * inertia)
    max_deflection_result_label.config(
        text=f"Maximum Deflection: {max_deflection} units"
    )


def calculate_bending_moment():
    try:
        load_beam = float(load_beam_entry.get())
        length_beam = float(length_beam_entry.get())
    except ValueError:
        bending_moment_result_label.config(
            text="Invalid input. Please enter numeric values."
        )
        return

    bending_moment = (load_beam * length_beam**4) / 4
    bending_moment_result_label.config(text=f"Bending Moment: {bending_moment} units")


def calculate_shear_reinforcement_ratio():
    try:
        fc_shear = float(fc_shear_entry.get())
        Vu = float(ultimate_shear_force_entry.get())
        b_shear = float(deck_width_shear_entry.get())
        d_shear = float(effective_depth_shear_entry.get())
        fy_shear = float(fy_shear_entry.get())
    except ValueError:
        shear_reinforcement_result_label.config(
            text="Invalid input. Please enter numeric values."
        )
        return

    rho_v_min = (3 * (fc_shear**0.5) * Vu) / (b_shear * d_shear * fy_shear)
    shear_reinforcement_result_label.config(
        text=f"Minimum Shear Reinforcement Ratio (ρv): {rho_v_min}"
    )


# Create the main window
root = tk.Tk()
root.title("Bridge Construction Project")
root.resizable(True, True)  # Set both width and height resizable to False
root.configure(bg="#5EADF2")

# Main Information
main_info_label = tk.Label(
    root, text="Welcome to the Bridge Construction Project", font=("Helvetica", 16)
)
main_info_label.pack()


style = ttk.Style(root)
style.configure("TNotebook.Tab", padding=[15, 8])

# Create a Notebook (tabs)
notebook = ttk.Notebook(root, style="TNotebook")
notebook_style = ttk.Style()
notebook_style.configure("TNotebook", background="#5EADF2")
# Bridge Design Section
bridge_design_frame = tk.Frame(notebook, bg="lightblue")

load_label = tk.Label(bridge_design_frame, text="Load on the Beam (𝑊):")
load_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

load_entry = tk.Entry(bridge_design_frame)
load_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)

length_label = tk.Label(bridge_design_frame, text="Length of the Beam (𝐿):")
length_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

length_entry = tk.Entry(bridge_design_frame)
length_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

elasticity_label = tk.Label(bridge_design_frame, text="Modulus of Elasticity (𝐸):")
elasticity_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

elasticity_entry = tk.Entry(bridge_design_frame)
elasticity_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)

inertia_label = tk.Label(bridge_design_frame, text="Moment of Inertia (𝐼):")
inertia_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

inertia_entry = tk.Entry(bridge_design_frame)
inertia_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

calculate_max_deflection_button = tk.Button(
    bridge_design_frame,
    text="Calculate Maximum Deflection",
    command=calculate_max_deflection,
)
calculate_max_deflection_button.grid(
    row=4, column=0, columnspan=2, sticky="w", padx=10, pady=10
)

max_deflection_result_label = tk.Label(bridge_design_frame, text="Maximum Deflection: ")
max_deflection_result_label.grid(row=5, column=0, sticky="w", padx=10, pady=10)

formula_label_max_deflection = tk.Label(
    bridge_design_frame,
    text="Formula: Maximum Deflection = (𝑊𝐿^3) / (48𝐸𝐼)",
    relief="solid",
    borderwidth=1,
    font=("Helvetica", 12),  # Set the font size
)
formula_label_max_deflection.grid(
    row=6, column=0, columnspan=2, sticky="n", padx=10, pady=(10, 0), ipady=10
)

# Superstructure and Deck Section
superstructure_frame = tk.Frame(notebook, bg="lightblue")

load_beam_label = tk.Label(superstructure_frame, text="Load on the Beam (𝑊):")
load_beam_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

load_beam_entry = tk.Entry(superstructure_frame)
load_beam_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)

length_beam_label = tk.Label(superstructure_frame, text="Length of the Beam (𝐿):")
length_beam_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

length_beam_entry = tk.Entry(superstructure_frame)
length_beam_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

calculate_bending_moment_button = tk.Button(
    superstructure_frame,
    text="Calculate Bending Moment",
    command=calculate_bending_moment,
)
calculate_bending_moment_button.grid(
    row=2, column=0, columnspan=2, sticky="w", padx=10, pady=10
)

bending_moment_result_label = tk.Label(superstructure_frame, text="Bending Moment: ")
bending_moment_result_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

formula_label_bending_moment = tk.Label(
    superstructure_frame,
    text="Formula: Bending Moment = (𝑊𝐿^4) / 4",
    relief="solid",
    borderwidth=1,
    font=("Helvetica", 12),  # Set the font size
)
formula_label_bending_moment.grid(
    row=6, column=0, columnspan=2, sticky="n", padx=10, pady=(10, 0), ipady=10
)
# Substructure and Foundation Section
foundation_frame = tk.Frame(notebook, bg="lightblue")

pile_base_area_label = tk.Label(foundation_frame, text="Area of Pile Base (𝐴𝑝):")
pile_base_area_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

pile_base_area_entry = tk.Entry(foundation_frame)
pile_base_area_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)

ultimate_soil_capacity_label = tk.Label(
    foundation_frame, text="Ultimate Soil Capacity (𝑞𝑝):"
)
ultimate_soil_capacity_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

ultimate_soil_capacity_entry = tk.Entry(foundation_frame)
ultimate_soil_capacity_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

pile_side_area_label = tk.Label(foundation_frame, text="Area of Pile Side (𝐴𝑠):")
pile_side_area_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

pile_side_area_entry = tk.Entry(foundation_frame)
pile_side_area_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)

ultimate_side_resistance_label = tk.Label(
    foundation_frame, text="Ultimate Side Resistance (𝑓𝑠):"
)
ultimate_side_resistance_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

ultimate_side_resistance_entry = tk.Entry(foundation_frame)
ultimate_side_resistance_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

calculate_pile_bearing_capacity_button = tk.Button(
    foundation_frame,
    text="Calculate Pile Bearing Capacity",
    command=calculate_pile_bearing_capacity,
)
calculate_pile_bearing_capacity_button.grid(
    row=4, column=0, columnspan=2, sticky="w", padx=10, pady=10
)

pile_bearing_capacity_result_label = tk.Label(
    foundation_frame, text="Bearing Capacity of Pile Foundation: "
)
pile_bearing_capacity_result_label.grid(row=5, column=0, sticky="w", padx=10, pady=10)

formula_label_pile_bearing_capacity = tk.Label(
    foundation_frame,
    text="Formula: 𝑄𝑝 = 𝐴𝑝*𝑞𝑝 + 𝐴𝑠*𝑓𝑠",
    relief="solid",
    borderwidth=1,
    font=("Helvetica", 12),
)
formula_label_pile_bearing_capacity.grid(
    row=6, column=0, columnspan=1, sticky="n", padx=10, pady=(10, 0), ipady=10
)

# Steel Reinforcement Quantities Section
reinforcement_frame = tk.Frame(notebook, bg="lightblue")

deck_width_label = tk.Label(reinforcement_frame, text="Deck Width (mm):")
deck_width_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

deck_width_entry = tk.Entry(reinforcement_frame)
deck_width_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)

effective_depth_label = tk.Label(reinforcement_frame, text="Effective Deck Depth (mm):")
effective_depth_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

effective_depth_entry = tk.Entry(reinforcement_frame)
effective_depth_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

fc_label = tk.Label(reinforcement_frame, text="Concrete Compressive Strength (MPa):")
fc_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

fc_entry = tk.Entry(reinforcement_frame)
fc_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)

fy_label = tk.Label(reinforcement_frame, text="Yield Strength of Steel (MPa):")
fy_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

fy_entry = tk.Entry(reinforcement_frame)
fy_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

calculate_reinforcement_button = tk.Button(
    reinforcement_frame,
    text="Calculate Reinforcement Area",
    command=calculate_reinforcement_area,
)
calculate_reinforcement_button.grid(
    row=4, column=0, columnspan=2, sticky="w", padx=10, pady=10
)

reinforcement_result_label = tk.Label(
    reinforcement_frame, text="Minimum Area of Reinforcement (As): "
)
reinforcement_result_label.grid(row=5, column=0, sticky="w", padx=10, pady=10)

formula_label_reinforcement = tk.Label(
    reinforcement_frame,
    text="Formula: (𝐴𝑠)𝑚𝑖𝑛 = 0.0025 × b × d × (f'c / fy)",
    relief="solid",
    borderwidth=1,
    font=("Helvetica", 12),
)
formula_label_reinforcement.grid(
    row=6, column=0, columnspan=1, sticky="n", padx=10, pady=(10, 0), ipady=10
)


# Shear Reinforcement Section
shear_reinforcement_frame = tk.Frame(notebook, bg="lightblue")

fc_shear_label = tk.Label(
    shear_reinforcement_frame, text="Concrete Compressive Strength (MPa):"
)
fc_shear_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

fc_shear_entry = tk.Entry(shear_reinforcement_frame)
fc_shear_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)

ultimate_shear_force_label = tk.Label(
    shear_reinforcement_frame, text="Design Ultimate Shear Force (kN):"
)
ultimate_shear_force_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

ultimate_shear_force_entry = tk.Entry(shear_reinforcement_frame)
ultimate_shear_force_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

deck_width_shear_label = tk.Label(shear_reinforcement_frame, text="Deck Width (mm):")
deck_width_shear_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

deck_width_shear_entry = tk.Entry(shear_reinforcement_frame)
deck_width_shear_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)

effective_depth_shear_label = tk.Label(
    shear_reinforcement_frame, text="Effective Deck Depth (mm):"
)
effective_depth_shear_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

effective_depth_shear_entry = tk.Entry(shear_reinforcement_frame)
effective_depth_shear_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

fy_shear_label = tk.Label(
    shear_reinforcement_frame, text="Yield Strength of Steel (MPa):"
)
fy_shear_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)

fy_shear_entry = tk.Entry(shear_reinforcement_frame)
fy_shear_entry.grid(row=4, column=1, sticky="w", padx=10, pady=10)

calculate_shear_reinforcement_button = tk.Button(
    shear_reinforcement_frame,
    text="Calculate Shear Reinforcement Ratio",
    command=calculate_shear_reinforcement_ratio,
)
calculate_shear_reinforcement_button.grid(
    row=5, column=0, columnspan=2, sticky="w", padx=10, pady=10
)

shear_reinforcement_result_label = tk.Label(
    shear_reinforcement_frame, text="Minimum Shear Reinforcement Ratio (ρv): "
)
shear_reinforcement_result_label.grid(row=6, column=0, sticky="w", padx=10, pady=10)

formula_label_shear_reinforcement = tk.Label(
    shear_reinforcement_frame,
    text="Formula: (𝜌𝑣)𝑚𝑖𝑛 = (3 * √f'c * Vu) / (b * d * fy)",
    relief="solid",
    borderwidth=1,
    font=("Helvetica", 12),
)
formula_label_shear_reinforcement.grid(
    row=7, column=0, columnspan=1, sticky="n", padx=10, pady=(10, 0), ipady=10
)
# Add tabs to the Notebook
notebook.add(reinforcement_frame, text="Reinforcement Quantities")
notebook.add(shear_reinforcement_frame, text="Shear Reinforcement Ratio")
notebook.add(bridge_design_frame, text="Bridge Design")
notebook.add(foundation_frame, text="Substructure and Foundation")
notebook.add(superstructure_frame, text="Superstructure and Deck")

# Menu Bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)


# Status Bar
status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Pack the Notebook
notebook.pack(fill=tk.BOTH, expand=True)

# Run the GUI
if __name__ == "__main__":
    root.mainloop()
