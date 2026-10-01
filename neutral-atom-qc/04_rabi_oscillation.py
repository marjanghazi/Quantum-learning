"""
=========================================================
04 - RABI OSCILLATION
Neutral-Atom Quantum Computing Learning
=========================================================

GOAL
----

Understand how an ideal two-level quantum system evolves
under a resonant coherent drive.

We start in:

    |0>

Under the simplest ideal resonant model:

    |ψ(t)> =
        cos(Ωt/2)|0>
        - i sin(Ωt/2)|1>

Therefore:

    P(0) = cos²(Ωt/2)

    P(1) = sin²(Ωt/2)

where:

    Ω = Rabi angular frequency
    t = time


IMPORTANT PHYSICS NOTE
----------------------

This is an EDUCATIONAL IDEAL MODEL.

It assumes:

    - exactly two levels
    - perfect resonance
    - constant drive strength
    - no spontaneous emission
    - no dephasing
    - no laser noise
    - no atomic motion
    - no additional atomic levels

A real neutral-atom experiment is more complicated.

Later files will introduce:

    - detuning
    - pulse shapes
    - π pulses
    - decoherence
    - Rydberg states
"""


# =========================================================
# IMPORTS
# =========================================================


# math gives us:
#
#     sin()
#     cos()
#     pi
#     sqrt()
#
import math


# NumPy is useful for generating arrays of time values.
#
# For example:
#
#     np.linspace(0, 10, 500)
#
# creates 500 values between 0 and 10.
#
import numpy as np


# Tkinter creates the graphical user interface.
#
import tkinter as tk


# ttk gives us more modern Tkinter widgets.
#
from tkinter import ttk


# ScrolledText is a text box with a scrollbar.
#
from tkinter.scrolledtext import ScrolledText


# Figure is Matplotlib's plotting container.
#
from matplotlib.figure import Figure


# FigureCanvasTkAgg lets us place Matplotlib
# inside a Tkinter application.
#
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# =========================================================
# RABI MODEL
# =========================================================


class RabiModel:

    """
    This class contains the quantum mathematics.

    It does NOT control the GUI.

    It stores:

        omega = Rabi angular frequency
        time  = current evolution time

    and calculates:

        alpha
        beta
        P(0)
        P(1)
        Bloch coordinates
    """


    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(self):

        # Rabi angular frequency Ω.
        #
        # We start with:
        #
        #     Ω = 2 rad/s
        #
        # This is deliberately small so that
        # the oscillation is easy to visualize.

        self.omega = 2.0


        # Start at:
        #
        #     t = 0
        #
        # Therefore:
        #
        #     |ψ(0)> = |0>

        self.time = 0.0


    # =====================================================
    # ALPHA
    # =====================================================

    def alpha(self):

        # Under the ideal resonant model:
        #
        #     α(t) = cos(Ωt/2)

        value = math.cos(

            self.omega
            *
            self.time
            /
            2
        )


        # Store as a complex number.
        #
        # Imaginary part = 0.

        return complex(
            value,
            0.0
        )


    # =====================================================
    # BETA
    # =====================================================

    def beta(self):

        # Under our Hamiltonian convention:
        #
        #     β(t) = -i sin(Ωt/2)
        #
        # The sign depends on Hamiltonian convention.
        #
        # The important probability result remains:
        #
        #     |β|² = sin²(Ωt/2)

        value = math.sin(

            self.omega
            *
            self.time
            /
            2
        )


        # -i * value means:
        #
        #     real part      = 0
        #     imaginary part = -value

        return complex(
            0.0,
            -value
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
    # NORMALIZATION
    # =====================================================

    def normalization(self):

        # Obtain probabilities.

        p0, p1 = self.probabilities()


        # For an ideal state:
        #
        #     P(0) + P(1) = 1

        return p0 + p1


    # =====================================================
    # BLOCH COORDINATES
    # =====================================================

    def bloch_coordinates(self):

        # Obtain amplitudes.

        alpha = self.alpha()

        beta = self.beta()


        # For a pure qubit:
        #
        #     x = 2 Re(α* β)
        #
        # where α* means complex conjugate.

        product = (
            alpha.conjugate()
            *
            beta
        )


        x = (
            2
            *
            product.real
        )


        # The Y coordinate is:
        #
        #     y = 2 Im(α* β)

        y = (
            2
            *
            product.imag
        )


        # Z coordinate:
        #
        #     z = |α|² - |β|²

        z = (
            abs(alpha) ** 2
            -
            abs(beta) ** 2
        )


        return x, y, z


    # =====================================================
    # SET OMEGA
    # =====================================================

    def set_omega(
        self,
        omega
    ):

        # Store new Rabi frequency.

        self.omega = omega


    # =====================================================
    # SET TIME
    # =====================================================

    def set_time(
        self,
        time
    ):

        # Store current evolution time.

        self.time = time


    # =====================================================
    # RESET
    # =====================================================

    def reset(self):

        # Return to:
        #
        #     t = 0
        #
        # which means:
        #
        #     |ψ> = |0>

        self.time = 0.0


    # =====================================================
    # RABI PERIOD
    # =====================================================

    def rabi_period(self):

        # Probability completes one full oscillation when:
        #
        #     ΩT = 2π
        #
        # Therefore:
        #
        #         2π
        #     T = --
        #         Ω

        if self.omega == 0:

            return math.inf


        return (
            2
            *
            math.pi
            /
            self.omega
        )


    # =====================================================
    # PI-PULSE TIME
    # =====================================================

    def pi_pulse_time(self):

        # A π pulse should take:
        #
        #     |0> → |1>
        #
        # We need:
        #
        #     Ωt = π
        #
        # Therefore:
        #
        #         π
        #     t = -
        #         Ω

        if self.omega == 0:

            return math.inf


        return (
            math.pi
            /
            self.omega
        )


    # =====================================================
    # PI/2-PULSE TIME
    # =====================================================

    def half_pi_pulse_time(self):

        # A π/2 pulse satisfies:
        #
        #     Ωt = π/2
        #
        # Therefore:
        #
        #          π
        #     t = ----
        #         2Ω
        #
        # Starting from |0>, this produces
        # equal measurement probabilities.

        if self.omega == 0:

            return math.inf


        return (
            math.pi
            /
            (
                2
                *
                self.omega
            )
        )


# =========================================================
# GUI
# =========================================================


class RabiGUI:

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
            "Neutral-Atom QC | 04 — Rabi Oscillation"
        )


        # Starting window size.

        self.root.geometry(
            "1400x900"
        )


        # Minimum size.

        self.root.minsize(
            1100,
            750
        )


        # -------------------------------------------------
        # CREATE QUANTUM MODEL
        # -------------------------------------------------

        self.model = RabiModel()


        # -------------------------------------------------
        # ANIMATION VARIABLES
        # -------------------------------------------------

        # False means animation is initially stopped.

        self.running = False


        # Animation step size.
        #
        # Every animation update,
        # time increases by this amount.

        self.animation_dt = 0.03


        # -------------------------------------------------
        # CREATE UI
        # -------------------------------------------------

        self.setup_style()

        self.create_header()

        self.create_main_area()

        self.create_learning_area()


        # Draw starting state.

        self.update_display()


        # Starting explanation.

        self.show_lesson(

            title="Rabi oscillation initialized",

            explanation=(
                "The system begins in |0⟩ at time t = 0.\n\n"

                "Our ideal resonant evolution is:\n\n"

                "    |ψ(t)⟩ = "
                "cos(Ωt/2)|0⟩ "
                "- i sin(Ωt/2)|1⟩\n\n"

                "At t = 0:\n\n"

                "    cos(0) = 1\n"
                "    sin(0) = 0\n\n"

                "so:\n\n"

                "    |ψ(0)⟩ = |0⟩"
            ),

            python_code=(
                "self.model = RabiModel()\n\n"

                "# __init__() sets:\n\n"

                "self.omega = 2.0\n"
                "self.time = 0.0\n\n"

                "# t = 0 means the initial state is |0>."
            )
        )


    # =====================================================
    # STYLE
    # =====================================================

    def setup_style(self):

        # Create ttk styling object.

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

            text=(
                "Neutral-Atom Quantum Computing"
            ),

            style="Title.TLabel"

        ).pack(
            anchor="w"
        )


        ttk.Label(

            header,

            text=(
                "04 — Rabi Oscillation"
            ),

            style="Section.TLabel"

        ).pack(
            anchor="w"
        )


        ttk.Label(

            header,

            text=(
                "Ideal resonant coherent evolution "
                "between |0⟩ and |1⟩"
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

            text="Rabi Oscillation Plot",

            padding=10
        )


        left.grid(

            row=0,

            column=0,

            sticky="nsew",

            padx=(0, 8)
        )


        # -------------------------------------------------
        # MATPLOTLIB FIGURE
        # -------------------------------------------------

        self.figure = Figure(

            figsize=(7, 5),

            dpi=100
        )


        # Create one standard 2D graph.

        self.ax = self.figure.add_subplot(
            111
        )


        # Put graph inside Tkinter.

        self.plot_canvas = FigureCanvasTkAgg(

            self.figure,

            master=left
        )


        self.plot_canvas.get_tk_widget().pack(

            fill="both",

            expand=True
        )


        ttk.Label(

            left,

            text=(
                "The curves show theoretical P(0) and P(1). "
                "The vertical marker shows the current time."
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
                13,
                "bold"
            ),

            justify="center"
        )


        self.state_label.pack(
            fill="x"
        )


        # -------------------------------------------------
        # RABI PARAMETERS
        # -------------------------------------------------

        parameter_frame = ttk.LabelFrame(

            right,

            text="2. Rabi Parameters",

            padding=10
        )


        parameter_frame.pack(

            fill="x",

            pady=5
        )


        self.omega_label = ttk.Label(

            parameter_frame,

            style="Value.TLabel"
        )


        self.omega_label.pack(
            anchor="w"
        )


        self.period_label = ttk.Label(

            parameter_frame,

            style="Value.TLabel"
        )


        self.period_label.pack(
            anchor="w"
        )


        self.pi_time_label = ttk.Label(

            parameter_frame,

            style="Value.TLabel"
        )


        self.pi_time_label.pack(
            anchor="w"
        )


        self.half_pi_time_label = ttk.Label(

            parameter_frame,

            style="Value.TLabel"
        )


        self.half_pi_time_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # CURRENT TIME
        # -------------------------------------------------

        time_frame = ttk.LabelFrame(

            right,

            text="3. Evolution Time",

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


        self.phase_angle_label = ttk.Label(

            time_frame,

            style="Value.TLabel"
        )


        self.phase_angle_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # PROBABILITIES
        # -------------------------------------------------

        probability_frame = ttk.LabelFrame(

            right,

            text="4. Measurement Probabilities",

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

            text="5. Bloch Coordinates",

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
        # OMEGA CONTROL
        # -------------------------------------------------

        omega_frame = ttk.LabelFrame(

            right,

            text="6. Change Rabi Frequency Ω",

            padding=10
        )


        omega_frame.pack(

            fill="x",

            pady=5
        )


        # Tkinter variable storing slider value.

        self.omega_var = tk.DoubleVar(

            value=self.model.omega
        )


        self.omega_slider_text = ttk.Label(

            omega_frame,

            text="Ω = 2.00 rad/s"
        )


        self.omega_slider_text.pack(
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
        # TIME CONTROL
        # -------------------------------------------------

        time_control_frame = ttk.LabelFrame(

            right,

            text="7. Explore Time",

            padding=10
        )


        time_control_frame.pack(

            fill="x",

            pady=5
        )


        self.time_var = tk.DoubleVar(
            value=0.0
        )


        self.time_slider = ttk.Scale(

            time_control_frame,

            from_=0.0,

            to=10.0,

            variable=self.time_var,

            command=self.time_changed
        )


        self.time_slider.pack(
            fill="x"
        )


        # -------------------------------------------------
        # SPECIAL PULSES
        # -------------------------------------------------

        pulse_frame = ttk.LabelFrame(

            right,

            text="8. Important Pulse Times",

            padding=10
        )


        pulse_frame.pack(

            fill="x",

            pady=5
        )


        ttk.Button(

            pulse_frame,

            text="Go to π/2 Pulse",

            command=self.go_half_pi,

            style="Action.TButton"

        ).pack(

            fill="x",

            pady=2
        )


        ttk.Button(

            pulse_frame,

            text="Go to π Pulse",

            command=self.go_pi,

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

            text="9. Animation",

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

            text="Reset",

            command=self.reset,

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
        # QUANTUM EXPLANATION
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
        # PYTHON CODE
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
NEW PYTHON CONCEPTS IN FILE 04
==============================


1. TIME-DEPENDENT FUNCTIONS

   alpha changes with time:

       cos(omega * time / 2)

   The result therefore depends on the
   current value stored in self.time.


2. math.inf

   math.inf represents infinity.

   We use it when omega = 0 because:

       pi / 0

   is undefined.


3. METHOD RETURN VALUES

   return math.pi / self.omega

   calculates and returns the pi-pulse time.


4. BOOLEAN VARIABLES

   self.running = False

   A Boolean has only two values:

       True
       False

   We use it to control animation.


5. TKINTER after()

   root.after(30, function)

   means:

       wait about 30 milliseconds
       then call function

   This lets us animate without freezing the GUI.


6. NUMPY ARRAYS

   times = np.linspace(...)

   creates many time points at once.


7. VECTORIZED MATHEMATICS

   np.sin(array)

   performs sin() on every value in the array.


8. GRAPH REFRESH

   ax.clear()

   removes the previous graph.

   Then we redraw using the current omega.


9. CONJUGATE

   alpha.conjugate()

   changes:

       a + bi

   into:

       a - bi


10. BLOCH COORDINATES FROM AMPLITUDES

    x = 2 Re(alpha* beta)

    y = 2 Im(alpha* beta)

    z = |alpha|² - |beta|²

    where alpha* means the complex conjugate.
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
    # FORMAT COMPLEX NUMBER
    # =====================================================

    def format_complex(
        self,
        value
    ):

        # Get real component.

        real = value.real


        # Get imaginary component.

        imag = value.imag


        # Determine displayed sign.

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

        # Obtain current amplitudes.

        alpha = self.model.alpha()

        beta = self.model.beta()


        # Obtain probabilities.

        p0, p1 = (
            self.model.probabilities()
        )


        # Obtain normalization.

        normalization = (
            self.model.normalization()
        )


        # Obtain Bloch coordinates.

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
        # PARAMETERS
        # -------------------------------------------------

        self.omega_label.config(

            text=(
                f"Ω = {self.model.omega:.4f} rad/s"
            )
        )


        period = (
            self.model.rabi_period()
        )


        pi_time = (
            self.model.pi_pulse_time()
        )


        half_pi_time = (
            self.model.half_pi_pulse_time()
        )


        self.period_label.config(

            text=(
                f"Rabi period T = {period:.4f} s"
            )
        )


        self.pi_time_label.config(

            text=(
                f"π-pulse time = {pi_time:.4f} s"
            )
        )


        self.half_pi_time_label.config(

            text=(
                f"π/2-pulse time = {half_pi_time:.4f} s"
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


        # Ωt is the accumulated rotation angle.

        rotation_angle = (
            self.model.omega
            *
            self.model.time
        )


        self.phase_angle_label.config(

            text=(
                f"Ωt = {rotation_angle:.4f} rad "
                f"= {math.degrees(rotation_angle):.1f}°"
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
        # CONTROL LABEL
        # -------------------------------------------------

        self.omega_slider_text.config(

            text=(
                f"Ω = {self.model.omega:.2f} rad/s"
            )
        )


        # -------------------------------------------------
        # DRAW GRAPH
        # -------------------------------------------------

        self.draw_plot()


    # =====================================================
    # DRAW RABI PLOT
    # =====================================================

    def draw_plot(self):

        # Clear previous graph.

        self.ax.clear()


        # -------------------------------------------------
        # CHOOSE TIME RANGE
        # -------------------------------------------------

        period = (
            self.model.rabi_period()
        )


        # Display approximately two periods.
        #
        # But never show less than 4 seconds,
        # so the graph remains easy to inspect.

        max_time = max(
            2 * period,
            4.0
        )


        # Make sure current animation time
        # remains visible.

        if self.model.time > max_time:

            max_time = (
                self.model.time
                *
                1.1
            )


        # -------------------------------------------------
        # GENERATE TIME ARRAY
        # -------------------------------------------------

        times = np.linspace(

            0,

            max_time,

            600
        )


        # -------------------------------------------------
        # CALCULATE P(0)
        # -------------------------------------------------

        probability_0 = (

            np.cos(

                self.model.omega
                *
                times
                /
                2

            ) ** 2
        )


        # -------------------------------------------------
        # CALCULATE P(1)
        # -------------------------------------------------

        probability_1 = (

            np.sin(

                self.model.omega
                *
                times
                /
                2

            ) ** 2
        )


        # -------------------------------------------------
        # DRAW CURVES
        # -------------------------------------------------

        self.ax.plot(

            times,

            probability_0,

            label="P(0)"
        )


        self.ax.plot(

            times,

            probability_1,

            label="P(1)"
        )


        # -------------------------------------------------
        # CURRENT TIME MARKER
        # -------------------------------------------------

        self.ax.axvline(

            self.model.time,

            linestyle="--",

            label="Current time"
        )


        # -------------------------------------------------
        # PI/2 MARKER
        # -------------------------------------------------

        self.ax.axvline(

            self.model.half_pi_pulse_time(),

            linestyle=":",

            label="π/2 pulse"
        )


        # -------------------------------------------------
        # PI MARKER
        # -------------------------------------------------

        self.ax.axvline(

            self.model.pi_pulse_time(),

            linestyle=":",

            label="π pulse"
        )


        # -------------------------------------------------
        # AXIS SETTINGS
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

            "Ideal Resonant Rabi Oscillation"
        )


        self.ax.grid(
            True,
            alpha=0.3
        )


        self.ax.legend()


        # Update Tkinter plot.

        self.plot_canvas.draw_idle()


    # =====================================================
    # OMEGA CHANGED
    # =====================================================

    def omega_changed(
        self,
        value=None
    ):

        # Read slider value.

        omega = (
            self.omega_var.get()
        )


        # Store in quantum model.

        self.model.set_omega(
            omega
        )


        # Refresh GUI.

        self.update_display()


        self.show_lesson(

            title="Rabi frequency changed",

            explanation=(
                f"Current Ω = {omega:.3f} rad/s.\n\n"

                "Ω controls how quickly the state oscillates.\n\n"

                "The ideal probability is:\n\n"

                "    P(1) = sin²(Ωt/2)\n\n"

                "Increasing Ω makes the oscillation happen "
                "faster.\n\n"

                "The π-pulse time is:\n\n"

                "    tπ = π / Ω\n\n"

                "Therefore a larger Ω produces a shorter "
                "π-pulse time."
            ),

            python_code=(
                "omega = self.omega_var.get()\n\n"

                "self.model.set_omega(omega)\n\n"

                "# Inside the model:\n\n"

                "self.omega = omega\n\n"

                "# Then probabilities are recalculated using:\n\n"

                "P1 = sin(omega * time / 2) ** 2"
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


        # Store new time.

        self.model.set_time(
            time
        )


        # Update GUI.

        self.update_display()


        p0, p1 = (
            self.model.probabilities()
        )


        self.show_lesson(

            title="Evolution time changed",

            explanation=(
                f"Current time = {time:.4f} s.\n\n"

                "The program evaluates:\n\n"

                "    α(t) = cos(Ωt/2)\n\n"

                "    β(t) = -i sin(Ωt/2)\n\n"

                "Then:\n\n"

                "    P(0) = |α|²\n"
                "    P(1) = |β|²\n\n"

                f"At this time:\n\n"

                f"    P(0) = {p0:.4f}\n"
                f"    P(1) = {p1:.4f}"
            ),

            python_code=(
                "time = self.time_var.get()\n\n"

                "self.model.set_time(time)\n\n"

                "# alpha:\n"
                "math.cos(omega * time / 2)\n\n"

                "# beta magnitude:\n"
                "math.sin(omega * time / 2)"
            )
        )


    # =====================================================
    # GO TO PI/2
    # =====================================================

    def go_half_pi(self):

        # Calculate required time.

        time = (
            self.model.half_pi_pulse_time()
        )


        # Store it.

        self.model.set_time(
            time
        )


        # Update slider.

        self.time_var.set(
            time
        )


        # Refresh display.

        self.update_display()


        self.show_lesson(

            title="π/2 pulse",

            explanation=(
                "A π/2 pulse satisfies:\n\n"

                "    Ωt = π/2\n\n"

                "so:\n\n"

                "    t = π / (2Ω)\n\n"

                "Starting from |0⟩:\n\n"

                "    α = cos(π/4) = 1/√2\n\n"

                "    β = -i sin(π/4) = -i/√2\n\n"

                "Therefore:\n\n"

                "    P(0) = 50%\n"
                "    P(1) = 50%\n\n"

                "This is an equal-probability superposition."
            ),

            python_code=(
                "time = math.pi / (2 * self.omega)\n\n"

                "# Then:\n\n"

                "alpha = cos(pi / 4)\n"
                "beta  = -i * sin(pi / 4)\n\n"

                "# Magnitudes squared:\n"
                "# P0 = 0.5\n"
                "# P1 = 0.5"
            )
        )


    # =====================================================
    # GO TO PI
    # =====================================================

    def go_pi(self):

        # Calculate π pulse time.

        time = (
            self.model.pi_pulse_time()
        )


        # Store time.

        self.model.set_time(
            time
        )


        # Move slider.

        self.time_var.set(
            time
        )


        # Refresh GUI.

        self.update_display()


        self.show_lesson(

            title="π pulse",

            explanation=(
                "A π pulse satisfies:\n\n"

                "    Ωt = π\n\n"

                "Therefore:\n\n"

                "    tπ = π / Ω\n\n"

                "At that moment:\n\n"

                "    α = cos(π/2) = 0\n\n"

                "    β = -i sin(π/2) = -i\n\n"

                "Therefore:\n\n"

                "    P(0) = 0\n"
                "    P(1) = 1\n\n"

                "In this ideal model the population has been "
                "completely transferred from |0⟩ to |1⟩."
            ),

            python_code=(
                "time = math.pi / self.omega\n\n"

                "# Substitute into beta:\n\n"

                "beta = -i * sin(omega * time / 2)\n\n"

                "# omega*time = pi\n\n"

                "beta = -i * sin(pi / 2)\n"
                "beta = -i\n\n"

                "# Therefore P(1) = 1."
            )
        )


    # =====================================================
    # START ANIMATION
    # =====================================================

    def start_animation(self):

        # Do not start a second loop
        # if one is already running.

        if self.running:

            return


        # Mark animation as active.

        self.running = True


        self.show_lesson(

            title="Animation started",

            explanation=(
                "Time will now increase automatically.\n\n"

                "For every animation step:\n\n"

                "    t = t + Δt\n\n"

                "Then Python recalculates:\n\n"

                "    α(t)\n"
                "    β(t)\n"
                "    P(0)\n"
                "    P(1)\n\n"

                "This produces the visible Rabi oscillation."
            ),

            python_code=(
                "self.running = True\n\n"

                "self.animate_step()\n\n"

                "# animate_step() repeatedly calls itself\n"
                "# using Tkinter's root.after()."
            )
        )


        # Start animation loop.

        self.animate_step()


    # =====================================================
    # ANIMATION STEP
    # =====================================================

    def animate_step(self):

        # Stop immediately if animation was paused.

        if not self.running:

            return


        # Increase time.

        new_time = (

            self.model.time
            +
            self.animation_dt
        )


        # If time becomes greater than 10 s,
        # restart at zero.

        if new_time > 10.0:

            new_time = 0.0


        # Store new time.

        self.model.set_time(
            new_time
        )


        # Update slider.

        self.time_var.set(
            new_time
        )


        # Refresh screen.

        self.update_display()


        # Ask Tkinter to call this function again
        # after about 30 milliseconds.

        self.root.after(

            30,

            self.animate_step
        )


    # =====================================================
    # PAUSE
    # =====================================================

    def pause_animation(self):

        # Setting running to False causes
        # animate_step() to stop continuing.

        self.running = False


        self.show_lesson(

            title="Animation paused",

            explanation=(
                "The current value of time has been preserved.\n\n"

                "No quantum mathematics changed here.\n\n"

                "We simply stopped increasing t automatically."
            ),

            python_code=(
                "self.running = False\n\n"

                "# animate_step() checks:\n\n"

                "if not self.running:\n"
                "    return"
            )
        )


    # =====================================================
    # RESET
    # =====================================================

    def reset(self):

        # Stop animation.

        self.running = False


        # Return model to t = 0.

        self.model.reset()


        # Move slider back to zero.

        self.time_var.set(
            0.0
        )


        # Refresh screen.

        self.update_display()


        self.show_lesson(

            title="System reset",

            explanation=(
                "Time has returned to zero.\n\n"

                "Therefore:\n\n"

                "    α = cos(0) = 1\n"
                "    β = -i sin(0) = 0\n\n"

                "so the system is again:\n\n"

                "    |ψ⟩ = |0⟩"
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

    # Print startup message in PowerShell.

    print(
        "Running 04_rabi_oscillation.py ..."
    )


    # Create main Tkinter window.

    root = tk.Tk()


    # Create our application.

    app = RabiGUI(
        root
    )


    # Start Tkinter event loop.

    root.mainloop()