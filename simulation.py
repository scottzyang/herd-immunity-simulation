import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus
import argparse


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger('simulation.txt')
        self.vacc_percentage = vacc_percentage
        self.virus = virus
        self.pop_size = pop_size
        self.society = self._create_population(vacc_percentage, initial_infected)
        self.newly_infected = []
        self.time_step_number = 0
        self.interactions = 0
        self.number_new_infections = 0
        self.final_infections = 0
        self.final_survivors = 0
        self.total_vax = 0
        self.fatalities = 0
        self.vax_saves = 0

    def _create_population(self, vacc_percentage, initial_infected):
        vaccinate_pop = int(round(self.pop_size * vacc_percentage))
        print(f'Current Vax Pop: {vaccinate_pop}')
        total_population = []

        # create population based on initial infected and vaccinated population
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
        # Return the list of people
        return total_population

    def _simulation_should_continue(self):
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
        # continue the simulation if there are still unvaxxed alive folks
        should_continue = True
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        while should_continue:
            # TODO: Increment the time_step_counter
            self.time_step_number += 1
            print(f'Current Time Step: {self.time_step_number}')
            self.time_step()
            self.logger.log_interactions(self.time_step_number, self.interactions, self.number_new_infections)
            should_continue = self._simulation_should_continue()

        # total infections
        for person in self.society:
            if person.infection is not None:
                self.final_infections += 1

        # determine final numbers
        for person in self.society:
            if person.is_vaccinated:
                self.total_vax += 1
                self.final_survivors += 1
            elif not person.is_alive:
                self.fatalities += 1
            
        self.logger.final_data(self.final_survivors, self.fatalities, self.final_infections, self.total_vax, self.interactions, self.number_new_infections, self.vax_saves)
        

    def time_step(self):
        '''
            if society is greater than 100, generate randome sample of 100
            else, if less than 100 the random group will be the same as society length

            Make sick people interact with 100 randomly selected people
        '''

        alive_people = [person for person in self.society if person.is_alive]

        if len(self.society) > 100:
            random_group = random.sample(alive_people, k=100)
        else: 
            random_group = alive_people

        # populate a list of sick people if their infection attribute is a virus
        sick_people = [person for person in self.society if person.infection is not None]

        # sick person interacts with random person
        for sick_person in sick_people:
            for random_person in random_group:
                self.interaction(sick_person, random_person)
                self.interactions += 1

        self._infect_newly_infected()

        # determine if the person survived the infection
        for person in self.society:
            if person.did_survive_infection():
                self.vax_saves += 1
            
            
        

    def interaction(self, infected_person, random_person):
        # if random person is not infected and unvaxxed
        if random_person.infection is None and not random_person.is_vaccinated:
            chance = random.random()
            if chance < self.virus.repro_rate:
                self.newly_infected.append(random_person)

    # change infection attribute of person if they were infected
    def _infect_newly_infected(self):
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