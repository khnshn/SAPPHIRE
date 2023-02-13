from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np
import math
import random


class Builder(ABC):
    @property
    @abstractmethod
    def simulation(self) -> None:
        pass

    @abstractmethod
    def set_days(self) -> None:
        pass

    @abstractmethod
    def set_hours_in_day(self) -> None:
        pass

    @abstractmethod
    def set_beeps_a_day(self) -> None:
        pass

    @abstractmethod
    def set_context_change_steps(self) -> None:
        pass

    @abstractmethod
    def set_beep_power(self) -> None:
        pass

    @abstractmethod
    def set_urge_max(self) -> None:
        pass

    @abstractmethod
    def set_r(self) -> None:
        pass

    @abstractmethod
    def set_b(self) -> None:
        pass

    @abstractmethod
    def set_rate(self) -> None:
        pass

    @abstractmethod
    def set_salience_decay(self) -> None:
        pass

    @abstractmethod
    def set_urge_decay(self) -> None:
        pass

    @abstractmethod
    def set_random_beep(self) -> None:
        pass

    @abstractmethod
    def set_min_c(self) -> None:
        pass

    @abstractmethod
    def set_context_aware_beep(self) -> None:
        pass

    @abstractmethod
    def set_predefined_times(self) -> None:
        pass

    @abstractmethod
    def set_max_c(self) -> None:
        pass

    @abstractmethod
    def set_salience_growth_ratio(self) -> None:
        pass

    @abstractmethod
    def set_predefined_context_info(self) -> None:
        pass

    @abstractmethod
    def set_context_estimator_function(self) -> None:
        pass

    @abstractmethod
    def set_context_reference(self) -> None:
        pass

    @abstractmethod
    def set_context_aware_threshold(self) -> None:
        pass

    @abstractmethod
    def set_use_prefedined_times_to_beep(self) -> None:
        pass

    @abstractmethod
    def set_override_inter_notification_steps(self) -> None:
        pass

    @abstractmethod
    def set_total_beeps(self) -> None:
        pass


class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._simulation = Simulation()

    @property
    def simulation(self) -> Simulation:
        simulation = self._simulation
        self.reset()
        return simulation

    def set_days(self, days) -> None:
        self._simulation._days = int(days)

    def set_hours_in_day(self, hours_in_day) -> None:
        self._simulation._hours_in_day = int(hours_in_day)

    def set_beeps_a_day(self, beeps_a_day) -> None:
        self._simulation._beeps_a_day = int(beeps_a_day)

    def set_context_change_steps(self, context_change_steps) -> None:
        self._simulation._context_change_steps = int(context_change_steps)

    def set_beep_power(self, beep_power) -> None:
        self._simulation._beep_power = float(beep_power)

    def set_urge_max(self, urge_max) -> None:
        self._simulation._urge_max = float(urge_max)

    def set_r(self, r) -> None:
        self._simulation._r = float(r)

    def set_b(self, b) -> None:
        self._simulation._b = float(b)

    def set_rate(self, rate) -> None:
        self._simulation._rate = float(rate)

    def set_salience_decay(self, salience_decay) -> None:
        self._simulation._salience_decay = float(salience_decay)

    def set_urge_decay(self, urge_decay) -> None:
        self._simulation._urge_decay = float(urge_decay)

    def set_random_beep(self, random_beep) -> None:
        self._simulation._random_beep = bool(random_beep)

    def set_min_c(self, min_c) -> None:
        self._simulation._min_c = float(min_c)

    def set_context_aware_beep(self, context_aware_beep) -> None:
        self._simulation._context_aware_beep = bool(context_aware_beep)

    def set_predefined_times(self, predefined_times) -> None:
        self._simulation._predefined_times = predefined_times

    def set_max_c(self, max_c) -> None:
        self._simulation._max_c = float(max_c)

    def set_salience_growth_ratio(self, salience_growth_ratio) -> None:
        self._simulation._salience_growth_ratio = float(salience_growth_ratio)

    def set_predefined_context_info(self, predefined_context_info) -> None:
        self._simulation._predefined_context_info = predefined_context_info

    def set_context_estimator_function(self, context_estimator_function) -> None:
        self._simulation._context_estimator_function = context_estimator_function

    def set_context_reference(self, context_reference) -> None:
        self._simulation._context_reference = context_reference

    def set_context_aware_threshold(self, context_aware_threshold) -> None:
        self._simulation._context_aware_threshold = float(context_aware_threshold)

    def set_use_prefedined_times_to_beep(self, use_prefedined_times_to_beep) -> None:
        self._simulation._use_prefedined_times_to_beep = bool(
            use_prefedined_times_to_beep
        )

    def set_override_inter_notification_steps(
        self, override_inter_notification_steps
    ) -> None:
        self._simulation._override_inter_notification_steps = int(
            override_inter_notification_steps
        )

    def set_total_beeps(self, total_beeps) -> None:
        self._simulation._total_beeps = int(total_beeps)


class Simulation:
    def __init__(self) -> None:
        self._days = (None,)
        self._hours_in_day = (None,)
        self._beeps_a_day = (None,)
        self._context_change_steps = (None,)
        self._beep_power = (None,)
        self._urge_max = (None,)
        self._r = (None,)
        self._b = (None,)
        self._rate = (None,)
        self._salience_decay = (None,)
        self._urge_decay = (None,)
        self._random_beep = (None,)
        self._min_c = (None,)
        self._context_aware_beep = (None,)
        self._predefined_times = ([],)
        self._max_c = (None,)
        self._salience_growth_ratio = (None,)
        self._predefined_context_info = ([],)
        self._context_estimator_function = (None,)
        self._context_reference = (np.array([]),)
        self._context_aware_threshold = (None,)
        self._use_prefedined_times_to_beep = (None,)
        self._override_inter_notification_steps = (None,)
        self._total_beeps = None

    def linear_function(self, r, x, b) -> float:
        """slope-intercept form linear function

        Args:
            r (float): slope
            x (float): x coordinate
            b (float): intercept

        Returns:
            float: y coordinate
        """
        return r * x + b

    def exp_function(self, n_0, rate, t) -> float:
        """generates decay or growth over time

        Args:
            n_0 (float): initial value
            rate (float): growth or decay rate
            t (float): time

        Returns:
            float: y coordinate
        """
        return n_0 * math.exp(rate * t)

    def send_beep(self, is_rnd=True) -> int:
        """generates a random beep by default

        Args:
            is_rnd (bool, optional): if set to false, always a beep will be made. Defaults to True.

        Returns:
            integer: 1 means beep; 0 means no beep
        """
        if is_rnd:
            return random.getrandbits(1)
        else:
            return 1

    def est_context(self, min=0.33, max=1.0) -> float:
        """randomly generates P(action|context)

        Args:
            min (float): min P(C_t|At). Defaults to 0.33.

        Returns:
            float: P(action|context)
        """
        return random.uniform(min, max)

    def decide(self, u, m, a, c, ca) -> float:
        """calculates P(action|urge,memory accessibility,context,beep)

        Args:
            u (float): P(U_t|A_t-1,U_t-1)
            m (float): P(M_t|N_t-1,M_t-1)
            a (flaot): P(A_t|U_t,M_t)
            c (float): P(C_t)
            ca (float): P(C_t|At)

        Returns:
            float: P(action|urge,memory accessibility,context)
        """
        return (ca / c) * a * m * u

    def is_in_fogg_signal_segment(self, x, y, h=0.8, k=0.8, r=0.3) -> bool:
        """hypothetical circle that represents prompts of type signal

        Args:
            x (float): Ability (B.J. Fogg)
            y (float): Motivation (B.J. Fogg)
            h (float, optional): circle x displacement. Defaults to 0.8.
            k (float, optional): circle y displacement. Defaults to 0.8.
            r (float, optional): circle radius. Defaults to 0.3.

        Returns:
            boolean: true if in cricle; otherwise, no
        """
        return math.pow((x - h), 2) + math.pow((y - h), 2) < math.pow(r, 2)

    def random_with_change(self, chance=50) -> int:
        """returns 0 or 1 randomly with chance

        Args:
            chance (int, optional): The intended outcome. Defaults to 50.

        Returns:
            int: 0 or 1
        """
        outcomes = [1] * chance + [0] * (100 - chance)
        return random.choice(outcomes)

    def simulate(self) -> tuple:
        """simulates human behavior during an experiment

        Returns:
            tuple: x, m, u, b, r, c
        """
        time_steps = self._days * self._hours_in_day
        inter_notification_steps = math.floor(self._hours_in_day / self._beeps_a_day)
        if self._override_inter_notification_steps > -1:
            inter_notification_steps = self._override_inter_notification_steps
        if self._total_beeps > 0 and len(self._predefined_times) > 0:
            inter_notification_steps = math.floor(
                (self._predefined_times[-1] - self._predefined_times[0])
                / self._total_beeps
            )
        beeps = []
        responses = []
        memory_accessibility = []
        urge = []
        context = []
        decay_start_time = 0
        growth_start_time = 0
        memory_accessibility.append(0)
        urge.append(self._urge_max)
        if (
            len(self._predefined_context_info) == 0
            or self._context_estimator_function is None
        ):
            context.append(self.est_context(self._min_c, self._max_c))
        else:
            context.append(
                self.context_estimator_function([[self._context_reference[0][2]]])[0][0]
            )

        for t in (
            [x for x in range(self._predefined_times[0], self._predefined_times[-1])]
            if len(self._predefined_times) > 0
            else [x for x in range(time_steps)]
        ):
            # send beep
            if len(self._predefined_times) > 0 and self._use_prefedined_times_to_beep:
                if t in self._predefined_times:
                    beep = 1
                else:
                    beep = 0
            else:
                if 1 not in beeps[-inter_notification_steps:]:
                    if self._context_aware_beep:
                        beep = int(context[-1] > self._context_aware_threshold)
                    else:
                        beep = self.send_beep(self._random_beep)
                else:
                    beep = 0
            beeps.append(beep)
            # update memory accessibility
            if beep == 1:
                decay_start_time = t
                memory_accessibility.append(
                    self.exp_function(self._beep_power, self._rate, 0)
                )
                self._beep_power -= self._salience_decay
            else:
                memory_accessibility.append(
                    self.exp_function(
                        self._beep_power, self._rate, t - decay_start_time
                    )
                )
            # calculate context
            if (
                len(self._predefined_context_info) == 0
                or self._context_estimator_function is None
            ):
                if t % self._context_change_steps == 0:  # to reduce entropy of context
                    context.append(self.est_context(self._min_c, self._max_c))
                else:
                    context.append(context[-1])
            else:
                current_context_info = None
                if t in self._predefined_times:
                    current_context_info = self._predefined_context_info[
                        np.where(self._predefined_times == t)[0][0]
                    ]
                else:
                    if (
                        len(self._context_reference[self._context_reference[:, 1] == t])
                        == 1
                    ):
                        current_context_info = self._context_reference[
                            self._context_reference[:, 1] == t
                        ][0][2]
                if current_context_info is not None:
                    context.append(
                        self.context_estimator_function([[current_context_info]])[0][0]
                    )  # todo p(a|c) or p(c|a)?
                else:
                    context.append(context[-1])
            # decide at time t
            response = 0
            if beep == 1:
                a = (
                    random.choice([i / 100 for i in range(80, 99)])
                    if self.is_in_fogg_signal_segment(
                        memory_accessibility[-1], urge[-1]
                    )
                    else random.choice([i / 100 for i in range(1, 10)])
                )
                response = self.random_with_change(
                    chance=int(
                        self.decide(
                            urge[-1], memory_accessibility[-1], a, 1, context[-1]
                        )
                        * 100
                    )
                )
            responses.append(response)
            # update urge
            if beep == 1 and response == 0:  # disturbing beep
                self._urge_max -= self._urge_decay
            if beep == 1 and response == 1:  # opportune moment
                self._urge_max = (
                    self._urge_max + self._urge_decay
                    if self._urge_max + self._urge_decay <= 1
                    else 1
                )
            if response == 1:
                growth_start_time = t
                urge.append(0)
            else:
                if urge[-1] == self._urge_max:
                    urge.append(self._urge_max)
                else:
                    urge.append(
                        self._urge_max
                        if self.linear_function(self._r, t - growth_start_time, self._b)
                        > self._urge_max
                        else self.linear_function(
                            self._r, t - growth_start_time, self._b
                        )
                    )
            if (
                self._beep_power + self._salience_decay * self._salience_growth_ratio
                <= 1
            ):
                self._beep_power += self._salience_decay * self._salience_growth_ratio
        return (
            (
                [
                    x
                    for x in range(
                        self._predefined_times[0], self._predefined_times[-1]
                    )
                ]
                if len(self._predefined_times) > 0
                else [x for x in range(time_steps)]
            ),
            memory_accessibility,
            urge,
            beeps,
            responses,
            context,
        )

    def get_attrib_value_list(self) -> list:
        return [
            (attr, getattr(self, attr))
            for attr in dir(self)
            if not attr.startswith("__")
        ]


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_default_simulation(self) -> None:
        self.builder.set_days(25)
        self.builder.set_hours_in_day(12)
        self.builder.set_beeps_a_day(5)
        self.builder.set_context_change_steps(2)
        self.builder.set_beep_power(1.0)
        self.builder.set_urge_max(1.0)
        self.builder.set_r(0.2)
        self.builder.set_b(0.0)
        self.builder.set_rate(-0.8)
        self.builder.set_salience_decay(0.01)
        self.builder.set_urge_decay(0.005)
        self.builder.set_random_beep(False)
        self.builder.set_min_c(0.33)
        self.builder.set_context_aware_beep(True)
        self.builder.set_predefined_times([])
        self.builder.set_max_c(0.7)
        self.builder.set_salience_growth_ratio(0.0015)
        self.builder.set_predefined_context_info([])
        self.builder.set_context_estimator_function(None)
        self.builder.set_context_reference(np.array([]))
        self.builder.set_context_aware_threshold(0.5)
        self.builder.set_use_prefedined_times_to_beep(True)
        self.builder.set_override_inter_notification_steps(-1)
        self.builder.set_total_beeps(-1)
