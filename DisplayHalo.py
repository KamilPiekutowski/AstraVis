from cyclops import *
from pointCloud import *
from omegaToolkit import *
import sys


scene = getSceneManager()
scene.addLoader(BinaryPointsLoader())
getDefaultCamera().setBackgroundColor(Color(0.0/255.0,0.0/255.0,0.0/255.0,0))

pointProgram = ProgramAsset()
pointProgram.name = "points"

pointProgram.vertexShaderName = "shaders/Sphere.vert"
pointProgram.fragmentShaderName = "shaders/Sphere.frag"
pointProgram.geometryShaderName = "shaders/Sphere.geom"

pointProgram.geometryOutVertices = 4
pointProgram.geometryInput = PrimitiveType.Points
pointProgram.geometryOutput = PrimitiveType.TriangleStrip
scene.addProgram(pointProgram)

pointScale = Uniform.create('pointScale', UniformType.Float, 1)
pointScale.setFloat(0.01)

pointCloudModel1 = ModelInfo()
pointCloudModel1.name = 'pointCloud1'
pointCloudModel1.path = 'data1.xyzb'
pointCloudModel1.options = "10000 0:1000000:1"
scene.loadModel(pointCloudModel1)

pointCloudModel2 = ModelInfo()
pointCloudModel2.name = 'pointCloud2'
pointCloudModel2.path = 'data2.xyzb'
pointCloudModel2.options = "10000 0:1000000:1"
scene.loadModel(pointCloudModel2)

pointCloud1 = StaticObject.create(pointCloudModel1.name)
pointCloud2 = StaticObject.create(pointCloudModel2.name)

# attach shader uniforms
mat = pointCloud1.getMaterial()
mat.setProgram(pointProgram.name)
mat.attachUniform(pointScale)

mat2 = pointCloud2.getMaterial()
mat2.setProgram(pointProgram.name)
mat2.attachUniform(pointScale)

#getDefaultCamera().setPosition(10000, 10000, 10000)
getDefaultCamera().setPosition(120, 0, 190)

#getDefaultCamera().lookAt(pointCloud.getBoundCenter(), Vector3(0,1,0))
getDefaultCamera().lookAt(pointCloud1.getBoundCenter(), Vector3(0,1,0))
getDefaultCamera().lookAt(pointCloud2.getBoundCenter(), Vector3(0,1,0))

setNearFarZ(0.001,10000)
#setNearFarZ(0.1,10000)
#pointCloud.setScale(Vector3(100, 100, 100))
pointCloud1.setScale(Vector3(1.5, 1.5, 1.5))
pointCloud2.setScale(Vector3(1.5, 1.5, 1.5))

mm = MenuManager.createAndInitialize()
menu = mm.getMainMenu()
if(menu == None):
	menu = mm.createMenu("main")
	mm.setMainMenu(menu)

mi1 = menu.addButton("Velocity", "toggleModel(0)")
mi2 = menu.addButton("Mass", "toggleModel(1)")
mi3 = menu.addSlider("Spin Parameter", "spinParameter")

def toggleModel(modelId):
	if(modelId == 0):
		pointCloud1.setVisible(True)
		pointCloud2.setVisible(False)	
		#getDefaultCamera().setBackgroundColor(Color(0.0/255.0,0.0/255.0,0.0/255.0,0))

	else:
		pointCloud1.setVisible(False)
                pointCloud2.setVisible(True)
		#getDefaultCamera().setBackgroundColor(Color(255.0/255.0,0.0/255.0,0.0/255.0,0))

def spinParameter:
                getDefaultCamera().setBackgroundColor(Color(255.0/255.0,0.0/255.0,0.0/255.0,0))


