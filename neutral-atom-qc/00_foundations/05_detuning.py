"""
=========================================================
05 - DETUNING
Neutral-Atom Quantum Computing Learning
=========================================================

GOAL
----

Understand what happens when the frequency of our driving
field does NOT exactly match the transition frequency of
our two-level quantum system.


DETUNING
--------

We define:

    Δ = ω_drive - ω_0

where:

    ω_drive = frequency of the applied drive
    ω_0     = natural transition frequency
    Δ       = detuning


If:

    Δ = 0

then the drive is exactly resonant.


If:

    Δ != 0

then the drive is off resonance.


GENERALIZED RABI FREQUENCY
--------------------------

When detuning exists, the effective oscillation frequency is:

    Ω_R = sqrt(Ω² + Δ²)

where:

    Ω   = resonant Rabi frequency / coupling strength
    Δ   = detuning
    Ω_R = generalized Rabi frequency


EXCITED-STATE PROBABILITY
-------------------------

Starting from |0>:

                 Ω²
    P(1) = --------------- *
            Ω² + Δ²

           sin²(
                sqrt(Ω² + Δ²) * t
                -------------------
                         2
               )


An important consequence is:

                     Ω²
    maximum P(1) = -----------
                    Ω² + Δ²


So:

    Δ = 0
        -> maximum P(1) = 1

but:

    |Δ| increases
        -> maximum P(1) decreases


IMPORTANT PHYSICS NOTE
----------------------

This is still an IDEAL EDUCATIONAL model.

We assume:

    - only two quantum levels
    - coherent driving
    - constant Ω
    - constant Δ
    - rotating-wave approximation
    - no decoherence
    - no spontaneous emission
    - no laser amplitude noise
    - no laser phase noise
    - no atomic motion
    - no multilevel atomic structure

A real neutral-atom experiment contains additional physics.

Also, the exact signs appearing in complex amplitudes can
depend on Hamiltonian and phase conventions.

The physically important population formula demonstrated
here is unchanged.
"""


# =========================================================
# IMPORTS
# =========================================================


# math contains standard mathematical functions.
#
# We use:
#
#     sqrt()
#     sin()
#     cos()
#     pi
#     degrees()
#
import math


# NumPy lets us efficiently calculate
# many time values for plotting.
#
import numpy as np


# Tkinter provides the GUI.
#
import tkinter as tk


# ttk contains modern Tkinter widgets.
#
from tkinter import ttk


# ScrolledText gives us a text box
# with a built-in scrollbar.
#
from tkinter.scrolledtext import ScrolledText


# Figure is Matplotlib's main plotting container.
#
from matplotlib.figure import Figure


# This lets Matplotlib appear inside Tkinter.
#
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# =========================================================
# DETUNED TWO-LEVEL MODEL
# =========================================================


class DetunedRabiModel:

    """
    Mathematical model of a coherently driven
    two-level quantum system with detuning.

    We store:

        omega
        delta
        time

    where:

        omega = Ω = resonant Rabi frequency
        delta = Δ = detuning
        time  = t

    We use the rotating-frame Hamiltonian convention:

            ℏ
        H = - [Ω sigma_x - Δ sigma_z]
            2

    equivalently, up to notation/sign convention:

            ℏ
        H = - [[-Δ, Ω],
            2   [ Ω, Δ]]

    The probability result is the important part here:

                     Ω²
        P(1) = --------------- sin²(Ω_R t / 2)
                 Ω² + Δ²

    with:

        Ω_R = sqrt(Ω² + Δ²)
    """


    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(self):

        # Coupling strength / resonant Rabi frequency.
        #
        # Units:
        #
        #     radians per second
        #
        self.omega = 2.0


        # Begin exactly on resonance.
        #
        # Δ = 0
        #
        self.delta = 0.0


        # Begin at time zero.
        #
        self.time = 0.0


    # =====================================================
    # GENERALIZED RABI FREQUENCY
    # =====================================================

    def generalized_rabi_frequency(self):

        # Equation:
        #
        #     Ω_R = sqrt(Ω² + Δ²)
        #
        # Python:
        #
        #     self.omega ** 2
        #
        # means:
        #
        #     Ω²

        omega_squared = (
            self.omega ** 2
        )


        delta_squared = (
            self.delta ** 2
        )


        total = (
            omega_squared
            +
            delta_squared
        )


        omega_r = math.sqrt(
            total
        )


        return omega_r


    # =====================================================
    # ALPHA AMPLITUDE
    # =====================================================

    def alpha(self):

        # Get generalized Rabi frequency.

        omega_r = (
            self.generalized_rabi_frequency()
        )


        # Avoid division by zero.
        #
        # This situation would require:
        #
        #     Ω = 0
        #     Δ = 0
        #
        # simultaneously.

        if omega_r == 0:

            return complex(
                1.0,
                0.0
            )


        # Calculate:
        #
        #     Ω_R t / 2

        angle = (
            omega_r
            *
            self.time
            /
            2
        )


        # Under our convention:
        #
        # α(t) =
        #
        #     cos(Ω_R t/2)
        #
        #       +
        #
        #     i (Δ / Ω_R) sin(Ω_R t/2)

        real_part = math.cos(
            angle
        )


        imaginary_part = (

            self.delta
            /
            omega_r

            *

            math.sin(
                angle
            )
        )


        return complex(

            real_part,

            imaginary_part
        )


    # =====================================================
    # BETA AMPLITUDE
    # =====================================================

    def beta(self):

        # Get generalized frequency.

        omega_r = (
            self.generalized_rabi_frequency()
        )


        # Prevent division by zero.

        if omega_r == 0:

            return complex(
                0.0,
                0.0
            )


        # Calculate Ω_R t / 2.

        angle = (

            omega_r
            *
            self.time
            /
            2
        )


        # Under our chosen convention:
        #
        #               Ω
        # β(t) = -i -------- sin(Ω_R t / 2)
        #              Ω_R

        imaginary_part = (

            -

            self.omega
            /
            omega_r

            *

            math.sin(
                angle
            )
        )


        return complex(

            0.0,

            imaginary_part
        )


    # =====================================================
    # PROBABILITIES
    # =====================================================

    def probabilities(self):

        # Calculate amplitudes.

        alpha = self.alpha()

        beta = self.beta()


        # Born rule:
        #
        #     P(0) = |α|²

        probability_0 = (

            abs(alpha) ** 2
        )


        # Born rule:
        #
        #     P(1) = |β|²

        probability_1 = (

            abs(beta) ** 2
        )


        return (

            probability_0,

            probability_1
        )


    # =====================================================
    # NORMALIZATION
    # =====================================================

    def normalization(self):

        # Obtain probabilities.

        p0, p1 = (
            self.probabilities()
        )


        # Their total should remain 1
        # in this ideal closed-system model.

        return (
            p0
            +
            p1
        )


    # =====================================================
    # MAXIMUM POSSIBLE EXCITATION
    # =====================================================

    def maximum_excited_probability(self):

        # The maximum excited-state probability is:
        #
        #              Ω²
        #     Pmax = ---------
        #            Ω² + Δ²


        denominator = (

            self.omega ** 2

            +

            self.delta ** 2
        )


        # Avoid zero division.

        if denominator == 0:

            return 0.0


        return (

            self.omega ** 2

            /

            denominator
        )


    # =====================================================
    # FIRST EXCITATION PEAK TIME
    # =====================================================

    def first_peak_time(self):

        # P(1) contains:
        #
        #     sin²(Ω_R t / 2)
        #
        # Its first maximum occurs when:
        #
        #     Ω_R t / 2 = π/2
        #
        # therefore:
        #
        #     Ω_R t = π
        #
        # and:
        #
        #           π
        #     t = -----
        #          Ω_R

        omega_r = (
            self.generalized_rabi_frequency()
        )


        if omega_r == 0:

            return math.inf


        return (

            math.pi
            /
            omega_r
        )


    # =====================================================
    # RESONANT PI-PULSE TIME
    # =====================================================

    def resonant_pi_time(self):

        # If Δ = 0, a π pulse occurs at:
        #
        #         π
        #     t = -
        #         Ω
        #
        # Off resonance, using this same duration does
        # NOT generally produce complete excitation.

        if self.omega == 0:

            return math.inf


        return (

            math.pi
            /
            self.omega
        )


    # =====================================================
    # BLOCH COORDINATES
    # =====================================================

    def bloch_coordinates(self):

        # Obtain amplitudes.

        alpha = self.alpha()

        beta = self.beta()


        # Calculate:
        #
        #     α* β
        #
        # where α* is complex conjugate.

        product = (

            alpha.conjugate()

            *

            beta
        )


        # Bloch X coordinate.

        x = (

            2

            *

            product.real
        )


        # Bloch Y coordinate.

        y = (

            2

            *

            product.imag
        )


        # Bloch Z coordinate.

        z = (

            abs(alpha) ** 2

            -

            abs(beta) ** 2
        )


        return (
            x,
            y,
            z
        )


    # =====================================================
    # SET OMEGA
    # =====================================================

    def set_omega(
        self,
        omega
    ):

        self.omega = omega


    # =====================================================
    # SET DELTA
    # =====================================================

    def set_delta(
        self,
        delta
    ):

        self.delta = delta


    # =====================================================
    # SET TIME
    # =====================================================

    def set_time(
        self,
        time
    ):

        self.time = time


    # =====================================================
    # RESONANCE
    # =====================================================

    def set_resonance(self):

        # Resonance means:
        #
        #     Δ = 0

        self.delta = 0.0


    # =====================================================
    # RESET
    # =====================================================

    def reset(self):

        # Return evolution to t = 0.
        #
        # We keep Ω and Δ unchanged.

        self.time = 0.0


# =========================================================
# GUI
# =========================================================


class DetuningGUI:

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
            "Neutral-Atom QC | 05 — Detuning"
        )


        # Starting size.

        self.root.geometry(
            "1450x920"
        )


        # Minimum size.

        self.root.minsize(
            1150,
            760
        )


        # -------------------------------------------------
        # CREATE PHYSICS MODEL
        # -------------------------------------------------

        self.model = (
            DetunedRabiModel()
        )


        # -------------------------------------------------
        # ANIMATION SETTINGS
        # -------------------------------------------------

        # False = animation initially stopped.

        self.running = False


        # Amount by which time increases
        # during each animation step.

        self.animation_dt = 0.03


        # -------------------------------------------------
        # BUILD GUI
        # -------------------------------------------------

        self.setup_style()

        self.create_header()

        self.create_main_area()

        self.create_learning_area()


        # Show initial state.

        self.update_display()


        # Initial explanation.

        self.show_lesson(

            title="Detuning lesson initialized",

            explanation=(
                "The system currently starts exactly on resonance.\n\n"

                "That means:\n\n"

                "    Δ = 0\n\n"

                "Therefore the generalized Rabi frequency is:\n\n"

                "    Ω_R = √(Ω² + 0²)\n"
                "        = Ω\n\n"

                "So this initially behaves exactly like the "
                "Rabi-oscillation model from File 04.\n\n"

                "Now we will change Δ and observe what happens."
            ),

            python_code=(
                "self.model = DetunedRabiModel()\n\n"

                "# Initial values:\n\n"

                "self.omega = 2.0\n"
                "self.delta = 0.0\n"
                "self.time = 0.0"
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


        style.configure(

            "Probability.Horizontal.TProgressbar",

            thickness=18
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

            text="05 — Detuning",

            style="Section.TLabel"

        ).pack(
            anchor="w"
        )


        ttk.Label(

            header,

            text=(
                "What happens when the drive frequency "
                "does not exactly match the transition?"
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


        # Give more space to graph.

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
        # LEFT — GRAPH
        # =================================================

        left = ttk.LabelFrame(

            main,

            text="Detuned Rabi Oscillation",

            padding=10
        )


        left.grid(

            row=0,

            column=0,

            sticky="nsew",

            padx=(0, 8)
        )


        # Create Matplotlib figure.

        self.figure = Figure(

            figsize=(7, 5),

            dpi=100
        )


        # One graph.

        self.ax = (
            self.figure.add_subplot(
                111
            )
        )


        # Embed in Tkinter.

        self.plot_canvas = (
            FigureCanvasTkAgg(

                self.figure,

                master=left
            )
        )


        self.plot_canvas.get_tk_widget().pack(

            fill="both",

            expand=True
        )


        ttk.Label(

            left,

            text=(
                "Solid curves show the current detuned evolution. "
                "The dashed reference shows the excited-state "
                "probability that would occur at Δ = 0."
            ),

            wraplength=700

        ).pack(
            fill="x",
            pady=(5, 0)
        )


        # =================================================
        # RIGHT
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
        # CURRENT STATE
        # -------------------------------------------------

        state_frame = ttk.LabelFrame(

            right,

            text="1. Current Quantum State",

            padding=10
        )


        state_frame.pack(

            fill="x",

            pady=(0, 5)
        )


        self.state_label = ttk.Label(

            state_frame,

            font=(
                "Cambria Math",
                12,
                "bold"
            ),

            justify="center"
        )


        self.state_label.pack(
            fill="x"
        )


        # -------------------------------------------------
        # FREQUENCIES
        # -------------------------------------------------

        frequency_frame = ttk.LabelFrame(

            right,

            text="2. Frequencies",

            padding=10
        )


        frequency_frame.pack(

            fill="x",

            pady=5
        )


        self.omega_label = ttk.Label(

            frequency_frame,

            style="Value.TLabel"
        )


        self.omega_label.pack(
            anchor="w"
        )


        self.delta_label = ttk.Label(

            frequency_frame,

            style="Value.TLabel"
        )


        self.delta_label.pack(
            anchor="w"
        )


        self.omega_r_label = ttk.Label(

            frequency_frame,

            style="Value.TLabel"
        )


        self.omega_r_label.pack(
            anchor="w"
        )


        self.resonance_label = ttk.Label(

            frequency_frame,

            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )


        self.resonance_label.pack(
            anchor="w",
            pady=(3, 0)
        )


        # -------------------------------------------------
        # IMPORTANT RESULTS
        # -------------------------------------------------

        result_frame = ttk.LabelFrame(

            right,

            text="3. Important Results",

            padding=10
        )


        result_frame.pack(

            fill="x",

            pady=5
        )


        self.max_probability_label = ttk.Label(

            result_frame,

            style="Value.TLabel"
        )


        self.max_probability_label.pack(
            anchor="w"
        )


        self.first_peak_label = ttk.Label(

            result_frame,

            style="Value.TLabel"
        )


        self.first_peak_label.pack(
            anchor="w"
        )


        self.resonant_pi_label = ttk.Label(

            result_frame,

            style="Value.TLabel"
        )


        self.resonant_pi_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # TIME
        # -------------------------------------------------

        time_frame = ttk.LabelFrame(

            right,

            text="4. Current Time",

            padding=10
        )


        time_frame.pack(

            fill="x",

            pady=5
        )


        self.time_label = ttk.Label(

            time_frame,

            style="Value.TLabel"
        )


        self.time_label.pack(
            anchor="w"
        )


        self.generalized_angle_label = ttk.Label(

            time_frame,

            style="Value.TLabel"
        )


        self.generalized_angle_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # PROBABILITIES
        # -------------------------------------------------

        probability_frame = ttk.LabelFrame(

            right,

            text="5. Measurement Probabilities",

            padding=10
        )


        probability_frame.pack(

            fill="x",

            pady=5
        )


        self.p0_label = ttk.Label(

            probability_frame,

            style="Value.TLabel"
        )


        self.p0_label.pack(
            anchor="w"
        )


        self.p0_bar = ttk.Progressbar(

            probability_frame,

            maximum=100,

            style="Probability.Horizontal.TProgressbar"
        )


        self.p0_bar.pack(

            fill="x",

            pady=(2, 5)
        )


        self.p1_label = ttk.Label(

            probability_frame,

            style="Value.TLabel"
        )


        self.p1_label.pack(
            anchor="w"
        )


        self.p1_bar = ttk.Progressbar(

            probability_frame,

            maximum=100,

            style="Probability.Horizontal.TProgressbar"
        )


        self.p1_bar.pack(

            fill="x",

            pady=(2, 5)
        )


        self.normalization_label = ttk.Label(

            probability_frame,

            style="Value.TLabel"
        )


        self.normalization_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # BLOCH COORDINATES
        # -------------------------------------------------

        bloch_frame = ttk.LabelFrame(

            right,

            text="6. Bloch Coordinates",

            padding=10
        )


        bloch_frame.pack(

            fill="x",

            pady=5
        )


        self.x_label = ttk.Label(

            bloch_frame,

            style="Value.TLabel"
        )


        self.x_label.pack(
            anchor="w"
        )


        self.y_label = ttk.Label(

            bloch_frame,

            style="Value.TLabel"
        )


        self.y_label.pack(
            anchor="w"
        )


        self.z_label = ttk.Label(

            bloch_frame,

            style="Value.TLabel"
        )


        self.z_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # OMEGA SLIDER
        # -------------------------------------------------

        omega_frame = ttk.LabelFrame(

            right,

            text="7. Drive Strength Ω",

            padding=10
        )


        omega_frame.pack(

            fill="x",

            pady=5
        )


        self.omega_var = tk.DoubleVar(

            value=self.model.omega
        )


        self.omega_slider_label = ttk.Label(

            omega_frame,

            text="Ω = 2.00 rad/s"
        )


        self.omega_slider_label.pack(
            anchor="w"
        )


        self.omega_slider = ttk.Scale(

            omega_frame,

            from_=0.25,

            to=10.0,

            variable=self.omega_var,

            command=self.omega_changed
        )


        self.omega_slider.pack(
            fill="x"
        )


        # -------------------------------------------------
        # DETUNING SLIDER
        # -------------------------------------------------

        detuning_frame = ttk.LabelFrame(

            right,

            text="8. Detuning Δ",

            padding=10
        )


        detuning_frame.pack(

            fill="x",

            pady=5
        )


        self.delta_var = tk.DoubleVar(
            value=0.0
        )


        self.delta_slider_label = ttk.Label(

            detuning_frame,

            text="Δ = 0.00 rad/s"
        )


        self.delta_slider_label.pack(
            anchor="w"
        )


        self.delta_slider = ttk.Scale(

            detuning_frame,

            from_=-10.0,

            to=10.0,

            variable=self.delta_var,

            command=self.delta_changed
        )


        self.delta_slider.pack(
            fill="x"
        )


        ttk.Button(

            detuning_frame,

            text="Set Exact Resonance  Δ = 0",

            command=self.set_resonance,

            style="Action.TButton"

        ).pack(

            fill="x",

            pady=(5, 0)
        )


        # -------------------------------------------------
        # TIME SLIDER
        # -------------------------------------------------

        time_control = ttk.LabelFrame(

            right,

            text="9. Evolution Time",

            padding=10
        )


        time_control.pack(

            fill="x",

            pady=5
        )


        self.time_var = tk.DoubleVar(
            value=0.0
        )


        self.time_slider = ttk.Scale(

            time_control,

            from_=0.0,

            to=12.0,

            variable=self.time_var,

            command=self.time_changed
        )


        self.time_slider.pack(
            fill="x"
        )


        # -------------------------------------------------
        # EXPERIMENT BUTTONS
        # -------------------------------------------------

        experiment_frame = ttk.LabelFrame(

            right,

            text="10. Experiments",

            padding=10
        )


        experiment_frame.pack(

            fill="x",

            pady=5
        )


        ttk.Button(

            experiment_frame,

            text="Go to First Excitation Peak",

            command=self.go_first_peak,

            style="Action.TButton"

        ).pack(

            fill="x",

            pady=2
        )


        ttk.Button(

            experiment_frame,

            text="Go to Resonant π-Pulse Time",

            command=self.go_resonant_pi_time,

            style="Action.TButton"

        ).pack(

            fill="x",

            pady=2
        )


        # -------------------------------------------------
        # ANIMATION
        # -------------------------------------------------

        animation_frame = ttk.LabelFrame(

            right,

            text="11. Animation",

            padding=10
        )


        animation_frame.pack(

            fill="x",

            pady=5
        )


        ttk.Button(

            animation_frame,

            text="Start",

            command=self.start_animation,

            style="Action.TButton"

        ).pack(

            side="left",

            fill="x",

            expand=True,

            padx=(0, 2)
        )


        ttk.Button(

            animation_frame,

            text="Pause",

            command=self.pause_animation,

            style="Action.TButton"

        ).pack(

            side="left",

            fill="x",

            expand=True,

            padx=2
        )


        ttk.Button(

            animation_frame,

            text="Reset Time",

            command=self.reset_time,

            style="Action.TButton"

        ).pack(

            side="left",

            fill="x",

            expand=True,

            padx=(2, 0)
        )


    # =====================================================
    # LEARNING AREA
    # =====================================================

    def create_learning_area(self):

        learning = ttk.LabelFrame(

            self.root,

            text="Python + Quantum Learning Console",

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
        # WHAT IS HAPPENING?
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
        # PYTHON BEHIND ACTION
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
        # NEW PYTHON
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
NEW PYTHON / MATH CONCEPTS IN FILE 05
=====================================


1. SQUARING

   value ** 2

   means:

       value²


2. SQUARE ROOT

   math.sqrt(value)

   calculates:

       √value


3. GENERALIZED RABI FREQUENCY

   omega_r = math.sqrt(
       omega ** 2 + delta ** 2
   )


4. FUNCTION COMPOSITION

   Several functions call other functions.

   Example:

       probabilities()
           ↓
       alpha()
       beta()
           ↓
       generalized_rabi_frequency()

   This keeps the program organized.


5. DENOMINATOR CHECK

   if denominator == 0:

   prevents Python from dividing by zero.


6. ABSOLUTE DETUNING IDEA

   Probability depends on:

       delta ** 2

   Therefore +delta and -delta give the same
   population oscillation in this simple model.

   Their complex phase evolution can still differ.


7. REFERENCE CURVES

   The graph calculates both:

       current detuned probability

   and:

       resonance probability

   so we can visually compare them.


8. max()

   max(a, b)

   returns whichever value is larger.


9. STATE VARIABLES

   The model stores:

       self.omega
       self.delta
       self.time

   Changing one changes the quantum calculation.


10. SCIENTIFIC MODEL STRUCTURE

    Parameters
       ↓
    equations
       ↓
    state amplitudes
       ↓
    probabilities
       ↓
    visualization
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

        # Unlock text area.

        self.lesson_text.config(
            state="normal"
        )


        # Remove previous content.

        self.lesson_text.delete(
            "1.0",
            tk.END
        )


        # Insert new explanation.

        self.lesson_text.insert(

            tk.END,

            f"{title}\n\n{explanation}"
        )


        # Lock again.

        self.lesson_text.config(
            state="disabled"
        )


        # Update Python-code tab.

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
    # FORMAT COMPLEX
    # =====================================================

    def format_complex(

        self,

        value
    ):

        # Separate real and imaginary pieces.

        real = value.real

        imag = value.imag


        # Decide displayed sign.

        sign = (

            "+"

            if imag >= 0

            else "-"
        )


        return (

            f"{real:.4f} "

            f"{sign} "

            f"{abs(imag):.4f}i"
        )


    # =====================================================
    # UPDATE DISPLAY
    # =====================================================

    def update_display(self):

        # Calculate current amplitudes.

        alpha = self.model.alpha()

        beta = self.model.beta()


        # Probabilities.

        p0, p1 = (
            self.model.probabilities()
        )


        # Generalized Rabi frequency.

        omega_r = (
            self.model.generalized_rabi_frequency()
        )


        # Maximum possible P(1).

        max_p1 = (
            self.model.maximum_excited_probability()
        )


        # First excitation peak.

        first_peak = (
            self.model.first_peak_time()
        )


        # Resonant pi time.

        resonant_pi = (
            self.model.resonant_pi_time()
        )


        # Normalization.

        normalization = (
            self.model.normalization()
        )


        # Bloch coordinates.

        x, y, z = (
            self.model.bloch_coordinates()
        )


        # -------------------------------------------------
        # QUANTUM STATE
        # -------------------------------------------------

        self.state_label.config(

            text=(
                "|ψ(t)⟩ =\n"

                f"({self.format_complex(alpha)})|0⟩\n"

                "+\n"

                f"({self.format_complex(beta)})|1⟩"
            )
        )


        # -------------------------------------------------
        # FREQUENCIES
        # -------------------------------------------------

        self.omega_label.config(

            text=(
                f"Ω = {self.model.omega:.4f} rad/s"
            )
        )


        self.delta_label.config(

            text=(
                f"Δ = {self.model.delta:.4f} rad/s"
            )
        )


        self.omega_r_label.config(

            text=(
                "Ω_R = √(Ω² + Δ²) "
                f"= {omega_r:.4f} rad/s"
            )
        )


        # Show resonance status.

        if abs(self.model.delta) < 1e-9:

            resonance_text = (
                "✓ ON RESONANCE"
            )

        else:

            resonance_text = (
                "OFF RESONANCE"
            )


        self.resonance_label.config(
            text=resonance_text
        )


        # -------------------------------------------------
        # IMPORTANT RESULTS
        # -------------------------------------------------

        self.max_probability_label.config(

            text=(
                "Maximum P(1) = "
                f"{max_p1:.4f} "
                f"= {max_p1 * 100:.1f}%"
            )
        )


        self.first_peak_label.config(

            text=(
                "First excitation peak = "
                f"{first_peak:.4f} s"
            )
        )


        self.resonant_pi_label.config(

            text=(
                "Resonant π time = "
                f"{resonant_pi:.4f} s"
            )
        )


        # -------------------------------------------------
        # TIME
        # -------------------------------------------------

        self.time_label.config(

            text=(
                f"t = {self.model.time:.4f} s"
            )
        )


        generalized_angle = (

            omega_r
            *
            self.model.time
        )


        self.generalized_angle_label.config(

            text=(
                "Ω_R t = "
                f"{generalized_angle:.4f} rad "
                f"= {math.degrees(generalized_angle):.1f}°"
            )
        )


        # -------------------------------------------------
        # PROBABILITIES
        # -------------------------------------------------

        self.p0_label.config(

            text=(
                f"P(0) = {p0:.4f} "
                f"= {p0 * 100:.1f}%"
            )
        )


        self.p1_label.config(

            text=(
                f"P(1) = {p1:.4f} "
                f"= {p1 * 100:.1f}%"
            )
        )


        self.p0_bar["value"] = (
            p0 * 100
        )


        self.p1_bar["value"] = (
            p1 * 100
        )


        self.normalization_label.config(

            text=(
                f"P(0) + P(1) = "
                f"{normalization:.6f}"
            )
        )


        # -------------------------------------------------
        # BLOCH COORDINATES
        # -------------------------------------------------

        self.x_label.config(

            text=f"x = {x:.4f}"
        )


        self.y_label.config(

            text=f"y = {y:.4f}"
        )


        self.z_label.config(

            text=f"z = {z:.4f}"
        )


        # -------------------------------------------------
        # SLIDER LABELS
        # -------------------------------------------------

        self.omega_slider_label.config(

            text=(
                f"Ω = {self.model.omega:.2f} rad/s"
            )
        )


        self.delta_slider_label.config(

            text=(
                f"Δ = {self.model.delta:.2f} rad/s"
            )
        )


        # -------------------------------------------------
        # GRAPH
        # -------------------------------------------------

        self.draw_plot()


    # =====================================================
    # DRAW GRAPH
    # =====================================================

    def draw_plot(self):

        # Remove previous plot.

        self.ax.clear()


        # Get generalized frequency.

        omega_r = (
            self.model.generalized_rabi_frequency()
        )


        # Get approximate oscillation period.

        if omega_r > 0:

            generalized_period = (

                2
                *
                math.pi
                /
                omega_r
            )

        else:

            generalized_period = 4.0


        # Show several oscillations.

        max_time = max(

            3 * generalized_period,

            5.0
        )


        # Make current time visible.

        if self.model.time > max_time:

            max_time = (

                self.model.time
                *
                1.1
            )


        # -------------------------------------------------
        # TIME ARRAY
        # -------------------------------------------------

        times = np.linspace(

            0,

            max_time,

            700
        )


        # -------------------------------------------------
        # CURRENT DETUNED P(1)
        # -------------------------------------------------

        denominator = (

            self.model.omega ** 2

            +

            self.model.delta ** 2
        )


        if denominator > 0:

            amplitude_factor = (

                self.model.omega ** 2

                /

                denominator
            )

        else:

            amplitude_factor = 0.0


        detuned_p1 = (

            amplitude_factor

            *

            np.sin(

                omega_r
                *
                times
                /
                2

            ) ** 2
        )


        # P(0) = 1 - P(1)

        detuned_p0 = (

            1.0

            -

            detuned_p1
        )


        # -------------------------------------------------
        # RESONANCE REFERENCE
        # -------------------------------------------------

        resonance_p1 = (

            np.sin(

                self.model.omega
                *
                times
                /
                2

            ) ** 2
        )


        # -------------------------------------------------
        # PLOT CURRENT P0
        # -------------------------------------------------

        self.ax.plot(

            times,

            detuned_p0,

            label="P(0) current"
        )


        # -------------------------------------------------
        # PLOT CURRENT P1
        # -------------------------------------------------

        self.ax.plot(

            times,

            detuned_p1,

            label="P(1) current"
        )


        # -------------------------------------------------
        # PLOT RESONANCE REFERENCE
        # -------------------------------------------------

        self.ax.plot(

            times,

            resonance_p1,

            linestyle="--",

            label="P(1) if Δ = 0"
        )


        # -------------------------------------------------
        # MAXIMUM P1 LINE
        # -------------------------------------------------

        self.ax.axhline(

            self.model.maximum_excited_probability(),

            linestyle=":",

            label="Maximum current P(1)"
        )


        # -------------------------------------------------
        # CURRENT TIME
        # -------------------------------------------------

        self.ax.axvline(

            self.model.time,

            linestyle="--",

            label="Current time"
        )


        # -------------------------------------------------
        # GRAPH SETTINGS
        # -------------------------------------------------

        self.ax.set_xlim(
            0,
            max_time
        )


        self.ax.set_ylim(
            -0.05,
            1.05
        )


        self.ax.set_xlabel(
            "Time t (seconds)"
        )


        self.ax.set_ylabel(
            "Probability"
        )


        self.ax.set_title(
            "Effect of Detuning on Rabi Oscillation"
        )


        self.ax.grid(
            True,
            alpha=0.3
        )


        self.ax.legend()


        # Redraw graph inside Tkinter.

        self.plot_canvas.draw_idle()


    # =====================================================
    # OMEGA CHANGED
    # =====================================================

    def omega_changed(

        self,

        value=None
    ):

        # Read slider.

        omega = (
            self.omega_var.get()
        )


        # Store new Ω.

        self.model.set_omega(
            omega
        )


        # Refresh.

        self.update_display()


        self.show_lesson(

            title="Drive strength Ω changed",

            explanation=(
                f"Ω is now {omega:.3f} rad/s.\n\n"

                "Ω controls how strongly the two quantum "
                "levels are coupled.\n\n"

                "The generalized frequency is:\n\n"

                "    Ω_R = √(Ω² + Δ²)\n\n"

                "The maximum excited-state probability is:\n\n"

                "             Ω²\n"
                "    Pmax = ---------\n"
                "           Ω² + Δ²\n\n"

                "If Ω becomes much larger than |Δ|, "
                "detuning becomes less important."
            ),

            python_code=(
                "omega = self.omega_var.get()\n\n"

                "self.model.set_omega(omega)\n\n"

                "# Inside model:\n\n"

                "self.omega = omega\n\n"

                "# Then Ω_R is recalculated:\n\n"

                "omega_r = math.sqrt(\n"
                "    self.omega ** 2\n"
                "    + self.delta ** 2\n"
                ")"
            )
        )


    # =====================================================
    # DELTA CHANGED
    # =====================================================

    def delta_changed(

        self,

        value=None
    ):

        # Read slider.

        delta = (
            self.delta_var.get()
        )


        # Store detuning.

        self.model.set_delta(
            delta
        )


        # Refresh.

        self.update_display()


        max_p1 = (
            self.model.maximum_excited_probability()
        )


        self.show_lesson(

            title="Detuning Δ changed",

            explanation=(
                f"Current Δ = {delta:.3f} rad/s.\n\n"

                "Detuning represents the frequency mismatch:\n\n"

                "    Δ = ω_drive - ω_0\n\n"

                "If Δ = 0, we are exactly resonant.\n\n"

                "If Δ ≠ 0, the drive is not perfectly matched "
                "to the transition.\n\n"

                "For the current parameters:\n\n"

                f"    maximum P(1) = {max_p1:.4f}\n"
                f"                 = {max_p1 * 100:.1f}%\n\n"

                "Notice the important result:\n\n"

                "larger |Δ| generally reduces the maximum "
                "population transfer."
            ),

            python_code=(
                "delta = self.delta_var.get()\n\n"

                "self.model.set_delta(delta)\n\n"

                "# Inside the model:\n\n"

                "self.delta = delta\n\n"

                "# Maximum excitation:\n\n"

                "max_p1 = (\n"
                "    omega ** 2\n"
                "    /\n"
                "    (omega ** 2 + delta ** 2)\n"
                ")"
            )
        )


    # =====================================================
    # TIME CHANGED
    # =====================================================

    def time_changed(

        self,

        value=None
    ):

        # Read time slider.

        time = (
            self.time_var.get()
        )


        # Store current time.

        self.model.set_time(
            time
        )


        # Refresh.

        self.update_display()


        p0, p1 = (
            self.model.probabilities()
        )


        self.show_lesson(

            title="Evolution time changed",

            explanation=(
                f"Current t = {time:.4f} s.\n\n"

                "The system evaluates the generalized Rabi "
                "frequency first:\n\n"

                "    Ω_R = √(Ω² + Δ²)\n\n"

                "Then it calculates:\n\n"

                "             Ω²\n"
                "    P(1) = --------- sin²(Ω_R t / 2)\n"
                "           Ω² + Δ²\n\n"

                f"Current P(0) = {p0:.4f}\n"
                f"Current P(1) = {p1:.4f}"
            ),

            python_code=(
                "time = self.time_var.get()\n\n"

                "self.model.set_time(time)\n\n"

                "omega_r = math.sqrt(\n"
                "    omega ** 2 + delta ** 2\n"
                ")\n\n"

                "p1 = (\n"
                "    omega ** 2\n"
                "    /\n"
                "    (omega ** 2 + delta ** 2)\n"
                "    *\n"
                "    math.sin(omega_r * time / 2) ** 2\n"
                ")"
            )
        )


    # =====================================================
    # SET RESONANCE
    # =====================================================

    def set_resonance(self):

        # Set Δ = 0.

        self.model.set_resonance()


        # Update slider.

        self.delta_var.set(
            0.0
        )


        # Refresh.

        self.update_display()


        self.show_lesson(

            title="Exact resonance restored",

            explanation=(
                "Detuning has been set to zero:\n\n"

                "    Δ = 0\n\n"

                "Therefore:\n\n"

                "    Ω_R = √(Ω²)\n"
                "        = Ω\n\n"

                "and:\n\n"

                "             Ω²\n"
                "    Pmax = -------\n"
                "             Ω²\n"
                "         = 1\n\n"

                "So this ideal model can again reach "
                "100% excitation."
            ),

            python_code=(
                "def set_resonance(self):\n"
                "    self.delta = 0.0\n\n"

                "# Resonance means zero frequency mismatch."
            )
        )


    # =====================================================
    # GO TO FIRST PEAK
    # =====================================================

    def go_first_peak(self):

        # Calculate time of first maximum.

        peak_time = (
            self.model.first_peak_time()
        )


        # Store it.

        self.model.set_time(
            peak_time
        )


        # Move slider.

        self.time_var.set(
            peak_time
        )


        # Refresh.

        self.update_display()


        p0, p1 = (
            self.model.probabilities()
        )


        self.show_lesson(

            title="First excitation peak",

            explanation=(
                "The first maximum of sin² occurs when:\n\n"

                "    Ω_R t = π\n\n"

                "so:\n\n"

                "        π\n"
                "    t = ---\n"
                "        Ω_R\n\n"

                f"Current first peak time = {peak_time:.4f} s\n\n"

                f"At that point P(1) = {p1:.4f}\n\n"

                "Important:\n\n"

                "When Δ ≠ 0, this may be the maximum of the "
                "oscillation, but the maximum can still be "
                "less than 100%."
            ),

            python_code=(
                "omega_r = self.generalized_rabi_frequency()\n\n"

                "peak_time = math.pi / omega_r\n\n"

                "# At this point:\n"
                "# sin²(omega_r * t / 2) = 1\n\n"

                "# But the prefactor remains:\n"
                "# omega² / (omega² + delta²)"
            )
        )


    # =====================================================
    # RESONANT PI TIME
    # =====================================================

    def go_resonant_pi_time(self):

        # Calculate t = π / Ω.

        pi_time = (
            self.model.resonant_pi_time()
        )


        # Store time.

        self.model.set_time(
            pi_time
        )


        # Move slider.

        self.time_var.set(
            pi_time
        )


        # Refresh.

        self.update_display()


        p0, p1 = (
            self.model.probabilities()
        )


        self.show_lesson(

            title="Resonant π-pulse duration applied",

            explanation=(
                "The resonant π-pulse duration is:\n\n"

                "    tπ = π / Ω\n\n"

                "When Δ = 0, this gives complete transfer:\n\n"

                "    |0⟩ → |1⟩\n\n"

                "But if Δ ≠ 0, the same pulse duration is "
                "generally no longer perfect.\n\n"

                f"For your current Δ:\n\n"

                f"    P(0) = {p0:.4f}\n"
                f"    P(1) = {p1:.4f}\n\n"

                "This demonstrates why frequency calibration "
                "matters in quantum control."
            ),

            python_code=(
                "pi_time = math.pi / self.omega\n\n"

                "self.time = pi_time\n\n"

                "# If delta = 0:\n"
                "#     P1 = 1\n\n"

                "# If delta != 0:\n"
                "#     P1 is generally less than 1."
            )
        )


    # =====================================================
    # START ANIMATION
    # =====================================================

    def start_animation(self):

        # Prevent multiple simultaneous animation loops.

        if self.running:

            return


        self.running = True


        self.show_lesson(

            title="Animation started",

            explanation=(
                "Time now increases automatically.\n\n"

                "At every step Python recalculates:\n\n"

                "    Ω_R\n"
                "      ↓\n"
                "    α(t), β(t)\n"
                "      ↓\n"
                "    P(0), P(1)\n"
                "      ↓\n"
                "    graph + labels\n\n"

                "Change Δ while the animation is running "
                "and observe the oscillation immediately."
            ),

            python_code=(
                "self.running = True\n\n"

                "self.animate_step()\n\n"

                "# animate_step() will repeatedly update time."
            )
        )


        self.animate_step()


    # =====================================================
    # ANIMATION STEP
    # =====================================================

    def animate_step(self):

        # Stop if Pause was pressed.

        if not self.running:

            return


        # Increase time.

        new_time = (

            self.model.time

            +

            self.animation_dt
        )


        # Restart after 12 seconds.

        if new_time > 12.0:

            new_time = 0.0


        # Store time.

        self.model.set_time(
            new_time
        )


        # Move time slider.

        self.time_var.set(
            new_time
        )


        # Refresh GUI.

        self.update_display()


        # Run again after roughly 30 ms.

        self.root.after(

            30,

            self.animate_step
        )


    # =====================================================
    # PAUSE ANIMATION
    # =====================================================

    def pause_animation(self):

        self.running = False


        self.show_lesson(

            title="Animation paused",

            explanation=(
                "Automatic time evolution has been paused.\n\n"

                "The current simulated quantum state is "
                "left at its present value of t."
            ),

            python_code=(
                "self.running = False\n\n"

                "# animate_step() sees False\n"
                "# and stops scheduling new updates."
            )
        )


    # =====================================================
    # RESET TIME
    # =====================================================

    def reset_time(self):

        # Stop animation.

        self.running = False


        # t = 0.

        self.model.reset()


        # Move slider.

        self.time_var.set(
            0.0
        )


        # Refresh.

        self.update_display()


        self.show_lesson(

            title="Time reset",

            explanation=(
                "Time has returned to zero.\n\n"

                "Regardless of detuning, our chosen initial state is:\n\n"

                "    |ψ(0)⟩ = |0⟩\n\n"

                "because:\n\n"

                "    α(0) = 1\n"
                "    β(0) = 0"
            ),

            python_code=(
                "self.model.reset()\n\n"

                "# Inside reset():\n\n"

                "self.time = 0.0"
            )
        )


# =========================================================
# START APPLICATION
# =========================================================


if __name__ == "__main__":

    # PowerShell message.

    print(
        "Running 05_detuning.py ..."
    )


    # Create Tkinter window.

    root = tk.Tk()


    # Create application.

    app = DetuningGUI(
        root
    )


    # Keep application alive.

    root.mainloop()