class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        filename = open(self.file_name, 'w')
        filename.write(f'Population size: {pop_size}\nVaccinated Percentage: {vacc_percentage}\nVirus Name: {virus_name}\nMortality Rate: {mortality_rate}\nReproduction Rate: {basic_repro_num}\n\n')
        filename.close()

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        filename = open(self.file_name, 'a')
        filename.write(f'Step number: {step_number}\nInteractions: {number_of_interactions}\nNew Infections: {number_of_new_infections}\n\n')
        filename.close()

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        filename = open(self.file_name, 'a')
        filename.write(f'Step number: {step_number}\nPopulation count: {population_count}\nNew fatalities: {number_of_new_fatalities}')
        filename.close()

    def log_time_step(self, time_step_number):
        filename = open(self.file_name)
        filename.write(f'Step Number:{time_step_number}\n')
        filename.close()

    def final_data(self, survivors, fatalities, final_infections, vaccinated_pop, interactions, infections, vax_saves):
        filename = open(self.file_name, 'a')
        filename.write(f'Survivors: {survivors}\nFatalities: {fatalities}\nFinal population Infected: {final_infections}\nVaccinated Populations: {vaccinated_pop}\nTotal Interactions: {interactions}\nTotal Infections: {infections}\nSaved by Vaccines: {vax_saves}')
        filename.close()
