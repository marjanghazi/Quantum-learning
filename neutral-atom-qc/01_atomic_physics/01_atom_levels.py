"""
=========================================================
01 - ATOMIC ENERGY LEVELS
Neutral-Atom Quantum Computing Learning
=========================================================

GOAL
----

Understand what atomic energy levels are and how transitions
between them relate to photon/laser energy.

Until now we used abstract states such as:

    |0>
    |1>

Now we begin connecting those ideas to atomic physics.


KEY IDEA
--------

Atoms do NOT normally have arbitrary energies.

Instead, they have discrete allowed energy levels.

Example:

    E3  -----------------
    E2  -----------------
    E1  -----------------
    E0  -----------------

An atom can move between two levels by absorbing or emitting
the correct amount of energy.


TRANSITION ENERGY
-----------------

If an atom moves from:

    E_initial

to:

    E_final

then:

    ΔE = E_final - E_initial


If:

    ΔE > 0

the atom gains energy.

This corresponds to an upward transition and normally
requires ABSORPTION of energy.


If:

    ΔE < 0

the atom loses energy.

This corresponds to a downward transition and may involve
EMISSION of a photon.


PHOTON RELATION
---------------

Photon energy is:

    E = h * frequency

or:

    E = hν

Therefore:

    ν = E / h


We can also calculate wavelength:

    λ = c / ν


IMPORTANT PHYSICS NOTE
----------------------

The energy levels in this program are EDUCATIONAL EXAMPLE
VALUES.

They are NOT calibrated energy levels of Rubidium,
Cesium or another real neutral-atom platform.

Real atoms contain:

    - electronic levels
    - hyperfine structure
    - Zeeman sublevels
    - fine structure
    - selection rules
    - polarization-dependent transitions
    - linewidths
    - many additional states

Also, having the correct photon energy does NOT automatically
mean a transition is allowed.

Real transitions must obey selection rules.

Those topics will come later.
"""


# =========================================================
# IMPORTS
# =========================================================


# math gives us basic mathematical functionality.
#
import math


# Tkinter creates the graphical interface.
#
import tkinter as tk


# ttk gives us modern GUI widgets such as:
#
#     Label
#     Button
#     Combobox
#     Frame
#
from tkinter import ttk


# ScrolledText creates a text area with a scrollbar.
#
from tkinter.scrolledtext import ScrolledText


# =========================================================
# PHYSICAL CONSTANTS
# =========================================================


# Planck's constant:
#
#     h = 6.62607015 × 10^-34 J·s
#
# This connects photon energy and frequency:
#
#     E = hν
#
PLANCK_CONSTANT = 6.62607015e-34


# Speed of light:
#
#     c = 299,792,458 m/s
#
# Used for:
#
#     λ = c / ν
#
SPEED_OF_LIGHT = 299_792_458


# One electron volt in joules:
#
#     1 eV = 1.602176634 × 10^-19 J
#
# Atomic energies are often conveniently expressed in eV.
#
EV_TO_JOULE = 1.602176634e-19


# =========================================================
# ATOMIC ENERGY MODEL
# =========================================================


class AtomLevelModel:

    """
    This class stores our EDUCATIONAL atomic energy levels.

    The model contains four example levels:

        Ground
        Excited 1
        Excited 2
        Excited 3

    Their energies are fictional educational values.

    We use them to learn:

        energy differences
        absorption
        emission
        photon frequency
        photon wavelength
    """


    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(self):

        # A Python list stores multiple items.
        #
        # Each item here is a dictionary.
        #
        # A dictionary stores:
        #
        #     key : value
        #
        # Example:
        #
        #     "name" : "Ground"
        #
        self.levels = [

            {
                "name": "Ground",
                "energy_ev": 0.0
            },

            {
                "name": "Excited 1",
                "energy_ev": 1.60
            },

            {
                "name": "Excited 2",
                "energy_ev": 2.10
            },

            {
                "name": "Excited 3",
                "energy_ev": 3.00
            }
        ]


        # Current atom position.
        #
        # Index 0 means:
        #
        #     self.levels[0]
        #
        # which is the Ground level.
        #
        self.current_level_index = 0


        # Initially select:
        #
        # Ground -> Excited 1
        #
        self.initial_index = 0

        self.final_index = 1


    # =====================================================
    # GET ONE LEVEL
    # =====================================================

    def get_level(
        self,
        index
    ):

        # Return one dictionary from the levels list.

        return self.levels[index]


    # =====================================================
    # GET ENERGY IN eV
    # =====================================================

    def energy_ev(
        self,
        index
    ):

        # Get selected level.

        level = self.get_level(
            index
        )


        # Read its energy.
        #
        # Example:
        #
        #     level["energy_ev"]
        #
        return level["energy_ev"]


    # =====================================================
    # GET ENERGY IN JOULES
    # =====================================================

    def energy_joule(
        self,
        index
    ):

        # First get energy in eV.

        energy_ev = self.energy_ev(
            index
        )


        # Convert:
        #
        #     eV -> joules
        #
        energy_joule = (

            energy_ev

            *

            EV_TO_JOULE
        )


        return energy_joule


    # =====================================================
    # ENERGY DIFFERENCE IN eV
    # =====================================================

    def delta_energy_ev(self):

        # Initial energy.

        initial_energy = self.energy_ev(
            self.initial_index
        )


        # Final energy.

        final_energy = self.energy_ev(
            self.final_index
        )


        # Calculate:
        #
        #     ΔE = E_final - E_initial
        #
        delta = (

            final_energy

            -

            initial_energy
        )


        return delta


    # =====================================================
    # ABSOLUTE TRANSITION ENERGY
    # =====================================================

    def photon_energy_ev(self):

        # A photon has positive energy.
        #
        # Therefore we use the MAGNITUDE:
        #
        #     |ΔE|
        #
        return abs(
            self.delta_energy_ev()
        )


    # =====================================================
    # TRANSITION ENERGY IN JOULES
    # =====================================================

    def photon_energy_joule(self):

        # Obtain transition energy in eV.

        energy_ev = (
            self.photon_energy_ev()
        )


        # Convert to joules.

        return (

            energy_ev

            *

            EV_TO_JOULE
        )


    # =====================================================
    # PHOTON FREQUENCY
    # =====================================================

    def photon_frequency(self):

        # Photon relation:
        #
        #     E = hν
        #
        # Therefore:
        #
        #         E
        #     ν = -
        #         h


        energy = (
            self.photon_energy_joule()
        )


        # If initial and final levels are identical:
        #
        #     ΔE = 0
        #
        # so there is no transition frequency.

        if energy == 0:

            return 0.0


        frequency = (

            energy

            /

            PLANCK_CONSTANT
        )


        return frequency


    # =====================================================
    # PHOTON WAVELENGTH
    # =====================================================

    def photon_wavelength(self):

        # First calculate photon frequency.

        frequency = (
            self.photon_frequency()
        )


        # Avoid division by zero.

        if frequency == 0:

            return math.inf


        # Relation:
        #
        #         c
        #     λ = -
        #         ν
        #
        wavelength = (

            SPEED_OF_LIGHT

            /

            frequency
        )


        return wavelength


    # =====================================================
    # TRANSITION TYPE
    # =====================================================

    def transition_type(self):

        # Calculate signed energy difference.

        delta = (
            self.delta_energy_ev()
        )


        # Higher final energy:
        #
        #     atom must gain energy.
        #
        if delta > 0:

            return "absorption"


        # Lower final energy:
        #
        #     atom loses energy.
        #
        if delta < 0:

            return "emission"


        # Same level.

        return "no transition"


    # =====================================================
    # SET TRANSITION
    # =====================================================

    def set_transition(
        self,
        initial_index,
        final_index
    ):

        # Store selected starting level.

        self.initial_index = (
            initial_index
        )


        # Store selected target level.

        self.final_index = (
            final_index
        )


    # =====================================================
    # APPLY EDUCATIONAL TRANSITION
    # =====================================================

    def apply_transition(self):

        # IMPORTANT:
        #
        # This does NOT simulate real atomic transition dynamics.
        #
        # It simply changes our educational model's
        # current level to the selected final level.

        self.current_level_index = (
            self.final_index
        )


# =========================================================
# GUI
# =========================================================


class AtomLevelsGUI:

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(
        self,
        root
    ):

        # Store main Tkinter window.

        self.root = root


        # Window title.

        self.root.title(
            "Neutral-Atom QC | Atomic Physics 01 — Atom Levels"
        )


        # Starting window size.

        self.root.geometry(
            "1400x900"
        )


        # Minimum allowed window size.

        self.root.minsize(
            1100,
            750
        )


        # -------------------------------------------------
        # CREATE PHYSICS MODEL
        # -------------------------------------------------

        self.model = AtomLevelModel()


        # -------------------------------------------------
        # BUILD INTERFACE
        # -------------------------------------------------

        self.setup_style()

        self.create_header()

        self.create_main_area()

        self.create_learning_area()


        # Display initial transition.

        self.update_display()


        # Show initial explanation.

        self.show_lesson(

            title="Atomic energy-level model initialized",

            explanation=(
                "We now stop treating |0⟩ and |1⟩ as completely "
                "abstract labels and begin thinking about real "
                "atomic energy structure.\n\n"

                "An atom can occupy specific allowed energy levels.\n\n"

                "In this educational model the atom begins in:\n\n"

                "    Ground = 0.00 eV\n\n"

                "and we initially examine the transition:\n\n"

                "    Ground → Excited 1\n\n"

                "The energies used here are fictional example "
                "values, not calibrated data for a real atom."
            ),

            python_code=(
                "self.model = AtomLevelModel()\n\n"

                "# AtomLevelModel.__init__() creates:\n\n"

                "self.levels = [\n"
                "    {'name': 'Ground', 'energy_ev': 0.0},\n"
                "    {'name': 'Excited 1', 'energy_ev': 1.60},\n"
                "    ...\n"
                "]\n\n"

                "# The list represents our allowed energy levels."
            )
        )


    # =====================================================
    # STYLE
    # =====================================================

    def setup_style(self):

        # Create ttk style manager.

        style = ttk.Style()


        try:

            style.theme_use(
                "clam"
            )

        except tk.TclError:

            pass


        style.configure(

            "Title.TLabel",

            font=(
                "Segoe UI",
                22,
                "bold"
            )
        )


        style.configure(

            "Section.TLabel",

            font=(
                "Segoe UI",
                14,
                "bold"
            )
        )


        style.configure(

            "Value.TLabel",

            font=(
                "Consolas",
                11
            )
        )


        style.configure(

            "Action.TButton",

            font=(
                "Segoe UI",
                10,
                "bold"
            ),

            padding=7
        )


    # =====================================================
    # HEADER
    # =====================================================

    def create_header(self):

        # Header container.

        header = ttk.Frame(

            self.root,

            padding=(
                20,
                15
            )
        )


        header.pack(
            fill="x"
        )


        ttk.Label(

            header,

            text="Neutral-Atom Quantum Computing",

            style="Title.TLabel"

        ).pack(
            anchor="w"
        )


        ttk.Label(

            header,

            text="Atomic Physics 01 — Atomic Energy Levels",

            style="Section.TLabel"

        ).pack(
            anchor="w"
        )


        ttk.Label(

            header,

            text=(
                "Discrete energies, transitions, photons, "
                "frequency and wavelength"
            )

        ).pack(
            anchor="w",
            pady=(3, 0)
        )


    # =====================================================
    # MAIN AREA
    # =====================================================

    def create_main_area(self):

        main = ttk.Frame(

            self.root,

            padding=(
                20,
                0,
                20,
                10
            )
        )


        main.pack(

            fill="both",

            expand=True
        )


        # Left visualization gets more space.

        main.columnconfigure(
            0,
            weight=3
        )


        main.columnconfigure(
            1,
            weight=2
        )


        main.rowconfigure(
            0,
            weight=1
        )


        # =================================================
        # LEFT SIDE
        # =================================================

        left = ttk.LabelFrame(

            main,

            text="Atomic Energy-Level Diagram",

            padding=10
        )


        left.grid(

            row=0,

            column=0,

            sticky="nsew",

            padx=(0, 8)
        )


        # Canvas lets us draw:
        #
        #     energy levels
        #     labels
        #     transition arrows
        #
        self.canvas = tk.Canvas(

            left,

            bg="white",

            highlightthickness=0
        )


        self.canvas.pack(

            fill="both",

            expand=True
        )


        # Whenever the window changes size,
        # redraw the diagram.

        self.canvas.bind(

            "<Configure>",

            self.canvas_resized
        )


        ttk.Label(

            left,

            text=(
                "The horizontal lines represent allowed energy levels. "
                "The arrow shows the selected transition. "
                "This is a simplified educational diagram."
            ),

            wraplength=700

        ).pack(
            fill="x",
            pady=(5, 0)
        )


        # =================================================
        # RIGHT SIDE
        # =================================================

        right = ttk.Frame(
            main
        )


        right.grid(

            row=0,

            column=1,

            sticky="nsew",

            padx=(8, 0)
        )


        # -------------------------------------------------
        # CURRENT ATOM LEVEL
        # -------------------------------------------------

        current_frame = ttk.LabelFrame(

            right,

            text="1. Current Atomic Level",

            padding=10
        )


        current_frame.pack(

            fill="x",

            pady=(0, 5)
        )


        self.current_level_label = ttk.Label(

            current_frame,

            font=(
                "Segoe UI",
                12,
                "bold"
            )
        )


        self.current_level_label.pack(
            anchor="w"
        )


        self.current_energy_label = ttk.Label(

            current_frame,

            style="Value.TLabel"
        )


        self.current_energy_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # SELECT TRANSITION
        # -------------------------------------------------

        select_frame = ttk.LabelFrame(

            right,

            text="2. Select Transition",

            padding=10
        )


        select_frame.pack(

            fill="x",

            pady=5
        )


        # Create readable names:
        #
        # Ground
        # Excited 1
        # Excited 2
        # Excited 3

        level_names = [

            level["name"]

            for level in self.model.levels
        ]


        # INITIAL LEVEL

        ttk.Label(

            select_frame,

            text="Initial level:"
        ).pack(
            anchor="w"
        )


        self.initial_var = tk.StringVar(

            value=level_names[
                self.model.initial_index
            ]
        )


        self.initial_combo = ttk.Combobox(

            select_frame,

            values=level_names,

            textvariable=self.initial_var,

            state="readonly"
        )


        self.initial_combo.pack(

            fill="x",

            pady=(2, 6)
        )


        # When user chooses another item:
        #
        # <<ComboboxSelected>>
        #
        # Tkinter calls transition_changed().

        self.initial_combo.bind(

            "<<ComboboxSelected>>",

            self.transition_changed
        )


        # FINAL LEVEL

        ttk.Label(

            select_frame,

            text="Final level:"
        ).pack(
            anchor="w"
        )


        self.final_var = tk.StringVar(

            value=level_names[
                self.model.final_index
            ]
        )


        self.final_combo = ttk.Combobox(

            select_frame,

            values=level_names,

            textvariable=self.final_var,

            state="readonly"
        )


        self.final_combo.pack(

            fill="x",

            pady=(2, 0)
        )


        self.final_combo.bind(

            "<<ComboboxSelected>>",

            self.transition_changed
        )


        # -------------------------------------------------
        # ENERGY INFORMATION
        # -------------------------------------------------

        energy_frame = ttk.LabelFrame(

            right,

            text="3. Transition Energy",

            padding=10
        )


        energy_frame.pack(

            fill="x",

            pady=5
        )


        self.initial_energy_label = ttk.Label(

            energy_frame,

            style="Value.TLabel"
        )


        self.initial_energy_label.pack(
            anchor="w"
        )


        self.final_energy_label = ttk.Label(

            energy_frame,

            style="Value.TLabel"
        )


        self.final_energy_label.pack(
            anchor="w"
        )


        self.delta_energy_label = ttk.Label(

            energy_frame,

            style="Value.TLabel"
        )


        self.delta_energy_label.pack(
            anchor="w"
        )


        self.photon_energy_label = ttk.Label(

            energy_frame,

            style="Value.TLabel"
        )


        self.photon_energy_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # TRANSITION TYPE
        # -------------------------------------------------

        type_frame = ttk.LabelFrame(

            right,

            text="4. Physical Interpretation",

            padding=10
        )


        type_frame.pack(

            fill="x",

            pady=5
        )


        self.transition_type_label = ttk.Label(

            type_frame,

            font=(
                "Segoe UI",
                11,
                "bold"
            )
        )


        self.transition_type_label.pack(
            anchor="w"
        )


        self.interpretation_label = ttk.Label(

            type_frame,

            wraplength=420,

            justify="left"
        )


        self.interpretation_label.pack(

            anchor="w",

            pady=(3, 0)
        )


        # -------------------------------------------------
        # PHOTON INFORMATION
        # -------------------------------------------------

        photon_frame = ttk.LabelFrame(

            right,

            text="5. Matching Photon / Laser",

            padding=10
        )


        photon_frame.pack(

            fill="x",

            pady=5
        )


        self.frequency_label = ttk.Label(

            photon_frame,

            style="Value.TLabel"
        )


        self.frequency_label.pack(
            anchor="w"
        )


        self.thz_label = ttk.Label(

            photon_frame,

            style="Value.TLabel"
        )


        self.thz_label.pack(
            anchor="w"
        )


        self.wavelength_m_label = ttk.Label(

            photon_frame,

            style="Value.TLabel"
        )


        self.wavelength_m_label.pack(
            anchor="w"
        )


        self.wavelength_nm_label = ttk.Label(

            photon_frame,

            style="Value.TLabel"
        )


        self.wavelength_nm_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # FORMULAS
        # -------------------------------------------------

        formula_frame = ttk.LabelFrame(

            right,

            text="6. Equations Being Used",

            padding=10
        )


        formula_frame.pack(

            fill="x",

            pady=5
        )


        ttk.Label(

            formula_frame,

            text=(
                "ΔE = Efinal − Einitial\n\n"
                "|ΔE| = hν\n\n"
                "ν = |ΔE| / h\n\n"
                "λ = c / ν"
            ),

            font=(
                "Cambria Math",
                11
            ),

            justify="left"

        ).pack(
            anchor="w"
        )


        # -------------------------------------------------
        # ACTION
        # -------------------------------------------------

        action_frame = ttk.LabelFrame(

            right,

            text="7. Educational Transition",

            padding=10
        )


        action_frame.pack(

            fill="x",

            pady=5
        )


        ttk.Button(

            action_frame,

            text="Illustrate Selected Transition",

            command=self.apply_transition,

            style="Action.TButton"

        ).pack(
            fill="x"
        )


        self.action_result_label = ttk.Label(

            action_frame,

            text=(
                "No transition illustrated yet."
            ),

            justify="center"
        )


        self.action_result_label.pack(

            fill="x",

            pady=(5, 0)
        )


        ttk.Label(

            action_frame,

            text=(
                "This button changes the educational model's "
                "current level. It does NOT simulate real "
                "transition probability or selection rules."
            ),

            wraplength=420,

            justify="left"

        ).pack(

            anchor="w",

            pady=(5, 0)
        )


    # =====================================================
    # LEARNING CONSOLE
    # =====================================================

    def create_learning_area(self):

        learning = ttk.LabelFrame(

            self.root,

            text="Python + Atomic Physics Learning Console",

            padding=10
        )


        learning.pack(

            fill="both",

            padx=20,

            pady=(0, 15)
        )


        notebook = ttk.Notebook(
            learning
        )


        notebook.pack(

            fill="both",

            expand=True
        )


        # -------------------------------------------------
        # PHYSICS TAB
        # -------------------------------------------------

        concept_tab = ttk.Frame(
            notebook
        )


        notebook.add(

            concept_tab,

            text="What is happening?"
        )


        self.lesson_text = ScrolledText(

            concept_tab,

            height=8,

            wrap="word",

            font=(
                "Segoe UI",
                10
            )
        )


        self.lesson_text.pack(

            fill="both",

            expand=True
        )


        # -------------------------------------------------
        # PYTHON TAB
        # -------------------------------------------------

        code_tab = ttk.Frame(
            notebook
        )


        notebook.add(

            code_tab,

            text="Python behind this action"
        )


        self.code_text = ScrolledText(

            code_tab,

            height=8,

            wrap="word",

            font=(
                "Consolas",
                10
            )
        )


        self.code_text.pack(

            fill="both",

            expand=True
        )


        # -------------------------------------------------
        # NEW PYTHON CONCEPTS
        # -------------------------------------------------

        python_tab = ttk.Frame(
            notebook
        )


        notebook.add(

            python_tab,

            text="New Python concepts"
        )


        python_guide = ScrolledText(

            python_tab,

            height=8,

            wrap="word",

            font=(
                "Segoe UI",
                10
            )
        )


        python_guide.pack(

            fill="both",

            expand=True
        )


        python_guide.insert(

            "1.0",

            """
NEW PYTHON / PHYSICS CONCEPTS IN THIS FILE
==========================================


1. LIST OF DICTIONARIES

   self.levels = [
       {
           "name": "Ground",
           "energy_ev": 0.0
       },
       ...
   ]

   A list stores several objects.

   Each dictionary stores information about one level.


2. ACCESSING A LIST

   self.levels[0]

   means:

       get item number 0


3. ACCESSING A DICTIONARY

   level["energy_ev"]

   means:

       get the value stored under "energy_ev"


4. LIST COMPREHENSION

   level_names = [
       level["name"]
       for level in self.model.levels
   ]

   This loops through the levels and creates
   a new list containing only their names.


5. COMBOBOX

   ttk.Combobox(...)

   creates a dropdown selection widget.


6. EVENT BINDING

   combo.bind(
       "<<ComboboxSelected>>",
       function
   )

   means:

       when selection changes
           ↓
       call the function


7. SCIENTIFIC NOTATION

   6.62607015e-34

   means:

       6.62607015 × 10^-34


8. PHYSICAL CONSTANTS

   We store important constants once:

       PLANCK_CONSTANT
       SPEED_OF_LIGHT
       EV_TO_JOULE


9. UNIT CONVERSION

   energy_joule = energy_ev * EV_TO_JOULE


10. ABSOLUTE VALUE

    abs(delta_energy)

    removes the sign.

    Photon energy must be positive even though ΔE
    tells us whether the atomic transition is
    upward or downward.


11. MODEL VS GUI

    AtomLevelModel
        ↓
    physics calculations

    AtomLevelsGUI
        ↓
    visualization and interaction
"""
        )


        python_guide.config(
            state="disabled"
        )


    # =====================================================
    # SHOW LESSON
    # =====================================================

    def show_lesson(

        self,

        title,

        explanation,

        python_code
    ):

        # Unlock physics explanation.

        self.lesson_text.config(
            state="normal"
        )


        # Delete previous explanation.

        self.lesson_text.delete(
            "1.0",
            tk.END
        )


        # Insert new explanation.

        self.lesson_text.insert(

            tk.END,

            f"{title}\n\n{explanation}"
        )


        # Lock it again.

        self.lesson_text.config(
            state="disabled"
        )


        # Do same with Python code.

        self.code_text.config(
            state="normal"
        )


        self.code_text.delete(
            "1.0",
            tk.END
        )


        self.code_text.insert(

            tk.END,

            python_code
        )


        self.code_text.config(
            state="disabled"
        )


    # =====================================================
    # FIND LEVEL INDEX FROM NAME
    # =====================================================

    def index_from_name(

        self,

        name
    ):

        # enumerate() gives us:
        #
        #     index
        #     item
        #
        # while looping through a list.

        for index, level in enumerate(
            self.model.levels
        ):

            # Compare current level's name.

            if level["name"] == name:

                return index


        # Fallback.

        return 0


    # =====================================================
    # TRANSITION SELECTION CHANGED
    # =====================================================

    def transition_changed(

        self,

        event=None
    ):

        # Read selected names from the GUI.

        initial_name = (
            self.initial_var.get()
        )


        final_name = (
            self.final_var.get()
        )


        # Convert names into list indices.

        initial_index = self.index_from_name(
            initial_name
        )


        final_index = self.index_from_name(
            final_name
        )


        # Store transition inside physics model.

        self.model.set_transition(

            initial_index,

            final_index
        )


        # Update everything visible.

        self.update_display()


        # Read useful calculated quantities.

        delta_ev = (
            self.model.delta_energy_ev()
        )


        transition_type = (
            self.model.transition_type()
        )


        self.show_lesson(

            title="Transition selection changed",

            explanation=(
                f"You selected:\n\n"

                f"    {initial_name}\n"
                f"        ↓\n"
                f"    {final_name}\n\n"

                f"The calculated energy difference is:\n\n"

                f"    ΔE = {delta_ev:.4f} eV\n\n"

                f"This is an {transition_type} transition.\n\n"

                "Python now uses |ΔE| to calculate the "
                "photon frequency and wavelength associated "
                "with this energy gap."
            ),

            python_code=(
                "initial_name = self.initial_var.get()\n"
                "final_name = self.final_var.get()\n\n"

                "initial_index = self.index_from_name(initial_name)\n"
                "final_index = self.index_from_name(final_name)\n\n"

                "self.model.set_transition(\n"
                "    initial_index,\n"
                "    final_index\n"
                ")\n\n"

                "# Then:\n\n"

                "delta_energy = (\n"
                "    final_energy\n"
                "    - initial_energy\n"
                ")"
            )
        )


    # =====================================================
    # UPDATE DISPLAY
    # =====================================================

    def update_display(self):

        # -------------------------------------------------
        # CURRENT LEVEL
        # -------------------------------------------------

        current_level = self.model.get_level(

            self.model.current_level_index
        )


        self.current_level_label.config(

            text=(
                f"Current level: "
                f"{current_level['name']}"
            )
        )


        self.current_energy_label.config(

            text=(
                "Current energy = "
                f"{current_level['energy_ev']:.4f} eV"
            )
        )


        # -------------------------------------------------
        # INITIAL + FINAL ENERGY
        # -------------------------------------------------

        initial_energy = self.model.energy_ev(

            self.model.initial_index
        )


        final_energy = self.model.energy_ev(

            self.model.final_index
        )


        delta_energy = (
            self.model.delta_energy_ev()
        )


        photon_energy_ev = (
            self.model.photon_energy_ev()
        )


        photon_energy_joule = (
            self.model.photon_energy_joule()
        )


        self.initial_energy_label.config(

            text=(
                "E_initial = "
                f"{initial_energy:.4f} eV"
            )
        )


        self.final_energy_label.config(

            text=(
                "E_final   = "
                f"{final_energy:.4f} eV"
            )
        )


        self.delta_energy_label.config(

            text=(
                "ΔE = E_final − E_initial = "
                f"{delta_energy:.4f} eV"
            )
        )


        self.photon_energy_label.config(

            text=(
                "|ΔE| = "
                f"{photon_energy_ev:.4f} eV "
                f"= {photon_energy_joule:.4e} J"
            )
        )


        # -------------------------------------------------
        # TRANSITION TYPE
        # -------------------------------------------------

        transition_type = (
            self.model.transition_type()
        )


        if transition_type == "absorption":

            heading = (
                "↑ ABSORPTION / UPWARD TRANSITION"
            )


            explanation = (
                "The final level has more energy than the "
                "initial level. The atom must gain energy. "
                "In a simplified picture, a matching photon "
                "can supply that energy."
            )


        elif transition_type == "emission":

            heading = (
                "↓ EMISSION / DOWNWARD TRANSITION"
            )


            explanation = (
                "The final level has less energy than the "
                "initial level. The atom loses energy. "
                "That energy can appear as an emitted photon."
            )


        else:

            heading = (
                "NO ENERGY-LEVEL CHANGE"
            )


            explanation = (
                "The selected initial and final levels are "
                "the same, so ΔE = 0."
            )


        self.transition_type_label.config(
            text=heading
        )


        self.interpretation_label.config(
            text=explanation
        )


        # -------------------------------------------------
        # PHOTON DATA
        # -------------------------------------------------

        frequency = (
            self.model.photon_frequency()
        )


        wavelength = (
            self.model.photon_wavelength()
        )


        self.frequency_label.config(

            text=(
                f"ν = {frequency:.4e} Hz"
            )
        )


        self.thz_label.config(

            text=(
                "ν = "
                f"{frequency / 1e12:.4f} THz"
            )
        )


        # Handle infinite wavelength.

        if math.isinf(
            wavelength
        ):

            wavelength_text = "∞"

            wavelength_nm_text = "∞"

        else:

            wavelength_text = (
                f"{wavelength:.4e} m"
            )


            wavelength_nm_text = (
                f"{wavelength * 1e9:.2f} nm"
            )


        self.wavelength_m_label.config(

            text=(
                f"λ = {wavelength_text}"
            )
        )


        self.wavelength_nm_label.config(

            text=(
                f"λ = {wavelength_nm_text}"
            )
        )


        # Draw energy levels.

        self.draw_levels()


    # =====================================================
    # CANVAS RESIZED
    # =====================================================

    def canvas_resized(

        self,

        event
    ):

        # Redraw energy-level diagram
        # whenever available space changes.

        self.draw_levels()


    # =====================================================
    # DRAW ENERGY LEVELS
    # =====================================================

    def draw_levels(self):

        # Remove previous drawing.

        self.canvas.delete(
            "all"
        )


        # Get current canvas size.

        width = (
            self.canvas.winfo_width()
        )


        height = (
            self.canvas.winfo_height()
        )


        # Tkinter can briefly report tiny sizes
        # when the GUI first starts.

        if width < 100:

            width = 700


        if height < 100:

            height = 500


        # -------------------------------------------------
        # DRAW TITLE
        # -------------------------------------------------

        self.canvas.create_text(

            width / 2,

            30,

            text="Simplified Atomic Energy Structure",

            font=(
                "Segoe UI",
                14,
                "bold"
            )
        )


        # -------------------------------------------------
        # ENERGY AXIS
        # -------------------------------------------------

        axis_x = 70


        top_margin = 80

        bottom_margin = 70


        self.canvas.create_line(

            axis_x,

            height - bottom_margin,

            axis_x,

            top_margin,

            arrow=tk.LAST,

            width=2
        )


        self.canvas.create_text(

            axis_x - 25,

            (
                top_margin
                +
                height
                -
                bottom_margin
            ) / 2,

            text="Energy",

            angle=90,

            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )


        # -------------------------------------------------
        # DETERMINE ENERGY SCALE
        # -------------------------------------------------

        energies = [

            level["energy_ev"]

            for level in self.model.levels
        ]


        max_energy = max(
            energies
        )


        # Avoid division by zero.

        if max_energy == 0:

            max_energy = 1.0


        usable_height = (

            height

            -

            top_margin

            -

            bottom_margin
        )


        # Dictionary will store the y coordinate
        # of every energy level.

        level_positions = {}


        # -------------------------------------------------
        # DRAW EACH LEVEL
        # -------------------------------------------------

        for index, level in enumerate(
            self.model.levels
        ):

            energy = (
                level["energy_ev"]
            )


            # Higher energy must appear HIGHER
            # on the canvas.
            #
            # Canvas y increases downward,
            # so we subtract from bottom position.

            y = (

                height
                -
                bottom_margin

                -

                (
                    energy
                    /
                    max_energy
                )

                *
                usable_height
            )


            # Save y coordinate.

            level_positions[index] = y


            # Draw horizontal energy line.

            self.canvas.create_line(

                width * 0.23,

                y,

                width * 0.72,

                y,

                width=3
            )


            # Level name.

            self.canvas.create_text(

                width * 0.20,

                y,

                text=(
                    level["name"]
                ),

                font=(
                    "Segoe UI",
                    11,
                    "bold"
                ),

                anchor="e"
            )


            # Energy value.

            self.canvas.create_text(

                width * 0.75,

                y,

                text=(
                    f"{energy:.2f} eV"
                ),

                font=(
                    "Consolas",
                    10
                ),

                anchor="w"
            )


            # Mark current atomic level.

            if (
                index
                ==
                self.model.current_level_index
            ):

                self.canvas.create_text(

                    width * 0.48,

                    y - 20,

                    text="● current atom",

                    font=(
                        "Segoe UI",
                        10,
                        "bold"
                    )
                )


        # -------------------------------------------------
        # DRAW SELECTED TRANSITION
        # -------------------------------------------------

        initial_y = level_positions[

            self.model.initial_index
        ]


        final_y = level_positions[

            self.model.final_index
        ]


        arrow_x = (
            width * 0.58
        )


        # If levels differ,
        # draw an arrow.

        if (
            self.model.initial_index
            !=
            self.model.final_index
        ):

            self.canvas.create_line(

                arrow_x,

                initial_y,

                arrow_x,

                final_y,

                arrow=tk.LAST,

                width=4
            )


            # Label transition.

            middle_y = (

                initial_y

                +
                final_y

            ) / 2


            transition_type = (
                self.model.transition_type()
            )


            self.canvas.create_text(

                arrow_x + 25,

                middle_y,

                text=transition_type,

                font=(
                    "Segoe UI",
                    10,
                    "bold"
                ),

                anchor="w"
            )


        else:

            self.canvas.create_text(

                width / 2,

                height - 30,

                text=(
                    "Select two different levels "
                    "to visualize a transition."
                ),

                font=(
                    "Segoe UI",
                    10
                )
            )


    # =====================================================
    # APPLY EDUCATIONAL TRANSITION
    # =====================================================

    def apply_transition(self):

        # Get transition type BEFORE changing
        # the current level.

        transition_type = (
            self.model.transition_type()
        )


        initial_level = self.model.get_level(

            self.model.initial_index
        )


        final_level = self.model.get_level(

            self.model.final_index
        )


        # If same level:
        #
        # there is nothing to change.

        if transition_type == "no transition":

            self.action_result_label.config(

                text=(
                    "Initial and final levels are the same."
                )
            )


            self.show_lesson(

                title="No transition",

                explanation=(
                    "You selected the same atomic level as both "
                    "the initial and final state.\n\n"

                    "Therefore:\n\n"

                    "    ΔE = 0\n\n"

                    "No transition energy is required."
                ),

                python_code=(
                    "if transition_type == 'no transition':\n"
                    "    # nothing changes\n"
                    "    ..."
                )
            )


            return


        # Update educational model's current level.

        self.model.apply_transition()


        # Refresh GUI.

        self.update_display()


        self.action_result_label.config(

            text=(
                f"Illustrated: "
                f"{initial_level['name']} "
                f"→ {final_level['name']}"
            )
        )


        # -------------------------------------------------
        # EXPLANATION
        # -------------------------------------------------

        delta_ev = (
            self.model.delta_energy_ev()
        )


        frequency = (
            self.model.photon_frequency()
        )


        wavelength_nm = (

            self.model.photon_wavelength()

            *

            1e9
        )


        if transition_type == "absorption":

            physical_text = (
                "The target level is higher, so the atom must "
                "gain energy. In the simple photon picture, "
                "a matching photon is absorbed."
            )


        else:

            physical_text = (
                "The target level is lower, so the atom loses "
                "energy. In the simple photon picture, that "
                "energy can be emitted as a photon."
            )


        self.show_lesson(

            title="Educational transition illustrated",

            explanation=(
                f"{initial_level['name']} "
                f"→ {final_level['name']}\n\n"

                f"ΔE = {delta_ev:.4f} eV\n\n"

                f"{physical_text}\n\n"

                "The corresponding photon has approximately:\n\n"

                f"    frequency = "
                f"{frequency / 1e12:.3f} THz\n\n"

                f"    wavelength = "
                f"{wavelength_nm:.2f} nm\n\n"

                "IMPORTANT:\n\n"

                "The GUI simply moved the educational atom marker. "
                "A real transition also depends on coupling strength, "
                "selection rules, pulse duration and other physics."
            ),

            python_code=(
                "self.model.apply_transition()\n\n"

                "# Inside the model:\n\n"

                "self.current_level_index = self.final_index\n\n"

                "# This does NOT solve atomic dynamics.\n"
                "# It simply changes the level shown in the GUI."
            )
        )


# =========================================================
# START APPLICATION
# =========================================================


if __name__ == "__main__":

    # This message appears in PowerShell.

    print(
        "Running 01_atom_levels.py ..."
    )


    # Create Tkinter's main application window.

    root = tk.Tk()


    # Create our GUI object.

    app = AtomLevelsGUI(
        root
    )


    # Keep GUI alive and listen for events.

    root.mainloop()