#!/home/kamilp/Documents/EVL/omegalib/build/bin/orun -i -s
import sys
from cyclops import *
from pointCloud import *

scene = getSceneManager()
scene.addLoader(BinaryPointsLoader())
getDefaultCamera().setBackgroundColor(Color(0,0,0,0))

pointProgram = ProgramAsset()
pointProgram.name = "points"
pointProgram.vertexShaderName = "./shaders/Sphere.vert"
pointProgram.fragmentShaderName = "./shaders/Sphere.frag"
pointProgram.geometryShaderName = "./shaders/Sphere.geom"
pointProgram.geometryOutVertices = 4
pointProgram.geometryInput = PrimitiveType.Points
pointProgram.geometryOutput = PrimitiveType.TriangleStrip
scene.addProgram(pointProgram)

pointScale = Uniform.create('pointScale', UniformType.Float, 1)
pointScale.setFloat(30)

pointCloudModel = ModelInfo()
pointCloudModel.name = 'pointCloud'
pointCloudModel.path = sys.argv[1]
pointCloudModel.options = "10000 100:1000000:5 20:100:4 6:20:2 0:5:1"
#pointCloudModel.options = "10000 100:1000000:20 20:100:10 6:20:5 0:5:5"
#pointCloudModel.options = "10000 0:1000000:1"
scene.loadModel(pointCloudModel)

pointCloud = StaticObject.create(pointCloudModel.name)
# attach shader uniforms
#pointCloud.setScale(Vector3(.5,.5,.5))
mat = pointCloud.getMaterial()
mat.setProgram(pointProgram.name)
mat.attachUniform(pointScale)

getDefaultCamera().setPosition(0, -300, 50)
getDefaultCamera().lookAt(pointCloud.getBoundCenter(), Vector3(0,-300,50))
#pos = getDefaultCamera().getBackgroundColor()
#print "Camera Position:"
#print pos
setNearFarZ(0.1,100000000)
#getMainMenu.get
