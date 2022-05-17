.. index:: pair: page; Quantizatiing 3D Segmentation Model
.. _doxid-pot_example_3d_segmentation__r_e_a_d_m_e:


Quantizatiing 3D Segmentation Model
===================================

:target:`doxid-pot_example_3d_segmentation__r_e_a_d_m_e_1md_openvino_tools_pot_openvino_tools_pot_api_samples_3d_segmentation_readme` This example demonstrates the use of the :ref:`Post-training Optimization Tool API <doxid-pot_compression_api__r_e_a_d_m_e>` for the task of quantizing a 3D segmentation model. The `Brain Tumor Segmentation <https://github.com/openvinotoolkit/open_model_zoo/blob/master/models/public/brain-tumor-segmentation-0002/brain-tumor-segmentation-0002.md>`__ model from PyTorch\* is used for this purpose. A custom ``DataLoader`` is created to load images in NIfTI format from `Medical Segmentation Decathlon BRATS 2017 <http://medicaldecathlon.com/>`__ dataset for 3D semantic segmentation task and the implementation of Dice Index metric is used for the model evaluation. In addition, this example demonstrates how one can use image metadata obtained during image reading and preprocessing to post-process the model raw output. The code of the example is available on `GitHub <https://github.com/openvinotoolkit/openvino/tree/master/tools/pot/openvino/tools/pot/api/samples/3d_segmentation>`__.

How to prepare the data
~~~~~~~~~~~~~~~~~~~~~~~

To run this example, you will need to download the Brain Tumors 2017 part of the Medical Segmentation Decathlon image database `http://medicaldecathlon.com/ <http://medicaldecathlon.com/>`__. 3D MRI data in NIfTI format can be found in the ``imagesTr`` folder, and segmentation masks are in ``labelsTr``.

How to Run the example
~~~~~~~~~~~~~~~~~~~~~~

#. Launch Model Downloader tool to download ``brain-tumor-segmentation-0002`` model from the Open Model Zoo repository.
   
   .. ref-code-block:: cpp
   
   	omz_downloader --name brain-tumor-segmentation-0002

#. Launch Model Converter tool to generate Intermediate Representation (IR) files for the model:
   
   .. ref-code-block:: cpp
   
   	omz_converter --name brain-tumor-segmentation-0002

#. Launch the example script from the example directory:
   
   .. ref-code-block:: cpp
   
   	python3 ./3d_segmentation_example.py -m <PATH_TO_IR_XML> -d <BraTS_2017/imagesTr> --mask-dir <BraTS_2017/labelsTr>
   
   Optional: you can specify .bin file of IR directly using the ``-w``, ``--weights`` options.

