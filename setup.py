from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
import os
import platform

if platform.system() == 'Darwin':
    os.environ['CC'] = '/usr/local/opt/llvm/bin/clang++'

ext_modules = [Extension("c_utils",
                         ["c_utils.pyx"],
                         libraries=["m"],
                         extra_compile_args=["-ffast-math", "-fopenmp"],
                         extra_link_args=["-lomp"]
                         )]

setup(name="c_utils", cmdclass={"build_ext": build_ext},
      ext_modules=ext_modules,
      include_dirs=[np.get_include()],
      compiler_directives={'boundscheck': False, 'wraparound': False,
                           'nonecheck': False, 'cdivision': True})
