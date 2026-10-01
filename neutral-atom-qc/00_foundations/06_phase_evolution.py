"""
=========================================================
06 - PHASE EVOLUTION
Neutral-Atom Quantum Computing Learning
=========================================================

GOAL
----

Understand that a quantum state can evolve even when
the measurement probabilities P(0) and P(1) remain unchanged.

We study states of the form:

                |0> + e^(iφ)|1>
    |ψ> = --------------------------
                        √2

Both amplitudes have magnitude:

    1 / √2

Therefore:

    P(0) = 1/2
    P(1) = 1/2

for EVERY value of φ.

However:

    φ

is the RELATIVE PHASE.

Changing φ changes the quantum state.


PHASE EVOLUTION
---------------

In this simplified model:

    φ(t) = φ₀ + ωt

where:

    φ₀ = initial relative phase
    ω  = phase-evolution angular frequency
    t  = time


GLOBAL PHASE
------------

We also allow a global phase:

    γ

so the state becomes:

    |ψ> =
        e^(iγ) / √2
        [
            |0> + e^(iφ)|1>
        ]

The factor:

    e^(iγ)

multiplies the ENTIRE state.

Changing γ alone does NOT change physical measurement
probabilities.

Relative phase φ DOES matter.


HOW DO WE DETECT RELATIVE PHASE?
--------------------------------

In the computational Z basis:

    P(0) = 50%
    P(1) = 50%

regardless of φ.

But if we measure in the X basis:

    |+> = (|0> + |1>) / √2

    |-> = (|0> - |1>) / √2

then:

    P(+) = cos²(φ/2)

    P(-) = sin²(φ/2)

Now the phase becomes observable through interference.


IMPORTANT PHYSICS NOTE
----------------------

This is an EDUCATIONAL ideal single-qubit model.

It is NOT yet a complete neutral-atom simulation.

In real systems, phase evolution may result from:

    - energy differences
    - laser phase
    - detuning
    - free evolution
    - magnetic-field shifts
    - AC Stark shifts
    - noise

Later we will study those effects more physically.
"""


# =========================================================
# IMPORTS
# =========================================================


# math gives us:
#
#     sin()
#     cos()
#     sqrt()
#     pi
#     radians()
#     degrees()
#
import math


# NumPy helps us calculate arrays of many time values
# for plotting phase evolution.
#
import numpy as np


# Tkinter creates the graphical interface.
#
import tkinter as tk


# ttk contains modern Tkinter widgets.
#
from tkinter import ttk


# ScrolledText gives us text areas
# with built-in scrollbars.
#
from tkinter.scrolledtext import ScrolledText


# Matplotlib Figure is our plotting container.
#
from matplotlib.figure import Figure


# This embeds Matplotlib inside Tkinter.
#
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# =========================================================
# PHASE EVOLUTION MODEL
# =========================================================


class PhaseEvolutionModel:

    """
    This class contains the quantum mathematics.

    We study an equal-amplitude qubit:

        |ψ> =
            e^(iγ) / √2
            [
                |0> + e^(iφ)|1>
            ]

    where:

        γ = global phase
        φ = relative phase

    and:

        φ(t) = φ₀ + ωt
    """


    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(self):

        # Phase evolution rate.
        #
        # Units:
        #
        #     radians / second
        #
        self.omega = 1.5


        # Start at time zero.

        self.time = 0.0


        # Initial relative phase:
        #
        #     φ₀ = 0
        #
        # Therefore initially:
        #
        #     |ψ> = |+>
        #
        self.phi_0 = 0.0


        # Global phase.
        #
        # Initially:
        #
        #     γ = 0
        #
        self.global_phase = 0.0


    # =====================================================
    # RELATIVE PHASE
    # =====================================================

    def relative_phase(self):

        # Equation:
        #
        #     φ(t) = φ₀ + ωt

        phi = (

            self.phi_0

            +

            self.omega
            *
            self.time
        )


        return phi


    # =====================================================
    # WRAPPED RELATIVE PHASE
    # =====================================================

    def wrapped_relative_phase(self):

        # relative_phase() may become:
        #
        #     450°
        #     810°
        #     1200°
        #
        # Physically, phase repeats every 360°.
        #
        # We wrap it into:
        #
        #     0 <= φ < 2π

        phi = self.relative_phase()


        wrapped = (

            phi

            %

            (
                2
                *
                math.pi
            )
        )


        return wrapped


    # =====================================================
    # GLOBAL PHASE FACTOR
    # =====================================================

    def global_phase_factor(self):

        # Euler's formula:
        #
        #     e^(iγ)
        #
        # becomes:
        #
        #     cos(γ) + i sin(γ)

        return complex(

            math.cos(
                self.global_phase
            ),

            math.sin(
                self.global_phase
            )
        )


    # =====================================================
    # ALPHA
    # =====================================================

    def alpha(self):

        # Equal-amplitude state:
        #
        #          e^(iγ)
        #     α = --------
        #            √2

        magnitude = (

            1

            /

            math.sqrt(2)
        )


        return (

            magnitude

            *

            self.global_phase_factor()
        )


    # =====================================================
    # BETA
    # =====================================================

    def beta(self):

        # Beta includes BOTH:
        #
        #     global phase γ
        #
        # and:
        #
        #     relative phase φ
        #
        #
        #                  e^(i(γ+φ))
        #     β = -----------------------
        #                       √2


        # Calculate total angle.

        total_phase = (

            self.global_phase

            +

            self.relative_phase()
        )


        # Create:
        #
        #     e^(i(γ+φ))

        phase_factor = complex(

            math.cos(
                total_phase
            ),

            math.sin(
                total_phase
            )
        )


        magnitude = (

            1

            /

            math.sqrt(2)
        )


        return (

            magnitude

            *

            phase_factor
        )


    # =====================================================
    # Z-BASIS PROBABILITIES
    # =====================================================

    def z_probabilities(self):

        # Obtain amplitudes.

        alpha = self.alpha()

        beta = self.beta()


        # Born rule:
        #
        #     P(0) = |α|²

        probability_0 = (

            abs(alpha) ** 2
        )


        # And:
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
    # X-BASIS PROBABILITIES
    # =====================================================

    def x_probabilities(self):

        # X-basis states:
        #
        #             |0> + |1>
        #     |+> = -------------
        #                  √2
        #
        #
        #             |0> - |1>
        #     |-> = -------------
        #                  √2


        # Obtain computational-basis amplitudes.

        alpha = self.alpha()

        beta = self.beta()


        # Amplitude for measuring |+>:
        #
        #     <+|ψ>
        #
        # which becomes:
        #
        #     (α + β) / √2

        plus_amplitude = (

            alpha
            +
            beta

        ) / math.sqrt(2)


        # Amplitude for |->
        #
        #     (α - β) / √2

        minus_amplitude = (

            alpha
            -
            beta

        ) / math.sqrt(2)


        # Convert amplitudes into probabilities.

        probability_plus = (

            abs(plus_amplitude) ** 2
        )


        probability_minus = (

            abs(minus_amplitude) ** 2
        )


        return (

            probability_plus,

            probability_minus
        )


    # =====================================================
    # NORMALIZATION
    # =====================================================

    def normalization(self):

        p0, p1 = (
            self.z_probabilities()
        )


        return (
            p0
            +
            p1
        )


    # =====================================================
    # BLOCH COORDINATES
    # =====================================================

    def bloch_coordinates(self):

        # Obtain relative phase.
        #
        # Notice that GLOBAL phase is not used.
        #
        # This is important.

        phi = (
            self.relative_phase()
        )


        # For equal amplitudes:
        #
        #     θ = 90°
        #
        # so the state lies on the equator.
        #
        # Therefore:
        #
        #     x = cos(φ)
        #     y = sin(φ)
        #     z = 0

        x = math.cos(
            phi
        )


        y = math.sin(
            phi
        )


        z = 0.0


        return (
            x,
            y,
            z
        )


    # =====================================================
    # PHASE PERIOD
    # =====================================================

    def phase_period(self):

        # Relative phase repeats whenever:
        #
        #     φ changes by 2π
        #
        # If:
        #
        #     φ = ωt
        #
        # then:
        #
        #     ωT = 2π
        #
        # therefore:
        #
        #         2π
        #     T = ---
        #         |ω|

        if self.omega == 0:

            return math.inf


        return (

            2
            *
            math.pi

            /

            abs(
                self.omega
            )
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
    # SET TIME
    # =====================================================

    def set_time(
        self,
        time
    ):

        self.time = time


    # =====================================================
    # SET INITIAL RELATIVE PHASE
    # =====================================================

    def set_phi_0(
        self,
        phi
    ):

        self.phi_0 = phi


    # =====================================================
    # SET GLOBAL PHASE
    # =====================================================

    def set_global_phase(
        self,
        gamma
    ):

        self.global_phase = gamma


    # =====================================================
    # PREPARE |+>
    # =====================================================

    def set_plus(self):

        # |+> has:
        #
        #     relative phase = 0°

        self.time = 0.0

        self.phi_0 = 0.0

        self.global_phase = 0.0


    # =====================================================
    # PREPARE |->
    # =====================================================

    def set_minus(self):

        # |-> has:
        #
        #     relative phase = 180°
        #
        #     φ = π

        self.time = 0.0

        self.phi_0 = math.pi

        self.global_phase = 0.0


    # =====================================================
    # PREPARE |+i>
    # =====================================================

    def set_plus_i(self):

        # |+i>:
        #
        #     relative phase = +90°
        #
        #     φ = π/2

        self.time = 0.0

        self.phi_0 = (

            math.pi
            /
            2
        )

        self.global_phase = 0.0


    # =====================================================
    # PREPARE |-i>
    # =====================================================

    def set_minus_i(self):

        # |-i>:
        #
        #     relative phase = -90°
        #
        # equivalent to:
        #
        #     270°
        #
        # so:
        #
        #     φ = 3π/2

        self.time = 0.0

        self.phi_0 = (

            3
            *
            math.pi
            /
            2
        )

        self.global_phase = 0.0


    # =====================================================
    # RESET TIME
    # =====================================================

    def reset_time(self):

        self.time = 0.0


# =========================================================
# GUI
# =========================================================


class PhaseEvolutionGUI:

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(
        self,
        root
    ):

        # Store main Tkinter window.

        self.root = root


        # Set window title.

        self.root.title(
            "Neutral-Atom QC | 06 — Phase Evolution"
        )


        # Starting window size.

        self.root.geometry(
            "1450x950"
        )


        # Minimum allowed size.

        self.root.minsize(
            1150,
            780
        )


        # -------------------------------------------------
        # CREATE QUANTUM MODEL
        # -------------------------------------------------

        self.model = (
            PhaseEvolutionModel()
        )


        # -------------------------------------------------
        # ANIMATION
        # -------------------------------------------------

        # Animation initially stopped.

        self.running = False


        # Amount of simulated time added
        # during one animation update.

        self.animation_dt = 0.03


        # -------------------------------------------------
        # BUILD INTERFACE
        # -------------------------------------------------

        self.setup_style()

        self.create_header()

        self.create_main_area()

        self.create_learning_area()


        # Show initial state.

        self.update_display()


        # Initial lesson.

        self.show_lesson(

            title="Phase evolution initialized",

            explanation=(
                "The initial state is |+⟩:\n\n"

                "          |0⟩ + |1⟩\n"
                "    |+⟩ = -----------\n"
                "               √2\n\n"

                "Both amplitudes have magnitude 1/√2.\n\n"

                "Therefore:\n\n"

                "    P(0) = 50%\n"
                "    P(1) = 50%\n\n"

                "However, the relative phase will now evolve "
                "with time according to:\n\n"

                "    φ(t) = φ₀ + ωt"
            ),

            python_code=(
                "self.model = PhaseEvolutionModel()\n\n"

                "# Initial values:\n\n"

                "self.omega = 1.5\n"
                "self.time = 0.0\n"
                "self.phi_0 = 0.0\n"
                "self.global_phase = 0.0"
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

            text="06 — Phase Evolution",

            style="Section.TLabel"

        ).pack(
            anchor="w"
        )


        ttk.Label(

            header,

            text=(
                "Understand relative phase, global phase "
                "and quantum interference"
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

        left = ttk.Frame(
            main
        )


        left.grid(

            row=0,

            column=0,

            sticky="nsew",

            padx=(0, 8)
        )


        left.rowconfigure(
            0,
            weight=3
        )


        left.rowconfigure(
            1,
            weight=2
        )


        left.columnconfigure(
            0,
            weight=1
        )


        # -------------------------------------------------
        # INTERFERENCE GRAPH
        # -------------------------------------------------

        plot_frame = ttk.LabelFrame(

            left,

            text="Phase → Interference",

            padding=10
        )


        plot_frame.grid(

            row=0,

            column=0,

            sticky="nsew",

            pady=(0, 5)
        )


        self.figure = Figure(

            figsize=(7, 4),

            dpi=100
        )


        self.ax = (
            self.figure.add_subplot(
                111
            )
        )


        self.plot_canvas = (
            FigureCanvasTkAgg(

                self.figure,

                master=plot_frame
            )
        )


        self.plot_canvas.get_tk_widget().pack(

            fill="both",

            expand=True
        )


        ttk.Label(

            plot_frame,

            text=(
                "Z-basis probabilities remain 50/50, but X-basis "
                "probabilities oscillate as relative phase evolves."
            ),

            wraplength=700

        ).pack(
            fill="x",
            pady=(5, 0)
        )


        # -------------------------------------------------
        # COMPLEX AMPLITUDE VISUALIZATION
        # -------------------------------------------------

        phase_frame = ttk.LabelFrame(

            left,

            text="Complex Amplitude Phase Arrows",

            padding=10
        )


        phase_frame.grid(

            row=1,

            column=0,

            sticky="nsew",

            pady=(5, 0)
        )


        self.phase_canvas = tk.Canvas(

            phase_frame,

            bg="white",

            highlightthickness=0
        )


        self.phase_canvas.pack(

            fill="both",

            expand=True
        )


        self.phase_canvas.bind(

            "<Configure>",

            self.canvas_resized
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
        # CURRENT STATE
        # -------------------------------------------------

        state_frame = ttk.LabelFrame(

            right,

            text="1. Current State",

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
        # PHASE INFORMATION
        # -------------------------------------------------

        phase_info = ttk.LabelFrame(

            right,

            text="2. Phase Information",

            padding=10
        )


        phase_info.pack(

            fill="x",

            pady=5
        )


        self.time_label = ttk.Label(

            phase_info,

            style="Value.TLabel"
        )


        self.time_label.pack(
            anchor="w"
        )


        self.omega_label = ttk.Label(

            phase_info,

            style="Value.TLabel"
        )


        self.omega_label.pack(
            anchor="w"
        )


        self.phi0_label = ttk.Label(

            phase_info,

            style="Value.TLabel"
        )


        self.phi0_label.pack(
            anchor="w"
        )


        self.relative_phase_label = ttk.Label(

            phase_info,

            style="Value.TLabel"
        )


        self.relative_phase_label.pack(
            anchor="w"
        )


        self.global_phase_label = ttk.Label(

            phase_info,

            style="Value.TLabel"
        )


        self.global_phase_label.pack(
            anchor="w"
        )


        self.period_label = ttk.Label(

            phase_info,

            style="Value.TLabel"
        )


        self.period_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # BLOCH COORDINATES
        # -------------------------------------------------

        bloch_frame = ttk.LabelFrame(

            right,

            text="3. Bloch Equator",

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
        # Z BASIS
        # -------------------------------------------------

        z_frame = ttk.LabelFrame(

            right,

            text="4. Z-Basis Measurement",

            padding=10
        )


        z_frame.pack(

            fill="x",

            pady=5
        )


        self.p0_label = ttk.Label(

            z_frame,

            style="Value.TLabel"
        )


        self.p0_label.pack(
            anchor="w"
        )


        self.p0_bar = ttk.Progressbar(

            z_frame,

            maximum=100,

            style="Probability.Horizontal.TProgressbar"
        )


        self.p0_bar.pack(

            fill="x",

            pady=(2, 5)
        )


        self.p1_label = ttk.Label(

            z_frame,

            style="Value.TLabel"
        )


        self.p1_label.pack(
            anchor="w"
        )


        self.p1_bar = ttk.Progressbar(

            z_frame,

            maximum=100,

            style="Probability.Horizontal.TProgressbar"
        )


        self.p1_bar.pack(

            fill="x",

            pady=(2, 5)
        )


        # -------------------------------------------------
        # X BASIS
        # -------------------------------------------------

        x_frame = ttk.LabelFrame(

            right,

            text="5. X-Basis Measurement — Interference",

            padding=10
        )


        x_frame.pack(

            fill="x",

            pady=5
        )


        self.pplus_label = ttk.Label(

            x_frame,

            style="Value.TLabel"
        )


        self.pplus_label.pack(
            anchor="w"
        )


        self.pplus_bar = ttk.Progressbar(

            x_frame,

            maximum=100,

            style="Probability.Horizontal.TProgressbar"
        )


        self.pplus_bar.pack(

            fill="x",

            pady=(2, 5)
        )


        self.pminus_label = ttk.Label(

            x_frame,

            style="Value.TLabel"
        )


        self.pminus_label.pack(
            anchor="w"
        )


        self.pminus_bar = ttk.Progressbar(

            x_frame,

            maximum=100,

            style="Probability.Horizontal.TProgressbar"
        )


        self.pminus_bar.pack(

            fill="x",

            pady=(2, 5)
        )


        # -------------------------------------------------
        # CONTROLS
        # -------------------------------------------------

        control_frame = ttk.LabelFrame(

            right,

            text="6. Phase Controls",

            padding=10
        )


        control_frame.pack(

            fill="x",

            pady=5
        )


        # Omega variable.

        self.omega_var = tk.DoubleVar(

            value=self.model.omega
        )


        self.omega_slider_label = ttk.Label(

            control_frame,

            text="ω = 1.50 rad/s"
        )


        self.omega_slider_label.pack(
            anchor="w"
        )


        self.omega_slider = ttk.Scale(

            control_frame,

            from_=0.0,

            to=6.0,

            variable=self.omega_var,

            command=self.controls_changed
        )


        self.omega_slider.pack(
            fill="x"
        )


        # Initial relative phase.

        self.phi0_var = tk.DoubleVar(
            value=0.0
        )


        self.phi0_slider_label = ttk.Label(

            control_frame,

            text="Initial φ₀ = 0°"
        )


        self.phi0_slider_label.pack(

            anchor="w",

            pady=(5, 0)
        )


        self.phi0_slider = ttk.Scale(

            control_frame,

            from_=0,

            to=360,

            variable=self.phi0_var,

            command=self.controls_changed
        )


        self.phi0_slider.pack(
            fill="x"
        )


        # Global phase.

        self.global_var = tk.DoubleVar(
            value=0.0
        )


        self.global_slider_label = ttk.Label(

            control_frame,

            text="Global γ = 0°"
        )


        self.global_slider_label.pack(

            anchor="w",

            pady=(5, 0)
        )


        self.global_slider = ttk.Scale(

            control_frame,

            from_=0,

            to=360,

            variable=self.global_var,

            command=self.controls_changed
        )


        self.global_slider.pack(
            fill="x"
        )


        # Time.

        self.time_var = tk.DoubleVar(
            value=0.0
        )


        self.time_slider_label = ttk.Label(

            control_frame,

            text="Time = 0.00 s"
        )


        self.time_slider_label.pack(

            anchor="w",

            pady=(5, 0)
        )


        self.time_slider = ttk.Scale(

            control_frame,

            from_=0,

            to=12,

            variable=self.time_var,

            command=self.time_changed
        )


        self.time_slider.pack(
            fill="x"
        )


        # -------------------------------------------------
        # PRESET STATES
        # -------------------------------------------------

        preset_frame = ttk.LabelFrame(

            right,

            text="7. Important Equal-Amplitude States",

            padding=10
        )


        preset_frame.pack(

            fill="x",

            pady=5
        )


        ttk.Button(

            preset_frame,

            text="|+⟩  φ=0°",

            command=self.prepare_plus

        ).pack(

            side="left",

            fill="x",

            expand=True
        )


        ttk.Button(

            preset_frame,

            text="|+i⟩  φ=90°",

            command=self.prepare_plus_i

        ).pack(

            side="left",

            fill="x",

            expand=True
        )


        ttk.Button(

            preset_frame,

            text="|−⟩  φ=180°",

            command=self.prepare_minus

        ).pack(

            side="left",

            fill="x",

            expand=True
        )


        ttk.Button(

            preset_frame,

            text="|−i⟩  φ=270°",

            command=self.prepare_minus_i

        ).pack(

            side="left",

            fill="x",

            expand=True
        )


        # -------------------------------------------------
        # ANIMATION
        # -------------------------------------------------

        animation_frame = ttk.LabelFrame(

            right,

            text="8. Animate Phase Evolution",

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
    # LEARNING CONSOLE
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
        # CONCEPT
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
        # CODE
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
NEW PYTHON / QUANTUM CONCEPTS IN FILE 06
========================================


1. MODULO OPERATOR %

   value % 360

   keeps an angle inside one 360-degree cycle.

   Example:

       450 % 360 = 90


2. GLOBAL PHASE FACTOR

   complex(
       cos(gamma),
       sin(gamma)
   )

   represents:

       e^(i gamma)


3. RELATIVE PHASE

   phi = phi_0 + omega * time

   changes the angle between alpha and beta.


4. SAME MAGNITUDE, DIFFERENT PHASE

   Two complex numbers can have the same magnitude
   but point in different directions in the
   complex plane.


5. BASIS CHANGE

   plus_amplitude = (alpha + beta) / sqrt(2)

   This asks:

       what is the amplitude of |+>?


6. INTERFERENCE

   alpha + beta

   may reinforce.

   alpha - beta

   may cancel.

   This is how phase can become measurable.


7. GLOBAL VS RELATIVE INFORMATION

   Multiplying BOTH alpha and beta by the same
   complex phase factor does not change
   measurable probabilities.

   Changing only their phase DIFFERENCE does.


8. PHASE PERIOD

   T = 2*pi / omega

   tells us how long it takes for relative phase
   to complete one full 360-degree cycle.


9. COMPLEX-PLANE ARROWS

   x = radius * cos(phase)

   y = radius * sin(phase)

   lets us draw complex amplitudes geometrically.


10. MODEL SEPARATION

    PhaseEvolutionModel
        ↓
    physics / mathematics

    PhaseEvolutionGUI
        ↓
    visualization / user interaction
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

        real = value.real

        imag = value.imag


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
    # FORMAT PERIOD
    # =====================================================

    def format_period(
        self,
        value
    ):

        # math.inf means infinity.

        if math.isinf(
            value
        ):

            return "∞"


        return (
            f"{value:.4f} s"
        )


    # =====================================================
    # UPDATE DISPLAY
    # =====================================================

    def update_display(self):

        # Current amplitudes.

        alpha = self.model.alpha()

        beta = self.model.beta()


        # Z basis probabilities.

        p0, p1 = (
            self.model.z_probabilities()
        )


        # X basis probabilities.

        p_plus, p_minus = (
            self.model.x_probabilities()
        )


        # Relative phase.

        phi = (
            self.model.relative_phase()
        )


        wrapped_phi = (
            self.model.wrapped_relative_phase()
        )


        # Bloch coordinates.

        x, y, z = (
            self.model.bloch_coordinates()
        )


        # -------------------------------------------------
        # STATE
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
        # PHASE INFO
        # -------------------------------------------------

        self.time_label.config(

            text=(
                f"t = {self.model.time:.4f} s"
            )
        )


        self.omega_label.config(

            text=(
                f"ω = {self.model.omega:.4f} rad/s"
            )
        )


        self.phi0_label.config(

            text=(
                "φ₀ = "
                f"{math.degrees(self.model.phi_0):.2f}°"
            )
        )


        self.relative_phase_label.config(

            text=(
                "Relative φ(t) = "
                f"{math.degrees(wrapped_phi):.2f}°"
            )
        )


        self.global_phase_label.config(

            text=(
                "Global γ = "
                f"{math.degrees(self.model.global_phase):.2f}°"
            )
        )


        self.period_label.config(

            text=(
                "Phase period = "
                f"{self.format_period(self.model.phase_period())}"
            )
        )


        # -------------------------------------------------
        # BLOCH
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
        # Z BASIS
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


        # -------------------------------------------------
        # X BASIS
        # -------------------------------------------------

        self.pplus_label.config(

            text=(
                f"P(+) = {p_plus:.4f} "
                f"= {p_plus * 100:.1f}%"
            )
        )


        self.pminus_label.config(

            text=(
                f"P(-) = {p_minus:.4f} "
                f"= {p_minus * 100:.1f}%"
            )
        )


        self.pplus_bar["value"] = (
            p_plus * 100
        )


        self.pminus_bar["value"] = (
            p_minus * 100
        )


        # -------------------------------------------------
        # CONTROL LABELS
        # -------------------------------------------------

        self.omega_slider_label.config(

            text=(
                f"ω = {self.model.omega:.2f} rad/s"
            )
        )


        self.phi0_slider_label.config(

            text=(
                "Initial φ₀ = "
                f"{math.degrees(self.model.phi_0):.1f}°"
            )
        )


        self.global_slider_label.config(

            text=(
                "Global γ = "
                f"{math.degrees(self.model.global_phase):.1f}°"
            )
        )


        self.time_slider_label.config(

            text=(
                f"Time = {self.model.time:.2f} s"
            )
        )


        # -------------------------------------------------
        # DRAWINGS
        # -------------------------------------------------

        self.draw_plot()

        self.draw_phase_arrows()


    # =====================================================
    # DRAW INTERFERENCE PLOT
    # =====================================================

    def draw_plot(self):

        # Remove previous graph.

        self.ax.clear()


        period = (
            self.model.phase_period()
        )


        # Choose a useful graph duration.

        if math.isinf(
            period
        ):

            max_time = 8.0

        else:

            max_time = max(

                2 * period,

                6.0
            )


        if self.model.time > max_time:

            max_time = (

                self.model.time

                *
                1.1
            )


        # Create many time values.

        times = np.linspace(

            0,

            max_time,

            700
        )


        # Calculate relative phase for every time.

        phi_values = (

            self.model.phi_0

            +

            self.model.omega

            *

            times
        )


        # X-basis probabilities.
        #
        # P(+) = cos²(phi/2)

        p_plus = (

            np.cos(

                phi_values
                /
                2

            ) ** 2
        )


        # P(-) = sin²(phi/2)

        p_minus = (

            np.sin(

                phi_values
                /
                2

            ) ** 2
        )


        # Draw P(+).

        self.ax.plot(

            times,

            p_plus,

            label="P(+)"
        )


        # Draw P(-).

        self.ax.plot(

            times,

            p_minus,

            label="P(-)"
        )


        # Show Z-basis probability as reference.
        #
        # It remains exactly 0.5.

        self.ax.axhline(

            0.5,

            linestyle=":",

            label="P(0)=P(1)=0.5"
        )


        # Show current time.

        self.ax.axvline(

            self.model.time,

            linestyle="--",

            label="Current time"
        )


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

            "Relative Phase Becomes Visible Through Interference"
        )


        self.ax.grid(
            True,
            alpha=0.3
        )


        self.ax.legend()


        self.plot_canvas.draw_idle()


    # =====================================================
    # CANVAS RESIZED
    # =====================================================

    def canvas_resized(

        self,

        event
    ):

        # Redraw when user resizes window.

        self.draw_phase_arrows()


    # =====================================================
    # DRAW PHASE ARROWS
    # =====================================================

    def draw_phase_arrows(self):

        # Clear old drawing.

        self.phase_canvas.delete(
            "all"
        )


        width = (
            self.phase_canvas.winfo_width()
        )


        height = (
            self.phase_canvas.winfo_height()
        )


        if width < 100:

            width = 700


        if height < 100:

            height = 250


        # Positions of the two complex planes.

        alpha_x = (
            width
            *
            0.28
        )


        beta_x = (
            width
            *
            0.72
        )


        center_y = (
            height
            *
            0.52
        )


        radius = min(

            width * 0.13,

            height * 0.30
        )


        # Get amplitudes.

        alpha = self.model.alpha()

        beta = self.model.beta()


        # Draw alpha.

        self.draw_complex_arrow(

            center_x=alpha_x,

            center_y=center_y,

            radius=radius,

            value=alpha,

            title="α — amplitude of |0⟩"
        )


        # Draw beta.

        self.draw_complex_arrow(

            center_x=beta_x,

            center_y=center_y,

            radius=radius,

            value=beta,

            title="β — amplitude of |1⟩"
        )


        # Show relative-phase message.

        self.phase_canvas.create_text(

            width / 2,

            height - 18,

            text=(
                "Relative phase = angle of β − angle of α"
            ),

            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )


    # =====================================================
    # DRAW ONE COMPLEX ARROW
    # =====================================================

    def draw_complex_arrow(

        self,

        center_x,

        center_y,

        radius,

        value,

        title
    ):

        # Draw complex-plane circle.

        self.phase_canvas.create_oval(

            center_x - radius,

            center_y - radius,

            center_x + radius,

            center_y + radius,

            outline="gray",

            width=2
        )


        # Real axis.

        self.phase_canvas.create_line(

            center_x - radius,

            center_y,

            center_x + radius,

            center_y,

            arrow=tk.LAST
        )


        # Imaginary axis.

        self.phase_canvas.create_line(

            center_x,

            center_y + radius,

            center_x,

            center_y - radius,

            arrow=tk.LAST
        )


        # Find magnitude.

        magnitude = abs(
            value
        )


        # Find complex phase.

        phase = math.atan2(

            value.imag,

            value.real
        )


        # Arrow length proportional to magnitude.

        arrow_length = (

            radius

            *
            magnitude
        )


        # x coordinate.

        end_x = (

            center_x

            +

            arrow_length

            *

            math.cos(
                phase
            )
        )


        # Canvas positive y points downward,
        # therefore subtract.

        end_y = (

            center_y

            -

            arrow_length

            *

            math.sin(
                phase
            )
        )


        # Draw amplitude arrow.

        self.phase_canvas.create_line(

            center_x,

            center_y,

            end_x,

            end_y,

            arrow=tk.LAST,

            width=4
        )


        # Title.

        self.phase_canvas.create_text(

            center_x,

            center_y - radius - 20,

            text=title,

            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )


        # Phase information.

        self.phase_canvas.create_text(

            center_x,

            center_y + radius + 20,

            text=(
                f"|amplitude| = {magnitude:.3f}    "
                f"phase = {math.degrees(phase):.1f}°"
            ),

            font=(
                "Consolas",
                9
            )
        )


    # =====================================================
    # CONTROLS CHANGED
    # =====================================================

    def controls_changed(

        self,

        value=None
    ):

        # Read omega.

        omega = (
            self.omega_var.get()
        )


        # Read initial relative phase in degrees.

        phi0_degrees = (
            self.phi0_var.get()
        )


        # Read global phase in degrees.

        global_degrees = (
            self.global_var.get()
        )


        # Convert degrees to radians.

        phi0 = math.radians(
            phi0_degrees
        )


        gamma = math.radians(
            global_degrees
        )


        # Update model.

        self.model.set_omega(
            omega
        )


        self.model.set_phi_0(
            phi0
        )


        self.model.set_global_phase(
            gamma
        )


        # Refresh screen.

        self.update_display()


        self.show_lesson(

            title="Phase controls changed",

            explanation=(
                f"ω = {omega:.3f} rad/s\n"
                f"φ₀ = {phi0_degrees:.1f}°\n"
                f"γ = {global_degrees:.1f}°\n\n"

                "The relative phase evolves as:\n\n"

                "    φ(t) = φ₀ + ωt\n\n"

                "Changing φ₀ changes the relationship between "
                "the |0⟩ and |1⟩ amplitudes.\n\n"

                "Changing γ rotates BOTH amplitudes together.\n\n"

                "Try moving only the global-phase slider.\n"
                "Both complex arrows rotate together, but "
                "P(0), P(1), P(+), P(-), and the Bloch "
                "coordinates remain unchanged."
            ),

            python_code=(
                "phi = phi_0 + omega * time\n\n"

                "# Relative phase affects beta relative to alpha.\n\n"

                "alpha = e^(i*gamma) / sqrt(2)\n\n"

                "beta = e^(i*(gamma + phi)) / sqrt(2)\n\n"

                "# gamma is added to BOTH amplitudes.\n"
                "# Therefore it is a global phase."
            )
        )


    # =====================================================
    # TIME CHANGED
    # =====================================================

    def time_changed(

        self,

        value=None
    ):

        # Read slider.

        time = (
            self.time_var.get()
        )


        # Store time.

        self.model.set_time(
            time
        )


        # Refresh.

        self.update_display()


        p_plus, p_minus = (
            self.model.x_probabilities()
        )


        self.show_lesson(

            title="Time changed",

            explanation=(
                f"Current t = {time:.4f} s.\n\n"

                "Relative phase is calculated using:\n\n"

                "    φ(t) = φ₀ + ωt\n\n"

                "Even though φ changes:\n\n"

                "    P(0) = 50%\n"
                "    P(1) = 50%\n\n"

                "But in the X basis:\n\n"

                f"    P(+) = {p_plus:.4f}\n"
                f"    P(-) = {p_minus:.4f}\n\n"

                "This is how interference reveals phase."
            ),

            python_code=(
                "self.time = time\n\n"

                "phi = self.phi_0 + self.omega * self.time\n\n"

                "p_plus = math.cos(phi / 2) ** 2\n\n"

                "p_minus = math.sin(phi / 2) ** 2"
            )
        )


    # =====================================================
    # SYNC CONTROLS
    # =====================================================

    def sync_controls(self):

        self.time_var.set(
            self.model.time
        )


        self.phi0_var.set(

            math.degrees(
                self.model.phi_0
            )
        )


        self.global_var.set(

            math.degrees(
                self.model.global_phase
            )
        )


    # =====================================================
    # PREPARE |+>
    # =====================================================

    def prepare_plus(self):

        self.model.set_plus()

        self.sync_controls()

        self.update_display()


        self.show_lesson(

            title="Prepared |+⟩",

            explanation=(
                "|+⟩ is:\n\n"

                "          |0⟩ + |1⟩\n"
                "    |+⟩ = -----------\n"
                "               √2\n\n"

                "Relative phase:\n\n"

                "    φ = 0°\n\n"

                "Z basis:\n\n"

                "    P(0) = 50%\n"
                "    P(1) = 50%\n\n"

                "X basis:\n\n"

                "    P(+) = 100%\n"
                "    P(-) = 0%"
            ),

            python_code=(
                "self.time = 0.0\n"
                "self.phi_0 = 0.0\n"
                "self.global_phase = 0.0"
            )
        )


    # =====================================================
    # PREPARE |->
    # =====================================================

    def prepare_minus(self):

        self.model.set_minus()

        self.sync_controls()

        self.update_display()


        self.show_lesson(

            title="Prepared |−⟩",

            explanation=(
                "|−⟩ is:\n\n"

                "          |0⟩ - |1⟩\n"
                "    |−⟩ = -----------\n"
                "               √2\n\n"

                "Relative phase:\n\n"

                "    φ = 180°\n\n"

                "Z basis is STILL 50/50.\n\n"

                "But X basis becomes:\n\n"

                "    P(+) = 0%\n"
                "    P(-) = 100%\n\n"

                "This proves that |+⟩ and |−⟩ are "
                "different even though their Z-basis "
                "probabilities are identical."
            ),

            python_code=(
                "self.phi_0 = math.pi\n\n"

                "# beta differs from alpha by 180 degrees."
            )
        )


    # =====================================================
    # PREPARE |+i>
    # =====================================================

    def prepare_plus_i(self):

        self.model.set_plus_i()

        self.sync_controls()

        self.update_display()


        self.show_lesson(

            title="Prepared |+i⟩",

            explanation=(
                "|+i⟩ has relative phase:\n\n"

                "    φ = 90°\n\n"

                "Its state is:\n\n"

                "           |0⟩ + i|1⟩\n"
                "    |ψ⟩ = -------------\n"
                "                √2\n\n"

                "The Bloch vector points toward +Y."
            ),

            python_code=(
                "self.phi_0 = math.pi / 2\n\n"

                "# pi/2 radians = 90 degrees."
            )
        )


    # =====================================================
    # PREPARE |-i>
    # =====================================================

    def prepare_minus_i(self):

        self.model.set_minus_i()

        self.sync_controls()

        self.update_display()


        self.show_lesson(

            title="Prepared |−i⟩",

            explanation=(
                "|−i⟩ has relative phase:\n\n"

                "    φ = 270°\n\n"

                "which is equivalent to:\n\n"

                "    -90°\n\n"

                "Its Bloch vector points toward -Y."
            ),

            python_code=(
                "self.phi_0 = 3 * math.pi / 2\n\n"

                "# 3*pi/2 = 270 degrees."
            )
        )


    # =====================================================
    # START ANIMATION
    # =====================================================

    def start_animation(self):

        if self.running:

            return


        self.running = True


        self.show_lesson(

            title="Phase evolution started",

            explanation=(
                "Time will now increase automatically.\n\n"

                "As time increases:\n\n"

                "    φ(t) = φ₀ + ωt\n\n"

                "so the beta amplitude rotates relative "
                "to alpha.\n\n"

                "Watch carefully:\n\n"

                "    P(0) stays at 50%\n"
                "    P(1) stays at 50%\n\n"

                "but:\n\n"

                "    P(+) and P(-) oscillate.\n\n"

                "This is phase evolution becoming visible "
                "through interference."
            ),

            python_code=(
                "self.running = True\n\n"

                "self.animate_step()\n\n"

                "# Every step increases time.\n"
                "# Changing time changes relative phase."
            )
        )


        self.animate_step()


    # =====================================================
    # ANIMATION STEP
    # =====================================================

    def animate_step(self):

        if not self.running:

            return


        # Increase time.

        new_time = (

            self.model.time

            +

            self.animation_dt
        )


        # Restart after 12 seconds.

        if new_time > 12:

            new_time = 0.0


        # Store time.

        self.model.set_time(
            new_time
        )


        # Update slider.

        self.time_var.set(
            new_time
        )


        # Refresh display.

        self.update_display()


        # Schedule next update.

        self.root.after(

            30,

            self.animate_step
        )


    # =====================================================
    # PAUSE
    # =====================================================

    def pause_animation(self):

        self.running = False


        self.show_lesson(

            title="Animation paused",

            explanation=(
                "Time evolution has been paused.\n\n"

                "The relative phase remains at its current value."
            ),

            python_code=(
                "self.running = False"
            )
        )


    # =====================================================
    # RESET TIME
    # =====================================================

    def reset_time(self):

        # Stop animation.

        self.running = False


        # Set t = 0.

        self.model.reset_time()


        # Update slider.

        self.time_var.set(
            0.0
        )


        # Refresh.

        self.update_display()


        self.show_lesson(

            title="Time reset",

            explanation=(
                "Time returned to zero.\n\n"

                "Therefore:\n\n"

                "    φ(t) = φ₀ + ω(0)\n\n"

                "so:\n\n"

                "    φ = φ₀"
            ),

            python_code=(
                "self.time = 0.0"
            )
        )


# =========================================================
# START APPLICATION
# =========================================================


if __name__ == "__main__":

    print(
        "Running 06_phase_evolution.py ..."
    )


    # Create main Tkinter window.

    root = tk.Tk()


    # Create our application.

    app = PhaseEvolutionGUI(
        root
    )


    # Keep GUI running.

    root.mainloop()