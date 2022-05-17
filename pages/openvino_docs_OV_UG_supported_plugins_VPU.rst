.. index:: pair: page; VPU devices
.. _doxid-openvino_docs__o_v__u_g_supported_plugins__v_p_u:


VPU devices
===========

:target:`doxid-openvino_docs__o_v__u_g_supported_plugins__v_p_u_1md_openvino_docs_ov_runtime_ug_supported_plugins_vpu`





.. toctree::
   :maxdepth: 1
   :hidden:

   openvino_docs_OV_UG_supported_plugins_MYRIAD
   openvino_docs_OV_UG_supported_plugins_HDDL

This chapter provides information on the OpenVINO Runtime plugins that enable inference of deep learning models on the supported VPU devices:

* Intel® Neural Compute Stick 2 powered by the Intel® Movidius™ Myriad™ X — Supported by the :ref:`MYRIAD Plugin <doxid-openvino_docs__o_v__u_g_supported_plugins__m_y_r_i_a_d>`

* Intel® Vision Accelerator Design with Intel® Movidius™ VPUs — Supported by the :ref:`HDDL Plugin <doxid-openvino_docs__o_v__u_g_supported_plugins__h_d_d_l>`

.. note:: With the OpenVINO™ 2020.4 release, Intel® Movidius™ Neural Compute Stick powered by the Intel® Movidius™ Myriad™ 2 is no longer supported.

Supported Networks
~~~~~~~~~~~~~~~~~~

Caffe\* :

* AlexNet

* CaffeNet

* GoogleNet (Inception) v1, v2, v4

* VGG family (VGG16, VGG19)

* SqueezeNet v1.0, v1.1

* ResNet v1 family (18\*\*\*, 50, 101, 152)

* MobileNet (mobilenet-v1-1.0-224, mobilenet-v2)

* Inception ResNet v2

* DenseNet family (121,161,169,201)

* SSD-300, SSD-512, SSD-MobileNet, SSD-GoogleNet, SSD-SqueezeNet

TensorFlow\* :

* AlexNet

* Inception v1, v2, v3, v4

* Inception ResNet v2

* MobileNet v1, v2

* ResNet v1 family (50, 101, 152)

* ResNet v2 family (50, 101, 152)

* SqueezeNet v1.0, v1.1

* VGG family (VGG16, VGG19)

* Yolo family (yolo-v2, yolo-v3, tiny-yolo-v1, tiny-yolo-v2, tiny-yolo-v3)

* faster_rcnn_inception_v2, faster_rcnn_resnet101

* ssd_mobilenet_v1

* DeepLab-v3+

MXNet\* :

* AlexNet and CaffeNet

* DenseNet family (121,161,169,201)

* SqueezeNet v1.1

* MobileNet v1, v2

* NiN

* ResNet v1 (101, 152)

* ResNet v2 (101)

* SqueezeNet v1.1

* VGG family (VGG16, VGG19)

* SSD-Inception-v3, SSD-MobileNet, SSD-ResNet-50, SSD-300

\*\*\* Network is tested on Intel Neural Compute Stick 2 with BatchNormalization fusion optimization disabled during Model Optimizer import

Optimizations
~~~~~~~~~~~~~

VPU plugins support layer fusion and decomposition.

Layer Fusion
------------

Fusing Rules
++++++++++++

Certain layers can be merged into convolution, ReLU, and Eltwise layers according to the patterns below:

* Convolution
  
  * Convolution + ReLU → Convolution
  
  * Convolution + Clamp → Convolution
  
  * Convolution + LeakyReLU → Convolution
  
  * Convolution (3x3, stride=1, padding=1) + Pooling (2x2, stride=2, padding=0) → Convolution

* Pooling + ReLU → Pooling

* FullyConnected + ReLU → FullyConnected

* Eltwise
  
  * Eltwise + ReLU → Eltwise
  
  * Eltwise + LeakyReLU → Eltwise
  
  * Eltwise + Clamp → Eltwise

Joining Rules
+++++++++++++

.. note:: Application of these rules depends on tensor sizes and resources available.

Layers can be joined only when the two conditions below are met:

* Layers are located on topologically independent branches.

* Layers can be executed simultaneously on the same hardware units.

Decomposition Rules
-------------------

* Convolution and Pooling layers are tiled resulting in the following pattern:
  
  * A Split layer that splits tensors into tiles
  
  * A set of tiles, optionally with service layers like Copy
  
  * Depending on a tiling scheme, a Concatenation or Sum layer that joins all resulting tensors into one and restores the full blob that contains the result of a tiled operation
  
  Names of tiled layers contain the ``@soc=M/N`` part, where ``M`` is the tile number and ``N`` is the number of tiles:
  
  .. image:: yolo_tiny_v1.png

.. note:: Nominal layers, such as Shrink and Expand, are not executed.

.. note:: VPU plugins can add extra layers like Copy.

VPU Common Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VPU plugins support the configuration parameters listed below. The parameters are passed as ``std::map<std::string, std::string>`` on ``:ref:`InferenceEngine::Core::LoadNetwork <doxid-class_inference_engine_1_1_core_1a7b0b5ab0009abc572762422105b5c666>``` or ``:ref:`InferenceEngine::Core::SetConfig <doxid-class_inference_engine_1_1_core_1a34aa9ac6fb237b634d5bf08b288e88d4>```. When specifying key values as raw strings (that is, when using Python API), omit the ``KEY_`` prefix.

.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Parameter Values
      - Default
      - Description
    * - ``KEY_VPU_HW_STAGES_OPTIMIZATION``
      - ``YES`` / ``NO``
      - ``YES``
      - Turn on HW stages usage Applicable for Intel Movidius Myriad X and Intel Vision Accelerator Design devices only.
    * - ``KEY_VPU_COMPUTE_LAYOUT``
      - ``VPU_AUTO`` , ``VPU_NCHW`` , ``VPU_NHWC``
      - ``VPU_AUTO``
      - Specify internal input and output layouts for network layers.
    * - ``KEY_VPU_PRINT_RECEIVE_TENSOR_TIME``
      - ``YES`` / ``NO``
      - ``NO``
      - Add device-side time spent waiting for input to PerformanceCounts. See `Data Transfer Pipelining <#VPU_DATA_TRANSFER_PIPELINING>`__ section for details.
    * - ``KEY_VPU_IGNORE_IR_STATISTIC``
      - ``YES`` / ``NO``
      - ``NO``
      - VPU plugin could use statistic present in IR in order to try to improve calculations precision. If you don't want statistic to be used enable this option.
    * - ``KEY_VPU_CUSTOM_LAYERS``
      - path to XML file
      - empty string
      - This option allows to pass XML file with custom layers binding. If layer is present in such file, it would be used during inference even if the layer is natively supported.

.. _VPU_DATA_TRANSFER_PIPELINING:

Data Transfer Pipelining
~~~~~~~~~~~~~~~~~~~~~~~~

MYRIAD plugin tries to pipeline data transfer to/from device with computations. While one infer request is executed, the data for next infer request can be uploaded to device in parallel. The same applies to result downloading.

``KEY_VPU_PRINT_RECEIVE_TENSOR_TIME`` configuration parameter can be used to check the efficiency of current pipelining. The new record in performance counters will show the time that device spent waiting for input before starting the inference. In a perfect pipeline this time should be near zero, which means that the data was already transferred when new inference started.

Troubleshooting
~~~~~~~~~~~~~~~

**Get the following message when running inference with the VPU plugin: "[VPU] Cannot convert layer <layer_name> due to unsupported layer type <layer_type>"**

This means that your topology has a layer that is unsupported by your target VPU plugin. To resolve this issue, you can implement the custom layer for the target device using the :ref:`OpenVINO™ Extensibility mechanism <doxid-openvino_docs__extensibility__u_g__intro>`. Or, to quickly get a working prototype, you can use the heterogeneous scenario with the default fallback policy (see the :ref:`Heterogeneous execution <doxid-openvino_docs__o_v__u_g__hetero_execution>` section). Use the HETERO mode with a fallback device that supports this layer, for example, CPU: ``HETERO:MYRIAD,CPU``. For a list of VPU-supported layers, see the Supported Layers section of the :ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>` page.

Known Layers Limitations
~~~~~~~~~~~~~~~~~~~~~~~~

* ``ScaleShift`` layer is supported for zero value of ``broadcast`` attribute only.

* ``CTCGreedyDecoder`` layer works with the ``ctc_merge_repeated`` attribute equal to 1.

* ``DetectionOutput`` layer works with zero values of ``interpolate_orientation`` and ``num_orient_classes`` parameters only.

* ``MVN`` layer uses fixed value for ``eps`` parameters (1e-9).

* ``Normalize`` layer uses fixed value for ``eps`` parameters (1e-9) and is supported for zero value of ``across_spatial`` only.

* ``Pad`` layer works only with 4D tensors.

See Also
~~~~~~~~

* :ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

* `Intel® Neural Compute Stick 2 Get Started <https://software.intel.com/en-us/neural-compute-stick/get-started>`__

