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

| **Parameter**                     | **Type**             | **Description**                                                                                                                                                        | Default       |
|-----------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| days                              | (int; optional)      | the experiment period as the number of days                                                                                                                            | 25            |
| hours_in_day                      | (int; optional)      | the total hours in a day that a beeps are allowed                                                                                                                      | 12            |
| beeps_a_day                       | (int; optional)      | the (maximum) number of allowed beeps per day                                                                                                                          | 5             |
| context_change_steps              | (int; optional)      | the number of time steps the context remains unchanged. applies only when lenght of predefined_context_info is 0 or context_estimator_function is None                 | 2             |
| beep_power                        | (int; optional)      | the maximum memory accessibility when a beep is received in percentage                                                                                                 | 1             |
| urge_max                          | (int; optional)      | the maximum possible motivation in percentage                                                                                                                          | 1             |
| r                                 | (float; optional)    | slope of the urge/motivation regeneration function                                                                                                                     | 0.2.          |
| b                                 | (int; optional)      | intercept of the urge/motivation regeneration function                                                                                                                 | 0             |
| rate                              | (float; optional)    | decay rate of the exponential function of memory accessibility                                                                                                         | -0.8.         |
| salience_decay                    | (float; optional)    | the amount the beep_power drops each time a beep is received                                                                                                           | 0.01.         |
| urge_decay                        | (float; optional)    | the amount the urge_max drops (increases) each time a beep is received at an inopportune (opportune) moment                                                            | 0.005.        |
| randm_beep                        | (bool; optional)     | to send beeps randomly or not. applies only when context_aware_beep is False                                                                                           | False.        |
| min_c                             | (float; optional)    | minimum probability of responding to beep given context. applies only when lenght of predefined_context_info is 0 or context_estimator_function is None                | 0.33.         |
| context_aware_beep                | (bool; optional)     | to send beeps according to the context or not                                                                                                                          | True.         |
| predefined_times                  | (list; optional)     | list of predefined beep times                                                                                                                                          | [].           |
| max_c                             | (float; optional)    | maximum probability of responding to beep given context. applies only when lenght of predefined_context_info is 0 or context_estimator_function is None.               | 0.7.          |
| salience_growth_ratio             | (float; optional)    | the factor of salience_decay. used to regenerate salience over time                                                                                                    | 0.0015.       |
| predefined_context_info           | (list; optional)     | probability of responding to a beep given context at predefined times. must be mappable to predefined_times                                                            | [].           |
| context_estimator_function        | (Any; optional)      | typically a trained ML model to estimate the probability of responding to a beep give a context                                                                        | None.         |
| context_reference                 | (np.array; optional) | list of predefined context information. must be mappable to predefined_times. must be an acceptable input to context_estimator_function                                | np.array([]). |
| context_aware_threshold           | (float; optional)    | the minimum acceptable probability of response based on a given context in order to send a beep                                                                        | 0.5.          |
| use_prefedined_times_to_beep      | (bool; optional)     | when True predefined_times is used                                                                                                                                     | True.         |
| override_inter_notification_steps | (int; optional)      | when set to greater than -1 it will override the calculated inter notification time based on the experiment protocol                                                   | -1            |
| total_beeps                       | (int; optional)      | when set to greater than -1 and when predefined_times exists it will determine the inter notification time so the total_beeps is achieved during the experiment period | -1            |

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