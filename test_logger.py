from logger import Logger

def test_logs():
  logger = Logger('test_logger_results.txt')
  logger.write_metadata(1200, 0.12, 'Ebola', 0.3, 0.14)
  logger.log_interactions(4, 500, 35)
  logger.final_data(320, 86, 60, 320, 5000, 234, 6000)
  filename = open(logger.file_name)

  assert filename.read() == '''Population size: 1200
Vaccinated Percentage: 0.12
Virus Name: Ebola
Mortality Rate: 0.3
Reproduction Rate: 0.14

Step number: 4
Interactions: 500
New Infections: 35

Survivors: 320
Fatalities: 86
Final population Infected: 60
Vaccinated Populations: 320
Total Interactions: 5000
Total Infections: 234
Saved by Vaccines: 6000'''

  
  
  