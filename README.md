<p align="center">
  <img alt="SAPPHIRE logo" height="100" src="https://raw.githubusercontent.com/khnshn/sapphire/main/gem.png">
</p>

# SAPPHIRE: SimulAting PrticiPant beHavIoR during Experiments

[![SAPPHIRE version](https://img.shields.io/badge/SAPPHIRE-v0.1.0-blue)](#)
[![license](https://img.shields.io/badge/license-GPL--3.0-green)](#)

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
```

`esm_sim.simulate()` returns:

`x`: x-ticks array, `m`: memory accessibility array, `u`: urge (motivation) array, `b`: beeps array, `r`: responses array, and `c`: context array

_the length of the arrays are equal_

### Creating a custom simulation

The parameters of the simulation can be customized by calling the setter methods of the builder. for example:

```python
builder.set_days(100)
builder.set_random_beep(False)
```

### Getting the parameter values of the simulation

```python
print(esm_sim.get_attrib_value_list())
```

Output (_values below correspond to the default builder_):

```
[('_b', 0), ('_beep_power', 1), ('_beeps_a_day', 5), ('_context_aware_beep', True), ('_context_aware_threshold', 0.5), ('_context_change_steps', 2), ('_context_estimator_function', None), ('_context_reference', array([], dtype=float64)), ('_days', 25), ('_hours_in_day', 12), ('_max_c', 0.7), ('_min_c', 0.33), ('_override_inter_notification_steps', -1), ('_predefined_context_info', []), ('_predefined_times', []), ('_r', 0.2), ('_random_beep', False), ('_rate', -0.8), ('_salience_decay', 0.01), ('_salience_growth_ratio', 0.0015), ('_total_beeps', -1), ('_urge_decay', 0.005), ('_urge_max', 1), ('_use_prefedined_times_to_beep', True), ('decide', <bound method Simulation.decide of <simulation.Simulation object at 0x011D6BC8>>), ('est_context', <bound method Simulation.est_context of <simulation.Simulation object at 0x011D6BC8>>), ('exp_function', <bound method Simulation.exp_function of <simulation.Simulation object at 0x011D6BC8>>), ('get_attrib_value_list', <bound method Simulation.get_attrib_value_list of <simulation.Simulation object at 0x011D6BC8>>), ('is_in_fogg_signal_segment', <bound method Simulation.is_in_fogg_signal_segment of <simulation.Simulation object at 0x011D6BC8>>), ('linear_function', <bound method Simulation.linear_function of <simulation.Simulation object at 0x011D6BC8>>), ('random_with_change', <bound method Simulation.random_with_change of <simulation.Simulation object at 0x011D6BC8>>), ('send_beep', <bound method Simulation.send_beep of <simulation.Simulation object at 0x011D6BC8>>), ('simulate', <bound method Simulation.simulate of <simulation.Simulation object at 0x011D6BC8>>)]
```

### Plotting the simulation output

```python
import utils

fig, plt = utils.plot_sim(x, m, u, b, r, c)
plt.show()
```

An example output plot of the simulaiton:
<br/>
<img alt="SAPPHIRE example" height="350" src="https://raw.githubusercontent.com/khnshn/sapphire/main/example.png">
<br/>

### Simulation parameters

| **Parameter**                     | **Type**             | **Description**                                                                                                                                                        | Default      |
| --------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| days                              | (int; optional)      | the experiment period as the number of days                                                                                                                            | 25           |
| hours_in_day                      | (int; optional)      | the total hours in a day that a beeps are allowed                                                                                                                      | 12           |
| beeps_a_day                       | (int; optional)      | the (maximum) number of allowed beeps per day                                                                                                                          | 5            |
| context_change_steps              | (int; optional)      | the number of time steps the context remains unchanged. applies only when lenght of predefined_context_info is 0 or context_estimator_function is None                 | 2            |
| beep_power                        | (float; optional)    | the maximum memory accessibility when a beep is received in percentage                                                                                                 | 1            |
| urge_max                          | (float; optional)    | the maximum possible motivation in percentage                                                                                                                          | 1            |
| r                                 | (float; optional)    | slope of the urge/motivation regeneration function                                                                                                                     | 0.2          |
| b                                 | (float; optional)    | intercept of the urge/motivation regeneration function                                                                                                                 | 0            |
| rate                              | (float; optional)    | decay rate of the exponential function of memory accessibility                                                                                                         | -0.8         |
| salience_decay                    | (float; optional)    | the amount the beep_power drops each time a beep is received                                                                                                           | 0.01         |
| urge_decay                        | (float; optional)    | the amount the urge_max drops (increases) each time a beep is received at an inopportune (opportune) moment                                                            | 0.005        |
| randm_beep                        | (bool; optional)     | to send beeps randomly or not. applies only when context_aware_beep is False                                                                                           | False        |
| min_c                             | (float; optional)    | minimum probability of responding to beep given context. applies only when lenght of predefined_context_info is 0 or context_estimator_function is None                | 0.33         |
| context_aware_beep                | (bool; optional)     | to send beeps according to the context or not                                                                                                                          | True         |
| predefined_times                  | (list; optional)     | list of predefined beep times                                                                                                                                          | []           |
| max_c                             | (float; optional)    | maximum probability of responding to beep given context. applies only when lenght of predefined_context_info is 0 or context_estimator_function is None.               | 0.7          |
| salience_growth_ratio             | (float; optional)    | the factor of salience_decay. used to regenerate salience over time                                                                                                    | 0.0015       |
| predefined_context_info           | (list; optional)     | probability of responding to a beep given context at predefined times. must be mappable to predefined_times                                                            | []           |
| context_estimator_function        | (Any; optional)      | typically a trained ML model to estimate the probability of responding to a beep give a context                                                                        | None         |
| context_reference                 | (np.array; optional) | list of predefined context information. must be mappable to predefined_times. must be an acceptable input to context_estimator_function                                | np.array([]) |
| context_aware_threshold           | (float; optional)    | the minimum acceptable probability of response based on a given context in order to send a beep                                                                        | 0.5          |
| use_prefedined_times_to_beep      | (bool; optional)     | when True predefined_times is used                                                                                                                                     | True         |
| override_inter_notification_steps | (int; optional)      | when set to greater than -1 it will override the calculated inter notification time based on the experiment protocol                                                   | -1           |
| total_beeps                       | (int; optional)      | when set to greater than -1 and when predefined_times exists it will determine the inter notification time so the total_beeps is achieved during the experiment period | -1           |

### Publications

- Alireza Khanshan, Pieter Van Gorp, and Panos Markopoulos. 2023. **Simulating Participant Behavior in Experience Sampling Method Research**. _In Extended Abstracts of the 2023 CHI Conference on Human Factors in Computing Systems (CHI EA '23). Association for Computing Machinery, New York, NY, USA, Article 250, 1–7._ https://doi.org/10.1145/3544549.3585586
