<p align="center">
  <img alt="SAPPHIRE logo" height="100" src="https://raw.githubusercontent.com/khnshn/sapphire/main/gem.png">
</p>

# SAPPHIRE: SimulAting PrticiPant beHavIoR during Experiments

## Instructions

### Running the default simulation

```python
import simulation as sim

director = sim.Director()
builder = sim.ConcreteBuilder()
director.builder = builder
director.build_default_simulation()
esm_sim = builder.simulation
x, m, u, b, r, c = esm_sim.simulate()
plot_sim(x, m, u, b, r, c)
```

### Simulation parameters


### Creating a custom simulation

The parameters of the simulation can be customized by calling the builder setter methods.

```python
builder.set_days(100)
builder.set_random_beep(False)
```

### Getting the parameter values of the default simulation
```python
print(esm_sim.get_attrib_value_list())
```

### Plotting the simulation output
```python
import utils

utils.plot_sim(x, m, u, b, r, c)
```
An example output plot of the simulaiton:
<br/>
<img alt="SAPPHIRE example" height="350" src="https://raw.githubusercontent.com/khnshn/sapphire/main/example.png">
<br/>