#python ray tracing implementation challenge
#shawn / Aug 2017
#-------------------------
#Some stuff can be easily missing:
#1. keep in mind when using tan/cos/sin, use radians not degrees

#-------------------------
import sys, math, multiprocessing, numpy

#------------------------
from Geo.Vector import Vector
from Geo.Ray import Ray
from Geo.Sphere import Sphere
from Geo.Plane import Plane
from Geo.Material import Material
from Geo.Geometry import Geometry

from Camera import Camera
from Light import PointLight, DiskLight
from Scene import Scene
from RenderWindow import RenderWindow


def main():
	#-------canvas size-----
	width = 600
	height = width

	renderView = RenderWindow(width,height)

	redLambert = Material(diffuseColor=Vector(0.9,0,0))
	blueLambert = Material(diffuseColor=Vector(0,0,0.9))
	greenLambert = Material(diffuseColor=Vector(0,0.9,0))
	whiteLambert = Material(diffuseColor=Vector(0.9,0.9,0.9))
	mirror = Material(reflectionColor=Vector(1,1,1),reflectionWeight=1)

	#-------Scene--------
	#important! This is a right handed coordinate system!
	sphere01 = Sphere(Vector(-15,-30,-136),20,material=whiteLambert)
	sphere02 = Sphere(Vector(10,-20,-136),30,material=whiteLambert)
	plane01 = Plane(Vector(0,-50,-136),Vector(0,1,0),material=whiteLambert) #bottom wall
	plane02 = Plane(Vector(-50,0,-136),Vector(1,0,0),material=redLambert) #left wall
	plane03 = Plane(Vector(0,0,-186),Vector(0,0,1),material=whiteLambert) #back wall
	plane04 = Plane(Vector(50,0,-136),Vector(-1,0,0),material=greenLambert) #right wall
	plane05 = Plane(Vector(0,50,-136),Vector(0,-1,0),material=whiteLambert) #top wall
	testPlane = Plane(Vector(0,30,-136),Vector(0,-1,0),w=20,h=20)
	light01 = DiskLight(Vector(0,40,-150),30) #light source on the top
	light02 = PointLight(Vector(-20,40,-160))
	light03 = PointLight(Vector(20,30,-90))

	newScene = Scene({"geometry":[sphere01,sphere02,plane01,plane02,plane03,plane04,plane05],"light":[light01]})

	cam = Camera(Vector(0,0,0),Vector(0,0,1),60)

	renderView.startRender(newScene,cam)

	sys.exit(renderView.app.exec_())


if __name__ == "__main__":
	main()
