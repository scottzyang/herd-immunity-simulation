class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.


    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        filename = open(self.file_name, 'a')
        filename.write(f'Population size: {pop_size}\nVaccinated Percentage: {vacc_percentage}\nVirus Name: {virus_name}\nMortality Rate: {mortality_rate}\nReproduction Rate: {basic_repro_num}\n\n')
        filename.close()

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        filename = open(self.file_name, 'a')
        filename.write(f'Step number: {step_number}\nInteractions: {number_of_interactions}\nNew Infections: {number_of_new_infections}\n\n')
        filename.close()

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        filename = open(self.file_name, 'a')
        filename.write(f'Step number: {step_number}\nPopulation count: {population_count}\nNew fatalities: {number_of_new_fatalities}')
        filename.close()

    def log_time_step(self, time_step_number):
        filename = open(self.file_name)
        filename.write(f'Step Number:{time_step_number}\n')
        filename.close()

    def final_data(self, survivors, fatalities, vaccinated_pop, interactions, infections, vax_saves):
        filename = open(self.file_name, 'a')
        filename.write(f'Survivors: {survivors}\nFatalities: {fatalities}\nVaccinated Populations: {vaccinated_pop}\nTotal Interactions: {interactions}\nTotal Infections: {infections}\nSaved by Vaccines: {vax_saves}')
        filename.close()
