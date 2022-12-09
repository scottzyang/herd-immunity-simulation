class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    # two additional tests
    virus2 = Virus("COVID", 1.0, 0.25)
    assert virus2.name == "COVID"
    assert virus2.repro_rate == 1.0
    assert virus2.mortality_rate == 0.25

    virus3 = Virus("H1N1", 0.2, 0.4)
    assert virus3.name == "H1N1"
    assert virus3.repro_rate == 0.2
    assert virus3.mortality_rate == 0.4
