scalaVersion := "2.12.6"

val scala12X = Range(1, 7).map(minor => s"2.12.$minor")
val scala11X = Range(1, 12).map(minor => s"2.11.$minor")
crossScalaVersions := scala11X ++ scala12X

lazy val root = (project in file(".")).
  settings(
    inThisBuild(List(
      organization := "com.example",
      scalaVersion := "2.12.6",
      version := "0.1.0-SNAPSHOT"
    )),
    name := "fetch-libraries"
  )
