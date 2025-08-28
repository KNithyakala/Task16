from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class PopulationPage:
    def __init__(self, driver):
        self.driver = driver
        self.population_xpath = "//div[@class='counter-ticker is-size-2-mobile']"

    def open(self):
        self.driver.get("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")

    def populationcount(self):
        wait=WebDriverWait(self.driver,10)
        population = wait.until(ec.presence_of_element_located((By.XPATH, self.population_xpath)))
        return population.text.strip()