"""
=========================================================
02 - QUBIT STATES
Neutral-Atom Quantum Computing Learning
=========================================================

GOAL
----

Understand how a general two-level quantum state is represented:

    |ψ> = α|0> + β|1>

where α and β may be COMPLEX numbers.

A valid state must satisfy:

    |α|² + |β|² = 1


NEW CONCEPTS IN THIS LESSON
---------------------------

1. Complex probability amplitudes
2. Magnitude of an amplitude
3. Phase of an amplitude
4. Relative phase
5. Basis states |0> and |1>
6. |+> and |-> states
7. Parameterizing a qubit using θ and φ
8. Why equal probabilities do not necessarily mean equal states


IMPORTANT PHYSICS NOTE
----------------------

This is still an EDUCATIONAL qubit model.

We are NOT yet modeling:

    - real atomic orbitals
    - laser frequencies
    - Rabi oscillations
    - Rydberg states
    - decoherence
    - optical tweezers
    - experimental hardware

We are learning the mathematical language that will later
describe those systems.
"""


# =========================================================
# IMPORTS
# =========================================================


# math contains normal real-number mathematical functions.
#
# Examples:
#
#     math.sqrt()
#     math.sin()
#     math.cos()
#     math.pi
#
import math


# cmath is similar to math,
# but it is designed for COMPLEX numbers.
#
# We use:
#
#     cmath.phase()
#
# to calculate the phase angle of a complex number.
#
import cmath


# random is used for simulated quantum measurement.
#
import random


# Tkinter provides the GUI.
#
import tkinter as tk


# ttk gives us modern Tkinter widgets.
#
from tkinter import ttk


# A text widget with a built-in scrollbar.
#
from tkinter.scrolledtext import ScrolledText


# =========================================================
# QUBIT MODEL
# =========================================================


class QubitState:

    """
    This class stores the mathematical state of one qubit.

    The state is:

        |ψ> = α|0> + β|1>

    alpha and beta are stored as Python complex numbers.
    """


    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(self):

        # Start in |0>.
        #
        # Mathematically:
        #
        #     |ψ> = 1|0> + 0|1>
        #
        # complex(1, 0) means:
        #
        #     1 + 0i
        #
        # Python also allows:
        #
        #     1 + 0j
        #
        # Python uses "j" instead of "i"
        # for the imaginary unit.

        self.alpha = complex(1.0, 0.0)

        self.beta = complex(0.0, 0.0)


    # -----------------------------------------------------
    # PROBABILITIES
    # -----------------------------------------------------

    def probabilities(self):

        # abs() works with complex numbers.
        #
        # Example:
        #
        #     z = 0.5 + 0.5j
        #
        #     abs(z)
        #
        # gives the magnitude:
        #
        #        ___________
        #       √(0.5²+0.5²)
        #
        # Probability is magnitude squared.

        probability_0 = abs(self.alpha) ** 2

        probability_1 = abs(self.beta) ** 2


        # Return both results.

        return probability_0, probability_1


    # -----------------------------------------------------
    # NORMALIZATION
    # -----------------------------------------------------

    def normalization(self):

        # Calculate:
        #
        #     |α|² + |β|²
        #
        # It should be approximately 1.

        return (
            abs(self.alpha) ** 2
            +
            abs(self.beta) ** 2
        )


    # -----------------------------------------------------
    # PHASES
    # -----------------------------------------------------

    def phases(self):

        # cmath.phase(z) returns the phase angle
        # of a complex number in RADIANS.
        #
        # Example:
        #
        #     phase(1) = 0
        #
        #     phase(i) = π/2
        #
        # If an amplitude is exactly zero,
        # its phase is not physically meaningful.
        #
        # For this educational GUI we show it as 0.

        if abs(self.alpha) > 1e-12:

            alpha_phase = cmath.phase(self.alpha)

        else:

            alpha_phase = 0.0


        if abs(self.beta) > 1e-12:

            beta_phase = cmath.phase(self.beta)

        else:

            beta_phase = 0.0


        return alpha_phase, beta_phase


    # -----------------------------------------------------
    # RELATIVE PHASE
    # -----------------------------------------------------

    def relative_phase(self):

        # Obtain the individual phases.

        alpha_phase, beta_phase = self.phases()


        # Relative phase means:
        #
        #     phase(beta) - phase(alpha)
        #
        # This difference is much more important physically
        # than a common global phase applied to the entire state.

        relative = beta_phase - alpha_phase


        # Return answer in radians.

        return relative


    # -----------------------------------------------------
    # SET |0>
    # -----------------------------------------------------

    def set_zero(self):

        # |0> means:
        #
        #     α = 1
        #     β = 0

        self.alpha = complex(1.0, 0.0)

        self.beta = complex(0.0, 0.0)


    # -----------------------------------------------------
    # SET |1>
    # -----------------------------------------------------

    def set_one(self):

        # |1> means:
        #
        #     α = 0
        #     β = 1

        self.alpha = complex(0.0, 0.0)

        self.beta = complex(1.0, 0.0)


    # -----------------------------------------------------
    # SET |+>
    # -----------------------------------------------------

    def set_plus(self):

        # |+> is:
        #
        #            |0> + |1>
        #     |+> = -----------
        #                √2
        #
        # Therefore:
        #
        #     α = 1/√2
        #     β = 1/√2

        value = 1 / math.sqrt(2)

        self.alpha = complex(value, 0.0)

        self.beta = complex(value, 0.0)


    # -----------------------------------------------------
    # SET |->
    # -----------------------------------------------------

    def set_minus(self):

        # |-> is:
        #
        #            |0> - |1>
        #     |-> = -----------
        #                √2
        #
        # Notice that the only change from |+>
        # is the sign of beta.
        #
        # Probabilities remain:
        #
        #     50% and 50%
        #
        # but the quantum state is different.

        value = 1 / math.sqrt(2)

        self.alpha = complex(value, 0.0)

        self.beta = complex(-value, 0.0)


    # -----------------------------------------------------
    # SET +i STATE
    # -----------------------------------------------------

    def set_plus_i(self):

        # Another important state:
        #
        #              |0> + i|1>
        #     |+i> = -------------
        #                   √2
        #
        # Therefore:
        #
        #     α = 1/√2
        #
        #     β = i/√2

        value = 1 / math.sqrt(2)

        self.alpha = complex(value, 0.0)

        self.beta = complex(0.0, value)


    # -----------------------------------------------------
    # CREATE STATE USING θ AND φ
    # -----------------------------------------------------

    def set_from_angles(
        self,
        theta,
        phi
    ):

        # A normalized pure qubit state can be written as:
        #
        #              θ                 θ
        #     |ψ> = cos(-)|0> + e^(iφ) sin(-)|1>
        #              2                 2
        #
        # More conventionally:
        #
        #     |ψ> =
        #
        #         cos(θ/2)|0>
        #
        #         +
        #
        #         e^(iφ) sin(θ/2)|1>
        #
        #
        # theta controls the probability distribution.
        #
        # phi controls relative phase.


        # alpha is real in this standard parameterization.

        alpha = math.cos(theta / 2)


        # Magnitude of beta.

        beta_magnitude = math.sin(theta / 2)


        # e^(iφ) can be written using Euler's formula:
        #
        #     e^(iφ) = cos(φ) + i sin(φ)
        #
        #
        # Python complex number:
        #
        #     real part      = cos(phi)
        #     imaginary part = sin(phi)

        phase_factor = complex(
            math.cos(phi),
            math.sin(phi)
        )


        # Multiply magnitude by phase factor.

        beta = beta_magnitude * phase_factor


        # Save values.

        self.alpha = complex(alpha, 0.0)

        self.beta = beta


    # -----------------------------------------------------
    # SAMPLE MEASUREMENT
    # -----------------------------------------------------

    def sample_measurement(self):

        # Obtain probabilities.

        probability_0, probability_1 = (
            self.probabilities()
        )


        # Generate random number:
        #
        #     0 <= r < 1

        random_number = random.random()


        # Divide probability interval.
        #
        # Example:
        #
        # P(0) = 0.70
        #
        # 0 ---------------- 0.70 -------- 1
        #        |0>                    |1>

        if random_number < probability_0:

            return 0, random_number


        return 1, random_number


    # -----------------------------------------------------
    # MEASURE + COLLAPSE
    # -----------------------------------------------------

    def measure_and_collapse(self):

        # Sample result.

        result, random_number = (
            self.sample_measurement()
        )


        # Collapse depending on outcome.

        if result == 0:

            self.set_zero()

        else:

            self.set_one()


        return result, random_number


# =========================================================
# GUI
# =========================================================


class QubitGUI:

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(self, root):

        # Store Tkinter main window.

        self.root = root


        # Window title.

        self.root.title(
            "Neutral-Atom QC | 02 — Qubit States"
        )


        # Starting window size.

        self.root.geometry(
            "1300x900"
        )


        # Minimum allowed size.

        self.root.minsize(
            1050,
            750
        )


        # Create our qubit object.

        self.qubit = QubitState()


        # Configure GUI appearance.

        self.setup_style()


        # Build sections.

        self.create_header()

        self.create_main_area()

        self.create_learning_area()


        # Initially show |0>.

        self.update_display()


        # Starting lesson.

        self.show_lesson(
            title="Qubit state initialized",
            explanation=(
                "The QubitState object was created.\n\n"
                "Its initial state is:\n\n"
                "    |ψ⟩ = |0⟩\n\n"
                "which means:\n\n"
                "    α = 1 + 0i\n"
                "    β = 0 + 0i\n\n"
                "Unlike the previous lesson, α and β are now "
                "stored as complex numbers because quantum "
                "probability amplitudes can contain phase."
            ),
            python_code=(
                "self.qubit = QubitState()\n\n"
                "# __init__() automatically runs:\n\n"
                "self.alpha = complex(1.0, 0.0)\n"
                "self.beta = complex(0.0, 0.0)\n\n"
                "# complex(real, imaginary)\n"
                "# creates a Python complex number."
            )
        )


    # =====================================================
    # STYLE
    # =====================================================

    def setup_style(self):

        # Create ttk Style object.

        style = ttk.Style()


        # Try using clam theme.

        try:

            style.theme_use("clam")

        except tk.TclError:

            pass


        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 22, "bold")
        )


        style.configure(
            "Section.TLabel",
            font=("Segoe UI", 14, "bold")
        )


        style.configure(
            "Subtitle.TLabel",
            font=("Segoe UI", 10)
        )


        style.configure(
            "Value.TLabel",
            font=("Consolas", 11)
        )


        style.configure(
            "Action.TButton",
            font=("Segoe UI", 10, "bold"),
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

        # Header container.

        header = ttk.Frame(
            self.root,
            padding=(20, 15)
        )


        # Stretch horizontally.

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
            text="02 — Qubit States",
            style="Section.TLabel"
        ).pack(
            anchor="w",
            pady=(4, 0)
        )


        ttk.Label(
            header,
            text=(
                "Complex amplitudes, probabilities, "
                "phase and arbitrary single-qubit states"
            ),
            style="Subtitle.TLabel"
        ).pack(
            anchor="w",
            pady=(3, 0)
        )


    # =====================================================
    # MAIN AREA
    # =====================================================

    def create_main_area(self):

        # Main frame.

        main = ttk.Frame(
            self.root,
            padding=(20, 0, 20, 10)
        )


        main.pack(
            fill="both",
            expand=True
        )


        # Create two columns.

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
            text="Qubit State Visualization",
            padding=12
        )


        left.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 8)
        )


        # Canvas is used to draw our visualization.

        self.canvas = tk.Canvas(
            left,
            bg="white",
            highlightthickness=0
        )


        self.canvas.pack(
            fill="both",
            expand=True
        )


        # Redraw when canvas changes size.

        self.canvas.bind(
            "<Configure>",
            self.on_canvas_resize
        )


        ttk.Label(
            left,
            text=(
                "The circles represent the complex amplitudes. "
                "Their radius represents magnitude, while the "
                "arrow direction represents phase."
            ),
            wraplength=650,
            justify="left"
        ).pack(
            fill="x",
            pady=(8, 0)
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
        # STATE
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
            font=("Cambria Math", 14, "bold"),
            justify="center"
        )


        self.state_label.pack(
            fill="x",
            pady=4
        )


        # -------------------------------------------------
        # AMPLITUDES
        # -------------------------------------------------

        amplitude_frame = ttk.LabelFrame(
            right,
            text="2. Complex Probability Amplitudes",
            padding=10
        )


        amplitude_frame.pack(
            fill="x",
            pady=5
        )


        self.alpha_label = ttk.Label(
            amplitude_frame,
            style="Value.TLabel"
        )


        self.alpha_label.pack(
            anchor="w",
            pady=2
        )


        self.beta_label = ttk.Label(
            amplitude_frame,
            style="Value.TLabel"
        )


        self.beta_label.pack(
            anchor="w",
            pady=2
        )


        self.alpha_magnitude_label = ttk.Label(
            amplitude_frame,
            style="Value.TLabel"
        )


        self.alpha_magnitude_label.pack(
            anchor="w",
            pady=2
        )


        self.beta_magnitude_label = ttk.Label(
            amplitude_frame,
            style="Value.TLabel"
        )


        self.beta_magnitude_label.pack(
            anchor="w",
            pady=2
        )


        # -------------------------------------------------
        # PHASE
        # -------------------------------------------------

        phase_frame = ttk.LabelFrame(
            right,
            text="3. Phase",
            padding=10
        )


        phase_frame.pack(
            fill="x",
            pady=5
        )


        self.alpha_phase_label = ttk.Label(
            phase_frame,
            style="Value.TLabel"
        )


        self.alpha_phase_label.pack(
            anchor="w",
            pady=2
        )


        self.beta_phase_label = ttk.Label(
            phase_frame,
            style="Value.TLabel"
        )


        self.beta_phase_label.pack(
            anchor="w",
            pady=2
        )


        self.relative_phase_label = ttk.Label(
            phase_frame,
            style="Value.TLabel"
        )


        self.relative_phase_label.pack(
            anchor="w",
            pady=2
        )


        # -------------------------------------------------
        # PROBABILITY
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


        self.probability_0_label = ttk.Label(
            probability_frame,
            style="Value.TLabel"
        )


        self.probability_0_label.pack(
            anchor="w"
        )


        self.progress_0 = ttk.Progressbar(
            probability_frame,
            maximum=100,
            style="Probability.Horizontal.TProgressbar"
        )


        self.progress_0.pack(
            fill="x",
            pady=(2, 5)
        )


        self.probability_1_label = ttk.Label(
            probability_frame,
            style="Value.TLabel"
        )


        self.probability_1_label.pack(
            anchor="w"
        )


        self.progress_1 = ttk.Progressbar(
            probability_frame,
            maximum=100,
            style="Probability.Horizontal.TProgressbar"
        )


        self.progress_1.pack(
            fill="x",
            pady=(2, 5)
        )


        self.normalization_label = ttk.Label(
            probability_frame,
            style="Value.TLabel"
        )


        self.normalization_label.pack(
            anchor="w",
            pady=(4, 0)
        )


        # -------------------------------------------------
        # PRESET STATES
        # -------------------------------------------------

        controls = ttk.LabelFrame(
            right,
            text="5. Prepare State",
            padding=10
        )


        controls.pack(
            fill="x",
            pady=5
        )


        button_row_1 = ttk.Frame(
            controls
        )


        button_row_1.pack(
            fill="x"
        )


        ttk.Button(
            button_row_1,
            text="|0⟩",
            command=self.prepare_zero,
            style="Action.TButton"
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 2)
        )


        ttk.Button(
            button_row_1,
            text="|1⟩",
            command=self.prepare_one,
            style="Action.TButton"
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(2, 0)
        )


        button_row_2 = ttk.Frame(
            controls
        )


        button_row_2.pack(
            fill="x",
            pady=(4, 0)
        )


        ttk.Button(
            button_row_2,
            text="|+⟩",
            command=self.prepare_plus,
            style="Action.TButton"
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 2)
        )


        ttk.Button(
            button_row_2,
            text="|−⟩",
            command=self.prepare_minus,
            style="Action.TButton"
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=2
        )


        ttk.Button(
            button_row_2,
            text="|+i⟩",
            command=self.prepare_plus_i,
            style="Action.TButton"
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(2, 0)
        )


        # -------------------------------------------------
        # ANGLE CONTROLS
        # -------------------------------------------------

        angle_frame = ttk.LabelFrame(
            right,
            text="6. Build State Using θ and φ",
            padding=10
        )


        angle_frame.pack(
            fill="x",
            pady=5
        )


        # θ variable stored in degrees.

        self.theta_var = tk.DoubleVar(
            value=0
        )


        # φ variable stored in degrees.

        self.phi_var = tk.DoubleVar(
            value=0
        )


        self.theta_text = ttk.Label(
            angle_frame,
            text="θ = 0°"
        )


        self.theta_text.pack(
            anchor="w"
        )


        self.theta_slider = ttk.Scale(
            angle_frame,
            from_=0,
            to=180,
            variable=self.theta_var,
            command=self.angle_changed
        )


        self.theta_slider.pack(
            fill="x",
            pady=(0, 5)
        )


        self.phi_text = ttk.Label(
            angle_frame,
            text="φ = 0°"
        )


        self.phi_text.pack(
            anchor="w"
        )


        self.phi_slider = ttk.Scale(
            angle_frame,
            from_=0,
            to=360,
            variable=self.phi_var,
            command=self.angle_changed
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
            fill="x",
            pady=2
        )


        ttk.Button(
            measurement_frame,
            text="Run 1000 Measurements",
            command=self.run_shots,
            style="Action.TButton"
        ).pack(
            fill="x",
            pady=2
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
    # LEARNING AREA
    # =====================================================

    def create_learning_area(self):

        learning_frame = ttk.LabelFrame(
            self.root,
            text="Python + Quantum Learning Console",
            padding=10
        )


        learning_frame.pack(
            fill="both",
            padx=20,
            pady=(0, 15)
        )


        notebook = ttk.Notebook(
            learning_frame
        )


        notebook.pack(
            fill="both",
            expand=True
        )


        # -------------------------------------------------
        # WHAT IS HAPPENING TAB
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
            font=("Segoe UI", 10)
        )


        self.lesson_text.pack(
            fill="both",
            expand=True
        )


        # -------------------------------------------------
        # PYTHON CODE TAB
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
            font=("Consolas", 10)
        )


        self.code_text.pack(
            fill="both",
            expand=True
        )


        # -------------------------------------------------
        # NEW PYTHON CONCEPTS TAB
        # -------------------------------------------------

        python_tab = ttk.Frame(
            notebook
        )


        notebook.add(
            python_tab,
            text="New Python concepts"
        )


        python_text = ScrolledText(
            python_tab,
            height=8,
            wrap="word",
            font=("Segoe UI", 10)
        )


        python_text.pack(
            fill="both",
            expand=True
        )


        python_text.insert(
            "1.0",
            """
NEW PYTHON CONCEPTS IN FILE 02
==============================

1. COMPLEX NUMBERS

   z = complex(3, 4)

   means:

       z = 3 + 4j

   Python uses j instead of i.


2. REAL AND IMAGINARY PARTS

   z.real
   z.imag


3. MAGNITUDE

   abs(z)

   For:

       z = 3 + 4j

   the magnitude is:

       sqrt(3² + 4²) = 5


4. COMPLEX PHASE

   cmath.phase(z)

   returns the angle of the complex number.


5. RADIANS

   Python trigonometric functions normally use radians.

   180 degrees = π radians

   We convert using:

       math.radians(degrees)


6. TRIGONOMETRIC FUNCTIONS

   math.sin(x)
   math.cos(x)


7. SLIDER VARIABLES

   tk.DoubleVar()

   stores a decimal number that Tkinter widgets can update.


8. EVENT CALLBACK

   command=self.angle_changed

   When the slider moves, Tkinter calls angle_changed().


9. FORMATTING COMPLEX NUMBERS

   We separately access:

       value.real
       value.imag

   so that the GUI can show them clearly.


10. SMALL NUMERICAL TOLERANCE

    1e-12

    means:

        0.000000000001

    It is useful because floating-point calculations
    are rarely perfectly exact.
"""
        )


        python_text.config(
            state="disabled"
        )


    # =====================================================
    # UPDATE LEARNING CONSOLE
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


        # Delete old contents.

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


        # Do same for Python code box.

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

    def format_complex(self, value):

        # Obtain real part.

        real = value.real


        # Obtain imaginary part.

        imag = value.imag


        # If imaginary component is positive,
        # display "+".

        sign = "+" if imag >= 0 else "-"


        # abs(imag) prevents output such as:
        #
        #     0.7 + -0.4i

        return (
            f"{real:.4f} "
            f"{sign} "
            f"{abs(imag):.4f}i"
        )


    # =====================================================
    # UPDATE DISPLAY
    # =====================================================

    def update_display(self):

        # Read state.

        alpha = self.qubit.alpha

        beta = self.qubit.beta


        # Calculate probabilities.

        probability_0, probability_1 = (
            self.qubit.probabilities()
        )


        # Calculate normalization.

        normalization = (
            self.qubit.normalization()
        )


        # Get phases.

        alpha_phase, beta_phase = (
            self.qubit.phases()
        )


        relative_phase = (
            self.qubit.relative_phase()
        )


        # -------------------------------------------------
        # STATE LABEL
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
        # AMPLITUDES
        # -------------------------------------------------

        self.alpha_label.config(
            text=(
                f"α = "
                f"{self.format_complex(alpha)}"
            )
        )


        self.beta_label.config(
            text=(
                f"β = "
                f"{self.format_complex(beta)}"
            )
        )


        self.alpha_magnitude_label.config(
            text=(
                f"|α| = "
                f"{abs(alpha):.6f}"
            )
        )


        self.beta_magnitude_label.config(
            text=(
                f"|β| = "
                f"{abs(beta):.6f}"
            )
        )


        # -------------------------------------------------
        # PHASES
        # -------------------------------------------------

        self.alpha_phase_label.config(
            text=(
                "phase(α) = "
                f"{math.degrees(alpha_phase):.1f}°"
            )
        )


        self.beta_phase_label.config(
            text=(
                "phase(β) = "
                f"{math.degrees(beta_phase):.1f}°"
            )
        )


        self.relative_phase_label.config(
            text=(
                "relative phase = "
                f"{math.degrees(relative_phase):.1f}°"
            )
        )


        # -------------------------------------------------
        # PROBABILITIES
        # -------------------------------------------------

        self.probability_0_label.config(
            text=(
                f"P(0) = |α|² = "
                f"{probability_0:.4f} "
                f"= {probability_0 * 100:.1f}%"
            )
        )


        self.probability_1_label.config(
            text=(
                f"P(1) = |β|² = "
                f"{probability_1:.4f} "
                f"= {probability_1 * 100:.1f}%"
            )
        )


        # Update progress bars.

        self.progress_0["value"] = (
            probability_0 * 100
        )


        self.progress_1["value"] = (
            probability_1 * 100
        )


        # -------------------------------------------------
        # NORMALIZATION
        # -------------------------------------------------

        if abs(normalization - 1.0) < 1e-9:

            status = "✓ normalized"

        else:

            status = "✗ NOT normalized"


        self.normalization_label.config(
            text=(
                f"|α|² + |β|² = "
                f"{normalization:.6f} "
                f"{status}"
            )
        )


        # Draw visualization.

        self.draw_state()


    # =====================================================
    # CANVAS RESIZE
    # =====================================================

    def on_canvas_resize(
        self,
        event
    ):

        # event contains information about the resize.
        #
        # We don't need the values directly here.

        self.draw_state()


    # =====================================================
    # DRAW STATE
    # =====================================================

    def draw_state(self):

        # Clear previous drawing.

        self.canvas.delete(
            "all"
        )


        # Current canvas dimensions.

        width = self.canvas.winfo_width()

        height = self.canvas.winfo_height()


        if width < 100:

            width = 650


        if height < 100:

            height = 450


        center_y = height / 2


        # Left and right complex-plane centers.

        alpha_x = width * 0.30

        beta_x = width * 0.70


        # Maximum circle radius.

        radius = min(
            width * 0.15,
            height * 0.25
        )


        # -----------------------------------------------
        # TITLE
        # -----------------------------------------------

        self.canvas.create_text(
            width / 2,
            30,
            text=(
                "Complex Amplitudes: "
                "Magnitude + Phase"
            ),
            font=("Segoe UI", 14, "bold")
        )


        # Draw alpha diagram.

        self.draw_complex_amplitude(
            center_x=alpha_x,
            center_y=center_y,
            radius=radius,
            value=self.qubit.alpha,
            label="α  →  amplitude of |0⟩"
        )


        # Draw beta diagram.

        self.draw_complex_amplitude(
            center_x=beta_x,
            center_y=center_y,
            radius=radius,
            value=self.qubit.beta,
            label="β  →  amplitude of |1⟩"
        )


        # -----------------------------------------------
        # BOTTOM MESSAGE
        # -----------------------------------------------

        self.canvas.create_text(
            width / 2,
            height - 35,
            text=(
                "Arrow length = magnitude     "
                "Arrow direction = phase"
            ),
            font=("Segoe UI", 11, "bold")
        )


    # =====================================================
    # DRAW ONE COMPLEX AMPLITUDE
    # =====================================================

    def draw_complex_amplitude(
        self,
        center_x,
        center_y,
        radius,
        value,
        label
    ):

        # Draw reference circle.

        self.canvas.create_oval(
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius,
            outline="gray",
            width=2
        )


        # Horizontal real axis.

        self.canvas.create_line(
            center_x - radius,
            center_y,
            center_x + radius,
            center_y,
            arrow=tk.LAST
        )


        # Vertical imaginary axis.
        #
        # Canvas y increases DOWNWARD,
        # so positive imaginary direction is drawn upward.

        self.canvas.create_line(
            center_x,
            center_y + radius,
            center_x,
            center_y - radius,
            arrow=tk.LAST
        )


        # Axis labels.

        self.canvas.create_text(
            center_x + radius,
            center_y + 18,
            text="Re"
        )


        self.canvas.create_text(
            center_x + 18,
            center_y - radius,
            text="Im"
        )


        # Magnitude of amplitude.

        magnitude = abs(value)


        # Phase of amplitude.

        phase = (
            cmath.phase(value)
            if magnitude > 1e-12
            else 0
        )


        # Arrow length depends on magnitude.

        arrow_length = (
            radius * magnitude
        )


        # Convert polar form into x coordinate.
        #
        # x = r cos(phi)

        end_x = (
            center_x
            +
            arrow_length * math.cos(phase)
        )


        # Canvas y direction is reversed.
        #
        # y = -r sin(phi)

        end_y = (
            center_y
            -
            arrow_length * math.sin(phase)
        )


        # Draw amplitude arrow.

        self.canvas.create_line(
            center_x,
            center_y,
            end_x,
            end_y,
            arrow=tk.LAST,
            width=4
        )


        # Label above diagram.

        self.canvas.create_text(
            center_x,
            center_y - radius - 35,
            text=label,
            font=("Segoe UI", 11, "bold")
        )


        # Magnitude and phase below diagram.

        self.canvas.create_text(
            center_x,
            center_y + radius + 35,
            text=(
                f"|amplitude| = {magnitude:.3f}\n"
                f"phase = {math.degrees(phase):.1f}°"
            ),
            font=("Consolas", 10)
        )


    # =====================================================
    # PREPARE |0>
    # =====================================================

    def prepare_zero(self):

        self.qubit.set_zero()

        self.update_display()


        self.result_label.config(
            text="Prepared |0⟩"
        )


        self.show_lesson(
            title="Prepared |0⟩",
            explanation=(
                "The state is:\n\n"
                "    |ψ⟩ = |0⟩\n\n"
                "Therefore:\n\n"
                "    α = 1\n"
                "    β = 0\n\n"
                "and:\n\n"
                "    P(0) = 100%\n"
                "    P(1) = 0%"
            ),
            python_code=(
                "def set_zero(self):\n\n"
                "    self.alpha = complex(1.0, 0.0)\n"
                "    self.beta = complex(0.0, 0.0)\n\n"
                "# complex(1.0, 0.0) means 1 + 0i."
            )
        )


    # =====================================================
    # PREPARE |1>
    # =====================================================

    def prepare_one(self):

        self.qubit.set_one()

        self.update_display()


        self.result_label.config(
            text="Prepared |1⟩"
        )


        self.show_lesson(
            title="Prepared |1⟩",
            explanation=(
                "The state is now:\n\n"
                "    |ψ⟩ = |1⟩\n\n"
                "so:\n\n"
                "    α = 0\n"
                "    β = 1\n\n"
                "and measurement gives |1⟩ "
                "with probability 100%."
            ),
            python_code=(
                "def set_one(self):\n\n"
                "    self.alpha = complex(0.0, 0.0)\n"
                "    self.beta = complex(1.0, 0.0)"
            )
        )


    # =====================================================
    # PREPARE |+>
    # =====================================================

    def prepare_plus(self):

        self.qubit.set_plus()

        self.update_display()


        self.result_label.config(
            text="Prepared |+⟩"
        )


        self.show_lesson(
            title="Prepared |+⟩",
            explanation=(
                "The |+⟩ state is:\n\n"
                "          |0⟩ + |1⟩\n"
                "    |+⟩ = -----------\n"
                "               √2\n\n"
                "Both amplitudes are positive.\n\n"
                "Measurement probabilities are:\n\n"
                "    P(0) = 50%\n"
                "    P(1) = 50%\n\n"
                "Remember these probabilities because we will "
                "compare this state with |−⟩."
            ),
            python_code=(
                "value = 1 / math.sqrt(2)\n\n"
                "self.alpha = complex(value, 0.0)\n"
                "self.beta  = complex(value, 0.0)\n\n"
                "# alpha ≈ +0.7071\n"
                "# beta  ≈ +0.7071"
            )
        )


    # =====================================================
    # PREPARE |->
    # =====================================================

    def prepare_minus(self):

        self.qubit.set_minus()

        self.update_display()


        self.result_label.config(
            text="Prepared |−⟩"
        )


        self.show_lesson(
            title="Prepared |−⟩",
            explanation=(
                "The |−⟩ state is:\n\n"
                "          |0⟩ - |1⟩\n"
                "    |−⟩ = -----------\n"
                "               √2\n\n"
                "Notice:\n\n"
                "    α ≈ +0.7071\n"
                "    β ≈ -0.7071\n\n"
                "Yet:\n\n"
                "    |α|² = 0.5\n"
                "    |β|² = 0.5\n\n"
                "Therefore |+⟩ and |−⟩ produce the SAME "
                "probabilities when measured directly in the "
                "|0⟩, |1⟩ basis.\n\n"
                "However, they are different quantum states "
                "because their relative phases are different."
            ),
            python_code=(
                "value = 1 / math.sqrt(2)\n\n"
                "self.alpha = complex(value, 0.0)\n"
                "self.beta  = complex(-value, 0.0)\n\n"
                "# beta changed sign.\n"
                "# Probability stays the same because:\n"
                "# abs(-0.7071) ** 2 = 0.5"
            )
        )


    # =====================================================
    # PREPARE |+i>
    # =====================================================

    def prepare_plus_i(self):

        self.qubit.set_plus_i()

        self.update_display()


        self.result_label.config(
            text="Prepared |+i⟩"
        )


        self.show_lesson(
            title="Prepared |+i⟩",
            explanation=(
                "Now beta is imaginary:\n\n"
                "           1              i\n"
                "    |ψ⟩ = --- |0⟩ + --- |1⟩\n"
                "           √2             √2\n\n"
                "The magnitude of both amplitudes is still:\n\n"
                "    1/√2\n\n"
                "so measurement probabilities remain 50/50.\n\n"
                "However, beta now has a phase of +90°.\n\n"
                "This demonstrates why quantum amplitudes cannot "
                "be understood using probabilities alone."
            ),
            python_code=(
                "value = 1 / math.sqrt(2)\n\n"
                "self.alpha = complex(value, 0.0)\n"
                "self.beta  = complex(0.0, value)\n\n"
                "# beta = 0 + 0.7071i\n"
                "# magnitude = 0.7071\n"
                "# phase = 90 degrees"
            )
        )


    # =====================================================
    # SLIDER CHANGED
    # =====================================================

    def angle_changed(
        self,
        value=None
    ):

        # Tkinter Scale passes its current value
        # to this callback.
        #
        # We don't actually need the "value" argument
        # because we read the DoubleVar directly.


        # Get θ in degrees.

        theta_degrees = (
            self.theta_var.get()
        )


        # Get φ in degrees.

        phi_degrees = (
            self.phi_var.get()
        )


        # Update visible labels.

        self.theta_text.config(
            text=(
                f"θ = {theta_degrees:.1f}°"
            )
        )


        self.phi_text.config(
            text=(
                f"φ = {phi_degrees:.1f}°"
            )
        )


        # math.sin() and math.cos()
        # expect RADIANS.
        #
        # Convert degrees -> radians.

        theta = math.radians(
            theta_degrees
        )


        phi = math.radians(
            phi_degrees
        )


        # Ask our qubit object to calculate
        # alpha and beta from θ and φ.

        self.qubit.set_from_angles(
            theta,
            phi
        )


        # Refresh GUI.

        self.update_display()


        # Explain.

        self.show_lesson(
            title="State changed using θ and φ",
            explanation=(
                "We are using the standard pure-qubit "
                "parameterization:\n\n"
                "    |ψ⟩ = cos(θ/2)|0⟩\n"
                "           + e^(iφ) sin(θ/2)|1⟩\n\n"
                f"Current θ = {theta_degrees:.1f}°\n"
                f"Current φ = {phi_degrees:.1f}°\n\n"
                "θ mainly controls how probability is distributed "
                "between |0⟩ and |1⟩.\n\n"
                "φ changes the relative phase.\n\n"
                "Try setting θ near 90°. Then move only φ.\n"
                "Notice that P(0) and P(1) stay approximately "
                "50/50 while the beta phase arrow rotates."
            ),
            python_code=(
                "theta = math.radians(theta_degrees)\n"
                "phi = math.radians(phi_degrees)\n\n"
                "alpha = math.cos(theta / 2)\n"
                "beta_magnitude = math.sin(theta / 2)\n\n"
                "phase_factor = complex(\n"
                "    math.cos(phi),\n"
                "    math.sin(phi)\n"
                ")\n\n"
                "beta = beta_magnitude * phase_factor\n\n"
                "# This implements:\n"
                "# beta = e^(iφ) sin(θ/2)"
            )
        )


    # =====================================================
    # MEASURE ONCE
    # =====================================================

    def measure_once(self):

        # Perform measurement and collapse.

        result, random_number = (
            self.qubit.measure_and_collapse()
        )


        # Update GUI after collapse.

        self.update_display()


        self.result_label.config(
            text=(
                f"Measured |{result}⟩   "
                f"(random = {random_number:.4f})"
            )
        )


        self.show_lesson(
            title=f"Measurement → |{result}⟩",
            explanation=(
                "Measurement depends on amplitude MAGNITUDES:\n\n"
                "    P(0) = |α|²\n"
                "    P(1) = |β|²\n\n"
                "The phase does not directly change probabilities "
                "for a measurement in this computational basis.\n\n"
                f"This shot produced |{result}⟩.\n\n"
                "The state has now collapsed into that basis state."
            ),
            python_code=(
                "result, random_number = (\n"
                "    self.qubit.measure_and_collapse()\n"
                ")\n\n"
                "# Internally:\n\n"
                "p0, p1 = self.probabilities()\n"
                "r = random.random()\n\n"
                "if r < p0:\n"
                "    result = 0\n"
                "else:\n"
                "    result = 1\n\n"
                "# Then the state collapses."
            )
        )


    # =====================================================
    # 1000 SHOTS
    # =====================================================

    def run_shots(self):

        shots = 1000


        counts = {
            0: 0,
            1: 0
        }


        # Store theoretical values first.

        theoretical_0, theoretical_1 = (
            self.qubit.probabilities()
        )


        # Repeat independent sampling.

        for _ in range(shots):

            result, _ = (
                self.qubit.sample_measurement()
            )


            counts[result] += 1


        measured_0 = (
            counts[0] / shots
        )


        measured_1 = (
            counts[1] / shots
        )


        self.result_label.config(
            text=(
                f"|0⟩: {counts[0]}   "
                f"|1⟩: {counts[1]}"
            )
        )


        self.show_lesson(
            title="1000-shot experiment",
            explanation=(
                "The current state was sampled 1000 times.\n\n"
                "Theoretical probabilities:\n\n"
                f"    P(0) = {theoretical_0:.4f}\n"
                f"    P(1) = {theoretical_1:.4f}\n\n"
                "Observed frequencies:\n\n"
                f"    |0⟩ = {measured_0:.4f}\n"
                f"    |1⟩ = {measured_1:.4f}\n\n"
                "Important experiment:\n\n"
                "Run 1000 shots for |+⟩.\n"
                "Then run 1000 shots for |−⟩.\n\n"
                "You should obtain approximately the same "
                "50/50 distribution even though the two states "
                "have different relative phases."
            ),
            python_code=(
                "shots = 1000\n\n"
                "counts = {0: 0, 1: 0}\n\n"
                "for _ in range(shots):\n"
                "    result, _ = self.qubit.sample_measurement()\n"
                "    counts[result] += 1\n\n"
                "# The underscore means:\n"
                "# 'I receive this value, but I do not need it.'"
            )
        )


# =========================================================
# START APPLICATION
# =========================================================


if __name__ == "__main__":

    # Show startup message in PowerShell.

    print(
        "Running 02_qubit_states.py ..."
    )


    # Create main Tkinter window.

    root = tk.Tk()


    # Build application.

    app = QubitGUI(
        root
    )


    # Keep GUI alive and listen for events.

    root.mainloop()