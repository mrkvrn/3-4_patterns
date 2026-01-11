from abc import ABC, abstractmethod

print("Bridge Pattern")

class Renderer(ABC):
    @abstractmethod
    def render_shape(self):
        pass

class VectorRenderer(Renderer):
    def render_shape(self):
        return "VectorRenderer: Creating scalable vector graphics."

class RasterRenderer(Renderer):
    def render_shape(self):
        return "RasterRenderer: Generating pixel-based image."

class Shape:
    def __init__(self, renderer):
        self._renderer = renderer
    
    def draw(self):
        return f"Shape: Drawing with:\n{self._renderer.render_shape()}"
