"""
=========================================================
03 - BLOCH SPHERE
Neutral-Atom Quantum Computing Learning
=========================================================

GOAL
----

Learn how a pure single-qubit state can be represented
geometrically on the Bloch sphere.

From the previous lesson:

    |ψ> = α|0> + β|1>

A normalized pure qubit can also be written as:

              θ                 θ
    |ψ> = cos(-)|0> + e^(iφ) sin(-)|1>
              2                 2

where:

    θ = theta
    φ = phi


The same state can be represented by a point:

    (x, y, z)

on a unit sphere:

    x = sin(θ) cos(φ)
    y = sin(θ) sin(φ)
    z = cos(θ)


IMPORTANT
---------

The Bloch sphere is a mathematical visualization.

It is NOT:

    - the physical shape of an atom
    - an electron orbit
    - a real sphere inside a quantum computer

It represents the STATE of one ideal qubit.
"""


# =========================================================
# IMPORTS
# =========================================================


# math provides:
#
#     sin()
#     cos()
#     sqrt()
#     radians()
#     degrees()
#     pi
#
import math


# cmath handles complex numbers.
#
# We use it mainly for complex phases.
#
import cmath


# random will let us simulate measurement.
#
import random


# NumPy helps us generate many values
# for drawing the 3D sphere.
#
import numpy as np


# Tkinter creates our graphical interface.
#
import tkinter as tk


# ttk provides modern-looking Tkinter widgets.
#
from tkinter import ttk


# ScrolledText gives us a text area
# with an automatic scrollbar.
#
from tkinter.scrolledtext import ScrolledText


# Figure is Matplotlib's main plotting container.
#
from matplotlib.figure import Figure


# FigureCanvasTkAgg lets us put a Matplotlib
# plot INSIDE a Tkinter application.
#
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# =========================================================
# QUBIT MODEL
# =========================================================


class BlochQubit:

    """
    This class stores the mathematical state of one qubit.

    Instead of directly storing alpha and beta,
    we primarily store:

        theta
        phi

    and calculate alpha and beta from them.

    This makes sense for the Bloch sphere because
    theta and phi are the sphere angles.
    """


    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(self):

        # Start at:
        #
        #     θ = 0
        #
        # This corresponds to:
        #
        #     |ψ> = |0>
        #
        # and the north pole of the Bloch sphere.

        self.theta = 0.0


        # phi does not matter at the north pole,
        # but we initialize it to zero.

        self.phi = 0.0


    # =====================================================
    # CALCULATE ALPHA
    # =====================================================

    def alpha(self):

        # Bloch-sphere parameterization:
        #
        #     α = cos(θ / 2)
        #
        # alpha is real in this standard representation.

        return complex(
            math.cos(self.theta / 2),
            0.0
        )


    # =====================================================
    # CALCULATE BETA
    # =====================================================

    def beta(self):

        # The magnitude of beta is:
        #
        #     sin(θ / 2)

        magnitude = math.sin(
            self.theta / 2
        )


        # The phase factor is:
        #
        #     e^(iφ)
        #
        # Euler's formula:
        #
        #     e^(iφ) = cos(φ) + i sin(φ)

        phase_factor = complex(
            math.cos(self.phi),
            math.sin(self.phi)
        )


        # Therefore:
        #
        #     β = e^(iφ) sin(θ/2)

        return magnitude * phase_factor


    # =====================================================
    # PROBABILITIES
    # =====================================================

    def probabilities(self):

        # Obtain alpha.

        alpha = self.alpha()


        # Obtain beta.

        beta = self.beta()


        # Born rule:
        #
        #     P(0) = |α|²

        probability_0 = abs(alpha) ** 2


        # And:
        #
        #     P(1) = |β|²

        probability_1 = abs(beta) ** 2


        return probability_0, probability_1


    # =====================================================
    # NORMALIZATION
    # =====================================================

    def normalization(self):

        # A valid quantum state satisfies:
        #
        #     |α|² + |β|² = 1

        p0, p1 = self.probabilities()


        return p0 + p1


    # =====================================================
    # BLOCH COORDINATES
    # =====================================================

    def bloch_coordinates(self):

        # The transformation from spherical coordinates
        # to Cartesian Bloch coordinates is:
        #
        #     x = sin(theta) cos(phi)
        #
        #     y = sin(theta) sin(phi)
        #
        #     z = cos(theta)


        x = (
            math.sin(self.theta)
            *
            math.cos(self.phi)
        )


        y = (
            math.sin(self.theta)
            *
            math.sin(self.phi)
        )


        z = math.cos(
            self.theta
        )


        return x, y, z


    # =====================================================
    # SET ANGLES
    # =====================================================

    def set_angles(
        self,
        theta,
        phi
    ):

        # Store the two angles.
        #
        # We expect radians.

        self.theta = theta

        self.phi = phi


    # =====================================================
    # PRESET |0>
    # =====================================================

    def set_zero(self):

        # North pole:
        #
        #     θ = 0

        self.theta = 0.0

        self.phi = 0.0


    # =====================================================
    # PRESET |1>
    # =====================================================

    def set_one(self):

        # South pole:
        #
        #     θ = π

        self.theta = math.pi

        self.phi = 0.0


    # =====================================================
    # PRESET |+>
    # =====================================================

    def set_plus(self):

        # |+> lies on +X.
        #
        #     θ = π/2
        #     φ = 0

        self.theta = math.pi / 2

        self.phi = 0.0


    # =====================================================
    # PRESET |->
    # =====================================================

    def set_minus(self):

        # |-> lies on -X.
        #
        #     θ = π/2
        #     φ = π

        self.theta = math.pi / 2

        self.phi = math.pi


    # =====================================================
    # PRESET |+i>
    # =====================================================

    def set_plus_i(self):

        # |+i> lies on +Y.
        #
        #     θ = π/2
        #     φ = π/2

        self.theta = math.pi / 2

        self.phi = math.pi / 2


    # =====================================================
    # PRESET |-i>
    # =====================================================

    def set_minus_i(self):

        # |-i> lies on -Y.
        #
        #     θ = π/2
        #     φ = 3π/2

        self.theta = math.pi / 2

        self.phi = 3 * math.pi / 2


    # =====================================================
    # SAMPLE MEASUREMENT
    # =====================================================

    def sample_measurement(self):

        # Get measurement probabilities.

        probability_0, probability_1 = (
            self.probabilities()
        )


        # Generate random number:
        #
        #     0 <= r < 1

        random_number = random.random()


        # If random value lies inside
        # the P(0) region:

        if random_number < probability_0:

            return 0, random_number


        # Otherwise:

        return 1, random_number


    # =====================================================
    # MEASURE AND COLLAPSE
    # =====================================================

    def measure_and_collapse(self):

        # Perform measurement.

        result, random_number = (
            self.sample_measurement()
        )


        # Collapse to corresponding pole.

        if result == 0:

            self.set_zero()

        else:

            self.set_one()


        return result, random_number


# =========================================================
# GUI
# =========================================================


class BlochSphereGUI:

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(
        self,
        root
    ):

        # Store main Tkinter window.

        self.root = root


        # Set title.

        self.root.title(
            "Neutral-Atom QC | 03 — Bloch Sphere"
        )


        # Initial window size.

        self.root.geometry(
            "1350x900"
        )


        # Minimum size.

        self.root.minsize(
            1100,
            750
        )


        # Create our mathematical qubit object.

        self.qubit = BlochQubit()


        # Configure ttk appearance.

        self.setup_style()


        # Create different UI sections.

        self.create_header()

        self.create_main_area()

        self.create_learning_area()


        # Show initial values.

        self.update_display()


        # Initial lesson.

        self.show_lesson(

            title="Bloch sphere initialized",

            explanation=(
                "The qubit begins in |0⟩.\n\n"

                "For |0⟩:\n\n"

                "    θ = 0°\n"
                "    φ = 0°\n\n"

                "The Bloch coordinates are:\n\n"

                "    x = 0\n"
                "    y = 0\n"
                "    z = 1\n\n"

                "Therefore the state vector points toward "
                "the north pole of the Bloch sphere."
            ),

            python_code=(
                "self.qubit = BlochQubit()\n\n"

                "# Inside __init__():\n\n"

                "self.theta = 0.0\n"
                "self.phi = 0.0\n\n"

                "# theta = 0 corresponds to |0>."
            )
        )


    # =====================================================
    # STYLE
    # =====================================================

    def setup_style(self):

        # Create style manager.

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

        # Header frame.

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
                "03 — Bloch Sphere"
            ),

            style="Section.TLabel"

        ).pack(
            anchor="w"
        )


        ttk.Label(

            header,

            text=(
                "Turn θ and φ into a geometric "
                "representation of a pure qubit state."
            )

        ).pack(
            anchor="w",
            pady=(3, 0)
        )


    # =====================================================
    # MAIN AREA
    # =====================================================

    def create_main_area(self):

        # Main container.

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


        # Left column larger than right.

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
        # LEFT SIDE — BLOCH SPHERE
        # =================================================

        left = ttk.LabelFrame(

            main,

            text="3D Bloch Sphere",

            padding=10
        )


        left.grid(

            row=0,

            column=0,

            sticky="nsew",

            padx=(0, 8)
        )


        # -------------------------------------------------
        # CREATE MATPLOTLIB FIGURE
        # -------------------------------------------------

        # Figure is the main Matplotlib drawing area.

        self.figure = Figure(

            figsize=(6, 5),

            dpi=100
        )


        # Add a 3D subplot.

        self.ax = self.figure.add_subplot(

            111,

            projection="3d"
        )


        # -------------------------------------------------
        # EMBED MATPLOTLIB IN TKINTER
        # -------------------------------------------------

        # FigureCanvasTkAgg connects the Matplotlib
        # figure to our Tkinter interface.

        self.plot_canvas = FigureCanvasTkAgg(

            self.figure,

            master=left
        )


        # Get the underlying Tkinter widget.

        self.plot_widget = (
            self.plot_canvas.get_tk_widget()
        )


        # Fill available area.

        self.plot_widget.pack(

            fill="both",

            expand=True
        )


        ttk.Label(

            left,

            text=(
                "The arrow represents the qubit state. "
                "θ moves from north to south; "
                "φ rotates around the Z axis."
            ),

            wraplength=650

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
        # STATE INFORMATION
        # -------------------------------------------------

        state_frame = ttk.LabelFrame(

            right,

            text="1. Quantum State",

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

            fill="x",

            pady=5
        )


        # -------------------------------------------------
        # ANGLES
        # -------------------------------------------------

        angle_info = ttk.LabelFrame(

            right,

            text="2. Bloch Angles",

            padding=10
        )


        angle_info.pack(

            fill="x",

            pady=5
        )


        self.theta_label = ttk.Label(

            angle_info,

            style="Value.TLabel"
        )


        self.theta_label.pack(
            anchor="w"
        )


        self.phi_label = ttk.Label(

            angle_info,

            style="Value.TLabel"
        )


        self.phi_label.pack(
            anchor="w"
        )


        # -------------------------------------------------
        # BLOCH COORDINATES
        # -------------------------------------------------

        coordinate_frame = ttk.LabelFrame(

            right,

            text="3. Bloch Coordinates",

            padding=10
        )


        coordinate_frame.pack(

            fill="x",

            pady=5
        )


        self.x_label = ttk.Label(

            coordinate_frame,

            style="Value.TLabel"
        )


        self.x_label.pack(
            anchor="w"
        )


        self.y_label = ttk.Label(

            coordinate_frame,

            style="Value.TLabel"
        )


        self.y_label.pack(
            anchor="w"
        )


        self.z_label = ttk.Label(

            coordinate_frame,

            style="Value.TLabel"
        )


        self.z_label.pack(
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

            style=(
                "Probability.Horizontal.TProgressbar"
            )
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

            style=(
                "Probability.Horizontal.TProgressbar"
            )
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
        # PRESET STATES
        # -------------------------------------------------

        presets = ttk.LabelFrame(

            right,

            text="5. Important States",

            padding=10
        )


        presets.pack(

            fill="x",

            pady=5
        )


        row1 = ttk.Frame(
            presets
        )


        row1.pack(
            fill="x"
        )


        ttk.Button(

            row1,

            text="|0⟩",

            command=self.prepare_zero

        ).pack(

            side="left",

            fill="x",

            expand=True
        )


        ttk.Button(

            row1,

            text="|1⟩",

            command=self.prepare_one

        ).pack(

            side="left",

            fill="x",

            expand=True
        )


        ttk.Button(

            row1,

            text="|+⟩",

            command=self.prepare_plus

        ).pack(

            side="left",

            fill="x",

            expand=True
        )


        row2 = ttk.Frame(
            presets
        )


        row2.pack(

            fill="x",

            pady=(4, 0)
        )


        ttk.Button(

            row2,

            text="|−⟩",

            command=self.prepare_minus

        ).pack(

            side="left",

            fill="x",

            expand=True
        )


        ttk.Button(

            row2,

            text="|+i⟩",

            command=self.prepare_plus_i

        ).pack(

            side="left",

            fill="x",

            expand=True
        )


        ttk.Button(

            row2,

            text="|−i⟩",

            command=self.prepare_minus_i

        ).pack(

            side="left",

            fill="x",

            expand=True
        )


        # -------------------------------------------------
        # SLIDERS
        # -------------------------------------------------

        slider_frame = ttk.LabelFrame(

            right,

            text="6. Control θ and φ",

            padding=10
        )


        slider_frame.pack(

            fill="x",

            pady=5
        )


        # Tkinter variable for theta.

        self.theta_var = tk.DoubleVar(

            value=0
        )


        # Tkinter variable for phi.

        self.phi_var = tk.DoubleVar(

            value=0
        )


        self.theta_slider_label = ttk.Label(

            slider_frame,

            text="θ = 0°"
        )


        self.theta_slider_label.pack(
            anchor="w"
        )


        self.theta_slider = ttk.Scale(

            slider_frame,

            from_=0,

            to=180,

            variable=self.theta_var,

            command=self.slider_changed
        )


        self.theta_slider.pack(

            fill="x",

            pady=(0, 5)
        )


        self.phi_slider_label = ttk.Label(

            slider_frame,

            text="φ = 0°"
        )


        self.phi_slider_label.pack(
            anchor="w"
        )


        self.phi_slider = ttk.Scale(

            slider_frame,

            from_=0,

            to=360,

            variable=self.phi_var,

            command=self.slider_changed
        )


        self.phi_slider.pack(
            fill="x"
        )


        # -------------------------------------------------
        # MEASUREMENT
        # -------------------------------------------------

        measurement_frame = ttk.LabelFrame(

            right,

            text="7. Measurement",

            padding=10
        )


        measurement_frame.pack(

            fill="x",

            pady=5
        )


        ttk.Button(

            measurement_frame,

            text="Measure Once + Collapse",

            command=self.measure_once,

            style="Action.TButton"

        ).pack(
            fill="x"
        )


        self.result_label = ttk.Label(

            measurement_frame,

            text="No measurement yet.",

            justify="center"
        )


        self.result_label.pack(

            fill="x",

            pady=(5, 0)
        )


    # =====================================================
    # LEARNING CONSOLE
    # =====================================================

    def create_learning_area(self):

        learning = ttk.LabelFrame(

            self.root,

            text=(
                "Python + Quantum Learning Console"
            ),

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
        # PYTHON CONCEPTS TAB
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
NEW PYTHON CONCEPTS IN FILE 03
==============================


1. NUMPY

   import numpy as np

   NumPy helps us work efficiently with many numbers.

   Example:

       np.linspace(0, 10, 100)

   creates 100 evenly spaced values between 0 and 10.


2. MESHGRID

   np.meshgrid(...)

   creates a two-dimensional grid of coordinates.

   We use this to generate many points on the sphere.


3. MATPLOTLIB FIGURE

   figure = Figure()

   A Figure is the overall plotting area.


4. SUBPLOT

   figure.add_subplot(
       111,
       projection="3d"
   )

   creates a 3D plotting coordinate system.


5. EMBEDDING MATPLOTLIB INTO TKINTER

   FigureCanvasTkAgg(...)

   lets a Matplotlib graph appear inside
   our Tkinter application.


6. SPHERICAL COORDINATES

   x = sin(theta) cos(phi)
   y = sin(theta) sin(phi)
   z = cos(theta)

   These equations convert angles into
   a position on the unit sphere.


7. UNPACKING

   x, y, z = qubit.bloch_coordinates()

   A function returns three values and
   Python stores them in three variables.


8. QUIVER

   ax.quiver(...)

   draws a vector arrow in a Matplotlib 3D plot.


9. CLEARING A GRAPH

   ax.clear()

   removes the previous drawing before
   drawing the updated state.


10. FLOATING-POINT TOLERANCE

    Values such as:

        cos(pi / 2)

    may become:

        6.123e-17

    instead of exactly 0.

    This is normal floating-point behavior.
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

        # Unlock explanation box.

        self.lesson_text.config(
            state="normal"
        )


        # Clear old content.

        self.lesson_text.delete(

            "1.0",

            tk.END
        )


        # Add new content.

        self.lesson_text.insert(

            tk.END,

            f"{title}\n\n{explanation}"
        )


        # Lock again.

        self.lesson_text.config(
            state="disabled"
        )


        # Update code box.

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
        number
    ):

        # Real component.

        real = number.real


        # Imaginary component.

        imag = number.imag


        # Decide which sign to display.

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

        # Get alpha.

        alpha = (
            self.qubit.alpha()
        )


        # Get beta.

        beta = (
            self.qubit.beta()
        )


        # Get probabilities.

        probability_0, probability_1 = (
            self.qubit.probabilities()
        )


        # Get Bloch coordinates.

        x, y, z = (
            self.qubit.bloch_coordinates()
        )


        # Get normalization.

        normalization = (
            self.qubit.normalization()
        )


        # -------------------------------------------------
        # STATE
        # -------------------------------------------------

        self.state_label.config(

            text=(
                "|ψ⟩ =\n"

                f"({self.format_complex(alpha)})|0⟩\n"

                "+\n"

                f"({self.format_complex(beta)})|1⟩"
            )
        )


        # -------------------------------------------------
        # ANGLES
        # -------------------------------------------------

        theta_deg = math.degrees(
            self.qubit.theta
        )


        phi_deg = math.degrees(
            self.qubit.phi
        )


        self.theta_label.config(

            text=(
                f"θ = {theta_deg:.2f}°"
            )
        )


        self.phi_label.config(

            text=(
                f"φ = {phi_deg:.2f}°"
            )
        )


        # -------------------------------------------------
        # COORDINATES
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
        # PROBABILITIES
        # -------------------------------------------------

        self.p0_label.config(

            text=(
                f"P(0) = {probability_0:.4f} "
                f"= {probability_0 * 100:.1f}%"
            )
        )


        self.p1_label.config(

            text=(
                f"P(1) = {probability_1:.4f} "
                f"= {probability_1 * 100:.1f}%"
            )
        )


        self.p0_bar["value"] = (
            probability_0 * 100
        )


        self.p1_bar["value"] = (
            probability_1 * 100
        )


        self.normalization_label.config(

            text=(
                f"|α|² + |β|² = "
                f"{normalization:.6f}"
            )
        )


        # -------------------------------------------------
        # UPDATE SLIDER LABELS
        # -------------------------------------------------

        self.theta_slider_label.config(

            text=f"θ = {theta_deg:.1f}°"
        )


        self.phi_slider_label.config(

            text=f"φ = {phi_deg:.1f}°"
        )


        # -------------------------------------------------
        # DRAW BLOCH SPHERE
        # -------------------------------------------------

        self.draw_bloch_sphere()


    # =====================================================
    # DRAW BLOCH SPHERE
    # =====================================================

    def draw_bloch_sphere(self):

        # Clear previous graph.

        self.ax.clear()


        # -------------------------------------------------
        # CREATE SPHERE POINTS
        # -------------------------------------------------

        # u goes around the sphere:
        #
        #     0 → 2π

        u = np.linspace(

            0,

            2 * np.pi,

            40
        )


        # v goes from north pole to south pole:
        #
        #     0 → π

        v = np.linspace(

            0,

            np.pi,

            25
        )


        # meshgrid creates every combination
        # of u and v.

        u, v = np.meshgrid(
            u,
            v
        )


        # Unit sphere equations.

        sphere_x = (
            np.cos(u)
            *
            np.sin(v)
        )


        sphere_y = (
            np.sin(u)
            *
            np.sin(v)
        )


        sphere_z = (
            np.cos(v)
        )


        # -------------------------------------------------
        # DRAW SPHERE WIREFRAME
        # -------------------------------------------------

        self.ax.plot_wireframe(

            sphere_x,

            sphere_y,

            sphere_z,

            rstride=2,

            cstride=2,

            linewidth=0.4,

            alpha=0.35
        )


        # -------------------------------------------------
        # DRAW X AXIS
        # -------------------------------------------------

        self.ax.plot(

            [-1.2, 1.2],

            [0, 0],

            [0, 0],

            linewidth=1
        )


        # -------------------------------------------------
        # DRAW Y AXIS
        # -------------------------------------------------

        self.ax.plot(

            [0, 0],

            [-1.2, 1.2],

            [0, 0],

            linewidth=1
        )


        # -------------------------------------------------
        # DRAW Z AXIS
        # -------------------------------------------------

        self.ax.plot(

            [0, 0],

            [0, 0],

            [-1.2, 1.2],

            linewidth=1
        )


        # -------------------------------------------------
        # AXIS LABELS
        # -------------------------------------------------

        self.ax.text(

            1.3,
            0,
            0,

            "+X\n|+⟩"
        )


        self.ax.text(

            -1.3,
            0,
            0,

            "-X\n|−⟩"
        )


        self.ax.text(

            0,
            1.3,
            0,

            "+Y\n|+i⟩"
        )


        self.ax.text(

            0,
            -1.3,
            0,

            "-Y\n|−i⟩"
        )


        self.ax.text(

            0,
            0,
            1.3,

            "+Z\n|0⟩"
        )


        self.ax.text(

            0,
            0,
            -1.3,

            "-Z\n|1⟩"
        )


        # -------------------------------------------------
        # CURRENT QUBIT VECTOR
        # -------------------------------------------------

        x, y, z = (
            self.qubit.bloch_coordinates()
        )


        # quiver draws an arrow.
        #
        # Start:
        #
        #     (0, 0, 0)
        #
        # End direction:
        #
        #     (x, y, z)

        self.ax.quiver(

            0,
            0,
            0,

            x,
            y,
            z,

            length=1,

            normalize=False,

            linewidth=3
        )


        # Draw point at tip.

        self.ax.scatter(

            [x],

            [y],

            [z],

            s=50
        )


        # -------------------------------------------------
        # SET LIMITS
        # -------------------------------------------------

        self.ax.set_xlim(
            -1.3,
            1.3
        )


        self.ax.set_ylim(
            -1.3,
            1.3
        )


        self.ax.set_zlim(
            -1.3,
            1.3
        )


        # -------------------------------------------------
        # AXIS NAMES
        # -------------------------------------------------

        self.ax.set_xlabel(
            "X"
        )


        self.ax.set_ylabel(
            "Y"
        )


        self.ax.set_zlabel(
            "Z"
        )


        # Set equal-looking box dimensions.

        self.ax.set_box_aspect(
            (1, 1, 1)
        )


        # Title above graph.

        self.ax.set_title(

            "Bloch Sphere State Vector"
        )


        # Choose a useful camera angle.

        self.ax.view_init(

            elev=20,

            azim=35
        )


        # Tell Tkinter/Matplotlib
        # to redraw the graph.

        self.plot_canvas.draw_idle()


    # =====================================================
    # SLIDER CHANGED
    # =====================================================

    def slider_changed(

        self,

        value=None
    ):

        # Read degrees from sliders.

        theta_degrees = (
            self.theta_var.get()
        )


        phi_degrees = (
            self.phi_var.get()
        )


        # Convert degrees to radians.

        theta = math.radians(
            theta_degrees
        )


        phi = math.radians(
            phi_degrees
        )


        # Update mathematical qubit.

        self.qubit.set_angles(

            theta,

            phi
        )


        # Refresh interface.

        self.update_display()


        # Explain current calculation.

        self.show_lesson(

            title="Bloch angles changed",

            explanation=(
                f"Current θ = {theta_degrees:.1f}°\n"
                f"Current φ = {phi_degrees:.1f}°\n\n"

                "The program calculates:\n\n"

                "    x = sin(θ) cos(φ)\n"
                "    y = sin(θ) sin(φ)\n"
                "    z = cos(θ)\n\n"

                "θ controls movement between the north "
                "and south poles.\n\n"

                "φ rotates the state around the Z axis."
            ),

            python_code=(
                "theta = math.radians(theta_degrees)\n"
                "phi = math.radians(phi_degrees)\n\n"

                "x = math.sin(theta) * math.cos(phi)\n"
                "y = math.sin(theta) * math.sin(phi)\n"
                "z = math.cos(theta)\n\n"

                "# These are spherical-coordinate equations."
            )
        )


    # =====================================================
    # SYNC SLIDERS
    # =====================================================

    def sync_sliders(self):

        # Convert internal radians back into degrees.

        theta_deg = math.degrees(
            self.qubit.theta
        )


        phi_deg = math.degrees(
            self.qubit.phi
        )


        # Update slider variables.

        self.theta_var.set(
            theta_deg
        )


        self.phi_var.set(
            phi_deg
        )


    # =====================================================
    # PREPARE |0>
    # =====================================================

    def prepare_zero(self):

        self.qubit.set_zero()

        self.sync_sliders()

        self.update_display()


        self.result_label.config(
            text="Prepared |0⟩"
        )


        self.show_lesson(

            title="|0⟩ — North Pole",

            explanation=(
                "|0⟩ is located at the north pole.\n\n"

                "    θ = 0°\n\n"

                "Bloch coordinates:\n\n"

                "    x = 0\n"
                "    y = 0\n"
                "    z = +1\n\n"

                "Measurement probabilities:\n\n"

                "    P(0) = 100%\n"
                "    P(1) = 0%"
            ),

            python_code=(
                "def set_zero(self):\n"
                "    self.theta = 0.0\n"
                "    self.phi = 0.0\n\n"

                "# z = cos(0) = 1"
            )
        )


    # =====================================================
    # PREPARE |1>
    # =====================================================

    def prepare_one(self):

        self.qubit.set_one()

        self.sync_sliders()

        self.update_display()


        self.result_label.config(
            text="Prepared |1⟩"
        )


        self.show_lesson(

            title="|1⟩ — South Pole",

            explanation=(
                "|1⟩ lies at the south pole.\n\n"

                "    θ = 180°\n\n"

                "Bloch coordinates:\n\n"

                "    x = 0\n"
                "    y = 0\n"
                "    z = -1\n\n"

                "Measurement probabilities:\n\n"

                "    P(0) = 0%\n"
                "    P(1) = 100%"
            ),

            python_code=(
                "def set_one(self):\n"
                "    self.theta = math.pi\n"
                "    self.phi = 0.0\n\n"

                "# z = cos(pi) = -1"
            )
        )


    # =====================================================
    # PREPARE |+>
    # =====================================================

    def prepare_plus(self):

        self.qubit.set_plus()

        self.sync_sliders()

        self.update_display()


        self.result_label.config(
            text="Prepared |+⟩"
        )


        self.show_lesson(

            title="|+⟩ — +X Direction",

            explanation=(
                "|+⟩ is:\n\n"

                "          |0⟩ + |1⟩\n"
                "    |+⟩ = -----------\n"
                "               √2\n\n"

                "Its Bloch angles are:\n\n"

                "    θ = 90°\n"
                "    φ = 0°\n\n"

                "Coordinates:\n\n"

                "    x = +1\n"
                "    y = 0\n"
                "    z = 0"
            ),

            python_code=(
                "self.theta = math.pi / 2\n"
                "self.phi = 0.0\n\n"

                "# x = sin(pi/2) * cos(0)\n"
                "# x = 1"
            )
        )


    # =====================================================
    # PREPARE |->
    # =====================================================

    def prepare_minus(self):

        self.qubit.set_minus()

        self.sync_sliders()

        self.update_display()


        self.result_label.config(
            text="Prepared |−⟩"
        )


        self.show_lesson(

            title="|−⟩ — -X Direction",

            explanation=(
                "|−⟩ is:\n\n"

                "          |0⟩ - |1⟩\n"
                "    |−⟩ = -----------\n"
                "               √2\n\n"

                "Its probabilities are still 50/50.\n\n"

                "However its relative phase is 180°.\n\n"

                "Therefore its Bloch vector points in "
                "the opposite direction from |+⟩."
            ),

            python_code=(
                "self.theta = math.pi / 2\n"
                "self.phi = math.pi\n\n"

                "# phi = pi = 180 degrees\n"
                "# therefore vector points toward -X."
            )
        )


    # =====================================================
    # PREPARE |+i>
    # =====================================================

    def prepare_plus_i(self):

        self.qubit.set_plus_i()

        self.sync_sliders()

        self.update_display()


        self.result_label.config(
            text="Prepared |+i⟩"
        )


        self.show_lesson(

            title="|+i⟩ — +Y Direction",

            explanation=(
                "|+i⟩ is:\n\n"

                "           |0⟩ + i|1⟩\n"
                "    |+i⟩ = -------------\n"
                "                √2\n\n"

                "Its phase is +90°.\n\n"

                "On the Bloch sphere this corresponds "
                "to the +Y direction."
            ),

            python_code=(
                "self.theta = math.pi / 2\n"
                "self.phi = math.pi / 2\n\n"

                "# phi = 90 degrees\n"
                "# vector points toward +Y."
            )
        )


    # =====================================================
    # PREPARE |-i>
    # =====================================================

    def prepare_minus_i(self):

        self.qubit.set_minus_i()

        self.sync_sliders()

        self.update_display()


        self.result_label.config(
            text="Prepared |−i⟩"
        )


        self.show_lesson(

            title="|−i⟩ — -Y Direction",

            explanation=(
                "|−i⟩ is:\n\n"

                "           |0⟩ - i|1⟩\n"
                "    |−i⟩ = -------------\n"
                "                √2\n\n"

                "Its relative phase is -90° "
                "(or equivalently 270°).\n\n"

                "The Bloch vector therefore points "
                "toward -Y."
            ),

            python_code=(
                "self.theta = math.pi / 2\n"
                "self.phi = 3 * math.pi / 2\n\n"

                "# 3*pi/2 = 270 degrees."
            )
        )


    # =====================================================
    # MEASURE ONCE
    # =====================================================

    def measure_once(self):

        # Save probabilities BEFORE collapse.

        probability_0, probability_1 = (
            self.qubit.probabilities()
        )


        # Measure.

        result, random_number = (
            self.qubit.measure_and_collapse()
        )


        # Sync sliders with collapsed state.

        self.sync_sliders()


        # Update display.

        self.update_display()


        # Show result.

        self.result_label.config(

            text=(
                f"Measured |{result}⟩ "
                f"(random={random_number:.4f})"
            )
        )


        self.show_lesson(

            title=f"Measurement collapsed to |{result}⟩",

            explanation=(
                "Before measurement:\n\n"

                f"    P(0) = {probability_0:.4f}\n"
                f"    P(1) = {probability_1:.4f}\n\n"

                f"Python generated random number "
                f"{random_number:.4f}.\n\n"

                f"The result was |{result}⟩.\n\n"

                "After measurement the Bloch vector collapses "
                "to one of the Z-axis poles:\n\n"

                "    |0⟩ → north pole\n"
                "    |1⟩ → south pole\n\n"

                "This is an ideal projective measurement model."
            ),

            python_code=(
                "result, random_number = (\n"
                "    self.qubit.measure_and_collapse()\n"
                ")\n\n"

                "if result == 0:\n"
                "    self.set_zero()\n"
                "else:\n"
                "    self.set_one()\n\n"

                "# Measurement in the computational basis\n"
                "# collapses the state onto the Z axis."
            )
        )


# =========================================================
# START APPLICATION
# =========================================================


if __name__ == "__main__":

    # This executes only when the file
    # is run directly.

    print(
        "Running 03_bloch_sphere.py ..."
    )


    # Create main Tkinter window.

    root = tk.Tk()


    # Create application object.

    app = BlochSphereGUI(
        root
    )


    # Keep GUI running.

    root.mainloop()