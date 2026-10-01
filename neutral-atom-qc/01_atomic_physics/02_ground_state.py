"""
=========================================================
02 - GROUND STATE
Neutral-Atom Quantum Computing Learning
=========================================================

GOAL
----

Understand what an atomic ground state really means.

The ground state is:

    the LOWEST allowed energy state of the atom.

It does NOT necessarily mean:

    "the atom has zero energy"

The number 0 can simply be our chosen energy reference.


IMPORTANT IDEA
--------------

Suppose an atom has these example energies:

    E3 = -0.9 eV
    E2 = -2.2 eV
    E1 = -3.4 eV
    E0 = -5.0 eV

The LOWEST value is:

    -5.0 eV

Therefore:

    E0 is the ground state.


ENERGY REFERENCE
----------------

We are allowed to shift all energies by the same amount.

Example:

Original:

    Ground = -5.0 eV
    E1     = -3.4 eV

Energy gap:

    ΔE = -3.4 - (-5.0)
       = 1.6 eV


Now shift everything by +5 eV:

    Ground = 0.0 eV
    E1     = 1.6 eV

Energy gap:

    ΔE = 1.6 - 0
       = 1.6 eV

The gap did NOT change.

This is extremely important:

    absolute reference can change
              ↓
    energy difference stays the same


NEUTRAL-ATOM CONNECTION
-----------------------

In neutral-atom quantum computing, the computational qubit
does NOT always mean:

    ground state = |0>
    excited electronic state = |1>

Often, two long-lived internal states inside the electronic
ground-state manifold are used as |0> and |1>.

Rydberg states can then be used temporarily when strong
atom-atom interactions are needed.


IMPORTANT PHYSICS NOTE
----------------------

The energy levels in this program are EDUCATIONAL EXAMPLE
VALUES.

They do NOT represent a specific Rubidium, Cesium, Strontium,
Ytterbium or other real atom.

Real atomic structure contains:

    electronic levels
    fine structure
    hyperfine structure
    Zeeman sublevels
    selection rules
    linewidths
    many other effects
"""


# =========================================================
# IMPORTS
# =========================================================


# math gives us:
#
#     infinity
#     mathematical helpers
#
import math


# Tkinter creates our GUI.
#
import tkinter as tk


# ttk gives us modern widgets.
#
from tkinter import ttk


# ScrolledText creates a text box
# with a vertical scrollbar.
#
from tkinter.scrolledtext import ScrolledText


# =========================================================
# PHYSICAL CONSTANTS
# =========================================================


# Planck constant:
#
#     h = 6.62607015 × 10^-34 J·s
#
PLANCK_CONSTANT = 6.62607015e-34


# Speed of light:
#
#     c = 299,792,458 m/s
#
SPEED_OF_LIGHT = 299_792_458


# Conversion:
#
#     1 eV = 1.602176634 × 10^-19 J
#
EV_TO_JOULE = 1.602176634e-19


# =========================================================
# GROUND-STATE MODEL
# =========================================================


class GroundStateModel:

    """
    This class contains the atomic-energy mathematics.

    It stores a few EDUCATIONAL energy levels and determines:

        - which one is the ground state
        - the energy gap from ground to another level
        - the matching photon frequency
        - the matching wavelength

    It also lets us shift the displayed energy reference.
    """


    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(self):

        # Store several example atomic levels.
        #
        # Each dictionary contains:
        #
        #     name
        #     energy_ev
        #
        # These values are fictional educational values.

        self.levels = [

            {
                "name": "Level 0",
                "energy_ev": -5.0
            },

            {
                "name": "Level 1",
                "energy_ev": -3.4
            },

            {
                "name": "Level 2",
                "energy_ev": -2.2
            },

            {
                "name": "Level 3",
                "energy_ev": -0.9
            }
        ]


        # Energy-reference offset.
        #
        # Initially:
        #
        #     offset = 0
        #
        # means display the stored values directly.

        self.reference_offset = 0.0


        # Find the ground state automatically.

        self.ground_index = (
            self.find_ground_state()
        )


        # The atom initially starts in the ground state.

        self.current_level_index = (
            self.ground_index
        )


        # Select Level 1 as the initial comparison level.

        self.selected_level_index = 1


    # =====================================================
    # FIND GROUND STATE
    # =====================================================

    def find_ground_state(self):

        # range(len(self.levels)) gives:
        #
        #     0, 1, 2, 3
        #
        # min(..., key=...) asks:
        #
        #     which index has the LOWEST energy?
        #
        ground_index = min(

            range(
                len(self.levels)
            ),

            key=lambda index:
                self.levels[index]["energy_ev"]
        )


        return ground_index


    # =====================================================
    # GET LEVEL
    # =====================================================

    def get_level(
        self,
        index
    ):

        return self.levels[index]


    # =====================================================
    # TRUE / STORED ENERGY
    # =====================================================

    def stored_energy(
        self,
        index
    ):

        level = self.get_level(
            index
        )


        return level["energy_ev"]


    # =====================================================
    # DISPLAYED ENERGY
    # =====================================================

    def displayed_energy(
        self,
        index
    ):

        # Shift all energy values by exactly
        # the same reference offset.

        return (

            self.stored_energy(index)

            +

            self.reference_offset
        )


    # =====================================================
    # GROUND ENERGY
    # =====================================================

    def ground_energy(self):

        return self.stored_energy(
            self.ground_index
        )


    # =====================================================
    # DISPLAYED GROUND ENERGY
    # =====================================================

    def displayed_ground_energy(self):

        return self.displayed_energy(
            self.ground_index
        )


    # =====================================================
    # ENERGY GAP FROM GROUND
    # =====================================================

    def energy_gap_from_ground(
        self,
        target_index=None
    ):

        # If no target is given,
        # use the level selected by the user.

        if target_index is None:

            target_index = (
                self.selected_level_index
            )


        # Target energy.

        target_energy = (
            self.stored_energy(
                target_index
            )
        )


        # Ground energy.

        ground_energy = (
            self.ground_energy()
        )


        # Calculate:
        #
        #     ΔE = E_target - E_ground

        gap = (

            target_energy

            -

            ground_energy
        )


        return gap


    # =====================================================
    # ENERGY GAP USING DISPLAYED VALUES
    # =====================================================

    def displayed_energy_gap(
        self
    ):

        # This calculates the gap using the shifted
        # displayed energies.
        #
        # It should give exactly the same answer.

        target = self.displayed_energy(

            self.selected_level_index
        )


        ground = (
            self.displayed_ground_energy()
        )


        return (
            target
            -
            ground
        )


    # =====================================================
    # GAP IN JOULES
    # =====================================================

    def energy_gap_joule(self):

        gap_ev = (
            abs(
                self.energy_gap_from_ground()
            )
        )


        return (

            gap_ev

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
        # therefore:
        #
        #     ν = E / h

        energy = (
            self.energy_gap_joule()
        )


        if energy == 0:

            return 0.0


        return (

            energy

            /

            PLANCK_CONSTANT
        )


    # =====================================================
    # PHOTON WAVELENGTH
    # =====================================================

    def photon_wavelength(self):

        frequency = (
            self.photon_frequency()
        )


        if frequency == 0:

            return math.inf


        # λ = c / ν

        return (

            SPEED_OF_LIGHT

            /

            frequency
        )


    # =====================================================
    # IS GROUND STATE?
    # =====================================================

    def is_ground_state(
        self,
        index
    ):

        # == means:
        #
        #     "is equal to?"
        #
        return (
            index
            ==
            self.ground_index
        )


    # =====================================================
    # SET SELECTED LEVEL
    # =====================================================

    def set_selected_level(
        self,
        index
    ):

        self.selected_level_index = index


    # =====================================================
    # SET REFERENCE OFFSET
    # =====================================================

    def set_reference_offset(
        self,
        offset
    ):

        self.reference_offset = offset


    # =====================================================
    # SET GROUND AS ZERO
    # =====================================================

    def set_ground_as_zero(self):

        # Suppose:
        #
        #     ground energy = -5 eV
        #
        # To display it as zero:
        #
        #     offset = +5 eV
        #
        # In general:
        #
        #     offset = -ground_energy

        self.reference_offset = (

            -
            self.ground_energy()
        )


    # =====================================================
    # RESET REFERENCE
    # =====================================================

    def reset_reference(self):

        self.reference_offset = 0.0


    # =====================================================
    # PREPARE GROUND
    # =====================================================

    def prepare_ground(self):

        # Move our educational marker
        # to the ground state.

        self.current_level_index = (
            self.ground_index
        )


    # =====================================================
    # PREPARE SELECTED LEVEL
    # =====================================================

    def prepare_selected_level(self):

        # IMPORTANT:
        #
        # This does NOT simulate a real atomic transition.
        #
        # It simply moves the educational marker.

        self.current_level_index = (
            self.selected_level_index
        )


# =========================================================
# GUI
# =========================================================


class GroundStateGUI:

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(
        self,
        root
    ):

        # Save main Tkinter window.

        self.root = root


        # Window title.

        self.root.title(
            "Neutral-Atom QC | Atomic Physics 02 — Ground State"
        )


        # Starting window size.

        self.root.geometry(
            "1420x900"
        )


        # Minimum allowed size.

        self.root.minsize(
            1100,
            750
        )


        # -------------------------------------------------
        # CREATE MODEL
        # -------------------------------------------------

        self.model = GroundStateModel()


        # -------------------------------------------------
        # BUILD GUI
        # -------------------------------------------------

        self.setup_style()

        self.create_header()

        self.create_main_area()

        self.create_learning_area()


        # Initial display.

        self.update_display()


        # Initial lesson.

        self.show_lesson(

            title="Ground-state lesson initialized",

            explanation=(
                "The ground state is the lowest allowed "
                "energy state of an atom.\n\n"

                "Our educational energy levels are:\n\n"

                "    Level 0 = -5.0 eV\n"
                "    Level 1 = -3.4 eV\n"
                "    Level 2 = -2.2 eV\n"
                "    Level 3 = -0.9 eV\n\n"

                "The smallest energy is -5.0 eV.\n\n"

                "Therefore Level 0 is automatically identified "
                "as the ground state.\n\n"

                "The negative energies here are fictional "
                "educational values."
            ),

            python_code=(
                "self.model = GroundStateModel()\n\n"

                "# Inside __init__():\n\n"

                "self.ground_index = self.find_ground_state()\n\n"

                "# find_ground_state() searches for\n"
                "# the level with the LOWEST energy."
            )
        )


    # =====================================================
    # STYLE
    # =====================================================

    def setup_style(self):

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

            text="Atomic Physics 02 — Ground State",

            style="Section.TLabel"

        ).pack(
            anchor="w"
        )


        ttk.Label(

            header,

            text=(
                "Lowest energy, energy references and "
                "excitation from the ground state"
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

            text="Atomic Energy Diagram",

            padding=10
        )


        left.grid(

            row=0,

            column=0,

            sticky="nsew",

            padx=(0, 8)
        )


        # Canvas will show:
        #
        #     energy axis
        #     allowed levels
        #     ground state
        #     selected level
        #     atom marker
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


        self.canvas.bind(

            "<Configure>",

            self.canvas_resized
        )


        ttk.Label(

            left,

            text=(
                "Move the energy reference and notice that every "
                "level moves numerically, but the energy gaps do "
                "not change."
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
        # GROUND STATE INFORMATION
        # -------------------------------------------------

        ground_frame = ttk.LabelFrame(

            right,

            text="1. Ground State",

            padding=10
        )


        ground_frame.pack(

            fill="x",

            pady=(0, 5)
        )


        self.ground_name_label = ttk.Label(

            ground_frame,

            font=(
                "Segoe UI",
                12,
                "bold"
            )
        )


        self.ground_name_label.pack(
            anchor="w"
        )


        self.ground_stored_energy_label = ttk.Label(

            ground_frame,

            style="Value.TLabel"
        )


        self.ground_stored_energy_label.pack(
            anchor="w"
        )


        self.ground_display_energy_label = ttk.Label(

            ground_frame,

            style="Value.TLabel"
        )


        self.ground_display_energy_label.pack(
            anchor="w"
        )


        ttk.Label(

            ground_frame,

            text=(
                "Ground state = lowest allowed energy, "
                "not necessarily zero energy."
            ),

            wraplength=420

        ).pack(
            anchor="w",
            pady=(4, 0)
        )


        # -------------------------------------------------
        # CURRENT ATOM
        # -------------------------------------------------

        current_frame = ttk.LabelFrame(

            right,

            text="2. Current Educational Atom State",

            padding=10
        )


        current_frame.pack(

            fill="x",

            pady=5
        )


        self.current_level_label = ttk.Label(

            current_frame,

            font=(
                "Segoe UI",
                11,
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
        # SELECT LEVEL
        # -------------------------------------------------

        target_frame = ttk.LabelFrame(

            right,

            text="3. Compare Ground With Another Level",

            padding=10
        )


        target_frame.pack(

            fill="x",

            pady=5
        )


        level_names = [

            level["name"]

            for level in self.model.levels
        ]


        self.selected_level_var = tk.StringVar(

            value=level_names[
                self.model.selected_level_index
            ]
        )


        self.level_combo = ttk.Combobox(

            target_frame,

            values=level_names,

            textvariable=self.selected_level_var,

            state="readonly"
        )


        self.level_combo.pack(
            fill="x"
        )


        self.level_combo.bind(

            "<<ComboboxSelected>>",

            self.level_changed
        )


        # -------------------------------------------------
        # ENERGY GAP
        # -------------------------------------------------

        gap_frame = ttk.LabelFrame(

            right,

            text="4. Energy Gap From Ground",

            padding=10
        )


        gap_frame.pack(

            fill="x",

            pady=5
        )


        self.target_energy_label = ttk.Label(

            gap_frame,

            style="Value.TLabel"
        )


        self.target_energy_label.pack(
            anchor="w"
        )


        self.gap_label = ttk.Label(

            gap_frame,

            style="Value.TLabel"
        )


        self.gap_label.pack(
            anchor="w"
        )


        self.display_gap_label = ttk.Label(

            gap_frame,

            style="Value.TLabel"
        )


        self.display_gap_label.pack(
            anchor="w"
        )


        self.gap_status_label = ttk.Label(

            gap_frame,

            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )


        self.gap_status_label.pack(

            anchor="w",

            pady=(3, 0)
        )


        # -------------------------------------------------
        # PHOTON INFORMATION
        # -------------------------------------------------

        photon_frame = ttk.LabelFrame(

            right,

            text="5. Energy Needed For Excitation",

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


        self.wavelength_label = ttk.Label(

            photon_frame,

            style="Value.TLabel"
        )


        self.wavelength_label.pack(
            anchor="w"
        )


        ttk.Label(

            photon_frame,

            text=(
                "These values come only from the example energy gap. "
                "A real atomic transition also requires appropriate "
                "selection rules and coupling."
            ),

            wraplength=420

        ).pack(
            anchor="w",
            pady=(4, 0)
        )


        # -------------------------------------------------
        # ENERGY REFERENCE
        # -------------------------------------------------

        reference_frame = ttk.LabelFrame(

            right,

            text="6. Change Energy Reference",

            padding=10
        )


        reference_frame.pack(

            fill="x",

            pady=5
        )


        self.reference_var = tk.DoubleVar(

            value=0.0
        )


        self.reference_label = ttk.Label(

            reference_frame,

            text="Reference offset = +0.00 eV"
        )


        self.reference_label.pack(
            anchor="w"
        )


        self.reference_slider = ttk.Scale(

            reference_frame,

            from_=-3.0,

            to=7.0,

            variable=self.reference_var,

            command=self.reference_changed
        )


        self.reference_slider.pack(

            fill="x",

            pady=(3, 5)
        )


        ttk.Button(

            reference_frame,

            text="Set Ground Energy = 0 eV",

            command=self.set_ground_zero,

            style="Action.TButton"

        ).pack(

            fill="x",

            pady=2
        )


        ttk.Button(

            reference_frame,

            text="Reset Original Reference",

            command=self.reset_reference,

            style="Action.TButton"

        ).pack(

            fill="x",

            pady=2
        )


        # -------------------------------------------------
        # PREPARATION
        # -------------------------------------------------

        prepare_frame = ttk.LabelFrame(

            right,

            text="7. Educational State Preparation",

            padding=10
        )


        prepare_frame.pack(

            fill="x",

            pady=5
        )


        ttk.Button(

            prepare_frame,

            text="Prepare Ground State",

            command=self.prepare_ground,

            style="Action.TButton"

        ).pack(

            fill="x",

            pady=2
        )


        ttk.Button(

            prepare_frame,

            text="Prepare Selected Level",

            command=self.prepare_selected,

            style="Action.TButton"

        ).pack(

            fill="x",

            pady=2
        )


        self.preparation_label = ttk.Label(

            prepare_frame,

            text="Atom begins in the ground state.",

            wraplength=420,

            justify="left"
        )


        self.preparation_label.pack(

            anchor="w",

            pady=(5, 0)
        )


    # =====================================================
    # LEARNING AREA
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
        # PHYSICS
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
        # PYTHON
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
NEW PYTHON / PHYSICS CONCEPTS
=============================


1. min()

   min(...) finds the smallest value.

   In this file we use:

       min(..., key=...)

   to find the level with the lowest energy.


2. range()

   range(4)

   produces:

       0
       1
       2
       3


3. len()

   len(self.levels)

   asks:

       how many levels are stored?


4. lambda

   lambda index:
       self.levels[index]["energy_ev"]

   is a small temporary function.

   It tells min():

       compare the energy of each index.


5. REFERENCE OFFSET

   displayed_energy =
       stored_energy + reference_offset

   Every level gets the SAME offset.


6. INVARIANT QUANTITY

   An invariant quantity does not change under
   a certain transformation.

   Here:

       shift every energy equally
            ↓
       energy difference stays unchanged


7. DEFAULT FUNCTION ARGUMENT

   def energy_gap_from_ground(
       self,
       target_index=None
   ):

   None means:

       no specific target was provided.


8. RETURNING BOOLEANS

   return index == self.ground_index

   returns:

       True
   or
       False


9. SCIENTIFIC MODEL VS VISUALIZATION

   GroundStateModel
       ↓
   stores physics/math

   GroundStateGUI
       ↓
   handles buttons, sliders and drawings


10. IMPORTANT PHYSICS LESSON

    The numerical zero of energy can often be
    chosen conveniently.

    Energy DIFFERENCES are what determine
    transition energies.
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

        # Unlock text widget.

        self.lesson_text.config(
            state="normal"
        )


        self.lesson_text.delete(
            "1.0",
            tk.END
        )


        self.lesson_text.insert(

            tk.END,

            f"{title}\n\n{explanation}"
        )


        self.lesson_text.config(
            state="disabled"
        )


        # Python tab.

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
    # INDEX FROM NAME
    # =====================================================

    def index_from_name(

        self,

        name
    ):

        # enumerate() gives:
        #
        #     index
        #     value
        #
        # at the same time.

        for index, level in enumerate(
            self.model.levels
        ):

            if level["name"] == name:

                return index


        return 0


    # =====================================================
    # LEVEL CHANGED
    # =====================================================

    def level_changed(

        self,

        event=None
    ):

        # Read the selected name.

        name = (
            self.selected_level_var.get()
        )


        # Convert name into list index.

        index = self.index_from_name(
            name
        )


        # Store selected level.

        self.model.set_selected_level(
            index
        )


        # Refresh GUI.

        self.update_display()


        gap = (
            self.model.energy_gap_from_ground()
        )


        self.show_lesson(

            title="Comparison level changed",

            explanation=(
                f"You selected {name}.\n\n"

                "We now compare it with the ground state.\n\n"

                "The important quantity is:\n\n"

                "    ΔE = E_selected − E_ground\n\n"

                f"For this selection:\n\n"

                f"    ΔE = {gap:.4f} eV\n\n"

                "This gap tells us how much energy separates "
                "the two atomic levels."
            ),

            python_code=(
                "name = self.selected_level_var.get()\n\n"

                "index = self.index_from_name(name)\n\n"

                "self.model.set_selected_level(index)\n\n"

                "# Energy gap:\n\n"

                "gap = (\n"
                "    target_energy\n"
                "    - ground_energy\n"
                ")"
            )
        )


    # =====================================================
    # REFERENCE CHANGED
    # =====================================================

    def reference_changed(

        self,

        value=None
    ):

        # Read slider value.

        offset = (
            self.reference_var.get()
        )


        # Store offset.

        self.model.set_reference_offset(
            offset
        )


        # Update screen.

        self.update_display()


        original_gap = (
            self.model.energy_gap_from_ground()
        )


        displayed_gap = (
            self.model.displayed_energy_gap()
        )


        self.show_lesson(

            title="Energy reference changed",

            explanation=(
                f"You shifted every displayed energy by "
                f"{offset:+.3f} eV.\n\n"

                "Notice:\n\n"

                f"    original gap = {original_gap:.4f} eV\n\n"

                f"    displayed gap = {displayed_gap:.4f} eV\n\n"

                "They are identical.\n\n"

                "Why?\n\n"

                "Because adding the same number to both energies "
                "cancels when we subtract them."
            ),

            python_code=(
                "displayed_ground = ground + offset\n"
                "displayed_target = target + offset\n\n"

                "gap = (\n"
                "    displayed_target\n"
                "    - displayed_ground\n"
                ")\n\n"

                "# Algebra:\n"
                "# (target + offset) - (ground + offset)\n"
                "# = target - ground"
            )
        )


    # =====================================================
    # SET GROUND ZERO
    # =====================================================

    def set_ground_zero(self):

        # Change model reference.

        self.model.set_ground_as_zero()


        # Synchronize slider.

        self.reference_var.set(

            self.model.reference_offset
        )


        # Refresh.

        self.update_display()


        self.show_lesson(

            title="Ground state set to 0 eV",

            explanation=(
                "We changed the ENERGY REFERENCE.\n\n"

                "The ground state now displays as:\n\n"

                "    E_ground = 0 eV\n\n"

                "But the physical energy gaps did NOT change.\n\n"

                "This is why textbooks often place the ground "
                "state at zero: it makes the diagram easier to "
                "read without changing transition energies."
            ),

            python_code=(
                "self.reference_offset = -self.ground_energy()\n\n"

                "# Example:\n"
                "# ground = -5 eV\n"
                "# offset = +5 eV\n\n"

                "# displayed ground:\n"
                "# -5 + 5 = 0 eV"
            )
        )


    # =====================================================
    # RESET REFERENCE
    # =====================================================

    def reset_reference(self):

        self.model.reset_reference()


        self.reference_var.set(
            0.0
        )


        self.update_display()


        self.show_lesson(

            title="Original energy reference restored",

            explanation=(
                "The display has returned to the original "
                "educational energy values.\n\n"

                "Again, this changes only our numerical reference. "
                "It does not alter the energy separation between "
                "levels."
            ),

            python_code=(
                "self.reference_offset = 0.0"
            )
        )


    # =====================================================
    # PREPARE GROUND
    # =====================================================

    def prepare_ground(self):

        # Move marker to ground state.

        self.model.prepare_ground()


        self.update_display()


        ground = self.model.get_level(

            self.model.ground_index
        )


        self.preparation_label.config(

            text=(
                f"Educational atom prepared in "
                f"{ground['name']}."
            )
        )


        self.show_lesson(

            title="Ground state prepared",

            explanation=(
                f"The educational atom marker is now on "
                f"{ground['name']}.\n\n"

                "This represents the atom occupying its lowest "
                "allowed energy state.\n\n"

                "IMPORTANT:\n\n"

                "This button does not simulate cooling, optical "
                "pumping or spontaneous decay. It simply changes "
                "the state marker in our educational model."
            ),

            python_code=(
                "self.current_level_index = self.ground_index\n\n"

                "# We simply tell our model:\n"
                "# current state = ground state"
            )
        )


    # =====================================================
    # PREPARE SELECTED LEVEL
    # =====================================================

    def prepare_selected(self):

        self.model.prepare_selected_level()


        self.update_display()


        level = self.model.get_level(

            self.model.selected_level_index
        )


        gap = (
            self.model.energy_gap_from_ground()
        )


        self.preparation_label.config(

            text=(
                f"Educational atom moved to "
                f"{level['name']}."
            )
        )


        self.show_lesson(

            title="Selected excited level prepared",

            explanation=(
                f"The educational marker is now on "
                f"{level['name']}.\n\n"

                f"Its energy gap above the ground state is:\n\n"

                f"    ΔE = {gap:.4f} eV\n\n"

                "A real experiment would need an appropriate "
                "physical preparation process. This button does "
                "not simulate the transition dynamics."
            ),

            python_code=(
                "self.current_level_index = (\n"
                "    self.selected_level_index\n"
                ")\n\n"

                "# This changes only our educational state marker."
            )
        )


    # =====================================================
    # UPDATE DISPLAY
    # =====================================================

    def update_display(self):

        # -------------------------------------------------
        # GROUND STATE
        # -------------------------------------------------

        ground = self.model.get_level(

            self.model.ground_index
        )


        self.ground_name_label.config(

            text=(
                f"Ground state: {ground['name']}"
            )
        )


        self.ground_stored_energy_label.config(

            text=(
                "Stored energy = "
                f"{self.model.ground_energy():.4f} eV"
            )
        )


        self.ground_display_energy_label.config(

            text=(
                "Displayed energy = "
                f"{self.model.displayed_ground_energy():.4f} eV"
            )
        )


        # -------------------------------------------------
        # CURRENT STATE
        # -------------------------------------------------

        current = self.model.get_level(

            self.model.current_level_index
        )


        self.current_level_label.config(

            text=(
                f"Current level: {current['name']}"
            )
        )


        current_display_energy = (
            self.model.displayed_energy(
                self.model.current_level_index
            )
        )


        self.current_energy_label.config(

            text=(
                "Displayed energy = "
                f"{current_display_energy:.4f} eV"
            )
        )


        # -------------------------------------------------
        # SELECTED LEVEL
        # -------------------------------------------------

        selected_energy = (
            self.model.displayed_energy(

                self.model.selected_level_index
            )
        )


        self.target_energy_label.config(

            text=(
                "Selected displayed energy = "
                f"{selected_energy:.4f} eV"
            )
        )


        # -------------------------------------------------
        # ENERGY GAP
        # -------------------------------------------------

        original_gap = (
            self.model.energy_gap_from_ground()
        )


        display_gap = (
            self.model.displayed_energy_gap()
        )


        self.gap_label.config(

            text=(
                "Physical gap ΔE = "
                f"{original_gap:.4f} eV"
            )
        )


        self.display_gap_label.config(

            text=(
                "Gap from displayed values = "
                f"{display_gap:.4f} eV"
            )
        )


        # Compare values with tolerance.

        if abs(
            original_gap
            -
            display_gap
        ) < 1e-10:

            status = (
                "✓ Energy gap unchanged by reference shift"
            )

        else:

            status = (
                "Energy-gap mismatch"
            )


        self.gap_status_label.config(
            text=status
        )


        # -------------------------------------------------
        # PHOTON
        # -------------------------------------------------

        frequency = (
            self.model.photon_frequency()
        )


        wavelength = (
            self.model.photon_wavelength()
        )


        self.frequency_label.config(

            text=(
                "ν = "
                f"{frequency:.4e} Hz "
                f"= {frequency / 1e12:.3f} THz"
            )
        )


        if math.isinf(
            wavelength
        ):

            wavelength_text = "∞"

        else:

            wavelength_text = (

                f"{wavelength * 1e9:.2f} nm"
            )


        self.wavelength_label.config(

            text=(
                f"λ = {wavelength_text}"
            )
        )


        # -------------------------------------------------
        # REFERENCE LABEL
        # -------------------------------------------------

        self.reference_label.config(

            text=(
                "Reference offset = "
                f"{self.model.reference_offset:+.2f} eV"
            )
        )


        # -------------------------------------------------
        # DRAW
        # -------------------------------------------------

        self.draw_energy_levels()


    # =====================================================
    # CANVAS RESIZE
    # =====================================================

    def canvas_resized(

        self,

        event
    ):

        self.draw_energy_levels()


    # =====================================================
    # DRAW ENERGY LEVELS
    # =====================================================

    def draw_energy_levels(self):

        # Remove previous drawing.

        self.canvas.delete(
            "all"
        )


        width = (
            self.canvas.winfo_width()
        )


        height = (
            self.canvas.winfo_height()
        )


        if width < 100:

            width = 700


        if height < 100:

            height = 500


        # -------------------------------------------------
        # TITLE
        # -------------------------------------------------

        self.canvas.create_text(

            width / 2,

            30,

            text="Ground State = Lowest Allowed Energy",

            font=(
                "Segoe UI",
                14,
                "bold"
            )
        )


        # -------------------------------------------------
        # AXIS
        # -------------------------------------------------

        axis_x = 70

        top = 80

        bottom = (
            height - 70
        )


        self.canvas.create_line(

            axis_x,

            bottom,

            axis_x,

            top,

            arrow=tk.LAST,

            width=2
        )


        self.canvas.create_text(

            axis_x - 25,

            (
                top
                +
                bottom
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
        # FIND DISPLAY ENERGY RANGE
        # -------------------------------------------------

        display_energies = [

            self.model.displayed_energy(index)

            for index in range(
                len(self.model.levels)
            )
        ]


        minimum_energy = min(
            display_energies
        )


        maximum_energy = max(
            display_energies
        )


        energy_range = (

            maximum_energy

            -

            minimum_energy
        )


        if energy_range == 0:

            energy_range = 1.0


        usable_height = (

            bottom

            -

            top
        )


        positions = {}


        # -------------------------------------------------
        # DRAW LEVELS
        # -------------------------------------------------

        for index, level in enumerate(
            self.model.levels
        ):

            energy = (
                self.model.displayed_energy(
                    index
                )
            )


            normalized = (

                energy

                -

                minimum_energy

            ) / energy_range


            # Higher energy appears higher,
            # while canvas y increases downward.

            y = (

                bottom

                -

                normalized

                *

                usable_height
            )


            positions[index] = y


            # Draw level line.

            self.canvas.create_line(

                width * 0.24,

                y,

                width * 0.72,

                y,

                width=3
            )


            # Name.

            label = level["name"]


            # Add ground-state label.

            if self.model.is_ground_state(
                index
            ):

                label += "  ← GROUND STATE"


            self.canvas.create_text(

                width * 0.21,

                y,

                text=label,

                anchor="e",

                font=(
                    "Segoe UI",
                    10,
                    "bold"
                )
            )


            # Display energy.

            self.canvas.create_text(

                width * 0.75,

                y,

                text=(
                    f"{energy:.2f} eV"
                ),

                anchor="w",

                font=(
                    "Consolas",
                    10
                )
            )


            # Current atom marker.

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
        # DRAW GAP ARROW
        # -------------------------------------------------

        ground_y = positions[
            self.model.ground_index
        ]


        selected_y = positions[
            self.model.selected_level_index
        ]


        if (
            self.model.selected_level_index
            !=
            self.model.ground_index
        ):

            arrow_x = (
                width * 0.60
            )


            self.canvas.create_line(

                arrow_x,

                ground_y,

                arrow_x,

                selected_y,

                arrow=tk.LAST,

                width=4
            )


            middle_y = (

                ground_y

                +
                selected_y

            ) / 2


            gap = (
                self.model.energy_gap_from_ground()
            )


            self.canvas.create_text(

                arrow_x + 20,

                middle_y,

                text=(
                    f"ΔE = {gap:.2f} eV"
                ),

                anchor="w",

                font=(
                    "Segoe UI",
                    10,
                    "bold"
                )
            )


# =========================================================
# START APPLICATION
# =========================================================


if __name__ == "__main__":

    # PowerShell message.

    print(
        "Running 02_ground_state.py ..."
    )


    # Create Tkinter main window.

    root = tk.Tk()


    # Create GUI.

    app = GroundStateGUI(
        root
    )


    # Begin Tkinter event loop.

    root.mainloop()