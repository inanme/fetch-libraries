import sbt._

object versions {
  val scalaTestV = sys.env.getOrElse("scalaTestV", throw new RuntimeException("scalaTestV"))
  val akkaV = sys.env.getOrElse("akkaV", throw new RuntimeException("akkaV"))
}

object Dependencies {

  import versions._

  val scalaTest = "org.scalatest" %% "scalatest" % scalaTestV

  val akka = Seq(
    "com.typesafe.akka" %% "akka-actor" % akkaV,
    "com.typesafe.akka" %% "akka-agent" % akkaV,
    "com.typesafe.akka" %% "akka-slf4j" % akkaV,
    "com.typesafe.akka" %% "akka-remote" % akkaV,
    "com.typesafe.akka" %% "akka-testkit" % akkaV,
    "com.typesafe.akka" %% "akka-stream" % akkaV,
    "com.typesafe.akka" %% "akka-stream-testkit" % akkaV,
    "com.typesafe.akka" %% "akka-cluster" % akkaV,
    "com.typesafe.akka" %% "akka-cluster-sharding" % akkaV,
    "com.typesafe.akka" %% "akka-distributed-data" % akkaV,
    "com.typesafe.akka" %% "akka-persistence" % akkaV
  )

  val akkaHttps = Seq(
    "com.typesafe.akka" %% "akka-http" % "10.1.3",
    "com.typesafe.akka" %% "akka-http-testkit" % "10.1.3"
  )

}
