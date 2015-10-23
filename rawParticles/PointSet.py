from cyclops import *
from pointCloud import *
from math import *
import sys

scene = getSceneManager()
scene.addLoader(BinaryPointsLoader())

pointProgram = ProgramAsset()
pointProgram.name = "points"
pointProgram.vertexShaderName = "shaders/Sphere.vert"
pointProgram.fragmentShaderName = "shaders/Sphere.frag"
pointProgram.geometryShaderName = "shaders/Sphere.geom"

#pointProgram.vertexShaderName = "star.vert"
#pointProgram.fragmentShaderName = "star.frag"

#pointProgram.vertexShaderName = "shadersSprite/star.vert"
#pointProgram.fragmentShaderName = "shadersSprite/star.frag"

pointProgram.geometryOutVertices = 4
pointProgram.geometryInput = PrimitiveType.Points
pointProgram.geometryOutput = PrimitiveType.TriangleStrip

scene.addProgram(pointProgram)

class PointSet:
    def __init__(self, file, color, pointScale):
        self.pointScale = Uniform.create('pointScale', UniformType.Float, 1)
        self.pointScale.setFloat(pointScale)
        
        #self.color = Uniform.create('color', UniformType.Color, 1)
        #self.color.setColor(color)
        
        self.model = ModelInfo()
        self.model.name = file
        self.model.path = file
        self.model.options = "10000 0:1000000:1"
        scene.loadModel(self.model)
        
        self.object = StaticObject.create(self.model.name)
        # attach shader uniforms
        self.material = self.object.getMaterial()
        self.material.setProgram(pointProgram.name)
        self.material.attachUniform(self.pointScale)
        #self.material.attachUniform(self.color)
        self.material.setTransparent(False)
        #self.material.setAdditive(True)
        #self.material.setDepthTestEnabled(False)
        
        #self.material.setDiffuseTexture('data/star1.png')
        #self.material.setPointSprite(True)

class HaloSet:
    def __init__(self, file, color, pointScale):
        self.pointScale = Uniform.create('pointScale', UniformType.Float, 1)
        self.pointScale.setFloat(pointScale)
        
        #self.color = Uniform.create('color', UniformType.Color, 1)
        #self.color.setColor(color)
        
        self.model = ModelInfo()
        self.model.name = file
        self.model.path = file
        self.model.options = "10000 0:1000000:1"
        scene.loadModel(self.model)
        
        self.object = StaticObject.create(self.model.name)
        # attach shader uniforms
        self.material = self.object.getMaterial()
        self.material.setProgram(pointProgram.name)
        self.material.attachUniform(self.pointScale)
        #self.material.attachUniform(self.color)
        self.material.setTransparent(True)
        #self.material.setAdditive(True)
        #self.material.setDepthTestEnabled(False)

        #self.material.setDiffuseTexture('star1.png')
        #self.material.setPointSprite(True)