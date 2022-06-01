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
    :maxdepth: 1

    notebooks/001-hello-world-with-output
    notebooks/002-openvino-api-with-output
    notebooks/003-hello-segmentation-with-output
    notebooks/004-hello-detection-with-output

Convert & Optimize
======================

.. toctree::
    :maxdepth: 1

    notebooks/101-tensorflow-to-openvino-with-output
    notebooks/102-pytorch-onnx-to-openvino-with-output
    notebooks/103-paddle-onnx-to-openvino-classification-with-output
    notebooks/104-model-tools-with-output
    notebooks/105-language-quantize-bert-with-output
    notebooks/106-auto-device-with-output
    notebooks/107-speech-recognition-quantization-with-output
    notebooks/110-ct-segmentation-quantize-with-output
    notebooks/data-preparation-ct-scan-with-output
    notebooks/pytorch-monai-training-with-output
    notebooks/111-detection-quantization-with-output
    notebooks/112-pytorch-post-training-quantization-nncf-with-output
    notebooks/113-image-classification-quantization-with-output
    notebooks/114-quantization-simplified-mode-with-output

Model Demos
==============

.. toctree::
    :maxdepth: 1

    notebooks/201-vision-monodepth-with-output
    notebooks/202-vision-superresolution-image-with-output
    notebooks/202-vision-superresolution-video-with-output
    notebooks/205-vision-background-removal-with-output
    notebooks/206-vision-paddlegan-anime-with-output
    notebooks/207-vision-paddlegan-superresolution-with-output
    notebooks/208-optical-character-recognition-with-output
    notebooks/209-handwritten-ocr-with-output
    notebooks/210-ct-scan-live-inference-with-output
    notebooks/211-speech-to-text-with-output
    notebooks/212-onnx-style-transfer-with-output
    notebooks/213-question-answering-with-output
    notebooks/214-vision-paddle-classification-with-output
    notebooks/215-image-inpainting-with-output
    notebooks/217-vision-deblur-with-output
    notebooks/218-vehicle-detection-and-recognition-with-output

Model Training
===============

.. toctree::
    :maxdepth: 1

    notebooks/301-tensorflow-training-openvino-with-output
    notebooks/301-tensorflow-training-openvino-pot-with-output
    notebooks/302-pytorch-quantization-aware-training-with-output
    notebooks/305-tensorflow-quantization-aware-training-with-output

Live Demos
===========

.. toctree::
    :maxdepth: 1

    notebooks/401-object-detection-with-output
    notebooks/402-pose-estimation-with-output
    notebooks/403-action-recognition-webcam-with-output
    notebooks/405-paddle-ocr-webcam-with-output