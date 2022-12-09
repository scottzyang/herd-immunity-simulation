import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus
import argparse


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger('simulation.txt')
        self.vacc_percentage = vacc_percentage
        # TODO: Store the virus in an attribute
        self.virus = virus
        self.pop_size = pop_size
        self.society = self._create_population(vacc_percentage, initial_infected)
        self.newly_infected = []
        self.time_step_number = 0
        self.interactions = 0
        self.number_new_infections = 0

        # TODO: Store pop_size in an attribute
        # TODO: Store the vacc_percentage in a variable
        # TODO: Store initial_infected in a variable
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        # TODO: Call self._create_population() and pass in the correct parameters.

    def _create_population(self, vacc_percentage, initial_infected):
        # TODO: Create a list of people (Person instances). This list 
        # should have a total number of people equal to the pop_size. 
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        vaccinate_pop = int(round(self.pop_size * vacc_percentage))
        print(f'Current Vax Pop: {vaccinate_pop}')
        total_population = []
        for i in range(int(self.pop_size)):
            if initial_infected > 0:
                total_population.append(Person(i, False, self.virus))
                initial_infected -= 1
            elif vaccinate_pop > 0: 
                # virus parameter defaults to None
                total_population.append(Person(i, True))
                vaccinate_pop -= 1
            else: 
                total_population.append(Person(i, False))
        # # TODO: Return the list of people
        return total_population

    def _simulation_should_continue(self):
        # This method will return a boolean indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # TODO: Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.

        ''' 
        loop through the entire population, if they are dead add them to the dead count.
        Compare dead count to initial population, if they are equal end sim.
        else, continue sim. 
        '''
        vax_counter = 0
        dead_counter = 0
        counter = 0
        for person in self.society:
            # if person is alive and not vaccinated add to counter
            if person.is_alive and not person.is_vaccinated:
                counter += 1
            elif person.is_alive and person.is_vaccinated:
                vax_counter += 1
            elif not person.is_alive:
                dead_counter += 1
        
        print(f'Current Vax: {vax_counter}\nCurrent Deaths: {dead_counter}\nStill Alive & Unvax: {counter}\n')
        
        # if counter is above 0, then sim should stop.
        if counter > 0:
            return True
        else:
            return False

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 
        should_continue = True

        while should_continue:
            # TODO: Increment the time_step_counter
            self.time_step_number += 1
            print(f'Current Time Step: {self.time_step_number}')
            self.time_step()
            should_continue = self._simulation_should_continue()
            # TODO: for every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        #def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        # self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 
        

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person

        '''
            if society is greater than 100, generate randome sample of 100
            else, if less than 100 the random group will be the same as society length
        '''

        alive_people = [person for person in self.society if person.is_alive]

        if len(self.society) > 100:
            random_group = random.sample(alive_people, k=100)
        else: 
            random_group = alive_people

        sick_people = [person for person in self.society if person.infection is not None]

        for sick_person in sick_people:
            for random_person in random_group:
                self.interaction(sick_person, random_person)
                self.interactions += 1

        self._infect_newly_infected()

        for person in self.society:
            person.did_survive_infection()
        

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
        
        # if random person is not infected and unvaxxed
        if random_person.infection is None and not random_person.is_vaccinated:
            chance = random.random()
            if chance < self.virus.repro_rate:
                self.newly_infected.append(random_person)
        # if random person is not vaxxed and not infected
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in self.newly_infected:
            person.infection = self.virus
            self.number_new_infections += 1
        

        self.newly_infected = []



if __name__ == "__main__":
    # Test your simulation here
    parser = argparse.ArgumentParser(description='simulates viral infection in population')
    # virus argument
    parser.add_argument('virus_name', metavar='virus_name', type=str, help='Add virus name')
    parser.add_argument('repro_num', metavar='repro_num', type=float, help='Add reproduction rate')
    parser.add_argument('mortality_rate', metavar='mortality_rate', type=float, help='Add mortality rate')
    parser.add_argument('pop_size', metavar='pop_size', type=int, help='Add population')
    parser.add_argument('vacc_percentage', metavar='vacc_percentage', type=float, help='Add vaccination percentage')
    parser.add_argument('initial_infected', metavar='initial_infected', type=int, help='Add initial infected')
    args = parser.parse_args()

    virus_name = args.virus_name
    repro_num = args.repro_num
    mortality_rate = args.mortality_rate
    pop_size = args.pop_size
    vacc_percentage = args.vacc_percentage
    initial_infected = args.initial_infected

    # virus_name = "Sniffles"
    # repro_num = 0.5
    # mortality_rate = 0.12
    # virus = Virus(virus_name, repro_num, mortality_rate)

    # # # Set some values used by the simulation
    # pop_size = 200
    # vacc_percentage = 0.1
    # initial_infected = 6

    # # Make a new instance of the imulation
    virus = Virus(virus_name, pop_size, vacc_percentage)
    #def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    # assert len(sim.society) == pop_size
    
    # vacc_counter = 0
    # for person in sim.society:
    #     if person.is_vaccinated:
    #         vacc_counter += 1
    
    # for person in sim.society:
    #     person.is_vaccinated = True

    # print(sim._simulation_should_continue())

    sim.run()