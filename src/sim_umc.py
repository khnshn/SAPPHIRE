import matplotlib.pyplot as plt
import math
import random
import itertools
import numpy as np


def linear_function(r, x, b):
    """slope-intercept form linear function

    Args:
        r (float): slope
        x (float): x coordinate
        b (float): intercept

    Returns:
        float: y coordinate
    """
    return r * x + b


def exp_function(n_0, rate, t):
    """generates decay or growth over time

    Args:
        n_0 (float): initial value
        rate (float): growth or decay rate
        t (float): time

    Returns:
        float: y coordinate
    """
    return n_0 * math.exp(rate * t)


def send_beep(is_rnd=True):
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


def est_context(min=0.33, max=1.0):
    """randomly generates P(action|context)

    Args:
        min (float): min P(C_t|At). Defaults to 0.33.

    Returns:
        float: P(action|context)
    """
    return random.uniform(min, max)


def decide(u, m, a, c, ca):
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


def is_in_fogg_signal_segment(x, y, h=0.8, k=0.8, r=0.3):
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


def random_with_change(chance=50):
    """returns 0 or 1 randomly with chance

    Args:
        chance (int, optional): The intended outcome. Defaults to 50.

    Returns:
        int: 0 or 1
    """
    outcomes = [1] * chance + [0] * (100 - chance)
    return random.choice(outcomes)


def simulate(
    days=25,
    hours_in_day=12,
    beeps_a_day=5,
    context_change_steps=2,
    beep_power=1,
    urge_max=1,
    r=0.2,
    b=0,
    rate=-0.8,
    salience_decay=0.01,
    urge_decay=0.005,
    randm_beep=False,
    min_c=0.33,
    context_aware_beep=True,
    predefined_times=[],
    max_c=0.7,
    salience_growth_ratio=0.0015,
    predefined_context_info=[],
    context_estimator_function=None,
    context_reference=np.array([]),
    context_aware_threshold=0.5,
    use_prefedined_times_to_beep=True,
    override_inter_notification_steps=-1,
    total_beeps=-1,
):
    """simulates human behavior during an experiment

    Args:
        days (int, optional): the experiment period as the number of days. Defaults to 25.
        hours_in_day (int, optional): the total hours in a day that a beeps are allowed. Defaults to 12.
        beeps_a_day (int, optional): the (maximum) number of allowed beeps per day. Defaults to 5.
        context_change_steps (int, optional): the number of time steps the context remains unchanged. applies only when lenght of predefined_context_info is 0 or context_estimator_function is None. Defaults to 2.
        beep_power (int, optional): the maximum memory accessibility when a beep is received in percentage. Defaults to 1.
        urge_max (int, optional): the maximum possible motivation in percentage. Defaults to 1.
        r (float, optional): slope of the urge/motivation regeneration function. Defaults to 0.2.
        b (int, optional): intercept of the urge/motivation regeneration function. Defaults to 0.
        rate (float, optional): decay rate of the exponential function of memory accessibility. Defaults to -0.8.
        salience_decay (float, optional): the amount the beep_power drops each time a beep is received. Defaults to 0.01.
        urge_decay (float, optional): the amount the urge_max drops (increases) each time a beep is received at an inopportune (opportune) moment. Defaults to 0.005.
        randm_beep (bool, optional): to send beeps randomly or not. applies only when context_aware_beep is False. Defaults to False.
        min_c (float, optional): minimum probability of responding to beep given context. applies only when lenght of predefined_context_info is 0 or context_estimator_function is None. Defaults to 0.33.
        context_aware_beep (bool, optional): to send beeps according to the context or not. Defaults to True.
        predefined_times (list, optional): list of predefined beep times. Defaults to [].
        max_c (float, optional): maximum probability of responding to beep given context. applies only when lenght of predefined_context_info is 0 or context_estimator_function is None.. Defaults to 0.7.
        salience_growth_ratio (float, optional): the factor of salience_decay. used to regenerate salience over time. Defaults to 0.0015.
        predefined_context_info (list, optional): probability of responding to a beep given context at predefined times. must be mappable to predefined_times. Defaults to [].
        context_estimator_function (_type_, optional): typically a trained ML model to estimate the probability of responding to a beep give a context. Defaults to None.
        context_reference (_type_, optional): list of predefined context information. must be mappable to predefined_times. must be an acceptable input to context_estimator_function. Defaults to np.array([]).
        context_aware_threshold (float, optional): the minimum acceptable probability of response based on a given context in order to send a beep. Defaults to 0.5.
        use_prefedined_times_to_beep (bool, optional): when True, predefined_times is used. Defaults to True.
        override_inter_notification_steps (int, optional): when set to greater than -1, it will override the calculated inter notification time based on the experiment protocol. Defaults to -1.
        total_beeps (int, optional): when set to greater than -1 and when predefined_times exists, it will determine the inter notification time so the total_beeps is achieved during the experiment period. Defaults to -1.

    Returns:
        _type_: _description_
    """
    time_steps = days * hours_in_day
    inter_notification_steps = math.floor(hours_in_day / beeps_a_day)
    if override_inter_notification_steps > -1:
        inter_notification_steps = override_inter_notification_steps
    if total_beeps > 0 and len(predefined_times) > 0:
        inter_notification_steps = math.floor(
            (predefined_times[-1] - predefined_times[0]) / total_beeps
        )
    beeps = []
    responses = []
    memory_accessibility = []
    urge = []
    context = []
    decay_start_time = 0
    growth_start_time = 0

    memory_accessibility.append(0)
    urge.append(urge_max)
    if len(predefined_context_info) == 0 or context_estimator_function is None:
        context.append(est_context(min_c, max_c))
    else:
        context.append(context_estimator_function([[context_reference[0][2]]])[0][0])

    for t in (
        [x for x in range(predefined_times[0], predefined_times[-1])]
        if len(predefined_times) > 0
        else [x for x in range(time_steps)]
    ):
        # send beep
        if len(predefined_times) > 0 and use_prefedined_times_to_beep:
            if t in predefined_times:
                beep = 1
            else:
                beep = 0
        else:
            if 1 not in beeps[-inter_notification_steps:]:
                if context_aware_beep:
                    beep = int(context[-1] > context_aware_threshold)
                else:
                    beep = send_beep(randm_beep)
            else:
                beep = 0
        beeps.append(beep)
        # update memory accessibility
        if beep == 1:
            decay_start_time = t
            memory_accessibility.append(exp_function(beep_power, rate, 0))
            beep_power -= salience_decay
        else:
            memory_accessibility.append(
                exp_function(beep_power, rate, t - decay_start_time)
            )
        # calculate context
        if len(predefined_context_info) == 0 or context_estimator_function is None:
            if t % context_change_steps == 0:  # to reduce entropy of context
                context.append(est_context(min_c, max_c))
            else:
                context.append(context[-1])
        else:
            current_context_info = None
            if t in predefined_times:
                current_context_info = predefined_context_info[
                    np.where(predefined_times == t)[0][0]
                ]
            else:
                if len(context_reference[context_reference[:, 1] == t]) == 1:
                    current_context_info = context_reference[
                        context_reference[:, 1] == t
                    ][0][2]
            if current_context_info is not None:
                context.append(
                    context_estimator_function([[current_context_info]])[0][0]
                )  # todo p(a|c) or p(c|a)?
            else:
                context.append(context[-1])
        # decide at time t
        response = 0
        if beep == 1:
            a = (
                random.choice([i / 100 for i in range(80, 99)])
                if is_in_fogg_signal_segment(memory_accessibility[-1], urge[-1])
                else random.choice([i / 100 for i in range(1, 10)])
            )
            response = random_with_change(
                chance=int(
                    decide(urge[-1], memory_accessibility[-1], a, 1, context[-1]) * 100
                )
            )
        responses.append(response)
        # update urge
        if beep == 1 and response == 0:  # disturbing beep
            urge_max -= urge_decay
        if beep == 1 and response == 1:  # opportune moment
            urge_max = urge_max + urge_decay if urge_max + urge_decay <= 1 else 1
        if response == 1:
            growth_start_time = t
            urge.append(0)
        else:
            if urge[-1] == urge_max:
                urge.append(urge_max)
            else:
                urge.append(
                    urge_max
                    if linear_function(r, t - growth_start_time, b) > urge_max
                    else linear_function(r, t - growth_start_time, b)
                )
        if beep_power + salience_decay * salience_growth_ratio <= 1:
            beep_power += salience_decay * salience_growth_ratio
    return (
        (
            [x for x in range(predefined_times[0], predefined_times[-1])]
            if len(predefined_times) > 0
            else [x for x in range(time_steps)]
        ),
        memory_accessibility,
        urge,
        beeps,
        responses,
        context,
    )


def plot_sim(x, m, u, b, r, c, annotations={"x": []}):
    """plots the simulation result

    Args:
        x (list): time steps
        m (list): memory accessibility values at each time step
        u (list): urge values at each time step
        b (list): beep values 0 or 1 at each time step
        r (list): response values 0 or 1 at each time step
        c (list): list of P(c|response=1) at each time step
    """
    fig, ax = plt.subplots()
    plt.plot(x, m[:-1], label="MA", color="tab:blue")
    plt.plot(x, u[:-1], label="Urge", color="tab:orange")
    plt.plot(x, c[:-1], label="Context", color="tab:gray", alpha=0.25)
    plt.step(
        x,
        [None if x == 0 else 0 for x in b],  # type: ignore
        ls="",
        marker="x",
        label="Prompt",
        color="tab:red",
    )
    plt.step(
        x,
        [None if x == 0 else 0 for x in r],  # type: ignore
        ls="",
        marker="o",
        label="Decision",
        color="tab:purple",
    )
    for loc in annotations["x"]:
        plt.axvline(x=loc, color="tab:red")
    plt.legend()
    plt.show()


def calc_stats(beeps, responses):
    """generates a statistical report based on input

    Args:
        beeps (list): a list of beeps where each item is 0 or 1
        responses (list): a list of responses where each item is 0 or 1

    Returns:
        dict: all the calculated statistics
    """
    if len(beeps) == 0 or beeps.count(1) == 0:
        ret_val = 0
    else:
        ret_val = responses.count(1) / beeps.count(1)
    return {"response_rate": ret_val}


def gird_search_simulate(params_dict):
    """runs simulations with each item of the product of input parameters

    Args:
        params_dict (dict): keyword arguments

    Raises:
        TypeError: each argument must be a list

    Returns:
        list: list of pairs of parameters and simulation output
    """
    lists = []
    input_output_pairs = []
    for key in params_dict:
        if type(params_dict[key]) is not list:
            raise TypeError
        lists.append(params_dict[key])
    scenarios = itertools.product(*lists)
    for scenario in scenarios:
        named_args = {}
        for index, key in enumerate(list(params_dict.keys())):
            named_args[key] = scenario[index]
        x, m, u, b, r, c = simulate(**named_args)
        input_output_pairs.append(([x, m, u, b, r, c], scenario))
    return input_output_pairs


def get_grid_search_params(params_dict):
    """calculates the product of its input dictionary

    Args:
        params_dict (dict): keyword arguments

    Raises:
        TypeError: each argument must be a list

    Returns:
        list: list of possible input parameters
    """
    lists = []
    inputs = []
    for key in params_dict:
        if type(params_dict[key]) is not list:
            raise TypeError
        lists.append(params_dict[key])
    scenarios = itertools.product(*lists)
    for scenario in scenarios:
        named_args = {}
        for index, key in enumerate(list(params_dict.keys())):
            named_args[key] = scenario[index]
        inputs.append(named_args)
    return inputs


if __name__ == "__main__":
    x, m, u, b, r, c = simulate()
    plot_sim(x, m, u, b, r, c)
