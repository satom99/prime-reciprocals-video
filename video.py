from manim import *

class Proof(Scene):
    def construct(self):
        self.wait(5)
        self.show_harmonic()
        self.question_primes()
        self.suppose_finite()
        self.series_as_limit()
        self.partial_sum()
        self.limit_definition()
        self.cauchy_condition()
        self.particular_epsilon()
        self.consider_Qq()
        self.factorize_q()
        self.invert_q()
        self.inverse_bound()
        self.contradiction()
        self.conclusion()
    
    def show_harmonic(self):
        title = Tex("Serie armónica")
        series = MathTex(
            "\\sum_{n = 1}^\\infty",
            "\\frac{1}{n}",
            "=",
            "\\infty"
        )
        self.group = VGroup(title, series).arrange(DOWN)

        self.play(
            ShowCreation(self.group)
        )
        self.wait(5)
        
    def question_primes(self):
        title = Tex("¿Qué ocurre para los primos?")
        series = MathTex(
            "\\sum_{n = 1}^\\infty",
            "\\frac{1}{p_n}"
        )
        group = VGroup(title, series).arrange(DOWN)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)
    
    def suppose_finite(self):
        title = Tex("Supongamos que es finita")
        series = MathTex(
            "\\sum_{n = 1}^\\infty",
            "\\frac{1}{p_n}",
            "=",
            "S"
        )
        group = VGroup(title, series).arrange(DOWN)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)
    
    def series_as_limit(self):
        title = Tex("Supongamos que es finita")
        limit = MathTex(
            "\\lim_{N \\to \\infty}",
            "\\sum_{n = 1}^N \\frac{1}{p_n}",
            "=",
            "S"
        )
        group = VGroup(title, limit).arrange(DOWN)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)
    
    def partial_sum(self):
        partial = self.group[1][1]
        surround_partial = SurroundingRectangle(partial)

        title = Tex("Supongamos que es finita")
        limit = MathTex(
            "\\lim_{N \\to \\infty}",
            "S_N",
            "=",
            "S"
        )
        group = VGroup(title, limit).arrange(DOWN)

        surround_partial_two = SurroundingRectangle(limit[1])

        self.play(
            ShowCreation(surround_partial)
        )
        self.wait(5)

        self.play(
            Transform(surround_partial, surround_partial_two),
            Transform(self.group, group)
        )
        self.wait(5)

        self.play(
            FadeOut(surround_partial)
        )
    
    def limit_definition(self):
        limit = self.group[1].copy()

        title = Tex(
            "$\\forall \\varepsilon$ ",
            "existe $K$ ",
            "tal que"
        )
        inequality = MathTex(
            "\\left| S_N - S \\right|",
            "<",
            "\\varepsilon"
        )
        bottom = Tex(
            "para toda $N \geq K$"
        )
        group = VGroup(
            title,
            inequality,
            bottom
        ).arrange(DOWN)

        self.add(limit)
        self.play(
            FadeOut(self.group)
        )
        self.play(
            ApplyMethod(limit.next_to, group, 1.5 * UP)
        )

        surround_limit = SurroundingRectangle(limit)

        self.play(
            ShowCreation(surround_limit)
        )
        self.wait(5)

        self.play(
            FadeIn(group)
        )
        self.wait(5)

        self.play(
            FadeOut(surround_limit),
            FadeOut(limit)
        )
        self.wait(5)

        self.group = group
    
    def cauchy_condition(self):
        title = Tex(
            "$\\forall \\varepsilon$ ",
            "existe $K$ ",
            "tal que"
        )
        inequality = MathTex(
            "\\left| S_N - S_M \\right|",
            "<",
            "\\varepsilon"
        )
        bottom = Tex(
            "para $N > M \geq K$"
        )
        group = VGroup(
            title,
            inequality,
            bottom
        ).arrange(DOWN)

        surround_left = SurroundingRectangle(inequality[0])

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)

        self.play(
            ShowCreation(surround_left)
        )
        self.wait(5)

        # Explicit
        inequality = MathTex(
            "\\sum_{n = M + 1}^N \\frac{1}{p_n}",
            "<",
            "\\varepsilon"
        )
        bottom = Tex(
            "para $N > M \geq K$"
        )
        group = VGroup(
            title,
            inequality,
            bottom
        ).arrange(DOWN)

        surround_left_two = SurroundingRectangle(inequality[0])

        self.play(
            Transform(surround_left, surround_left_two),
            Transform(self.group, group)
        )
        self.wait(5)

        # N to infinity
        inequality = MathTex(
            "\\sum_{n = M + 1}^\\infty \\frac{1}{p_n}",
            "<",
            "\\varepsilon"
        )
        bottom = Tex(
            "para toda $M \geq K$"
        )
        group = VGroup(
            title,
            inequality,
            bottom
        ).arrange(DOWN)

        surround_left_three = SurroundingRectangle(inequality[0])

        self.play(
            Transform(surround_left, surround_left_three),
            Transform(self.group, group)
        )
        self.wait(5)
    
        # M equal to K
        inequality = MathTex(
            "\\sum_{n = K + 1}^\\infty \\frac{1}{p_n}",
            "<",
            "\\varepsilon"
        )
        group = VGroup(
            title,
            inequality,
            bottom
        ).arrange(DOWN)

        surround_left_four = SurroundingRectangle(inequality[0])

        self.play(
            Transform(surround_left, surround_left_four),
            Transform(self.group, group),
            FadeOut(self.group[2])
        )
        self.wait(5)

        wihtout_bottom = VGroup(
            self.group[0],
            self.group[1]
        )

        self.play(
            FadeOut(surround_left)
        )
        self.play(
            ApplyMethod(wihtout_bottom.arrange, DOWN)
        )
        self.wait(5)

        self.group = wihtout_bottom
    
    def particular_epsilon(self):
        title = Tex(
            "Para $\\varepsilon = \\frac{1}{2}$ ",
            "existe $K$ ",
            "tal que"
        )
        inequality = MathTex(
            "\\sum_{n = K + 1}^\\infty \\frac{1}{p_n}",
            "<",
            "\\frac{1}{2}"
        )
        group = VGroup(title, inequality).arrange(DOWN)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)
    
    def consider_Qq(self):
        title = Tex(
            "Ahora consideremos"
        )
        number_Q = MathTex(
            "Q",
            "=",
            "p_1 \\cdots p_K"
        )
        numbers_q = MathTex(
            "q_n",
            "=",
            "1 + nQ"
        )
        group = VGroup(
            title,
            number_Q,
            numbers_q
        ).arrange(DOWN)

        self.play(
            FadeOut(self.group)
        )
        self.play(
            FadeIn(title),
            FadeIn(number_Q)
        )
        self.wait(5)

        self.play(
            FadeIn(numbers_q)
        )
        self.wait(5)

        self.group = group
    
    def factorize_q(self):
        number_Q = self.group[1]
        numbers_q = self.group[2]

        consideration = VGroup(number_Q, numbers_q)

        numbers_q = MathTex(
            "q_n",
            "=",
            "1 + nQ",
            "=",
            "\\prod_{i = 1}^{s_n} p_{\\sigma_n(i)}"
        )
        group = VGroup(
            number_Q.copy(),
            numbers_q
        ).arrange(DOWN)

        except_left = VGroup(
            numbers_q[2],
            numbers_q[3],
            numbers_q[4]
        )
        surround_right = SurroundingRectangle(except_left)

        self.play(
            FadeOut(self.group[0]),
            ApplyMethod(consideration.arrange, DOWN)
        )
        self.wait(5)

        self.play(
            Transform(consideration, group)
        )
        self.wait(5)

        self.play(
            ShowCreation(surround_right)
        )
        self.wait(5)

        self.play(
            Uncreate(surround_right)
        )
        self.wait(5)

        self.group = consideration
    
    def invert_q(self):
        inverse = MathTex(
            "\\frac{1}{q_n}",
            "=",
            "\\frac{1}{1 + nQ}",
            "=",
            "\\frac{1}{\\prod\\limits_{i = 1}^{s_n} p_{\\sigma_n(i)}}"
        )
        group = VGroup(
            self.group[0],
            self.group[1],
            inverse
        )
        without_q = VGroup(
            group[0],
            group[2]
        )

        self.play(
            ApplyMethod(self.group.next_to, inverse, UP)
        )
        self.play(
            FadeIn(inverse)
        )
        self.wait(5)

        self.play(
            FadeOut(group[1]),
            ApplyMethod(without_q.arrange, DOWN)
        )
        self.wait(5)

        self.group = without_q
    
    def inverse_bound(self):
        inverse = MathTex(
            "\\frac{1}{q_n}",
            "=",
            "\\frac{1}{1 + nQ}",
            "=",
            "\\frac{1}{\\prod\\limits_{i = 1}^{s_n} p_{\\sigma_n(i)}}",
            "\leq",
            "\\sum_{i = 1}^{s_n} \\frac{1}{p_{\\sigma_n(i)}}"
        )
        group = VGroup(
            self.group[0].copy(),
            inverse
        ).arrange(DOWN)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)

        # Second bound
        inverse = MathTex(
            "\\frac{1}{q_n}",
            "=",
            "\\frac{1}{1 + nQ}",
            "=",
            "\\frac{1}{\\prod\\limits_{i = 1}^{s_n} p_{\\sigma_n(i)}}",
            "\leq",
            "\\sum_{i = 1}^{s_n} \\frac{1}{p_{\\sigma_n(i)}}",
            "\leq",
            "\\sum_{i = K + 1}^\\infty \\frac{1}{p_i}"
        )
        group = VGroup(
            self.group[0].copy(),
            inverse
        ).arrange(DOWN)

        head = VGroup(
            inverse[0],
            inverse[1],
            inverse[2],
        )
        tail = inverse[8]

        surround_head = SurroundingRectangle(head)
        surround_tail = SurroundingRectangle(tail)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)

        self.play(
            ShowCreation(surround_head),
            ShowCreation(surround_tail)
        )
        self.wait(5)

        # Keep head and tail
        inverse = MathTex(
            "\\frac{1}{q_n}",
            "=",
            "\\frac{1}{1 + nQ}",
            "\leq",
            "\\sum_{i = K + 1}^\\infty \\frac{1}{p_i}"
        )
        group = VGroup(
            self.group[0].copy(),
            inverse
        ).arrange(DOWN)

        head = VGroup(
            inverse[0],
            inverse[1],
            inverse[2],
        )
        tail = inverse[4]

        surround_head_two = SurroundingRectangle(head)
        surround_tail_two = SurroundingRectangle(tail)

        self.play(
            Transform(surround_head, surround_head_two),
            Transform(surround_tail, surround_tail_two),
            Transform(self.group, group)
        )
        self.wait(5)

        self.play(
            FadeOut(surround_head),
            FadeOut(surround_tail)
        )
        self.wait(5)

        # Bound holds for the sum
        inverse = MathTex(
            "\\sum_{n = 1}^\\infty \\frac{1}{q_n}",
            "=",
            "\\sum_{n = 1}^\\infty \\frac{1}{1 + nQ}",
            "\leq",
            "\\sum_{i = K + 1}^\\infty \\frac{1}{p_i}"
        )
        group = VGroup(
            self.group[0].copy(),
            inverse
        ).arrange(DOWN)

        middle = inverse[2]
        tail = inverse[4]

        surround_middle = SurroundingRectangle(middle)
        surround_tail = SurroundingRectangle(tail)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)

        self.play(
            ShowCreation(surround_middle),
            ShowCreation(surround_tail)
        )
        self.wait(5)

        # Keep middle and tail
        inverse = MathTex(
            "\\sum_{n = 1}^\\infty \\frac{1}{1 + nQ}",
            "\leq",
            "\\sum_{i = K + 1}^\\infty \\frac{1}{p_i}"
        )
        group = VGroup(
            self.group[0].copy(),
            inverse
        ).arrange(DOWN)

        middle = inverse[0]
        tail = inverse[2]

        surround_middle_two = SurroundingRectangle(middle)
        surround_tail_two = SurroundingRectangle(tail)

        self.play(
            Transform(surround_middle, surround_middle_two),
            Transform(surround_tail, surround_tail_two),
            Transform(self.group, group)
        )
        self.wait(5)

        self.play(
            FadeOut(surround_middle),
            FadeOut(surround_tail)
        )
        self.wait(5)

        # Bigger bound
        inverse = MathTex(
            "\\sum_{n = 1}^\\infty \\frac{1}{1 + nQ}",
            "\leq",
            "\\sum_{i = K + 1}^\\infty \\frac{1}{p_i}",
            "\leq",
            "\\sum_{t = 1}^\\infty",
            "\\left( \\sum_{i = K + 1}^\\infty \\frac{1}{p_i} \\right)^t"
        )
        group = VGroup(
            self.group[0].copy(),
            inverse
        ).arrange(DOWN)

        head = inverse[0]
        tail = VGroup(
            inverse[4],
            inverse[5]
        )

        surround_head = SurroundingRectangle(head)
        surround_tail = SurroundingRectangle(tail)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)

        self.play(
            ShowCreation(surround_head),
            ShowCreation(surround_tail)
        )
        self.wait(5)

        # Keep head and tail
        inverse = MathTex(
            "\\sum_{n = 1}^\\infty \\frac{1}{1 + nQ}",
            "\leq",
            "\\sum_{t = 1}^\\infty",
            "\\left( \\sum_{i = K + 1}^\\infty \\frac{1}{p_i} \\right)^t"
        )
        group = VGroup(
            self.group[0].copy(),
            inverse
        ).arrange(DOWN)

        head = inverse[0]
        tail = VGroup(
            inverse[2],
            inverse[3]
        )
        power = inverse[3]

        surround_head_two = SurroundingRectangle(head)
        surround_tail_two = SurroundingRectangle(tail)
        surround_power = SurroundingRectangle(power)

        self.play(
            Transform(surround_head, surround_head_two),
            Transform(surround_tail, surround_tail_two),
            Transform(self.group, group)
        )
        self.wait(5)

        self.play(
            FadeOut(surround_head),
            FadeOut(surround_tail)
        )
        self.wait(5)

        self.play(
            ShowCreation(surround_power)
        )
        self.wait(5)

        bound_group = group
        bound_surround = surround_power

        self.play(
            FadeOut(surround_power)
        )

        # Flashback to particular epsilon
        self.particular_epsilon()

        inequality = MathTex(
            "\\left( \\sum_{n = K + 1}^\\infty \\frac{1}{p_n} \\right)^t",
            "<",
            "\\left( \\frac{1}{2} \\right)^t"
        )
        group = VGroup(
            self.group[0].copy(),
            inequality
        ).arrange(DOWN)

        power = inequality[0]

        epsilon_surround_power = SurroundingRectangle(power)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)

        self.play(
            ShowCreation(epsilon_surround_power)
        )
        self.wait(5)

        self.play(
            Transform(self.group, bound_group),
            Transform(epsilon_surround_power, bound_surround)
        )
        self.wait(5)

        # Epsilon bound
        inverse = MathTex(
            "\\sum_{n = 1}^\\infty \\frac{1}{1 + nQ}",
            "\leq",
            "\\sum_{t = 1}^\\infty",
            "\\left( \\sum_{i = K + 1}^\\infty \\frac{1}{p_i} \\right)^t",
            "<",
            "\\sum_{t = 1}^\\infty",
            "\\left( \\frac{1}{2} \\right)^t"
        )
        group = VGroup(
            self.group[0].copy(),
            inverse
        ).arrange(DOWN)

        power = inverse[3]
        surround_power = SurroundingRectangle(power)

        head = inverse[0]
        tail = VGroup(
            inverse[5],
            inverse[6]
        )

        surround_head = SurroundingRectangle(head)
        surround_tail = SurroundingRectangle(tail)

        self.play(
            Transform(self.group, group),
            Transform(epsilon_surround_power, surround_power)
        )
        self.wait(5)

        self.play(
            FadeOut(epsilon_surround_power)
        )
        self.wait(5)

        self.play(
            ShowCreation(surround_head),
            ShowCreation(surround_tail)
        )
        self.wait(5)

        # Keep head and tail
        inverse = MathTex(
            "\\sum_{n = 1}^\\infty \\frac{1}{1 + nQ}",
            "<",
            "\\sum_{t = 1}^\\infty",
            "\\left( \\frac{1}{2} \\right)^t"
        )
        group = VGroup(
            self.group[0].copy(),
            inverse
        ).arrange(DOWN)

        head = inverse[0]
        tail = VGroup(
            inverse[2],
            inverse[3]
        )

        surround_head_two = SurroundingRectangle(head)
        surround_tail_two = SurroundingRectangle(tail)

        self.play(
            Transform(surround_head, surround_head_two),
            Transform(surround_tail, surround_tail_two),
            ReplacementTransform(self.group, group)
        )
        self.wait(5)

        self.group = group

        self.play(
            FadeOut(surround_head),
            FadeOut(surround_tail)
        )
        self.wait(5)

        # Keep the inequality
        group = VGroup(
            self.group[1]
        )

        self.play(
            FadeOut(self.group[0]),
            ApplyMethod(group.arrange, DOWN)
        )
        self.wait(5)

        self.group = group
    
    def contradiction(self):
        inequality = self.group[0]

        head = inequality[0]
        tail = VGroup(
            inequality[2],
            inequality[3]
        )

        brace_head = Brace(head)
        brace_head_text = brace_head.get_tex("= \infty")

        brace_tail = Brace(tail)
        brace_tail_text = brace_tail.get_tex("< \infty")

        self.play(
            ShowCreation(brace_tail),
            ShowCreation(brace_tail_text)
        )
        self.wait(5)

        self.play(
            ShowCreation(brace_head),
            ShowCreation(brace_head_text)
        )
        self.wait(5)

        self.group.add(brace_head, brace_head_text)
        self.group.add(brace_tail, brace_tail_text)
    
    def conclusion(self):
        self.question_primes()

        # Cannot be finite
        series = MathTex(
            "\\sum_{n = 1}^\\infty",
            "\\frac{1}{p_n}",
            "\\neq",
            "S"
        )
        group = VGroup(
            self.group[0],
            series
        ).arrange(DOWN)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)

        # Must be infinite
        series = MathTex(
            "\\sum_{n = 1}^\\infty",
            "\\frac{1}{p_n}",
            "=",
            "\\infty"
        )
        group = VGroup(
            self.group[0],
            series
        ).arrange(DOWN)

        self.play(
            Transform(self.group, group)
        )
        self.wait(5)

        self.play(
            FadeOut(self.group)
        )