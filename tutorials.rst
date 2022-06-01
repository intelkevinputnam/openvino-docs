.. index:: pair: page; Tutorials
.. _doxid-tutorials:


Tutorials
=========

:target:`doxid-tutorials_1md_openvino_docs_tutorials`





.. _notebook tutorials:

.. toctree::
   :maxdepth: 2
   :caption: Notebooks
   :hidden:

   notebooks/notebooks

This collection of Python tutorials are written for running on `Jupyter\* <https://jupyter.org>`__ notebooks. The tutorials provide an introduction to the OpenVINO™ toolkit and explain how to use the Python API and tools for optimized deep learning inference. You can run the code one section at a time to see how to integrate your application with OpenVINO™ libraries.

|binder_link|

.. |binder_link| raw:: html 

   <a href="https://mybinder.org/v2/gh/openvinotoolkit/openvino_notebooks/HEAD?filepath=notebooks%2F001-hello-world%2F001-hello-world.ipynb" target="_blank"><img src="https://mybinder.org/badge_logo.svg" alt="Binder"></a>

Tutorials showing this logo may be run remotely using Binder with no setup, although running the notebooks on a local system is recommended for best performance. See the `OpenVINO™ Notebooks Installation Guide <https://github.com/openvinotoolkit/openvino_notebooks/blob/main/README.md#-installation-guide>`__ to install and run locally.

Getting Started
=================

.. toctree::
    :depth: 1

    notebooks/001-hello-world
    notebooks/002-openvino-api
    notebooks/003-hello-segmentation
    notebooks/004-hello-detection

Convert & Optimize
======================

.. toctree::
    :depth:

    notebooks/101-tensorflow-to-openvino
    notebooks/102-pytorch-onnx-to-openvino
    notebooks/103-paddle-onnx-to-openvino-classification
    notebooks/104-model-tools
    notebooks/105-language-quantize-bert
    notebooks/106-auto-device
    notebooks/107-speech-recognition-quantization
    notebooks/110-ct-segmentation-quantize
    notebooks/data-preparation-ct-scan
    notebooks/pytorch-monai-training
    notebooks/111-detection-quantization
    notebooks/112-pytorch-post-training-quantization-nncf
    notebooks/113-image-classification-quantization
    notebooks/114-quantization-simplified-mode

Model Demos
==============

.. toctree::
    :depth:

    notebooks/201-vision-monodepth
    notebooks/202-vision-superresolution-image
    notebooks/202-vision-superresolution-video
    notebooks/205-vision-background-removal
    notebooks/206-vision-paddlegan-anime
    notebooks/207-vision-paddlegan-superresolution
    notebooks/208-optical-character-recognition
    notebooks/209-handwritten-ocr
    notebooks/210-ct-scan-live-inference
    notebooks/211-speech-to-text
    notebooks/212-onnx-style-transfer
    notebooks/213-question-answering
    notebooks/214-vision-paddle-classification
    notebooks/215-image-inpainting
    notebooks/217-vision-deblur
    notebooks/218-vehicle-detection-and-recognition

Model Training
===============

.. toctree::
    :depth:

    notebooks/301-tensorflow-training-openvino
    notebooks/301-tensorflow-training-openvino-pot
    notebooks/302-pytorch-quantization-aware-training
    notebooks/305-tensorflow-quantization-aware-training

Live Demos
===========

.. toctree::
    :depth:
    
    notebooks/401-object-detection
    notebooks/402-pose-estimation
    notebooks/403-action-recognition-webcam
    notebooks/405-paddle-ocr-webcam