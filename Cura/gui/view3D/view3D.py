__author__ = 'Jaime van Kessel'
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

class View3D(object):
	def __init__(self):
		self._scene = None #A view 3D has a scene responsible for data storage of what is in the 3D world.
		self._renderer_list = [] #The view holds a set of renderers, such as machine renderer or object renderer.
		self._machine = None # Reference to the machine

	def render(self): #todo: Unsure about name.
		for renderer in self._renderer_list:
			renderer.render() #call all render functions

	def addRenderer(self, renderer):
		self._renderer_list.append(renderer);

	def setScene(self,scene):
		self._scene(scene)

	def getScene(self):
		return self._scene

	def setMachine(self,machine):
		self._machine = machine

	def getMachine(self):
		return self._machine

	def _init3DView(self):
		'''
		Setup the basics of the 3D view
		'''
		#TODO: hardcoded values for height & width
		view_port_width = 10;
		view_port_height = 10;
		#size = self.GetSize() #get size of view. TODO
		glViewport(0, 0, view_port_width, view_port_height)
		glLoadIdentity()

		glLightfv(GL_LIGHT0, GL_POSITION, [0.2, 0.2, 1.0, 0.0])

		glDisable(GL_RESCALE_NORMAL)
		glDisable(GL_LIGHTING)
		glDisable(GL_LIGHT0)
		glEnable(GL_DEPTH_TEST)
		glDisable(GL_CULL_FACE)
		glDisable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

		glClearColor(0.8, 0.8, 0.8, 1.0)
		glClearStencil(0)
		glClearDepth(1.0)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		aspect = float(view_port_width) / float(view_port_height)
		machine_size = [self._machine.getValueByName('machine_width'),self._machine.getValueByName('machine_height'),self._machine.getValueByName('machine_depth')]
		gluPerspective(45.0, aspect, 1.0, numpy.max(machine_size) * 4)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)