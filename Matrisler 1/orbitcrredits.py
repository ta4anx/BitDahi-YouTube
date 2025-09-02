from manim import *
import random
class endingbackground(Scene):
    def construct(self):
        # Define the center of the orbits, off-screen at the bottom right
        orbit_center = RIGHT * 7 + DOWN * 4

        # Lists of mathematical symbols
        symbols_tex = [
            r"\alpha", r"\beta", r"\gamma", r"\delta", r"\epsilon", r"\zeta", r"\eta",
            r"\theta", r"\iota", r"\kappa", r"\lambda", r"\mu", r"\nu", r"\xi",
            r"+", r"-", r"\times", r"\div", r"=", r"\neq", r"<", r">",
            r"\sqrt{2}", r"\int", r"\sum", r"\lim", r"\infty", r"\partial",
            r"\mathbb{N}", r"\mathbb{Z}", r"\mathbb{Q}", r"\mathbb{R}", r"\mathbb{C}",
            r"\forall", r"\exists", r"\in", r"\notin", r"\subset", r"\supset",
            r"\wedge", r"\vee", r"\neg", r"\implies", r"\iff", r"\bot", r"\top"
        ]

        # Parameters for 8 orbits
        num_orbits = 8
        radii = [2 + i * 0.8 for i in range(num_orbits)]
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
        speeds = [0.1 + i * 0.05 for i in range(num_orbits)] # Different rotation speeds
        spin_speeds = [0.5 + i * 0.2 for i in range(num_orbits)] # Different self-spin speeds
        # Outer orbits have more symbols, are slower, and spin slower
        num_symbols_per_orbit = [3, 4, 5, 8, 11, 14, 17, 23] # Total must match len(symbols_tex)
        speeds = [0.2 - i * 0.02 for i in range(num_orbits)] # Slower for outer orbits
        spin_speeds = [1.0 - i * 0.1 for i in range(num_orbits)] # Slower spin for outer orbits

        # Shuffle symbols to randomize their distribution
        random.shuffle(symbols_tex)

        # Assign symbols to orbits based on num_symbols_per_orbit
        symbols_by_orbit = []
        start_index = 0
        for num in num_symbols_per_orbit:
            end_index = start_index + num
            symbols_by_orbit.append(symbols_tex[start_index:end_index])
            start_index = end_index
        # Create and animate symbols for each orbit
        all_symbols = VGroup()
        for i in range(num_orbits):
            orbit_symbols = VGroup()
            # Distribute a subset of symbols on this orbit
            symbols_on_this_orbit = symbols_tex[i::num_orbits]
            num_symbols_on_orbit = len(symbols_on_this_orbit)
            
            for j, tex in enumerate(symbols_on_this_orbit):
                symbol = MathTex(tex, color=colors[i % len(colors)]).scale(0.8)
                # Set initial position
                angle = 2 * PI * j / num_symbols_on_orbit
                symbol.move_to(orbit_center + radii[i] * (np.cos(angle) * RIGHT + np.sin(angle) * UP))
                # Set initial orientation to face away from the center
                symbol.rotate(angle)
                orbit_symbols.add(symbol)

            # Add an updater to the group of symbols for this orbit
            def create_updater(orbit_group, radius, speed, spin_speed):
                def updater(mob, dt):
                    # Orbit rotation
                    mob.rotate(speed * dt, about_point=orbit_center)
                    # Keep symbols oriented relative to the center
                    for submob in mob:
                        # Counter-rotate to nullify the orbit's rotation effect on the symbol's orientation
                        submob.rotate(-speed * dt)
                        # Add the independent spin
                        submob.rotate(spin_speed * dt)
                return updater

            orbit_symbols.add_updater(create_updater(orbit_symbols, radii[i], speeds[i], spin_speeds[i]))
            all_symbols.add(orbit_symbols)

        self.add(all_symbols)
        self.wait(20)