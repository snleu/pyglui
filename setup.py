import os, platform

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

if platform.system() == 'Darwin':
	includes = ['/System/Library/Frameworks/OpenGL.framework/Versions/Current/Headers/']
	f = '-framework'
	link_args = [f, 'OpenGL']
	libs = []
else:
    includes = ['/usr/include/GL',]
    libs = ['GL']
    link_args = []


extensions = [
	Extension(	name="pyglui.ui",
				sources=['pyglui/ui.pyx'],
				include_dirs = includes,
				libraries = libs,
				extra_link_args=link_args,
				extra_compile_args=[]),
	Extension(	name="pyglui.cygl.utils",
				sources=['pyglui/cygl/utils.pyx'],
				include_dirs = includes,
				libraries = libs,
				extra_link_args=link_args,
				extra_compile_args=[]),
	Extension(	name="pyglui.pyfontstash",
				sources=['pyglui/pyfontstash/pyfontstash.pyx'],
				include_dirs = includes,
				libraries = libs,
				extra_link_args=link_args,
				extra_compile_args=['-D FONTSTASH_IMPLEMENTATION','-D GLFONTSTASH_IMPLEMENTATION'])
]

setup( 	name="pyglui",
		version="0.0.1",
		packages = ['pyglui'],
		py_modules = ['pyglui.cygl.'], #add  __init__.py in pyglui/cygl
		description="OpenGL UI powered by cython",
		ext_modules=cythonize(extensions)
)