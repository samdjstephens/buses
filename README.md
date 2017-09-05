# Buses

The project has two goals:
1. To validate a hypothesis about why buses always seem to come in clusters (i.e. you wait a long time for the bus and then 2 turn up at the same time). This is elaborated below.
2. To write a event-loop based system from scratch to better understand their workings

# Hypothesis

This simulation is designed to test the idea that buses will naturally come together as a result of passengers waiting at bus stops and then boarding buses. The basic idea is as follows:

As a bus travels its route, it picks up passengers. Once the passengers have boarded this bus, there will temporarily be fewer (or zero) passengers waiting for the next bus. If the second bus happens to be close enough behind the first that the number of passengers has not replenished to the same amount then this bus will likely take less time at the bus stop. If noone arrived, it may even skip the bus stop altogether. The closer the buses are to eachother, the stronger the effect, so over time we expect buses to become clustered together.

# Simulation

### Assumptions
To explicitly list the simplifying assumptions made:

1. Bus stops "refill" with passengers at a random rate
1. Every bus stop is equally busy in the sense that the mean time between passengers arriving is the same at all stops
1. Each additional passenger boarding the bus increases the time the bus is waiting at the bus stop. Specifically, the time goes up linearly with the number of passengers waiting
1. Buses move at constant speed between bus stops
1. Buses have no maximum capacity
1. Bus passengers never get off the bus
1. The bus route is circular
1. The buses starting on the route stay on the route permanently and no new buses join

### Time steps
The simulation is run in discrete time steps. At each time step the following things can happen:
1. A bus can travel one unit of distance between bus stops.
2. A bus can load one passenger
3. A passenger can arrive at a bus stop (this is a random event, with the time between two passengers arriving drawn from a poisson distribution)

# Results
Setup: A circular route with 2 bus stops separated on one side by 1000 units and on the other by 800 units. Each stop starts with 0 - 2 passengers (randomly chosen) and, on average, a new passenger arrives every 100 time steps. The two buses are placed randomly on the route.

### Bus separation distance (units) vs. Time (time steps)
![Separation over time](https://user-images.githubusercontent.com/5969393/30070633-fa08f3b4-925b-11e7-8843-387cadc87c57.png)

### Analysis
- Firstly, this plot clearly shows the separation distance between the two buses is closing over time
- The rate that the distances closes increases with time (shown by the gradient getting steeper)
- For the first 30K time steps, there is a regular pattern in which the distance temporarily increases before "resetting" then temporarily decreases and resets. Given the buses are, at this point, around 800 units apart and that this is one of the distances between the two bus stops, it is assumed that the up-spikes are caused by the trailing bus stopping for passengers just before the leading bus and visa-versa for the down-spikes. The up-spike, down-spike effect disappears after 30K time steps, presumably because the times at which the buses are at bus stops are no longer co-occurring. To validate these assumptions we could increase the resolution for the early time steps and overlay a graphic showing when the buses are stopped.
- The time it takes for the buses to come together is quite slow. 100K time steps represents ~50 circuits for a bus. This is probably down to the relative time taken for different actions: particularly the small amount of time taken to load passengers (1 per time step) compared to time travelling. To calibrate this better, a greater understanding of the dynamics of the system over time would be instructive - e.g. a plot of number of passengers at bus stop A over time.
