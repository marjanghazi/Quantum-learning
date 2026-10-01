"""
=========================================================
03 - RYDBERG STATE
Neutral-Atom Quantum Computing Learning
=========================================================

GOAL
----

Understand what a Rydberg state is and why highly excited
atoms are useful in neutral-atom quantum computing.

This program teaches:

    principal quantum number n
    hydrogen-like energy scaling
    binding energy
    ionization threshold
    characteristic size scaling
    equivalent excitation energy
    why Rydberg states enable strong interactions


IMPORTANT
---------

This is an EDUCATIONAL hydrogen-like model.

It is NOT a realistic simulation of a specific experimental
atom such as Rubidium or Cesium.

The circles drawn by this program are NOT classical
electron orbits.

They only visualize characteristic spatial scaling.
"""


# =========================================================
# IMPORTS
# =========================================================

import math

import tkinter as tk

from tkinter import ttk

from tkinter.scrolledtext import ScrolledText


# =========================================================
# PHYSICAL CONSTANTS
# =========================================================


# Hydrogen ground-state energy.
HYDROGEN_GROUND_ENERGY_EV = -13.6


# Bohr radius in meters.
BOHR_RADIUS = 5.29177210903e-11


# Electron volt -> joule.
EV_TO_JOULE = 1.602176634e-19


# Planck constant.
PLANCK_CONSTANT = 6.62607015e-34


# Speed of light.
SPEED_OF_LIGHT = 299_792_458


# =========================================================
# RYDBERG PHYSICS MODEL
# =========================================================


class RydbergStateModel:

    """
    Educational hydrogen-like Rydberg model.

    The main parameter is:

        n

    where n is the principal quantum number.
    """

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(self):

        # Start at n = 30.
        self.n = 30


    # =====================================================
    # SET n
    # =====================================================

    def set_n(
        self,
        n
    ):

        # Convert to an integer.
        n = int(
            round(n)
        )


        # Prevent values below 1.
        self.n = max(
            1,
            n
        )


    # =====================================================
    # ENERGY
    # =====================================================

    def energy_ev(self):

        # Hydrogen equation:
        #
        #            -13.6
        # E_n = --------------
        #              n²

        return (

            HYDROGEN_GROUND_ENERGY_EV

            /

            (
                self.n ** 2
            )
        )


    # =====================================================
    # BINDING ENERGY
    # =====================================================

    def binding_energy_ev(self):

        # Bound-state energy is negative.
        #
        # Binding-energy magnitude is positive.

        return abs(
            self.energy_ev()
        )


    # =====================================================
    # CHARACTERISTIC RADIUS
    # =====================================================

    def characteristic_radius_m(self):

        # Simplified hydrogenic scaling:
        #
        # r_n ≈ n² a₀

        return (

            self.n ** 2

            *

            BOHR_RADIUS
        )


    # =====================================================
    # RADIUS IN NANOMETERS
    # =====================================================

    def characteristic_radius_nm(self):

        return (

            self.characteristic_radius_m()

            *

            1e9
        )


    # =====================================================
    # SIZE SCALE
    # =====================================================

    def radius_ratio(self):

        # Relative to n = 1:
        #
        # ratio = n²

        return (
            self.n ** 2
        )


    # =====================================================
    # EXCITATION ENERGY FROM n = 1
    # =====================================================

    def excitation_energy_ev(self):

        # Ground energy:
        #
        # -13.6 eV

        ground_energy = (
            HYDROGEN_GROUND_ENERGY_EV
        )


        # Target high-n energy.

        target_energy = (
            self.energy_ev()
        )


        # ΔE = E_final - E_initial

        return (

            target_energy

            -

            ground_energy
        )


    # =====================================================
    # EXCITATION ENERGY IN JOULES
    # =====================================================

    def excitation_energy_joule(self):

        return (

            self.excitation_energy_ev()

            *

            EV_TO_JOULE
        )


    # =====================================================
    # EQUIVALENT PHOTON FREQUENCY
    # =====================================================

    def equivalent_photon_frequency(self):

        # E = hν
        #
        # ν = E/h

        energy = (
            self.excitation_energy_joule()
        )


        if energy == 0:

            return 0.0


        return (

            energy

            /

            PLANCK_CONSTANT
        )


    # =====================================================
    # EQUIVALENT WAVELENGTH
    # =====================================================

    def equivalent_wavelength_m(self):

        frequency = (
            self.equivalent_photon_frequency()
        )


        if frequency == 0:

            return math.inf


        return (

            SPEED_OF_LIGHT

            /

            frequency
        )


    # =====================================================
    # DISTANCE FROM IONIZATION
    # =====================================================

    def distance_from_ionization_ev(self):

        # In this energy reference:
        #
        # ionization threshold = 0 eV
        #
        # therefore distance from zero is
        # the binding-energy magnitude.

        return (
            self.binding_energy_ev()
        )


    # =====================================================
    # EDUCATIONAL CATEGORY
    # =====================================================

    def state_category(self):

        # These categories are only for teaching.
        #
        # They are not universal physical boundaries.

        if self.n <= 5:

            return "Low-lying atomic state"


        elif self.n < 15:

            return "Excited atomic state"


        else:

            return "Highly excited / Rydberg-like state"


# =========================================================
# FULL PAGE SCROLLING SYSTEM
# =========================================================


class ScrollablePage(ttk.Frame):

    """
    Makes the WHOLE application page vertically scrollable.

    Structure:

        root
         ↓
        ScrollablePage
         ↓
        Canvas
         ↓
        content Frame
         ↓
        entire application UI
    """

    def __init__(
        self,
        parent
    ):

        super().__init__(
            parent
        )


        # -------------------------------------------------
        # MAIN SCROLLING CANVAS
        # -------------------------------------------------

        self.canvas = tk.Canvas(

            self,

            highlightthickness=0,

            borderwidth=0
        )


        # -------------------------------------------------
        # VERTICAL SCROLLBAR
        # -------------------------------------------------

        self.scrollbar = ttk.Scrollbar(

            self,

            orient="vertical",

            command=self.canvas.yview
        )


        # Connect scrollbar.
        self.canvas.configure(

            yscrollcommand=
            self.scrollbar.set
        )


        # Layout.
        self.canvas.pack(

            side="left",

            fill="both",

            expand=True
        )


        self.scrollbar.pack(

            side="right",

            fill="y"
        )


        # -------------------------------------------------
        # CONTENT FRAME
        # -------------------------------------------------

        self.content = ttk.Frame(
            self.canvas
        )


        # Put frame inside canvas.

        self.window_id = (
            self.canvas.create_window(

                (
                    0,
                    0
                ),

                window=self.content,

                anchor="nw"
            )
        )


        # -------------------------------------------------
        # EVENTS
        # -------------------------------------------------

        # Whenever content size changes:
        #
        # update scrollable area.

        self.content.bind(

            "<Configure>",

            self.update_scroll_region
        )


        # Whenever window width changes:
        #
        # make content width match canvas width.

        self.canvas.bind(

            "<Configure>",

            self.resize_content
        )


        # Windows mouse wheel.

        self.canvas.bind_all(

            "<MouseWheel>",

            self.mousewheel
        )


        # Linux mouse wheel.

        self.canvas.bind_all(

            "<Button-4>",

            self.mousewheel_linux_up
        )


        self.canvas.bind_all(

            "<Button-5>",

            self.mousewheel_linux_down
        )


        # Keyboard scrolling.

        parent.bind(

            "<Prior>",

            lambda event:
                self.canvas.yview_scroll(
                    -5,
                    "units"
                )
        )


        parent.bind(

            "<Next>",

            lambda event:
                self.canvas.yview_scroll(
                    5,
                    "units"
                )
        )


        parent.bind(

            "<Home>",

            lambda event:
                self.canvas.yview_moveto(
                    0
                )
        )


        parent.bind(

            "<End>",

            lambda event:
                self.canvas.yview_moveto(
                    1
                )
        )


    # =====================================================
    # UPDATE SCROLL REGION
    # =====================================================

    def update_scroll_region(
        self,
        event=None
    ):

        self.canvas.configure(

            scrollregion=
            self.canvas.bbox(
                "all"
            )
        )


    # =====================================================
    # RESPONSIVE WIDTH
    # =====================================================

    def resize_content(
        self,
        event
    ):

        self.canvas.itemconfigure(

            self.window_id,

            width=event.width
        )


    # =====================================================
    # WINDOWS MOUSEWHEEL
    # =====================================================

    def mousewheel(
        self,
        event
    ):

        # Check whether mouse is currently over
        # a text widget that has its own scrollbar.
        #
        # If so, let that widget behave normally.

        widget_class = (
            event.widget.winfo_class()
        )


        if widget_class == "Text":

            return


        self.canvas.yview_scroll(

            int(
                -1
                *
                (
                    event.delta / 120
                )
            ),

            "units"
        )


    # =====================================================
    # LINUX MOUSEWHEEL
    # =====================================================

    def mousewheel_linux_up(
        self,
        event
    ):

        self.canvas.yview_scroll(

            -1,

            "units"
        )


    def mousewheel_linux_down(
        self,
        event
    ):

        self.canvas.yview_scroll(

            1,

            "units"
        )


# =========================================================
# MAIN GUI
# =========================================================


class RydbergStateGUI:

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(
        self,
        root
    ):

        # Save root.
        self.root = root


        # Window title.
        self.root.title(

            "Neutral-Atom QC | Atomic Physics 03 — Rydberg State"
        )


        # Start maximized-looking.
        self.root.geometry(
            "1450x900"
        )


        # Minimum size.
        self.root.minsize(
            1050,
            650
        )


        # -------------------------------------------------
        # MODEL
        # -------------------------------------------------

        self.model = (
            RydbergStateModel()
        )


        # -------------------------------------------------
        # STYLE
        # -------------------------------------------------

        self.setup_style()


        # -------------------------------------------------
        # CREATE FULL PAGE SCROLLER
        # -------------------------------------------------

        self.page = ScrollablePage(
            self.root
        )


        self.page.pack(

            fill="both",

            expand=True
        )


        # Everything goes inside page.content.

        self.body = (
            self.page.content
        )


        # Responsive full width.
        self.body.columnconfigure(
            0,
            weight=1
        )


        # -------------------------------------------------
        # CREATE UI
        # -------------------------------------------------

        self.create_header()

        self.create_main_area()

        self.create_learning_area()

        self.create_footer()


        # -------------------------------------------------
        # INITIAL DRAW
        # -------------------------------------------------

        self.update_display()


        self.show_lesson(

            title="Rydberg-state lesson initialized",

            explanation=(
                "A Rydberg state is a highly excited atomic "
                "state with a large principal quantum number n.\n\n"

                f"Current value:\n\n"

                f"    n = {self.model.n}\n\n"

                "As n increases:\n\n"

                "    energy approaches 0 eV\n"
                "    binding becomes weaker\n"
                "    characteristic size increases strongly\n\n"

                "These properties are connected to the strong "
                "interactions that make Rydberg states useful "
                "for neutral-atom quantum computing."
            ),

            python_code=(
                "self.model = RydbergStateModel()\n\n"

                "# Initial model value:\n\n"

                "self.n = 30\n\n"

                "# Changing n causes the physics values\n"
                "# and visualizations to be recalculated."
            )
        )


        # Ensure scroll region is correct
        # after everything exists.

        self.root.after(

            200,

            self.refresh_scroll_region
        )


    # =====================================================
    # REFRESH SCROLL REGION
    # =====================================================

    def refresh_scroll_region(self):

        self.page.update_scroll_region()


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

            "CardTitle.TLabel",

            font=(
                "Segoe UI",
                11,
                "bold"
            )
        )


        style.configure(

            "Value.TLabel",

            font=(
                "Consolas",
                10
            )
        )


        style.configure(

            "Small.TLabel",

            font=(
                "Segoe UI",
                9
            )
        )


        style.configure(

            "Action.TButton",

            font=(
                "Segoe UI",
                9,
                "bold"
            ),

            padding=7
        )


    # =====================================================
    # HEADER
    # =====================================================

    def create_header(self):

        header = ttk.Frame(

            self.body,

            padding=(
                20,
                15,
                20,
                10
            )
        )


        header.grid(

            row=0,

            column=0,

            sticky="ew"
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

            text="Atomic Physics 03 — Rydberg State",

            style="Section.TLabel"

        ).pack(

            anchor="w",

            pady=(3, 0)
        )


        ttk.Label(

            header,

            text=(
                "Highly excited atoms, principal quantum number, "
                "energy scaling and characteristic spatial size"
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

            self.body,

            padding=(
                15,
                0,
                15,
                10
            )
        )


        main.grid(

            row=1,

            column=0,

            sticky="ew"
        )


        # Left visualization.
        main.columnconfigure(

            0,

            weight=3,

            minsize=600
        )


        # Right controls.
        main.columnconfigure(

            1,

            weight=2,

            minsize=420
        )


        # =================================================
        # LEFT COLUMN
        # =================================================

        left = ttk.Frame(
            main
        )


        left.grid(

            row=0,

            column=0,

            sticky="nsew",

            padx=(0, 8)
        )


        left.columnconfigure(
            0,
            weight=1
        )


        # -------------------------------------------------
        # ENERGY DIAGRAM
        # -------------------------------------------------

        energy_frame = ttk.LabelFrame(

            left,

            text="Hydrogen-Like Energy-Level Picture",

            padding=10
        )


        energy_frame.grid(

            row=0,

            column=0,

            sticky="ew",

            pady=(0, 8)
        )


        # IMPORTANT:
        #
        # Explicit height prevents Tkinter from
        # crushing the diagram.

        self.energy_canvas = tk.Canvas(

            energy_frame,

            height=410,

            bg="white",

            highlightthickness=0
        )


        self.energy_canvas.pack(

            fill="x",

            expand=True
        )


        self.energy_canvas.bind(

            "<Configure>",

            self.canvas_resized
        )


        ttk.Label(

            energy_frame,

            text=(
                "High-n levels are physically very close together. "
                "The diagram therefore uses schematic vertical "
                "spacing while keeping the numerical energies correct."
            ),

            wraplength=760,

            justify="left"

        ).pack(

            anchor="w",

            pady=(7, 0)
        )


        # -------------------------------------------------
        # SIZE VISUALIZATION
        # -------------------------------------------------

        size_frame = ttk.LabelFrame(

            left,

            text="Characteristic Size Scaling",

            padding=10
        )


        size_frame.grid(

            row=1,

            column=0,

            sticky="ew",

            pady=(0, 8)
        )


        self.size_canvas = tk.Canvas(

            size_frame,

            height=300,

            bg="white",

            highlightthickness=0
        )


        self.size_canvas.pack(

            fill="x",

            expand=True
        )


        self.size_canvas.bind(

            "<Configure>",

            self.canvas_resized
        )


        ttk.Label(

            size_frame,

            text=(
                "The circles are schematic representations of "
                "characteristic spatial extent, not classical "
                "electron orbits."
            ),

            wraplength=760,

            justify="left"

        ).pack(

            anchor="w",

            pady=(7, 0)
        )


        # =================================================
        # RIGHT COLUMN
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


        right.columnconfigure(
            0,
            weight=1
        )


        # -------------------------------------------------
        # 1. CURRENT STATE
        # -------------------------------------------------

        state_frame = ttk.LabelFrame(

            right,

            text="1. Current Atomic State",

            padding=12
        )


        state_frame.grid(

            row=0,

            column=0,

            sticky="ew",

            pady=(0, 7)
        )


        self.n_label = ttk.Label(

            state_frame,

            style="CardTitle.TLabel"
        )


        self.n_label.pack(
            anchor="w"
        )


        self.category_label = ttk.Label(

            state_frame,

            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )


        self.category_label.pack(

            anchor="w",

            pady=(4, 0)
        )


        # -------------------------------------------------
        # 2. ENERGY
        # -------------------------------------------------

        energy_info = ttk.LabelFrame(

            right,

            text="2. Energy",

            padding=12
        )


        energy_info.grid(

            row=1,

            column=0,

            sticky="ew",

            pady=7
        )


        self.energy_label = ttk.Label(

            energy_info,

            style="Value.TLabel"
        )


        self.energy_label.pack(
            anchor="w"
        )


        self.binding_label = ttk.Label(

            energy_info,

            style="Value.TLabel"
        )


        self.binding_label.pack(

            anchor="w",

            pady=(3, 0)
        )


        self.ionization_label = ttk.Label(

            energy_info,

            style="Value.TLabel"
        )


        self.ionization_label.pack(

            anchor="w",

            pady=(3, 0)
        )


        # -------------------------------------------------
        # 3. SIZE
        # -------------------------------------------------

        size_info = ttk.LabelFrame(

            right,

            text="3. Characteristic Size",

            padding=12
        )


        size_info.grid(

            row=2,

            column=0,

            sticky="ew",

            pady=7
        )


        self.radius_label = ttk.Label(

            size_info,

            style="Value.TLabel"
        )


        self.radius_label.pack(
            anchor="w"
        )


        self.radius_ratio_label = ttk.Label(

            size_info,

            style="Value.TLabel"
        )


        self.radius_ratio_label.pack(

            anchor="w",

            pady=(3, 0)
        )


        # -------------------------------------------------
        # 4. EXCITATION
        # -------------------------------------------------

        excitation_frame = ttk.LabelFrame(

            right,

            text="4. Excitation From n = 1",

            padding=12
        )


        excitation_frame.grid(

            row=3,

            column=0,

            sticky="ew",

            pady=7
        )


        self.excitation_energy_label = ttk.Label(

            excitation_frame,

            style="Value.TLabel"
        )


        self.excitation_energy_label.pack(
            anchor="w"
        )


        self.frequency_label = ttk.Label(

            excitation_frame,

            style="Value.TLabel"
        )


        self.frequency_label.pack(

            anchor="w",

            pady=(3, 0)
        )


        self.wavelength_label = ttk.Label(

            excitation_frame,

            style="Value.TLabel"
        )


        self.wavelength_label.pack(

            anchor="w",

            pady=(3, 0)
        )


        ttk.Separator(

            excitation_frame,

            orient="horizontal"

        ).pack(

            fill="x",

            pady=8
        )


        ttk.Label(

            excitation_frame,

            text=(
                "These frequency and wavelength values represent "
                "the total hydrogen-model energy gap only. Real "
                "Rydberg excitation depends on the atomic species, "
                "selection rules and experimental excitation scheme."
            ),

            wraplength=410,

            justify="left"

        ).pack(
            anchor="w"
        )


        # -------------------------------------------------
        # 5. n CONTROL
        # -------------------------------------------------

        control_frame = ttk.LabelFrame(

            right,

            text="5. Change Principal Quantum Number n",

            padding=12
        )


        control_frame.grid(

            row=4,

            column=0,

            sticky="ew",

            pady=7
        )


        self.n_var = tk.DoubleVar(

            value=self.model.n
        )


        self.n_slider_label = ttk.Label(

            control_frame,

            style="CardTitle.TLabel"
        )


        self.n_slider_label.pack(
            anchor="w"
        )


        self.n_slider = ttk.Scale(

            control_frame,

            from_=1,

            to=100,

            variable=self.n_var,

            command=self.n_changed
        )


        self.n_slider.pack(

            fill="x",

            pady=(10, 3)
        )


        scale_labels = ttk.Frame(
            control_frame
        )


        scale_labels.pack(
            fill="x"
        )


        ttk.Label(

            scale_labels,

            text="n = 1"

        ).pack(
            side="left"
        )


        ttk.Label(

            scale_labels,

            text="n = 100"

        ).pack(
            side="right"
        )


        # -------------------------------------------------
        # 6. PRESETS
        # -------------------------------------------------

        preset_frame = ttk.LabelFrame(

            right,

            text="6. Compare States",

            padding=12
        )


        preset_frame.grid(

            row=5,

            column=0,

            sticky="ew",

            pady=7
        )


        preset_grid = ttk.Frame(
            preset_frame
        )


        preset_grid.pack(
            fill="x"
        )


        presets = [
            1,
            10,
            30,
            60,
            90
        ]


        for column, n in enumerate(
            presets
        ):

            preset_grid.columnconfigure(

                column,

                weight=1
            )


            ttk.Button(

                preset_grid,

                text=f"n = {n}",

                command=lambda value=n:
                    self.set_preset(
                        value
                    ),

                style="Action.TButton"

            ).grid(

                row=0,

                column=column,

                sticky="ew",

                padx=2
            )


        # -------------------------------------------------
        # 7. IMPORTANCE
        # -------------------------------------------------

        importance_frame = ttk.LabelFrame(

            right,

            text="7. Why Rydberg States Matter",

            padding=12
        )


        importance_frame.grid(

            row=6,

            column=0,

            sticky="ew",

            pady=7
        )


        ttk.Label(

            importance_frame,

            text=(
                "Highly excited Rydberg atoms can interact much "
                "more strongly over distance than ordinary "
                "ground-state neutral atoms."
            ),

            wraplength=410,

            justify="left"

        ).pack(
            anchor="w"
        )


        ttk.Label(

            importance_frame,

            text=(
                "\nRydberg excitation\n"
                "        ↓\n"
                "strong atom-atom interaction\n"
                "        ↓\n"
                "blockade / entanglement / gates"
            ),

            font=(
                "Consolas",
                10
            ),

            justify="left"

        ).pack(
            anchor="w"
        )


        # -------------------------------------------------
        # 8. QUBIT CLARIFICATION
        # -------------------------------------------------

        qubit_frame = ttk.LabelFrame(

            right,

            text="8. Important Qubit Clarification",

            padding=12
        )


        qubit_frame.grid(

            row=7,

            column=0,

            sticky="ew",

            pady=7
        )


        ttk.Label(

            qubit_frame,

            text=(
                "|0⟩ and |1⟩\n"
                "    → computational / storage states\n\n"

                "|r⟩\n"
                "    → temporary Rydberg state\n\n"

                "The Rydberg state is commonly used when strong "
                "atom-atom interaction is required. It is not "
                "automatically the permanent |1⟩ state."
            ),

            wraplength=410,

            justify="left"

        ).pack(
            anchor="w"
        )


    # =====================================================
    # LEARNING CONSOLE
    # =====================================================

    def create_learning_area(self):

        learning = ttk.LabelFrame(

            self.body,

            text="Python + Atomic Physics Learning Console",

            padding=10
        )


        learning.grid(

            row=2,

            column=0,

            sticky="ew",

            padx=15,

            pady=(0, 12)
        )


        notebook = ttk.Notebook(
            learning
        )


        notebook.pack(

            fill="both",

            expand=True
        )


        # -------------------------------------------------
        # CONCEPT TAB
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

            height=11,

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
        # CODE TAB
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

            height=11,

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
        # NEW PYTHON TAB
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

            height=11,

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
NEW PYTHON / UI CONCEPTS
========================


1. FULL-PAGE SCROLLING

   Tkinter windows do not automatically scroll.

   We build:

       Canvas
          ↓
       embedded Frame
          ↓
       whole application

   Then the Canvas scrolls vertically.


2. SCROLL REGION

   canvas.bbox("all")

   calculates how large the complete application
   content currently is.


3. MOUSE-WHEEL EVENT

   <MouseWheel>

   lets us call a function whenever the user
   moves the mouse wheel.


4. RESPONSIVE WIDTH

   canvas.itemconfigure(
       window_id,
       width=event.width
   )

   keeps the embedded application frame the same
   width as the visible window.


5. FIXED CANVAS HEIGHT

   height=410

   prevents the energy diagram from being crushed
   when many other widgets are present.


6. SCHEMATIC ENERGY SPACING

   High-n hydrogenic levels physically become very
   close together near 0 eV.

   If we draw their actual energies directly onto
   a small screen, the lines overlap.

   Therefore:

       numerical energy
            ↓
       remains physically calculated

   while:

       visual y-position
            ↓
       uses clean schematic spacing


7. INTEGER SLIDER VALUE

   int(round(value))

   converts the continuous Tkinter slider value
   into a clean integer n.


8. LAMBDA WITH STORED VALUE

   command=lambda value=n:
       self.set_preset(value)

   ensures each button remembers its own n value.


9. LOGARITHMIC VISUAL COMPRESSION

   Real size scaling follows:

       n²

   For n=90:

       n² = 8100

   A literal 8100× larger circle cannot fit on screen.

   Therefore only the DRAWING is compressed.

   The numerical result remains the true n² scaling
   of this educational hydrogenic model.


10. SEPARATING MODEL AND GUI

    RydbergStateModel
          ↓
    physics calculations

    RydbergStateGUI
          ↓
    user interface and visualization
"""
        )


        python_guide.config(
            state="disabled"
        )


    # =====================================================
    # FOOTER
    # =====================================================

    def create_footer(self):

        footer = ttk.Frame(

            self.body,

            padding=(
                15,
                0,
                15,
                20
            )
        )


        footer.grid(

            row=3,

            column=0,

            sticky="ew"
        )


        ttk.Separator(

            footer,

            orient="horizontal"

        ).pack(

            fill="x",

            pady=(0, 10)
        )


        ttk.Label(

            footer,

            text=(
                "Educational hydrogen-like model • "
                "Not a calibrated real-atom simulation"
            ),

            font=(
                "Segoe UI",
                9,
                "italic"
            )

        ).pack(
            anchor="center"
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

        # Physics explanation.
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


        # Python explanation.
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
    # n SLIDER CHANGED
    # =====================================================

    def n_changed(

        self,

        value=None
    ):

        # Slider returns floating-point value.
        #
        # Convert to nearest integer.

        n = int(

            round(
                self.n_var.get()
            )
        )


        self.model.set_n(
            n
        )


        # Do NOT continuously call n_var.set()
        # here because it can create unnecessary
        # callback cycles while dragging.


        self.update_display()


        self.show_lesson(

            title="Principal quantum number changed",

            explanation=(
                f"Current principal quantum number:\n\n"

                f"    n = {n}\n\n"

                "The hydrogen-like model uses:\n\n"

                "    Eₙ = -13.6 / n²\n\n"

                "and approximately:\n\n"

                "    rₙ ∝ n²\n\n"

                "As n increases, the state becomes less strongly "
                "bound and its characteristic spatial extent "
                "increases strongly."
            ),

            python_code=(
                "n = int(round(self.n_var.get()))\n\n"

                "self.model.set_n(n)\n\n"

                "# Hydrogenic energy:\n"
                "energy = -13.6 / (n ** 2)\n\n"

                "# Characteristic radius:\n"
                "radius = (n ** 2) * BOHR_RADIUS"
            )
        )


    # =====================================================
    # PRESET
    # =====================================================

    def set_preset(

        self,

        n
    ):

        self.model.set_n(
            n
        )


        self.n_var.set(
            n
        )


        self.update_display()


        self.show_lesson(

            title=f"Preset selected: n = {n}",

            explanation=(
                f"Current state:\n\n"

                f"    n = {n}\n\n"

                f"Category:\n\n"

                f"    {self.model.state_category()}\n\n"

                "Compare the presets and observe:\n\n"

                "    n increases\n"
                "        ↓\n"
                "    energy approaches 0 eV\n"
                "        ↓\n"
                "    binding gets weaker\n"
                "        ↓\n"
                "    characteristic size grows"
            ),

            python_code=(
                f"self.model.set_n({n})\n\n"

                f"self.n_var.set({n})\n\n"

                "self.update_display()"
            )
        )


    # =====================================================
    # UPDATE DISPLAY
    # =====================================================

    def update_display(self):

        # Calculate model values.

        energy = (
            self.model.energy_ev()
        )


        binding = (
            self.model.binding_energy_ev()
        )


        radius_nm = (
            self.model.characteristic_radius_nm()
        )


        radius_ratio = (
            self.model.radius_ratio()
        )


        excitation_ev = (
            self.model.excitation_energy_ev()
        )


        frequency = (
            self.model.equivalent_photon_frequency()
        )


        wavelength = (
            self.model.equivalent_wavelength_m()
        )


        # -------------------------------------------------
        # CURRENT STATE
        # -------------------------------------------------

        self.n_label.config(

            text=(
                "Principal quantum number: "
                f"n = {self.model.n}"
            )
        )


        self.category_label.config(

            text=(
                self.model.state_category()
            )
        )


        # -------------------------------------------------
        # ENERGY
        # -------------------------------------------------

        self.energy_label.config(

            text=(
                f"Eₙ = {energy:.6f} eV"
            )
        )


        self.binding_label.config(

            text=(
                "Binding-energy magnitude = "
                f"{binding:.6f} eV"
            )
        )


        self.ionization_label.config(

            text=(
                "Distance to ionization threshold = "
                f"{binding:.6f} eV"
            )
        )


        # -------------------------------------------------
        # SIZE
        # -------------------------------------------------

        self.radius_label.config(

            text=(
                "Characteristic radius ≈ "
                f"{radius_nm:.4f} nm"
            )
        )


        self.radius_ratio_label.config(

            text=(
                "Relative size scale ≈ "
                f"{radius_ratio:,} × n=1"
            )
        )


        # -------------------------------------------------
        # EXCITATION
        # -------------------------------------------------

        self.excitation_energy_label.config(

            text=(
                "ΔE from n=1 = "
                f"{excitation_ev:.6f} eV"
            )
        )


        self.frequency_label.config(

            text=(
                "Equivalent frequency:\n"
                f"ν = {frequency:.4e} Hz\n"
                f"  = {frequency / 1e12:.3f} THz"
            )
        )


        if math.isinf(
            wavelength
        ):

            wavelength_text = "∞"

        else:

            wavelength_text = (

                f"{wavelength * 1e9:.3f} nm"
            )


        self.wavelength_label.config(

            text=(
                "Equivalent wavelength:\n"
                f"λ = {wavelength_text}"
            )
        )


        # -------------------------------------------------
        # SLIDER LABEL
        # -------------------------------------------------

        self.n_slider_label.config(

            text=(
                f"n = {self.model.n}"
            )
        )


        # Draw diagrams.

        self.draw_energy_diagram()

        self.draw_size_diagram()


        # Let Tkinter update requested sizes.

        self.root.after_idle(

            self.refresh_scroll_region
        )


    # =====================================================
    # CANVAS RESIZED
    # =====================================================

    def canvas_resized(

        self,

        event=None
    ):

        self.draw_energy_diagram()

        self.draw_size_diagram()


    # =====================================================
    # ENERGY DIAGRAM
    # =====================================================

    def draw_energy_diagram(self):

        self.energy_canvas.delete(
            "all"
        )


        width = (
            self.energy_canvas.winfo_width()
        )


        height = (
            self.energy_canvas.winfo_height()
        )


        # Avoid tiny startup geometry.

        if width < 500:

            width = 750


        if height < 350:

            height = 410


        # -------------------------------------------------
        # TITLE
        # -------------------------------------------------

        self.energy_canvas.create_text(

            width / 2,

            28,

            text="Hydrogen-Like Energy Levels",

            font=(
                "Segoe UI",
                14,
                "bold"
            )
        )


        self.energy_canvas.create_text(

            width / 2,

            51,

            text=(
                "Schematic spacing for readability — "
                "energy values remain calculated"
            ),

            font=(
                "Segoe UI",
                9
            )
        )


        # -------------------------------------------------
        # SAFE DRAWING AREA
        # -------------------------------------------------

        axis_x = 65


        label_x = 135


        line_start_x = 190


        line_end_x = max(

            line_start_x + 250,

            width - 235
        )


        value_x = (
            line_end_x + 20
        )


        threshold_y = 82


        first_level_y = 132


        bottom_y = (
            height - 45
        )


        # -------------------------------------------------
        # ENERGY AXIS
        # -------------------------------------------------

        self.energy_canvas.create_line(

            axis_x,

            bottom_y,

            axis_x,

            threshold_y,

            arrow=tk.LAST,

            width=2
        )


        self.energy_canvas.create_text(

            axis_x - 30,

            (
                threshold_y
                +
                bottom_y
            )
            /
            2,

            text="Energy",

            angle=90,

            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )


        # -------------------------------------------------
        # IONIZATION THRESHOLD
        # -------------------------------------------------

        self.energy_canvas.create_line(

            line_start_x,

            threshold_y,

            line_end_x,

            threshold_y,

            dash=(
                6,
                4
            ),

            width=2
        )


        self.energy_canvas.create_text(

            value_x,

            threshold_y,

            text="0 eV",

            anchor="w",

            font=(
                "Consolas",
                10,
                "bold"
            )
        )


        self.energy_canvas.create_text(

            value_x + 55,

            threshold_y,

            text="ionization threshold",

            anchor="w",

            font=(
                "Segoe UI",
                9
            )
        )


        # -------------------------------------------------
        # LEVELS TO DISPLAY
        # -------------------------------------------------

        sample_levels = [

            1,
            2,
            3,
            5,
            10,
            self.model.n
        ]


        # Remove duplicates.
        sample_levels = sorted(

            set(
                sample_levels
            ),

            reverse=True
        )


        number_of_levels = len(
            sample_levels
        )


        # -------------------------------------------------
        # CLEAN EVEN SPACING
        # -------------------------------------------------

        available_height = (

            bottom_y

            -

            first_level_y
        )


        if number_of_levels > 1:

            row_spacing = (

                available_height

                /

                (
                    number_of_levels - 1
                )
            )

        else:

            row_spacing = 0


        # -------------------------------------------------
        # DRAW LEVELS
        # -------------------------------------------------

        for row_index, n in enumerate(
            sample_levels
        ):

            y = (

                first_level_y

                +

                row_index

                *

                row_spacing
            )


            energy = (

                HYDROGEN_GROUND_ENERGY_EV

                /

                (
                    n ** 2
                )
            )


            current = (
                n
                ==
                self.model.n
            )


            # Current line thicker.
            width_value = (

                5

                if current

                else 2
            )


            # Energy line.
            self.energy_canvas.create_line(

                line_start_x,

                y,

                line_end_x,

                y,

                width=width_value
            )


            # Left n label.
            if current:

                n_text = (
                    f"n = {n}   ← current"
                )

            else:

                n_text = (
                    f"n = {n}"
                )


            self.energy_canvas.create_text(

                label_x,

                y,

                text=n_text,

                anchor="e",

                font=(

                    "Segoe UI",

                    9,

                    "bold"
                    if current
                    else "normal"
                )
            )


            # Numerical energy.
            self.energy_canvas.create_text(

                value_x,

                y,

                text=(
                    f"{energy:.6f} eV"
                ),

                anchor="w",

                font=(
                    "Consolas",
                    9
                )
            )


        # -------------------------------------------------
        # BOTTOM MESSAGE
        # -------------------------------------------------

        self.energy_canvas.create_text(

            width / 2,

            height - 16,

            text=(
                "Higher n → energy approaches 0 eV → "
                "electron becomes more weakly bound"
            ),

            font=(
                "Segoe UI",
                9,
                "bold"
            )
        )


    # =====================================================
    # SIZE DIAGRAM
    # =====================================================

    def draw_size_diagram(self):

        self.size_canvas.delete(
            "all"
        )


        width = (
            self.size_canvas.winfo_width()
        )


        height = (
            self.size_canvas.winfo_height()
        )


        if width < 500:

            width = 750


        if height < 240:

            height = 300


        # -------------------------------------------------
        # TITLE
        # -------------------------------------------------

        self.size_canvas.create_text(

            width / 2,

            25,

            text="Characteristic Spatial Scale",

            font=(
                "Segoe UI",
                13,
                "bold"
            )
        )


        # -------------------------------------------------
        # POSITIONS
        # -------------------------------------------------

        center_y = (
            height * 0.53
        )


        left_x = (
            width * 0.25
        )


        right_x = (
            width * 0.73
        )


        # -------------------------------------------------
        # n = 1 REFERENCE
        # -------------------------------------------------

        reference_radius = 20


        self.size_canvas.create_oval(

            left_x - reference_radius,

            center_y - reference_radius,

            left_x + reference_radius,

            center_y + reference_radius,

            width=3
        )


        # nucleus marker.
        self.size_canvas.create_oval(

            left_x - 4,

            center_y - 4,

            left_x + 4,

            center_y + 4,

            fill="black"
        )


        self.size_canvas.create_text(

            left_x,

            center_y - 55,

            text="n = 1",

            font=(
                "Segoe UI",
                11,
                "bold"
            )
        )


        self.size_canvas.create_text(

            left_x,

            center_y + 55,

            text=(
                "reference scale ≈ a₀"
            ),

            font=(
                "Segoe UI",
                9
            )
        )


        # -------------------------------------------------
        # CURRENT SIZE
        # -------------------------------------------------

        ratio = (
            self.model.radius_ratio()
        )


        # True scale is n².
        #
        # We use logarithmic compression only
        # for graphical drawing.

        compressed_ratio = (

            math.log10(

                max(
                    ratio,
                    1
                )
            )

            /

            4
        )


        compressed_ratio = max(

            0,

            min(
                1,
                compressed_ratio
            )
        )


        max_radius = min(

            100,

            height * 0.30,

            width * 0.14
        )


        current_radius = (

            25

            +

            compressed_ratio

            *

            (
                max_radius
                -
                25
            )
        )


        self.size_canvas.create_oval(

            right_x - current_radius,

            center_y - current_radius,

            right_x + current_radius,

            center_y + current_radius,

            width=3
        )


        self.size_canvas.create_oval(

            right_x - 4,

            center_y - 4,

            right_x + 4,

            center_y + 4,

            fill="black"
        )


        self.size_canvas.create_text(

            right_x,

            center_y
            -
            current_radius
            -
            22,

            text=(
                f"n = {self.model.n}"
            ),

            font=(
                "Segoe UI",
                11,
                "bold"
            )
        )


        self.size_canvas.create_text(

            right_x,

            center_y
            +
            current_radius
            +
            22,

            text=(
                f"hydrogenic size scale ≈ "
                f"{ratio:,}×"
            ),

            font=(
                "Segoe UI",
                9,
                "bold"
            )
        )


        # -------------------------------------------------
        # ARROW
        # -------------------------------------------------

        arrow_start = (
            left_x + 85
        )


        arrow_end = (

            right_x

            -

            current_radius

            -

            25
        )


        if arrow_end > arrow_start:

            self.size_canvas.create_line(

                arrow_start,

                center_y,

                arrow_end,

                center_y,

                arrow=tk.LAST,

                width=2
            )


            self.size_canvas.create_text(

                (
                    arrow_start
                    +
                    arrow_end
                )
                /
                2,

                center_y - 18,

                text="n increases",

                font=(
                    "Segoe UI",
                    9,
                    "bold"
                )
            )


        # -------------------------------------------------
        # BOTTOM EXPLANATION
        # -------------------------------------------------

        self.size_canvas.create_text(

            width / 2,

            height - 16,

            text=(
                "Schematic spatial extent only — "
                "not a classical electron orbit"
            ),

            font=(
                "Segoe UI",
                9,
                "bold"
            )
        )


# =========================================================
# START APPLICATION
# =========================================================


if __name__ == "__main__":

    print(
        "Running 03_rydberg_state.py ..."
    )


    # Create application window.

    root = tk.Tk()


    # Create GUI.

    app = RydbergStateGUI(
        root
    )


    # Run application.

    root.mainloop()