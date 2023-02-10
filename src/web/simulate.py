import sys

sys.path.append("../")
import simulation as sim
import utils
import io
import base64


def simulate_base():
    director = sim.Director()
    builder = sim.ConcreteBuilder()
    director.builder = builder
    director.build_default_simulation()
    esm_sim = builder.simulation
    return esm_sim.simulate()


def simulate_get_base64():
    x, m, u, b, r, c = simulate_base()
    fig, plt = utils.plot_sim(x, m, u, b, r, c)
    plt_bytes = io.BytesIO()
    plt.savefig(plt_bytes, format="png")
    plt_bytes.seek(0)
    return base64.b64encode(plt_bytes.read()).decode()


def simulate_get_data():
    x, m, u, b, r, c = simulate_base()
    return (x, m)


def get_simulation_params():
    director = sim.Director()
    builder = sim.ConcreteBuilder()
    director.builder = builder
    print("default sim")
    director.build_default_simulation()
    esm_sim = builder.simulation
    return esm_sim.get_attrib_value_list()
