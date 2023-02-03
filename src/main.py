import simulation as sim
import utils


if __name__ == "__main__":
    director = sim.Director()
    builder = sim.ConcreteBuilder()
    director.builder = builder
    print("default sim")
    director.build_default_simulation()
    # print("customize sim")
    # builder.set_days(100)
    # builder.set_random_beep(False)
    esm_sim = builder.simulation
    print(esm_sim.get_attrib_value_list())
    x, m, u, b, r, c = esm_sim.simulate()
    utils.plot_sim(x, m, u, b, r, c)

    # print("custom sim")
    # builder.set_days(100)
    # builder.set_random_beep(False)
