from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation

def test_simulation():
  virus = Virus('Ebola', 0.2, 0.12)
  sim = Simulation(virus, 1200, 0.1, 12)
  assert len(sim.society) == sim.pop_size
  assert sim.virus.name == 'Ebola'
  assert sim.vacc_percentage == 0.1

def test_virus():
    virus = Virus("COVID", 1.0, 0.25)
    assert virus.name == "COVID"
    assert virus.repro_rate == 1.0
    assert virus.mortality_rate == 0.25