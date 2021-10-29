#!/usr/bin/env python
# Joahannes B. D. da Costa <joahannes@lrc.ic.unicamp.br>

from __future__ import division

import os
import sys
import subprocess
import logging
import tempfile
import time
import numpy as np

from optparse import OptionParser

# VCC
import sumo_manager
import cluster_manager

import allocation_manager
import task_manager
import log_manager

import traci
import json

def run_clustering(step, number_of_tasks, radius, resource, weight):

	radius = radius / 1000 # for dbscan
	delta_resource = resource # 1, 2, 3, 4
	delta_weight = weight # 1, 5, 10, 15, 20, 25, 50, 100, 200, 300

	vehicles_list = traci.vehicle.getIDList()

	log_manager.get_informations(radius, delta_resource, delta_weight) # for log
	
	# clustering
	cluster_manager.prepare_nodes(vehicles_list, delta_resource, delta_weight, radius, number_of_tasks, step)
			  
def run(network, begin, end, interval, radius, resource, weight):
	logging.debug("Building scenario")	
	logging.debug("Running simulation now")   

	step = 1

	logging.debug("Generating tasks")
	tasks = task_manager.load_number_of_tasks()
	task_index = 0

	# interval in seconds
	logging.debug("Clustering interval: %d" % interval)

	while step == 1 or traci.simulation.getMinExpectedNumber() > 0:
		logging.debug("Minimum expected number of vehicles: %d" % traci.simulation.getMinExpectedNumber())
		traci.simulationStep()
		logging.debug("Simulation time %d" % step)

		# print("Step:", step)
		number_of_tasks = tasks[0]

		if step % interval == 0:
			# begin
			if step >= begin:
				print ("\n*** [DEBUG]:",step)
				tasks.pop(0) # remove numero de tarefa ja usado
				run_clustering(step, number_of_tasks, radius, resource, weight)

		# finish
		if step > end:
			break

		step += 1
	
	time.sleep(10)
	logging.debug("Simulation finished")
	traci.close()
	sys.stdout.flush()
	time.sleep(10)
		
def start_simulation(sumo, scenario, network, begin, end, interval, output, summary, radius, resource, weight):
	logging.debug("Finding unused port")
	
	unused_port_lock = sumo_manager.UnusedPortLock()
	unused_port_lock.__enter__()
	remote_port = sumo_manager.find_unused_port()
	
	logging.debug("Port %d was found" % remote_port)
	
	logging.debug("Starting SUMO as a server")
	
	sumo = subprocess.Popen([sumo, "-c", scenario, "--tripinfo-output", output, "--device.emissions.probability", "1.0", "--summary-output", summary ,"--remote-port", str(remote_port)], stdout=sys.stdout, stderr=sys.stderr)    
	unused_port_lock.release()
			
	try:     
		traci.init(remote_port)    
		run(network, begin, end, interval, radius, resource, weight)
	except:
		logging.exception("Something bad happened")
	finally:
		logging.exception("Terminating SUMO")  
		sumo_manager.terminate_sumo(sumo)
		unused_port_lock.__exit__()
		
def main():
	# Option handling
	parser = OptionParser()
	parser.add_option("-c", "--command", dest="command", default="sumo", help="The command used to run SUMO [default: %default]", metavar="COMMAND")
	parser.add_option("-s", "--scenario", dest="scenario", default="cologne.sumo.cfg", help="A SUMO configuration file [default: %default]", metavar="FILE")
	parser.add_option("-n", "--network", dest="network", default="network.net.xml", help="A SUMO network definition file [default: %default]", metavar="FILE")    
	parser.add_option("-b", "--begin", dest="begin", type="int", default=0, action="store", help="The simulation time (s) at which the re-routing begins [default: %default]", metavar="BEGIN")
	parser.add_option("-e", "--end", dest="end", type="int", default=10800, action="store", help="The simulation time (s) at which the re-routing ends [default: %default]", metavar="END")
	parser.add_option("-i", "--interval", dest="interval", type="int", default=30, action="store", help="The interval (s) of classification [default: %default]", metavar="INTERVAL")
	parser.add_option("-o", "--output", dest="output", default="reroute.xml", help="The XML file at which the output must be written [default: %default]", metavar="FILE")
	parser.add_option("-l", "--logfile", dest="logfile", default=os.path.join(tempfile.gettempdir(), "sumo-launchd.log"), help="log messages to logfile [default: %default]", metavar="FILE")
	parser.add_option("-m", "--summary", dest="summary", default="summary.xml", help="The XML file at which the summary output must be written [default: %default]", metavar="FILE")
	# parser.add_option("-r", "--route-log", dest="route_log", default="route-log.txt", help="Log of the entire route of each vehicle [default: %default]", metavar="FILE")

	# for VCC
	parser.add_option("-t", "--radius", dest="radius", type="int", default=100, action="store", help="Transmission range [default: %default]", metavar="RADIUS")
	parser.add_option("-r", "--resource", dest="resource", type="int", default=1, action="store", help="Resource for each vehicle [default: %default]", metavar="RESOURCE")
	parser.add_option("-w", "--weight", dest="weight", type="int", default=1, action="store", help="Avg weight for each task [default: %default]", metavar="WEIGHT")

	(options, args) = parser.parse_args()
	
	logging.basicConfig(filename=options.logfile, level=logging.DEBUG)
	logging.debug("Logging to %s" % options.logfile)
	
	if args:
		logging.warning("Superfluous command line arguments: \"%s\"" % " ".join(args))
		
	start_simulation(options.command, options.scenario, options.network, options.begin, options.end, options.interval, options.output, options.summary, options.radius, options.resource, options.weight)

if __name__ == "__main__":
	main()
