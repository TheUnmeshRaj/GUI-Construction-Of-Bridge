import tkinter as tk
from tkinter import ttk

# token : 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
# last change


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
root.resizable(False, False)  # Set both width and height resizable to False

# Main Information
main_info_label = tk.Label(
    root, text="Welcome to the Bridge Construction Project", font=("Helvetica", 10)
)
main_info_label.pack()

# Create a Notebook (tabs)
notebook = ttk.Notebook(root, style="Dark.TNotebook")
# Bridge Design Section
bridge_design_frame = tk.Frame(notebook)
load_label = tk.Label(bridge_design_frame, text="Load on the Beam (𝑊):")
load_entry = tk.Entry(bridge_design_frame)

length_label = tk.Label(bridge_design_frame, text="Length of the Beam (𝐿):")
length_entry = tk.Entry(bridge_design_frame)

elasticity_label = tk.Label(bridge_design_frame, text="Modulus of Elasticity (𝐸):")
elasticity_entry = tk.Entry(bridge_design_frame)

inertia_label = tk.Label(bridge_design_frame, text="Moment of Inertia (𝐼):")
inertia_entry = tk.Entry(bridge_design_frame)

calculate_max_deflection_button = tk.Button(
    bridge_design_frame,
    text="Calculate Maximum Deflection",
    command=calculate_max_deflection,
)
max_deflection_result_label = tk.Label(bridge_design_frame, text="Maximum Deflection: ")

formula_label_max_deflection = tk.Label(
    bridge_design_frame,
    text="Formula: Maximum Deflection = (𝑊𝐿^3) / (48𝐸𝐼)",
    relief="solid",
    borderwidth=1,
)

load_label.pack()
load_entry.pack()
length_label.pack()
length_entry.pack()
elasticity_label.pack()
elasticity_entry.pack()
inertia_label.pack()
inertia_entry.pack()
calculate_max_deflection_button.pack()
max_deflection_result_label.pack()
formula_label_max_deflection.pack()

# Superstructure and Deck Section
superstructure_frame = tk.Frame(notebook)
load_beam_label = tk.Label(superstructure_frame, text="Load on the Beam (𝑊):")
load_beam_entry = tk.Entry(superstructure_frame)

length_beam_label = tk.Label(superstructure_frame, text="Length of the Beam (𝐿):")
length_beam_entry = tk.Entry(superstructure_frame)

calculate_bending_moment_button = tk.Button(
    superstructure_frame,
    text="Calculate Bending Moment",
    command=calculate_bending_moment,
)
bending_moment_result_label = tk.Label(superstructure_frame, text="Bending Moment: ")

formula_label_bending_moment = tk.Label(
    superstructure_frame,
    text="Formula: Bending Moment = (𝑊𝐿^4) / 4",
    relief="solid",
    borderwidth=1,
)

load_beam_label.pack()
load_beam_entry.pack()
length_beam_label.pack()
length_beam_entry.pack()
calculate_bending_moment_button.pack()
bending_moment_result_label.pack()
formula_label_bending_moment.pack()

# Substructure and Foundation Section
foundation_frame = tk.Frame(notebook)
pile_base_area_label = tk.Label(foundation_frame, text="Area of Pile Base (𝐴𝑝):")
pile_base_area_entry = tk.Entry(foundation_frame)

ultimate_soil_capacity_label = tk.Label(
    foundation_frame, text="Ultimate Soil Capacity (𝑞𝑝):"
)
ultimate_soil_capacity_entry = tk.Entry(foundation_frame)

pile_side_area_label = tk.Label(foundation_frame, text="Area of Pile Side (𝐴𝑠):")
pile_side_area_entry = tk.Entry(foundation_frame)

ultimate_side_resistance_label = tk.Label(
    foundation_frame, text="Ultimate Side Resistance (𝑓𝑠):"
)
ultimate_side_resistance_entry = tk.Entry(foundation_frame)

calculate_pile_bearing_capacity_button = tk.Button(
    foundation_frame,
    text="Calculate Pile Bearing Capacity",
    command=calculate_pile_bearing_capacity,
)
pile_bearing_capacity_result_label = tk.Label(
    foundation_frame, text="Bearing Capacity of Pile Foundation: "
)

formula_label_pile_bearing_capacity = tk.Label(
    foundation_frame,
    text="Formula: 𝑄𝑝 = 𝐴𝑝*𝑞𝑝 + 𝐴𝑠*𝑓𝑠",
    relief="solid",
    borderwidth=1,
)

pile_base_area_label.pack()
pile_base_area_entry.pack()
ultimate_soil_capacity_label.pack()
ultimate_soil_capacity_entry.pack()
pile_side_area_label.pack()
pile_side_area_entry.pack()
ultimate_side_resistance_label.pack()
ultimate_side_resistance_entry.pack()
calculate_pile_bearing_capacity_button.pack()
pile_bearing_capacity_result_label.pack()
formula_label_pile_bearing_capacity.pack()

# Steel Reinforcement Quantities Section
reinforcement_frame = tk.Frame(notebook)
deck_width_label = tk.Label(reinforcement_frame, text="Deck Width (mm):")
deck_width_entry = tk.Entry(reinforcement_frame)

effective_depth_label = tk.Label(reinforcement_frame, text="Effective Deck Depth (mm):")
effective_depth_entry = tk.Entry(reinforcement_frame)

fc_label = tk.Label(reinforcement_frame, text="Concrete Compressive Strength (MPa):")
fc_entry = tk.Entry(reinforcement_frame)

fy_label = tk.Label(reinforcement_frame, text="Yield Strength of Steel (MPa):")
fy_entry = tk.Entry(reinforcement_frame)

calculate_reinforcement_button = tk.Button(
    reinforcement_frame,
    text="Calculate Reinforcement Area",
    command=calculate_reinforcement_area,
)
reinforcement_result_label = tk.Label(
    reinforcement_frame, text="Minimum Area of Reinforcement (As): "
)

formula_label_reinforcement = tk.Label(
    reinforcement_frame,
    text="Formula: (𝐴𝑠)𝑚𝑖𝑛 = 0.0025 × b × d × (f'c / fy)",
    relief="solid",
    borderwidth=1,
)

deck_width_label.pack()
deck_width_entry.pack()
effective_depth_label.pack()
effective_depth_entry.pack()
fc_label.pack()
fc_entry.pack()
fy_label.pack()
fy_entry.pack()
calculate_reinforcement_button.pack()
reinforcement_result_label.pack()
formula_label_reinforcement.pack()

# Shear Reinforcement Section
shear_reinforcement_frame = tk.Frame(notebook)
fc_shear_label = tk.Label(
    shear_reinforcement_frame, text="Concrete Compressive Strength (MPa):"
)
fc_shear_entry = tk.Entry(shear_reinforcement_frame)

ultimate_shear_force_label = tk.Label(
    shear_reinforcement_frame, text="Design Ultimate Shear Force (kN):"
)
ultimate_shear_force_entry = tk.Entry(shear_reinforcement_frame)

deck_width_shear_label = tk.Label(shear_reinforcement_frame, text="Deck Width (mm):")
deck_width_shear_entry = tk.Entry(shear_reinforcement_frame)

effective_depth_shear_label = tk.Label(
    shear_reinforcement_frame, text="Effective Deck Depth (mm):"
)
effective_depth_shear_entry = tk.Entry(shear_reinforcement_frame)

fy_shear_label = tk.Label(
    shear_reinforcement_frame, text="Yield Strength of Steel (MPa):"
)
fy_shear_entry = tk.Entry(shear_reinforcement_frame)

calculate_shear_reinforcement_button = tk.Button(
    shear_reinforcement_frame,
    text="Calculate Shear Reinforcement Ratio",
    command=calculate_shear_reinforcement_ratio,
)
shear_reinforcement_result_label = tk.Label(
    shear_reinforcement_frame, text="Minimum Shear Reinforcement Ratio (ρv): "
)

formula_label_shear_reinforcement = tk.Label(
    shear_reinforcement_frame,
    text="Formula: (𝜌𝑣)𝑚𝑖𝑛 = (3 * √f'c * Vu) / (b * d * fy)",
    relief="solid",
    borderwidth=1,
)

fc_shear_label.pack()
fc_shear_entry.pack()
ultimate_shear_force_label.pack()
ultimate_shear_force_entry.pack()
deck_width_shear_label.pack()
deck_width_shear_entry.pack()
effective_depth_shear_label.pack()
effective_depth_shear_entry.pack()
fy_shear_label.pack()
fy_shear_entry.pack()
calculate_shear_reinforcement_button.pack()
shear_reinforcement_result_label.pack()
formula_label_shear_reinforcement.pack()

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
