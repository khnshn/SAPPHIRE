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
    return clean_for_chartjs(x, m, u, b, r, c)


def clean_for_chartjs(x, m, u, b, r, c):
    return (
        x,
        m,
        u,
        [0 if i == 1 else None for i in b],
        [0 if i == 1 else None for i in r],
        c,
    )


def simulate_custom_get_data(params, upload_data):
    director = sim.Director()
    builder = sim.ConcreteBuilder()
    director.builder = builder
    #
    # builder.set_days(100)
    n_participants = int(params[0][1])
    if "beep_times" in upload_data.keys():
        n_participants = set(upload_data["beep_times"][:, 0])
    params.remove(
        params[0]
    )  # remove the number of participants for it is not among the setters
    X = []
    M = []
    U = []
    B = []
    R = []
    C = []
    for n in range(n_participants):
        director.build_default_simulation()
        for p in params:
            setter = getattr(builder, "set_" + p[0].replace("-", "_"))
            setter(p[1])
        if (
            0 < len(upload_data) < 4
        ):  # hard coded for now, referring to the 4 required files
            raise ValueError(
                "Incorrect number of files are uploaded: {}".format(
                    ",".join(upload_data.keys())
                )
            )
        else:
            for key in upload_data.keys():
                setter = getattr(builder, "set_" + key.replace("-", "_"))
                setter(upload_data[key])
        esm_sim = builder.simulation
        x, m, u, b, r, c = esm_sim.simulate()
        X.append(x)
        M.append(m)
        U.append(u)
        B.append(b)
        R.append(r)
        C.append(c)
    return (clean_for_chartjs(x, m, u, b, r, c), (X, M, U, B, R, C))


def get_simulation_params():
    director = sim.Director()
    builder = sim.ConcreteBuilder()
    director.builder = builder
    print("default sim")
    director.build_default_simulation()
    esm_sim = builder.simulation
    return esm_sim.get_attrib_value_list()
