from cyclops import *
from pointCloud import *
from omegaToolkit import *
from math import *
import sys
import PointSet
import time
#import Manipulator

timeStepsRaw = [
                PointSet.PointSet('data/points1200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points1300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points1400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points1500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points1600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points1700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points1800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points1900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points2000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points2100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points2200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points2300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points2400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points2500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points2600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points2700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points2800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points2900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points3000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points3100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points3200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points3300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points3400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points3500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points3600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points3700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points3800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points3900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points4000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points4100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points4200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points4300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points4400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points4500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points4600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points4700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points4800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points4900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points5000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points5100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points5200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points5300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points5400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points5500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points5600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points5700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points5800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points5900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points6000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points6100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points6200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points6300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points6400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points6500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points6600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points6700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points6800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points6900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points7000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points7100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points7200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points7300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points7400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points7500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points7600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points7700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points7800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points7900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points8000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points8100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points8200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points8300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points8400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points8500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points8600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points8700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points8800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points8900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.PointSet('data/points9910.xyzb', Color(1, 1, 1, 1), 0.01)
                ]


timeStepsHal = [
                PointSet.HaloSet('data/halos1200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos1300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos1400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos1500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos1600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos1700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos1800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos1900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos2000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos2100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos2200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos2300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos2400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos2500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos2600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos2700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos2800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos2900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos3000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos3100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos3200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos3300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos3400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos3500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos3600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos3700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos3800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos3900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos4000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos4100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos4200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos4300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos4400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos4500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos4600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos4700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos4800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos4900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos5000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos5100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos5200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos5300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos5400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos5500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos5600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos5700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos5800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos5900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos6000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos6100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos6200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos6300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos6400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos6500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos6600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos6700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos6800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos6900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos7000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos7100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos7200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos7300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos7400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos7500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos7600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos7700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos7800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos7900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos8000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos8100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos8200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos8300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos8400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos8500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos8600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos8700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos8800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos8900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9000.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9100.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9200.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9300.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9400.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9500.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9600.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9700.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9800.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9900.xyzb', Color(1, 1, 1, 1), 0.01),
                PointSet.HaloSet('data/halos9910.xyzb', Color(1, 1, 1, 1), 0.01)
                ]




scene = getSceneManager()

#windowSize = Uniform.create('windowSize', UniformType.Vector2f, 1)

pivot = SceneNode.create('pivot')

for ps in timeStepsRaw:
    #ps.material.attachUniform(windowSize)
    pivot.addChild(ps.object)
    ps.object.setPosition(0, 0, 0)

for ps in timeStepsHal:
#    ps.material.attachUniform(windowSize)
    pivot.addChild(ps.object)
    ps.object.setPosition(0, 0, 0)

pivot.setScale(1.0, 1.0, 1.0)
#Manipulator.root = pivot


def v(id):
    reset()
    if id < 12:
        id = 12
    timeStepsRaw[id-12].object.setVisible(True)
    timeStepsHal[id-12].object.setVisible(True)

def reset():
    for i in range(0, 89):
        if timeStepsRaw[i].object.isVisible():
            timeStepsRaw[i].object.setVisible(False)
        if timeStepsHal[i].object.isVisible():
            timeStepsHal[i].object.setVisible(False)

def timelapse(start, end, step):
    reset()
    for i in xrange(start-12, end-12, step):
        timeStepsRaw[i].object.setVisible(True)
        timeStepsHal[i].object.setVisible(True)


def pTog(x):
    for i in range(0, 89):
        if x:
            timeStepsRaw[i].object.setVisible(True)
        else:
            timeStepsRaw[i].object.setVisible(False)

def hTog(x):
    for i in range(0, 89):
        if x:
            timeStepsHal[i].object.setVisible(True)
        else:
            timeStepsHal[i].object.setVisible(False)

funcTimer = 0.0
currentIndex = 0
setAnimate = False



def a():
    reset()
    global setAnimate
    setAnimate = not setAnimate

    #    for i in range(0, 88):
    #        timeStepsRaw[i].object.setVisible(False)
    #        timeStepsHal[i].object.setVisible(False)
    #        timeStepsRaw[i+1].object.setVisible(True)
    #        timeStepsHal[i+1].object.setVisible(True)
    #        time.sleep(1)


def onUpdate(frame, time, dt):
    
    global funcTimer
    global currentIndex
    global setAnimate
    
    funcTimer += dt

    if funcTimer > .15 and setAnimate:
        
        timeStepsHal[currentIndex].object.setVisible(True)
        
        if currentIndex > 10:
            timeStepsHal[currentIndex - 10].object.setVisible(False)
    
        currentIndex += 1

        if currentIndex > 88:
            reset()
            currentIndex = 0

        funcTimer = 0.0



    
    #print(frame, time, dt, funcTimer)
    
setUpdateFunction(onUpdate)








c = getDefaultCamera()
c.setBackgroundColor(Color('black'))
c.getController().setSpeed(20)
c.setPosition(100, 40, 150)

#getDefaultCamera().lookAt(pointCloud.getBoundCenter(), Vector3(0,1,0))

setNearFarZ(0.01, 10000)

v(45)


#--------------------------------------------------------------------------------
# Add a window resized callback (and call it once when the program starts)
#windowSize = Uniform.create('windowSize', UniformType.Vector2f, 1)
#ps.material.attachUniform(windowSize)

#def windowResized():
#    dc = getDisplayConfig()
#    cr = dc.getCanvasRect()
#    windowSize.setVector2f(Vector2(cr[2], cr[3]))
#getDisplayConfig().canvasChangedCommand = 'windowResized()'
#windowResized()