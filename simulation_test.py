import pytest 
from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation

def simulation_test():
  sim = Simulation('Ebola', 1200, 0.1, 12)
  assert len(sim.society) == sim.pop_size
  assert sim.virus.name == 'Ebola'
  assert sim.vacc_percentage == 0.1

def virus_test():
    virus = Virus("COVID", 1.0, 0.25)
    assert virus.name == "COVID"
    assert virus.repro_rate == 1.0
    assert virus.mortality_rate == 0.25