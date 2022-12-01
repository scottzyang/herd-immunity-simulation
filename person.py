import random
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        # define attributes for person class
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_infected = False
        self.is_alive = True

    def did_survive_infection(self):
        # Generate random number to determine survivability chance of infected person
        if self.infection is not None:
            self.is_infected = True
            survival_chance = random.uniform(0, 1)
            # print(survival_chance)
            if survival_chance < self.infection.mortality_rate:
                self.is_vaccinated = False
                self.is_alive = False
                return self.is_alive
            else:
                self.is_vaccinated = True
                return self.is_alive
        # logic for non-infected person        
        else:
            self.is_infected = False
            return self.is_alive


if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class
    # TODO Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)

    print('----------------------')
    print(unvaccinated_person._id)
    print(unvaccinated_person.is_vaccinated)
    print(unvaccinated_person.infection)
    print('----------------------')

    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)

    # verify attributes of person instance
    assert infected_person._id == 3
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is not None
    assert infected_person.is_alive is True or False
    print(f'Is alive: {infected_person.did_survive_infection()}')

    # create pool of unvaccinated 100 people
    people = []
    for i in range(1, 100):
        infected = Person(i, False, virus)
        people.append(infected)

    # evaluate if person has survived and increment corresponding values
    survived = 0
    did_not_survive = 0
    for person in people:
        if person.did_survive_infection():
            survived += 1
        else: 
            did_not_survive += 1
    
    print('----------------------')
    print(f'Survived: {survived}')
    print(f'Deaths: {did_not_survive}')

    # create pool of 100 uninfected people
    uninfected_people = []

    for i in range(1, 100):
        uninfected = Person(i, False)
        uninfected_people.append(uninfected)


    # generate random number to evalute infection count in pool of 100 people
    got_infected = 0
    immune = 0

    for person in uninfected_people:
        immunity = random.uniform(0, 1)
        if immunity < virus.repro_rate:
            person.infection = virus
            got_infected += 1
        else:
            immune += 1

    print('----------------------')
    print(f'Infected: {got_infected}')
    print(f'Immune: {immune}')
    print('----------------------')



    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.