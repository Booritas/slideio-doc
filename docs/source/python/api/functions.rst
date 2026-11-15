Module functions
================

.. currentmodule:: slideio

.. autofunction:: open_slide
.. autofunction:: get_driver_ids
.. autofunction:: get_version
.. autofunction:: set_log_level
.. autofunction:: transform_scene
.. autofunction:: convert_scene
.. autofunction:: compare_images

Example:

.. code-block:: python

   import slideio
   slideio.get_driver_ids()
   > ['AFI', 'BIF', 'CZI', 'DCM', 'GDAL', 'LIF', 'MRXS', 'ND2', 'NDPI', 'OMETIFF', 'PHTIFF', 'QPTIFF', 'SCN', 'SVS', 'VSI', 'ZVI']
   slide = slideio.open_slide("/data/a.czi", "CZI")
   slide.num_scenes
   > 1
