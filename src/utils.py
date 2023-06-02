import matplotlib

# matplotlib.use(
#     "SVG"
# )  # surpasses UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
import matplotlib.pyplot as plt


def plot_sim(x, m, u, b, r, c, annotations={"x": []}):
    """plots the simulation result

    Args:
        x (list): time steps
        m (list): memory accessibility values at each time step
        u (list): urge values at each time step
        b (list): beep values 0 or 1 at each time step
        r (list): response values 0 or 1 at each time step
        c (list): list of P(c|response=1) at each time step

    Returns:
        tuple: simulation figure and plot
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
    return (fig, plt)


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
