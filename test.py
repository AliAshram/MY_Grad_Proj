import traci
import sumolib
import os 
import matplotlib.pyplot as plt
import numpy as np
sumo_config = os.path.join("Intersection","Enviroment.sumocfg")


# Start SUMO with TraCI
sumo_binary = sumolib.checkBinary('sumo-gui')
traci.start([sumo_binary, "-c", sumo_config])
def main():
    maxStep = 5400
    step = 0
    queue_length = 0
    queue_length_episod = []
    rand_plot = []
    while step < maxStep :
        traci.simulationStep()
        step +=1 
        queue_length =_get_queue_length()
        queue_length_episod.append(queue_length)
    print(max(queue_length_episod))
    plot(queue_length_episod)
    save_txt_data(queue_length_episod)

def _get_queue_length():
    halt_N = traci.edge.getLastStepHaltingNumber("N2TL")
    halt_W = traci.edge.getLastStepHaltingNumber("W2TL")
    halt_S = traci.edge.getLastStepHaltingNumber("S2TL")
    halt_E = traci.edge.getLastStepHaltingNumber("E2TL")
    queue_length = halt_N + halt_E + halt_S + halt_W
    return queue_length
def plot(data):

    plt.figure(figsize=(8, 6))  # Set figure size
    plt.plot(data,"-")
    plt.ylabel('Queue length')
    plt.xlabel('Steps')
    plt.margins(0)
    plt.savefig("noAI/ali.png")
    #plt.ylim(min_val - 0.05 * abs(min_val), max_val + 0.05 * abs(max_val))
    
def save_txt_data(data):
     with open("noAI/ali.txt", "w") as file:
            for value in data:
                    file.write("%s\n" % value)

def read_txt (path):
     with open(path, "r") as file:
        lines = [line.strip() for line in file] 
        print(lines)
        return lines

main()