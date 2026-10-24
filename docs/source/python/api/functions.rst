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
   > ['AFI', 'CZI', 'DCM', 'GDAL', 'NDPI', 'OMETIFF', 'PHTIFF', 'QPTIFF', 'SCN', 'SVS', 'VSI', 'ZVI']
   slide = slideio.open_slide(file_path="/data/a.czi", driver_id="CZI")
   slide.num_scenes
   > 1
