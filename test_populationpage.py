import time
import signal
import sys,os
import pytest

sys.path.append(os.path.dirname(os.path.abspath("D:/Workspace/PAT/Task16")))
from Task16.pages.populationpage import PopulationPage

#Initialising stop=False
stop = False

#This function is triggered when Ctrl+C is pressed
#sig = SIGINT(2), frame= Where Ctrl+C is pressed
#It is changes Stop=True so that program will stop

def signal_handler(sig,frame):
    #making stop as global variable
    global stop
    print("\nCTRL+C pressed! Stop!")
    stop = True

@pytest.mark.usefixtures("driversetup")
class TestPopulation:
    def test_population(self,driversetup):
        #creating instance PopulationPage class
        population_page = PopulationPage(driver=driversetup)
        population_page.open()
        print("\n Live population count (Press CTRL+C to stop):\n")

        # while loop - is to get the value until stop_script =False
        while not stop:
            population = population_page.populationcount()
            print("Population count:", population)

            # Call the signal_handler function once Ctrl+C is pressed.
            signal.signal(signal.SIGINT, signal_handler)
            time.sleep(1)