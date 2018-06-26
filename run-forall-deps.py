#!/usr/bin/env python

from os import environ
from subprocess import Popen, STDOUT


scalaTests=["3.0.{}".format(i) for i in range(1, 6)] 
akkas24 = ["2.4.{}".format(i) for i in range(15, 21)]
akkas25 = ["2.5.{}".format(i) for i in range(14)]
akkas = akkas25 + akkas24


for akkaV in akkas:
	for scalaTestV in scalaTests:
		print(("%s %s") % (akkaV, scalaTestV))
		my_env = environ.copy()
		my_env["akkaV"]=akkaV
		my_env["scalaTestV"]=scalaTestV
		#sbtEnv = environ.copy().update({"akkaV": akkaV, "scalaTestV" : scalaTestV})
		process = Popen(["sbt ';+clean;+test'"], shell=True, env= my_env)
		process.communicate()
		exit_code = process.wait()
