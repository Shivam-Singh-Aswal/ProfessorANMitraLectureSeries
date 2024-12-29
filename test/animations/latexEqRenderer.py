from manim import *

class AnimateLatexEquation(Scene):
    def construct(self):
        # Define the LaTeX equations
        equation = MathTex(r"\text{The Three-body Problem}").set_color(BLACK)
        eq1 = MathTex(r"(\lambda_0^{-1} - h_0(P_2))\phi_0(P_2) = \int d^3\xi D^{-1}(P_2, \xi)[f_0\phi_0(\xi) + f_1\phi_1(\xi) + C(\xi + \frac{1}{2}P_2)f/(\mathbf{P_2} + \frac{1}{2}\xi)\chi(\xi)]").set_color(BLACK)
        eq2 = MathTex(r"P_2^2(\lambda_0^{-1} - h_0(P_2))\phi_1(P_2) = \int d^3\xi D^{-1}(P_2, \xi)[F_0\phi_0(\xi) + F_1\phi_1(\xi) + i(\mathbf{P_2} + \frac{1}{2}\xi)T(\xi + \frac{1}{2}\mathbf{P_2})k_0\chi(\xi)]").set_color(BLACK)
        eq3 = MathTex(r"\chi(P)(\lambda_1^{-1} - h_1(P)) = 2\int d^3\xi D^{-1}(P, \xi)t/(\xi + \frac{1}{2}P) \times [C(P + \frac{1}{2}\xi)\phi_0(\xi) + \frac{1}{8}T(P + \frac{1}{2}\xi)k_1\phi_1(\xi)]").set_color(BLACK)

        # Center the first equation
        #equation.move_to(ORIGIN)
        equation.move_to(UP*3)

        # Position subsequent equations below the first one, with a buffer (space) in between
        eq1.next_to(equation, DOWN, buff=0.5)
        eq2.next_to(eq1, DOWN, buff=0.5)
        eq3.next_to(eq2, DOWN, buff=0.5)

        # Scale the equations if they are too large for the frame
        equations = VGroup(equation, eq1, eq2, eq3)
        equations.scale(0.6)  # Adjust the scale to fit the equations into the frame

        # Animate each equation appearing
        self.play(Write(equation))
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))

        # Wait for a moment
        self.wait(1)

        # Save the result as a GIF with transparent background
        self.renderer.camera.background_color = (0, 0, 0, 0)  # Set transparent background

# Run the scene
if __name__ == "__main__":
    from manim import config
    config.background_color = (0, 0, 0, 0)  # Transparent background
    config.frame_height = 7  # Increase frame height
    config.frame_width = 12  # Increase frame width
    config.media_dir = "./media"  # Set your desired media directory
    scene = AnimateLatexEquation()
    scene.render()

