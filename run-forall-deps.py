#!/usr/bin/env python

import os, errno
from subprocess import Popen, STDOUT
from uuid import uuid4


def my_exec(command):
	process = Popen([command], shell=True)
	process.communicate()
	exit_code = process.wait()

my_exec("git clean -fxd")
my_exec("git reset --hard origin/master")

scalaTests=["""
"org.scalatest" %% "scalatest" % "3.0.{}"
""".format(i) for i in range(1, 6)] 

akkas24=["""
"com.typesafe.akka" %% "akka-actor" % "2.4.{0}",
"com.typesafe.akka" %% "akka-agent" % "2.4.{0}",
"com.typesafe.akka" %% "akka-slf4j" % "2.4.{0}",
"com.typesafe.akka" %% "akka-remote" % "2.4.{0}",
"com.typesafe.akka" %% "akka-testkit" % "2.4.{0}",
"com.typesafe.akka" %% "akka-stream" % "2.4.{0}",
"com.typesafe.akka" %% "akka-stream-testkit" % "2.4.{0}",
"com.typesafe.akka" %% "akka-cluster" % "2.4.{0}",
"com.typesafe.akka" %% "akka-cluster-sharding" % "2.4.{0}",
"com.typesafe.akka" %% "akka-persistence" % "2.4.{0}"
""".format(i) for i in range(16, 21)]


akkas25=[""" 
"com.typesafe.akka" %% "akka-actor" % "2.5.{0}",
"com.typesafe.akka" %% "akka-agent" % "2.5.{0}",
"com.typesafe.akka" %% "akka-slf4j" % "2.5.{0}",
"com.typesafe.akka" %% "akka-remote" % "2.5.{0}",
"com.typesafe.akka" %% "akka-testkit" % "2.5.{0}",
"com.typesafe.akka" %% "akka-stream" % "2.5.{0}",
"com.typesafe.akka" %% "akka-stream-testkit" % "2.5.{0}",
"com.typesafe.akka" %% "akka-cluster" % "2.5.{0}",
"com.typesafe.akka" %% "akka-cluster-sharding" % "2.5.{0}",
"com.typesafe.akka" %% "akka-persistence" % "2.5.{0}"
""".format(i) for i in range(14)]

deps = scalaTests + akkas24 + akkas25

projectnames = ["P{}".format(uuid4()) for _ in deps]
projectnamesWithBT = ["`{}`".format(projectname) for projectname in projectnames]
projectnamesJoined = ", \n".join(projectnamesWithBT)

with open("build.sbt", "a+") as f:
	f.write(""".aggregate({})\n""".format(projectnamesJoined))

for i, (dep, projectname) in enumerate(zip(deps, projectnames)):
	if i > 1000:
		break;
	else:
		filename = "{}/src/main/scala/example/Hello.scala".format(projectname)
		buildsbt = "{}/build.sbt".format(projectname)
		if not os.path.exists(os.path.dirname(filename)):
		    try:
		    	print(filename)
		        os.makedirs(os.path.dirname(filename))
		    except OSError as exc: # Guard against race condition
		        if exc.errno != errno.EEXIST:
		            raise
		with open(buildsbt, "w") as f:
			f.write("""
val scala12X = Range(1, 7).map(minor => s"2.12.$minor")
val scala11X = Range(1, 12).map(minor => s"2.11.$minor")
crossScalaVersions := scala11X ++ scala12X
name := "{}"
libraryDependencies ++= Seq({})
""".format(projectname, dep))

		with open(filename, "w") as f:
		    f.write("""
package example

object Hello extends Greeting with App {
  println(greeting)
}

trait Greeting {
  lazy val greeting: String = "hello"
}
""")
		with open("build.sbt", "a+") as f:
			f.write("""val `{}`=project\n""".format(projectname))

my_exec("sbt ';+clean;+compile'")


# 		pass
		# print(("%s %s") % (akkaV, scalaTestV))
		# my_env = environ.copy()
		# my_env["akkaV"]=akkaV
		# my_env["scalaTestV"]=scalaTestV
		# #sbtEnv = environ.copy().update({"akkaV": akkaV, "scalaTestV" : scalaTestV})
		# process = Popen(["sbt ';+clean;+compile'"], shell=True, env= my_env)
		# process.communicate()
		# exit_code = process.wait()
