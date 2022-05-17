.. index:: pair: page; Post-training Optimization Tool API Examples
.. _doxid-pot_example__r_e_a_d_m_e:


Post-training Optimization Tool API Examples
============================================

:target:`doxid-pot_example__r_e_a_d_m_e_1md_openvino_tools_pot_openvino_tools_pot_api_samples_readme`





.. toctree::
   :maxdepth: 1
   :hidden:

   Quantizatiing Image Classification Model <pot_example_classification_README>
   Quantizatiing Object Detection Model with Accuracy Control  <pot_example_object_detection_README>
   Quantizatiing Cascaded Model <pot_example_face_detection_README>
   Quantizatiing Semantic Segmentation Model <pot_example_segmentation_README>
   Quantizatiing 3D Segmentation Model <pot_example_3d_segmentation_README>
   Quantizatiing for GNA Device <pot_example_speech_README>

The Post-training Optimization Tool contains multiple examples that demonstrate how to use its :ref:`API <doxid-pot_compression_api__r_e_a_d_m_e>` to optimize DL models. All available examples can be found on `GitHub <https://github.com/openvinotoolkit/openvino/tree/master/tools/pot/openvino/tools/pot/api/samples>`__.

The following examples demonstrate the implementation of ``Engine``, ``Metric``, and ``DataLoader`` interfaces for various use cases:

#. :ref:`Quantizing Image Classification model <doxid-pot_example_classification__r_e_a_d_m_e>`
   
   * Uses single ``MobilenetV2`` model from TensorFlow\*
   
   * Implements ``DataLoader`` to load .JPEG images and annotations of Imagenet database
   
   * Implements ``Metric`` interface to calculate Accuracy at top-1 metric
   
   * Uses DefaultQuantization algorithm for quantization model

#. :ref:`Quantizing Object Detection Model with Accuracy Control <doxid-pot_example_object_detection__r_e_a_d_m_e>`
   
   * Uses single ``MobileNetV1 FPN`` model from TensorFlow\*
   
   * Implements ``Dataloader`` to load images of COCO database
   
   * Implements ``Metric`` interface to calculate mAP@[.5:.95] metric
   
   * Uses ``AccuracyAwareQuantization`` algorithm for quantization model

#. :ref:`Quantizing Semantic Segmentation Model <doxid-pot_example_segmentation__r_e_a_d_m_e>`
   
   * Uses single ``DeepLabV3`` model from TensorFlow\*
   
   * Implements ``DataLoader`` to load .JPEG images and annotations of Pascal VOC 2012 database
   
   * Implements ``Metric`` interface to calculate Mean Intersection Over Union metric
   
   * Uses DefaultQuantization algorithm for quantization model

#. :ref:`Quantizing 3D Segmentation Model <doxid-pot_example_3d_segmentation__r_e_a_d_m_e>`
   
   * Uses single ``Brain Tumor Segmentation`` model from PyTorch\*
   
   * Implements ``DataLoader`` to load images in NIfTI format from Medical Segmentation Decathlon BRATS 2017 database
   
   * Implements ``Metric`` interface to calculate Dice Index metric
   
   * Demonstrates how to use image metadata obtained during data loading to post-process the raw model output
   
   * Uses DefaultQuantization algorithm for quantization model

#. :ref:`Quantizing Cascaded model <doxid-pot_example_face_detection__r_e_a_d_m_e>`
   
   * Uses cascaded (composite) ``MTCNN`` model from Caffe\* that consists of three separate models in an OpenVino Intermediate Representation (IR)
   
   * Implements ``Dataloader`` to load .jpg images of WIDER FACE database
   
   * Implements ``Metric`` interface to calculate Recall metric
   
   * Implements ``Engine`` class that is inherited from ``IEEngine`` to create a complex staged pipeline to sequentially execute each of the three stages of the MTCNN model, represented by multiple models in IR. It uses engine helpers to set model in OpenVino Inference Engine and process raw model output for the correct statistics collection
   
   * Uses DefaultQuantization algorithm for quantization model

#. :ref:`Quantizing for GNA Device <doxid-pot_example_speech__r_e_a_d_m_e>`
   
   * Uses models from Kaldi\*
   
   * Implements ``DataLoader`` to data in .ark format
   
   * Uses DefaultQuantization algorithm for quantization model

After execution of each example above the quantized model is placed into the folder ``optimized``. The accuracy validation of the quantized model is performed right after the quantization.

