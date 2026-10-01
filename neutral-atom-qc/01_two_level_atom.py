"""
=========================================================
01 - TWO-LEVEL ATOM
Neutral-Atom Quantum Computing Learning
=========================================================

WHAT ARE WE LEARNING?

A very simple quantum system can be represented using two states:

    |0>  -> ground state
    |1>  -> excited state

The quantum state is:

    |ψ> = α|0> + β|1>

where:

    α = amplitude of |0>
    β = amplitude of |1>

The measurement probabilities are:

    P(0) = |α|²
    P(1) = |β|²

and a valid quantum state must satisfy:

    |α|² + |β|² = 1


IMPORTANT PHYSICS NOTE
----------------------

This program is an EDUCATIONAL two-level quantum model.

It is NOT yet a complete physical simulation of a real neutral atom.

Real neutral-atom systems involve things such as:

    - atomic energy structures
    - laser coupling
    - transition frequencies
    - Rabi frequencies
    - detuning
    - decoherence
    - spontaneous emission
    - Rydberg states

We will learn those step-by-step later.
"""


# =========================================================
# IMPORTS
# =========================================================


# "math" gives us mathematical functions.
#
# We will use:
#
#     math.sqrt()
#
# to calculate square roots.
import math


# "random" gives us pseudo-random numbers.
#
# Quantum measurement is probabilistic.
#
# We will use:
#
#     random.random()
#
# which gives a random decimal number between:
#
#     0.0 <= number < 1.0
import random


# tkinter is Python's built-in GUI library.
#
# "as tk" means:
#
#     instead of writing:
#
#         tkinter.Canvas
#
#     we can write:
#
#         tk.Canvas
import tkinter as tk


# ttk contains modern-looking Tkinter widgets.
#
# Examples:
#
#     ttk.Button
#     ttk.Label
#     ttk.Frame
#     ttk.Progressbar
from tkinter import ttk


# ScrolledText is a text box that automatically
# includes a scrollbar.
#
# We use it for our learning/explanation panels.
from tkinter.scrolledtext import ScrolledText


# =========================================================
# QUANTUM SYSTEM
# =========================================================


# "class" creates a BLUEPRINT.
#
# Think of:
#
#     class TwoLevelAtom
#
# as the definition of what our simplified
# quantum atom should contain and what it can do.
class TwoLevelAtom:

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    # __init__ is a special Python method.
    #
    # It automatically runs when we create an object:
    #
    #     atom = TwoLevelAtom()
    #
    # "self" means:
    #
    #     this specific object
    #
    # So:
    #
    #     self.alpha
    #
    # means:
    #
    #     the alpha value belonging to this atom.
    def __init__(self):

        # We begin in the ground state:
        #
        #     |ψ> = 1|0> + 0|1>
        #
        # Therefore:
        #
        #     α = 1
        #     β = 0

        self.alpha = 1.0
        self.beta = 0.0


    # -----------------------------------------------------
    # CALCULATE PROBABILITIES
    # -----------------------------------------------------

    def probabilities(self):

        # Quantum mechanics tells us that probability
        # comes from the squared magnitude of amplitude.
        #
        #     P(0) = |α|²
        #
        # Python:
        #
        #     abs(self.alpha)
        #
        # finds the magnitude of alpha.
        #
        # "** 2" means:
        #
        #     raise to the power of 2.

        probability_0 = abs(self.alpha) ** 2

        # Same calculation for beta:
        #
        #     P(1) = |β|²

        probability_1 = abs(self.beta) ** 2

        # "return" sends values back to whoever
        # called this function.
        #
        # Example:
        #
        #     p0, p1 = atom.probabilities()

        return probability_0, probability_1


    # -----------------------------------------------------
    # CHECK NORMALIZATION
    # -----------------------------------------------------

    def normalization(self):

        # A valid quantum state must satisfy:
        #
        #     |α|² + |β|² = 1
        #
        # Here we calculate that total.

        total = (
            abs(self.alpha) ** 2
            +
            abs(self.beta) ** 2
        )

        # Send the calculated value back.

        return total


    # -----------------------------------------------------
    # PREPARE GROUND STATE
    # -----------------------------------------------------

    def set_ground_state(self):

        # Ground state:
        #
        #     |ψ> = |0>
        #
        # which is the same as:
        #
        #     |ψ> = 1|0> + 0|1>

        self.alpha = 1.0
        self.beta = 0.0


    # -----------------------------------------------------
    # PREPARE EXCITED STATE
    # -----------------------------------------------------

    def set_excited_state(self):

        # Excited state:
        #
        #     |ψ> = |1>
        #
        # which means:
        #
        #     α = 0
        #     β = 1

        self.alpha = 0.0
        self.beta = 1.0


    # -----------------------------------------------------
    # PREPARE EQUAL SUPERPOSITION
    # -----------------------------------------------------

    def set_equal_superposition(self):

        # Equal superposition means:
        #
        #           1              1
        #     |ψ> = ─── |0> + ─── |1>
        #           √2             √2
        #
        # Why 1/sqrt(2)?
        #
        # Because:
        #
        #     |1/√2|² = 1/2
        #
        # so:
        #
        #     P(0) = 0.5
        #     P(1) = 0.5

        self.alpha = 1 / math.sqrt(2)

        self.beta = 1 / math.sqrt(2)


    # -----------------------------------------------------
    # SAMPLE A MEASUREMENT
    # -----------------------------------------------------

    def sample_measurement(self):

        # First obtain the theoretical probabilities.

        probability_0, probability_1 = self.probabilities()

        # Generate a random number:
        #
        # Example:
        #
        #     0.2384
        #
        # or:
        #
        #     0.8172
        #
        # The value is always between 0 and 1.

        random_number = random.random()

        # Suppose:
        #
        #     P(0) = 0.70
        #
        # We divide the interval:
        #
        #     0 -------------------- 0.70 ----------- 1
        #              |0>                       |1>
        #
        # If the random number is less than 0.70,
        # return measurement result 0.

        if random_number < probability_0:

            return 0, random_number

        # If the previous condition was False,
        # the outcome must be |1>.

        return 1, random_number


    # -----------------------------------------------------
    # MEASURE AND COLLAPSE
    # -----------------------------------------------------

    def measure_and_collapse(self):

        # Perform one probabilistic measurement.

        result, random_number = self.sample_measurement()

        # Quantum measurement causes the state to collapse
        # into the measured basis state.
        #
        # If we measured 0:

        if result == 0:

            # Collapse:
            #
            #     |ψ> -> |0>

            self.set_ground_state()

        else:

            # Otherwise collapse:
            #
            #     |ψ> -> |1>

            self.set_excited_state()

        # Return both:
        #
        #     measurement result
        #     random number used
        #
        # The random number is returned only because
        # this is an educational program.

        return result, random_number


# =========================================================
# GUI
# =========================================================


# This class controls everything that appears
# in the graphical interface.
class QuantumGUI:

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    def __init__(self, root):

        # Save the main Tkinter window inside the object.

        self.root = root

        # Set the text shown in the title bar.

        self.root.title(
            "Neutral-Atom QC | 01 — Two-Level Atom"
        )

        # Set the initial window size.
        #
        # width = 1250 pixels
        # height = 850 pixels

        self.root.geometry("1250x850")

        # Do not allow the window to become
        # too small to understand.

        self.root.minsize(1000, 700)


        # -------------------------------------------------
        # CREATE OUR QUANTUM OBJECT
        # -------------------------------------------------

        # This line creates an actual TwoLevelAtom object
        # from the class blueprint we created earlier.

        self.atom = TwoLevelAtom()


        # -------------------------------------------------
        # PREPARE GUI
        # -------------------------------------------------

        # Configure visual styles.

        self.setup_style()

        # Create heading.

        self.create_header()

        # Create main experiment area.

        self.create_main_area()

        # Create educational explanation area.

        self.create_learning_area()

        # Update all displayed values.

        self.update_display()

        # Show the starting explanation.

        self.show_lesson(
            title="Program started",
            explanation=(
                "The program created a TwoLevelAtom object.\n\n"
                "Its initial state is the ground state:\n\n"
                "    |ψ⟩ = 1|0⟩ + 0|1⟩\n\n"
                "Therefore:\n\n"
                "    α = 1\n"
                "    β = 0\n"
                "    P(0) = 1\n"
                "    P(1) = 0\n\n"
                "At this stage we are using a simplified "
                "mathematical two-level model, not a complete "
                "physical atom."
            ),
            python_code=(
                "self.atom = TwoLevelAtom()\n\n"
                "# Python creates an object using our class.\n"
                "# __init__() automatically runs.\n\n"
                "self.alpha = 1.0\n"
                "self.beta = 0.0"
            )
        )


    # =====================================================
    # STYLE
    # =====================================================

    def setup_style(self):

        # Create an object that controls ttk styling.

        style = ttk.Style()

        # Try using the "clam" theme.
        #
        # Different operating systems sometimes
        # support different themes.

        try:

            style.theme_use("clam")

        # TclError could occur if the theme
        # is not available.

        except tk.TclError:

            # "pass" means:
            #
            #     do nothing
            #
            # The program can continue using
            # the default theme.

            pass


        # Large page heading.

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 22, "bold")
        )


        # Secondary heading.

        style.configure(
            "Section.TLabel",
            font=("Segoe UI", 14, "bold")
        )


        # Smaller descriptive text.

        style.configure(
            "Subtitle.TLabel",
            font=("Segoe UI", 10)
        )


        # Monospace-style numbers.

        style.configure(
            "Value.TLabel",
            font=("Consolas", 11)
        )


        # Main buttons.

        style.configure(
            "Action.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=8
        )


        # Probability progress bars.

        style.configure(
            "Probability.Horizontal.TProgressbar",
            thickness=18
        )


    # =====================================================
    # HEADER
    # =====================================================

    def create_header(self):

        # Frame = container for other GUI elements.

        header = ttk.Frame(
            self.root,
            padding=(20, 15)
        )

        # pack() places the frame in the window.
        #
        # fill="x" means:
        #
        #     stretch horizontally.

        header.pack(fill="x")


        # Main title.

        ttk.Label(
            header,
            text="Neutral-Atom Quantum Computing",
            style="Title.TLabel"
        ).pack(anchor="w")


        # Lesson title.

        ttk.Label(
            header,
            text="01 — Two-Level Atom",
            style="Section.TLabel"
        ).pack(
            anchor="w",
            pady=(4, 0)
        )


        # Description.

        ttk.Label(
            header,
            text=(
                "Learn the quantum concept AND the Python "
                "code controlling the simulation."
            ),
            style="Subtitle.TLabel"
        ).pack(
            anchor="w",
            pady=(3, 0)
        )


    # =====================================================
    # MAIN EXPERIMENT AREA
    # =====================================================

    def create_main_area(self):

        # Main container.

        main = ttk.Frame(
            self.root,
            padding=(20, 0, 20, 10)
        )

        main.pack(
            fill="both",
            expand=True
        )


        # grid() divides the frame into rows and columns.
        #
        # Column 0 = atom visualization.
        # Column 1 = controls/information.

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
            text="Visual Quantum Model",
            padding=12
        )

        left.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 8)
        )


        # Canvas allows us to draw lines,
        # rectangles, arrows and text.

        self.canvas = tk.Canvas(
            left,
            bg="white",
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )


        # Whenever the canvas changes size,
        # redraw the atomic diagram.
        #
        # "<Configure>" is a Tkinter event.

        self.canvas.bind(
            "<Configure>",
            self.on_canvas_resize
        )


        # Explanation under the visualization.

        ttk.Label(
            left,
            text=(
                "The horizontal lines represent our simplified "
                "two-level energy model. The bars show the "
                "probability of measuring each state."
            ),
            wraplength=600,
            justify="left"
        ).pack(
            fill="x",
            pady=(8, 0)
        )


        # =================================================
        # RIGHT SIDE
        # =================================================

        right = ttk.Frame(main)

        right.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(8, 0)
        )


        # -------------------------------------------------
        # QUANTUM STATE
        # -------------------------------------------------

        state_frame = ttk.LabelFrame(
            right,
            text="1. Current Quantum State",
            padding=12
        )

        state_frame.pack(
            fill="x",
            pady=(0, 6)
        )


        # This label will later contain:
        #
        #     |ψ> = α|0> + β|1>

        self.state_label = ttk.Label(
            state_frame,
            font=("Cambria Math", 16, "bold"),
            justify="center"
        )

        self.state_label.pack(
            fill="x",
            pady=5
        )


        # -------------------------------------------------
        # AMPLITUDES
        # -------------------------------------------------

        amplitude_frame = ttk.LabelFrame(
            right,
            text="2. Probability Amplitudes",
            padding=10
        )

        amplitude_frame.pack(
            fill="x",
            pady=6
        )


        # Label for alpha.

        self.alpha_label = ttk.Label(
            amplitude_frame,
            style="Value.TLabel"
        )

        self.alpha_label.pack(
            anchor="w",
            pady=2
        )


        # Label for beta.

        self.beta_label = ttk.Label(
            amplitude_frame,
            style="Value.TLabel"
        )

        self.beta_label.pack(
            anchor="w",
            pady=2
        )


        ttk.Label(
            amplitude_frame,
            text=(
                "Amplitude is not probability. "
                "Probability is obtained by squaring "
                "the magnitude of the amplitude."
            ),
            wraplength=400
        ).pack(
            anchor="w",
            pady=(5, 0)
        )


        # -------------------------------------------------
        # PROBABILITIES
        # -------------------------------------------------

        probability_frame = ttk.LabelFrame(
            right,
            text="3. Measurement Probabilities",
            padding=10
        )

        probability_frame.pack(
            fill="x",
            pady=6
        )


        # P(0) text.

        self.probability_0_label = ttk.Label(
            probability_frame,
            style="Value.TLabel"
        )

        self.probability_0_label.pack(
            anchor="w"
        )


        # Visual P(0) progress bar.

        self.progress_0 = ttk.Progressbar(
            probability_frame,
            maximum=100,
            style="Probability.Horizontal.TProgressbar"
        )

        self.progress_0.pack(
            fill="x",
            pady=(2, 6)
        )


        # P(1) text.

        self.probability_1_label = ttk.Label(
            probability_frame,
            style="Value.TLabel"
        )

        self.probability_1_label.pack(
            anchor="w"
        )


        # Visual P(1) progress bar.

        self.progress_1 = ttk.Progressbar(
            probability_frame,
            maximum=100,
            style="Probability.Horizontal.TProgressbar"
        )

        self.progress_1.pack(
            fill="x",
            pady=(2, 6)
        )


        # Normalization text.

        self.normalization_label = ttk.Label(
            probability_frame,
            style="Value.TLabel"
        )

        self.normalization_label.pack(
            anchor="w",
            pady=(4, 0)
        )


        # -------------------------------------------------
        # CONTROLS
        # -------------------------------------------------

        controls = ttk.LabelFrame(
            right,
            text="4. Experiment",
            padding=10
        )

        controls.pack(
            fill="x",
            pady=6
        )


        # Ground state button.
        #
        # command=self.set_ground
        #
        # means:
        #
        # when the user clicks this button,
        # Python runs self.set_ground().

        ttk.Button(
            controls,
            text="Prepare Ground State  |0⟩",
            command=self.set_ground,
            style="Action.TButton"
        ).pack(
            fill="x",
            pady=2
        )


        # Excited state button.

        ttk.Button(
            controls,
            text="Prepare Excited State  |1⟩",
            command=self.set_excited,
            style="Action.TButton"
        ).pack(
            fill="x",
            pady=2
        )


        # Superposition button.

        ttk.Button(
            controls,
            text="Prepare Equal Superposition",
            command=self.set_superposition,
            style="Action.TButton"
        ).pack(
            fill="x",
            pady=2
        )


        # Single measurement.

        ttk.Button(
            controls,
            text="Measure Once + Collapse",
            command=self.measure_once,
            style="Action.TButton"
        ).pack(
            fill="x",
            pady=2
        )


        # Repeated measurements.

        ttk.Button(
            controls,
            text="Run 1000 Measurements",
            command=self.run_shots,
            style="Action.TButton"
        ).pack(
            fill="x",
            pady=2
        )


        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        result_frame = ttk.LabelFrame(
            right,
            text="5. Result",
            padding=10
        )

        result_frame.pack(
            fill="both",
            expand=True,
            pady=(6, 0)
        )


        self.result_label = ttk.Label(
            result_frame,
            text="No measurement yet.",
            font=("Segoe UI", 12, "bold"),
            justify="center"
        )

        self.result_label.pack(
            fill="x",
            pady=3
        )


        self.shots_label = ttk.Label(
            result_frame,
            text="",
            style="Value.TLabel",
            justify="center"
        )

        self.shots_label.pack(
            fill="x",
            pady=3
        )


    # =====================================================
    # LEARNING AREA
    # =====================================================

    def create_learning_area(self):

        # This section explains what the program is doing.

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


        # Notebook creates tabs.

        notebook = ttk.Notebook(
            learning_frame
        )

        notebook.pack(
            fill="both",
            expand=True
        )


        # -------------------------------------------------
        # TAB 1
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
        # TAB 2
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
        # TAB 3
        # -------------------------------------------------

        python_tab = ttk.Frame(
            notebook
        )

        notebook.add(
            python_tab,
            text="Python concepts"
        )


        python_guide = ScrolledText(
            python_tab,
            height=8,
            wrap="word",
            font=("Segoe UI", 10)
        )

        python_guide.pack(
            fill="both",
            expand=True
        )


        # Insert basic Python explanations.

        python_guide.insert(
            "1.0",
            """
PYTHON CONCEPTS USED IN THIS PROGRAM
====================================

1. import

   import math

   Loads another Python module so we can use its functionality.


2. variable

   self.alpha = 1.0

   A variable stores a value.


3. class

   class TwoLevelAtom:

   A class is a blueprint for creating objects.


4. object

   self.atom = TwoLevelAtom()

   This creates an object using the TwoLevelAtom blueprint.


5. self

   self.alpha

   "self" means the current object.


6. method

   def probabilities(self):

   A method is a function that belongs to a class.


7. return

   return probability_0, probability_1

   Sends information back to the code that called the function.


8. if / else

   if random_number < probability_0:
       return 0
   else:
       return 1

   Allows Python to make a decision.


9. for loop

   for _ in range(1000):

   Repeats code many times.


10. dictionary

    counts = {
        0: 0,
        1: 0
    }

    Stores key-value pairs.


11. f-string

    f"P(0) = {probability_0:.3f}"

    Allows variables to be placed directly inside text.


12. callback

    command=self.measure_once

    Tkinter calls this method when the button is clicked.


13. event

    self.canvas.bind("<Configure>", self.on_canvas_resize)

    Runs code when something happens in the GUI.


14. __name__ == "__main__"

    This checks whether this Python file was started directly.

"""
        )

        # Prevent accidental editing.

        python_guide.config(
            state="disabled"
        )


    # =====================================================
    # LEARNING PANEL UPDATE
    # =====================================================

    def show_lesson(
        self,
        title,
        explanation,
        python_code
    ):

        # Make the explanation box editable temporarily.

        self.lesson_text.config(
            state="normal"
        )

        # Remove old text.

        self.lesson_text.delete(
            "1.0",
            tk.END
        )

        # Add new title and explanation.

        self.lesson_text.insert(
            tk.END,
            f"{title}\n\n{explanation}"
        )

        # Lock the text box again.

        self.lesson_text.config(
            state="disabled"
        )


        # Now update the Python-code tab.

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
    # DISPLAY UPDATE
    # =====================================================

    def update_display(self):

        # Read alpha from our atom object.

        alpha = self.atom.alpha

        # Read beta.

        beta = self.atom.beta


        # Calculate probabilities.

        probability_0, probability_1 = (
            self.atom.probabilities()
        )


        # Check normalization.

        normalization = (
            self.atom.normalization()
        )


        # -------------------------------------------------
        # QUANTUM STATE TEXT
        # -------------------------------------------------

        self.state_label.config(
            text=(
                f"|ψ⟩ = "
                f"({alpha:.4f})|0⟩ "
                f"+ "
                f"({beta:.4f})|1⟩"
            )
        )


        # -------------------------------------------------
        # AMPLITUDE TEXT
        # -------------------------------------------------

        self.alpha_label.config(
            text=f"α = {alpha:.6f}"
        )


        self.beta_label.config(
            text=f"β = {beta:.6f}"
        )


        # -------------------------------------------------
        # PROBABILITY TEXT
        # -------------------------------------------------

        self.probability_0_label.config(
            text=(
                f"P(0) = |α|² "
                f"= {probability_0:.6f} "
                f"= {probability_0 * 100:.1f}%"
            )
        )


        self.probability_1_label.config(
            text=(
                f"P(1) = |β|² "
                f"= {probability_1:.6f} "
                f"= {probability_1 * 100:.1f}%"
            )
        )


        # -------------------------------------------------
        # PROGRESS BARS
        # -------------------------------------------------

        self.progress_0["value"] = (
            probability_0 * 100
        )


        self.progress_1["value"] = (
            probability_1 * 100
        )


        # -------------------------------------------------
        # NORMALIZATION
        # -------------------------------------------------

        # abs(normalization - 1) calculates how far
        # the result is from exactly 1.

        if abs(normalization - 1.0) < 0.000001:

            status = "✓ Valid normalized state"

        else:

            status = "✗ State is NOT normalized"


        self.normalization_label.config(
            text=(
                f"|α|² + |β|² = "
                f"{normalization:.6f}   {status}"
            )
        )


        # -------------------------------------------------
        # REDRAW VISUALIZATION
        # -------------------------------------------------

        self.draw_atom(
            probability_0,
            probability_1
        )


    # =====================================================
    # CANVAS RESIZE EVENT
    # =====================================================

    def on_canvas_resize(self, event):

        # We do not actually need "event" yet,
        # but Tkinter automatically sends it.
        #
        # Recalculate probabilities.

        probability_0, probability_1 = (
            self.atom.probabilities()
        )

        # Redraw using the new canvas size.

        self.draw_atom(
            probability_0,
            probability_1
        )


    # =====================================================
    # DRAW TWO-LEVEL SYSTEM
    # =====================================================

    def draw_atom(
        self,
        probability_0,
        probability_1
    ):

        # Remove everything currently drawn.

        self.canvas.delete("all")


        # Ask Tkinter for current canvas width.

        width = self.canvas.winfo_width()

        # Ask for current height.

        height = self.canvas.winfo_height()


        # During initial startup, Tkinter may temporarily
        # report a very small size.

        if width < 100:

            width = 600


        if height < 100:

            height = 450


        # Horizontal center.

        center_x = width / 2


        # Position ground state lower on screen.

        ground_y = height * 0.68


        # Position excited state higher.

        excited_y = height * 0.28


        # =================================================
        # TITLE INSIDE DIAGRAM
        # =================================================

        self.canvas.create_text(
            center_x,
            30,
            text="Simplified Two-Level Quantum System",
            font=("Segoe UI", 14, "bold")
        )


        # =================================================
        # EXCITED ENERGY LEVEL
        # =================================================

        self.canvas.create_line(
            center_x - 150,
            excited_y,
            center_x + 150,
            excited_y,
            width=3
        )


        self.canvas.create_text(
            center_x - 175,
            excited_y,
            text="|1⟩",
            font=("Cambria Math", 16, "bold"),
            anchor="e"
        )


        self.canvas.create_text(
            center_x + 175,
            excited_y,
            text="Excited state",
            font=("Segoe UI", 10),
            anchor="w"
        )


        # =================================================
        # GROUND ENERGY LEVEL
        # =================================================

        self.canvas.create_line(
            center_x - 150,
            ground_y,
            center_x + 150,
            ground_y,
            width=3
        )


        self.canvas.create_text(
            center_x - 175,
            ground_y,
            text="|0⟩",
            font=("Cambria Math", 16, "bold"),
            anchor="e"
        )


        self.canvas.create_text(
            center_x + 175,
            ground_y,
            text="Ground state",
            font=("Segoe UI", 10),
            anchor="w"
        )


        # =================================================
        # ENERGY ARROW
        # =================================================

        self.canvas.create_line(
            center_x + 240,
            ground_y,
            center_x + 240,
            excited_y,
            arrow=tk.LAST,
            width=2
        )


        self.canvas.create_text(
            center_x + 265,
            (ground_y + excited_y) / 2,
            text="Energy",
            font=("Segoe UI", 10),
            angle=90
        )


        # =================================================
        # PROBABILITY BARS
        # =================================================

        bar_width = 200

        bar_height = 26


        # -------------------------------------------------
        # P(1)
        # -------------------------------------------------

        excited_bar_y = excited_y - 60


        self.canvas.create_rectangle(
            center_x - bar_width / 2,
            excited_bar_y,
            center_x + bar_width / 2,
            excited_bar_y + bar_height,
            outline="gray"
        )


        # Filled width is:
        #
        #     total width × probability

        filled_1 = (
            bar_width * probability_1
        )


        self.canvas.create_rectangle(
            center_x - bar_width / 2,
            excited_bar_y,
            center_x - bar_width / 2 + filled_1,
            excited_bar_y + bar_height,
            fill="#dc2626",
            outline=""
        )


        self.canvas.create_text(
            center_x,
            excited_bar_y - 15,
            text=(
                f"P(1) = "
                f"{probability_1:.3f}"
            ),
            font=("Segoe UI", 10, "bold")
        )


        # -------------------------------------------------
        # P(0)
        # -------------------------------------------------

        ground_bar_y = ground_y + 45


        self.canvas.create_rectangle(
            center_x - bar_width / 2,
            ground_bar_y,
            center_x + bar_width / 2,
            ground_bar_y + bar_height,
            outline="gray"
        )


        filled_0 = (
            bar_width * probability_0
        )


        self.canvas.create_rectangle(
            center_x - bar_width / 2,
            ground_bar_y,
            center_x - bar_width / 2 + filled_0,
            ground_bar_y + bar_height,
            fill="#2563eb",
            outline=""
        )


        self.canvas.create_text(
            center_x,
            ground_bar_y + 45,
            text=(
                f"P(0) = "
                f"{probability_0:.3f}"
            ),
            font=("Segoe UI", 10, "bold")
        )


    # =====================================================
    # PREPARE GROUND STATE
    # =====================================================

    def set_ground(self):

        # Ask our quantum object to become |0>.

        self.atom.set_ground_state()


        # Clear old experiment results.

        self.result_label.config(
            text="Prepared |0⟩"
        )

        self.shots_label.config(
            text=""
        )


        # Refresh the GUI.

        self.update_display()


        # Explain the action.

        self.show_lesson(
            title="Ground state prepared",
            explanation=(
                "You prepared the system in |0⟩.\n\n"
                "Mathematically:\n\n"
                "    α = 1\n"
                "    β = 0\n\n"
                "Therefore:\n\n"
                "    P(0) = |1|² = 1\n"
                "    P(1) = |0|² = 0\n\n"
                "A measurement must therefore return |0⟩."
            ),
            python_code=(
                "def set_ground(self):\n"
                "    self.atom.set_ground_state()\n"
                "    self.update_display()\n\n"
                "# Inside TwoLevelAtom:\n\n"
                "def set_ground_state(self):\n"
                "    self.alpha = 1.0\n"
                "    self.beta = 0.0\n\n"
                "# self.atom refers to our TwoLevelAtom object.\n"
                "# The method changes its stored state."
            )
        )


    # =====================================================
    # PREPARE EXCITED STATE
    # =====================================================

    def set_excited(self):

        # Change state to |1>.

        self.atom.set_excited_state()


        # Update result message.

        self.result_label.config(
            text="Prepared |1⟩"
        )

        self.shots_label.config(
            text=""
        )


        # Refresh screen.

        self.update_display()


        # Educational explanation.

        self.show_lesson(
            title="Excited state prepared",
            explanation=(
                "You prepared the system in |1⟩.\n\n"
                "Mathematically:\n\n"
                "    α = 0\n"
                "    β = 1\n\n"
                "Therefore:\n\n"
                "    P(0) = 0\n"
                "    P(1) = 1\n\n"
                "So measurement must return |1⟩."
            ),
            python_code=(
                "def set_excited(self):\n"
                "    self.atom.set_excited_state()\n"
                "    self.update_display()\n\n"
                "def set_excited_state(self):\n"
                "    self.alpha = 0.0\n"
                "    self.beta = 1.0"
            )
        )


    # =====================================================
    # PREPARE SUPERPOSITION
    # =====================================================

    def set_superposition(self):

        # Change the quantum state.

        self.atom.set_equal_superposition()


        # Update message.

        self.result_label.config(
            text="Prepared equal superposition"
        )

        self.shots_label.config(
            text=""
        )


        # Update displayed numbers.

        self.update_display()


        # Explain both Python and quantum meaning.

        self.show_lesson(
            title="Equal superposition prepared",
            explanation=(
                "The state is now:\n\n"
                "          1               1\n"
                "    |ψ⟩ = ── |0⟩ + ── |1⟩\n"
                "          √2              √2\n\n"
                "Numerically:\n\n"
                "    α ≈ 0.7071\n"
                "    β ≈ 0.7071\n\n"
                "Squaring them gives:\n\n"
                "    P(0) = 0.5\n"
                "    P(1) = 0.5\n\n"
                "This does NOT mean the atom is classically "
                "'half in each state'. It is a quantum "
                "superposition represented by probability amplitudes."
            ),
            python_code=(
                "def set_equal_superposition(self):\n\n"
                "    self.alpha = 1 / math.sqrt(2)\n"
                "    self.beta = 1 / math.sqrt(2)\n\n"
                "# math.sqrt(2) calculates √2.\n\n"
                "# 1 / √2 ≈ 0.70710678\n\n"
                "# Squaring it:\n"
                "# 0.70710678² ≈ 0.5"
            )
        )


    # =====================================================
    # SINGLE MEASUREMENT
    # =====================================================

    def measure_once(self):

        # Perform a measurement.
        #
        # Two values are returned:
        #
        #     result
        #     random_number

        result, random_number = (
            self.atom.measure_and_collapse()
        )


        # Show result.

        self.result_label.config(
            text=f"Measured → |{result}⟩"
        )


        # Show the random number so that the student
        # can understand the simulation mechanism.

        self.shots_label.config(
            text=(
                f"Random number used: "
                f"{random_number:.6f}\n"
                f"State collapsed to |{result}⟩"
            )
        )


        # Because measurement collapsed the state,
        # refresh alpha, beta and probabilities.

        self.update_display()


        # Explain the result.

        self.show_lesson(
            title=f"Measurement result: |{result}⟩",
            explanation=(
                "For this educational simulation, Python generated "
                f"the random number {random_number:.6f}.\n\n"
                "Before measurement, the probability of |0⟩ "
                "determined how much of the interval [0,1) "
                "belonged to outcome 0.\n\n"
                f"The selected result was |{result}⟩.\n\n"
                "After the measurement, this program collapses "
                f"the state to |{result}⟩.\n\n"
                "Try this experiment:\n\n"
                "1. Click Equal Superposition\n"
                "2. Look at P(0)=50% and P(1)=50%\n"
                "3. Click Measure Once\n"
                "4. Observe the collapse\n"
                "5. Click Measure Once again\n\n"
                "The second measurement should return the same "
                "state because the first measurement collapsed it."
            ),
            python_code=(
                "result, random_number = "
                "self.atom.measure_and_collapse()\n\n"
                "def sample_measurement(self):\n"
                "    p0, p1 = self.probabilities()\n"
                "    random_number = random.random()\n\n"
                "    if random_number < p0:\n"
                "        return 0, random_number\n\n"
                "    return 1, random_number\n\n"
                "def measure_and_collapse(self):\n"
                "    result, random_number = "
                "self.sample_measurement()\n\n"
                "    if result == 0:\n"
                "        self.set_ground_state()\n"
                "    else:\n"
                "        self.set_excited_state()\n\n"
                "    return result, random_number"
            )
        )


    # =====================================================
    # 1000 MEASUREMENTS
    # =====================================================

    def run_shots(self):

        # Number of simulated experimental repetitions.

        shots = 1000


        # Dictionary used to count results.
        #
        # At the beginning:
        #
        #     zero outcomes = 0
        #     one outcomes  = 0

        counts = {
            0: 0,
            1: 0
        }


        # Store theoretical probabilities before
        # running the experiment.

        theoretical_0, theoretical_1 = (
            self.atom.probabilities()
        )


        # range(shots) produces:
        #
        #     0, 1, 2, 3, ..., 999
        #
        # Therefore the loop runs 1000 times.
        #
        # We use "_" because we do not actually need
        # the loop-number variable.

        for _ in range(shots):

            # Sample one measurement.
            #
            # IMPORTANT:
            #
            # We use sample_measurement(), NOT
            # measure_and_collapse().
            #
            # This represents repeatedly preparing
            # the SAME initial state for each shot.

            result, _ = (
                self.atom.sample_measurement()
            )


            # If result is 0:
            #
            #     counts[0] += 1
            #
            # If result is 1:
            #
            #     counts[1] += 1

            counts[result] += 1


        # Experimental frequency for 0.

        experimental_0 = (
            counts[0] / shots
        )


        # Experimental frequency for 1.

        experimental_1 = (
            counts[1] / shots
        )


        # Update main result.

        self.result_label.config(
            text="1000-shot experiment complete"
        )


        # Display results.

        self.shots_label.config(
            text=(
                f"|0⟩ → {counts[0]} shots "
                f"({experimental_0 * 100:.1f}%)\n"
                f"|1⟩ → {counts[1]} shots "
                f"({experimental_1 * 100:.1f}%)"
            )
        )


        # Explain theory versus experiment.

        self.show_lesson(
            title="1000 repeated measurements",
            explanation=(
                "This experiment simulates 1000 independent shots.\n\n"
                "For every shot, we assume that the same quantum "
                "state is prepared again before measurement.\n\n"
                "THEORETICAL PROBABILITIES\n\n"
                f"    P(0) = {theoretical_0:.4f}\n"
                f"    P(1) = {theoretical_1:.4f}\n\n"
                "EXPERIMENTAL FREQUENCIES\n\n"
                f"    |0⟩ = {counts[0]}/{shots} "
                f"= {experimental_0:.4f}\n"
                f"    |1⟩ = {counts[1]}/{shots} "
                f"= {experimental_1:.4f}\n\n"
                "The experimental values usually approach the "
                "theoretical probabilities as the number of "
                "shots becomes large.\n\n"
                "Try Equal Superposition several times. You probably "
                "will not get exactly 500 and 500 every time. "
                "That statistical variation is expected."
            ),
            python_code=(
                "shots = 1000\n\n"
                "counts = {\n"
                "    0: 0,\n"
                "    1: 0\n"
                "}\n\n"
                "for _ in range(shots):\n\n"
                "    result, _ = self.atom.sample_measurement()\n\n"
                "    counts[result] += 1\n\n"
                "experimental_0 = counts[0] / shots\n"
                "experimental_1 = counts[1] / shots\n\n"
                "# Notice that sample_measurement() does NOT\n"
                "# change alpha or beta.\n"
                "# That lets every shot represent a freshly\n"
                "# prepared copy of the same state."
            )
        )


# =========================================================
# START APPLICATION
# =========================================================


# Python automatically creates a special variable:
#
#     __name__
#
# If we run this file directly:
#
#     python 01_two_level_atom.py
#
# then:
#
#     __name__ == "__main__"
#
# becomes True.
if __name__ == "__main__":

    # Print something in PowerShell so we know
    # the script started.

    print(
        "Running 01_two_level_atom.py ..."
    )


    # tk.Tk() creates the main application window.

    root = tk.Tk()


    # Create our QuantumGUI object and give it
    # the main Tkinter window.

    app = QuantumGUI(root)


    # mainloop() keeps the GUI alive.
    #
    # Without this line, Python would create the
    # window and immediately finish the program.

    root.mainloop()