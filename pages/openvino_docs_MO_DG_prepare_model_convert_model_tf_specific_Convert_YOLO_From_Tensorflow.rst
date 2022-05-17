.. index:: pair: page; Convert TensorFlow YOLO Models
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__y_o_l_o__from__tensorflow:


Convert TensorFlow YOLO Models
==============================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__y_o_l_o__from__tensorflow_1md_openvino_docs_mo_dg_prepare_model_convert_model_tf_specific_convert_yolo_from_tensorflow` This document explains how to convert real-time object detection YOLOv1\*, YOLOv2\*, YOLOv3\* and YOLOv4\* public models to the Intermediate Representation (IR). All YOLO\* models are originally implemented in the DarkNet\* framework and consist of two files:

* ``.cfg`` file with model configurations

* ``.weights`` file with model weights

Depending on a YOLO model version, the Model Optimizer converts it differently:

* YOLOv4 must be first converted from Keras\* to TensorFlow 2\*.

* YOLOv3 has several implementations. This tutorial uses a TensorFlow implementation of YOLOv3 model, which can be directly converted to an IR.

* YOLOv1 and YOLOv2 models must be first converted to TensorFlow\* using DarkFlow\*.

.. _yolov4-to-ir:

Convert YOLOv4 Model to IR
~~~~~~~~~~~~~~~~~~~~~~~~~~

This section explains how to convert the YOLOv4 Keras\* model from the `https://github.com/david8862/keras-YOLOv3-model-set <https://github.com/david8862/keras-YOLOv3-model-set>`__ repository to an IR. To convert the YOLOv4 model, follow the instructions below:

#. Download YOLOv4 weights and associated with it cfg file:



* for YOLOv4 (`weights <https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights>`__ / `config file <https://github.com/david8862/keras-YOLOv3-model-set/raw/6c9aff7bb0c1660704ad07c85739e95885676e5b/cfg/yolov4.cfg>`__)

* for YOLOv4-tiny (`weights <https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights>`__ / `config file <https://raw.githubusercontent.com/david8862/keras-YOLOv3-model-set/6b4a0ee63771262363e8224b0ee915cad6c5e93e/cfg/yolov4-tiny.cfg>`__)



#. Clone the repository with the YOLOv4 model:
   
   .. ref-code-block:: cpp
   
   	git clone https://github.com/david8862/keras-YOLOv3-model-set

#. Convert the model to the TensorFlow 2\* format:



* for YOLOv4:
  
  .. ref-code-block:: cpp
  
  	python keras-YOLOv3-model-set/tools/model_converter/convert.py <path_to_cfg_file>/yolov4.cfg <path_to_weights>/yolov4.weights <saved_model_dir>

* for YOLOv4-tiny:
  
  .. ref-code-block:: cpp
  
  	python keras-YOLOv3-model-set/tools/model_converter/convert.py <path_to_cfg_file>/yolov4-tiny.cfg <path_to_weights>/yolov4-tiny.weights <saved_model_dir>



#. Run Model Optimizer to converter the model from the TensorFlow 2 format to an IR:

.. note:: Before you run the conversion, make sure you have installed all the Model Optimizer dependencies for TensorFlow 2.





.. ref-code-block:: cpp

	mo --saved_model_dir yolov4 --output_dir models/IRs --input_shape [1,608,608,3] --model_name yolov4

.. _yolov3-to-ir:

Convert YOLOv3 Model to IR
~~~~~~~~~~~~~~~~~~~~~~~~~~

On GitHub\*, you can find several public versions of TensorFlow YOLOv3 model implementation. This section explains how to convert YOLOv3 model from the `https://github.com/mystic123/tensorflow-yolo-v3 <https://github.com/mystic123/tensorflow-yolo-v3>`__ repository (commit ed60b90) to an IR , but the process is similar for other versions of TensorFlow YOLOv3 model.

.. _yolov3-overview:

Overview of YOLOv3 Model Architecture
-------------------------------------

Originally, YOLOv3 model includes feature extractor called ``Darknet-53`` with three branches at the end that make detections at three different scales. These branches must end with the YOLO ``Region`` layer.

``Region`` layer was first introduced in the DarkNet framework. Other frameworks, including TensorFlow, do not have the ``Region`` implemented as a single layer, so every author of public YOLOv3 model creates it using simple layers. This badly affects performance. For this reason, the main idea of YOLOv3 model conversion to IR is to cut off these custom ``Region`` -like parts of the model and complete the model with the ``Region`` layers where required.

Dump YOLOv3 TensorFlow\* Model
------------------------------

To dump TensorFlow model out of `https://github.com/mystic123/tensorflow-yolo-v3 <https://github.com/mystic123/tensorflow-yolo-v3>`__ GitHub repository (commit ed60b90), follow the instructions below:

#. Clone the repository:
   
   
   
   .. ref-code-block:: cpp
   
   	git clone https://github.com/mystic123/tensorflow-yolo-v3.git
   	cd tensorflow-yolo-v3

#. (Optional) Checkout to the commit that the conversion was tested on:
   
   
   
   .. ref-code-block:: cpp
   
   	git checkout ed60b90

#. Download `coco.names <https://github.com/AlexeyAB/darknet/blob/master/data/coco.names>`__ file from the DarkNet website **OR** use labels that fit your task.

#. Download the `yolov3.weights <https://pjreddie.com/media/files/yolov3.weights>`__ (for the YOLOv3 model) or `yolov3-tiny.weights <https://pjreddie.com/media/files/yolov3-tiny.weights>`__ (for the YOLOv3-tiny model) file **OR** use your pre-trained weights with the same structure.

#. Install PIL, which is used by the conversion script in the repo:
   
   .. ref-code-block:: cpp
   
   	pip install pillow

#. Run a converter:
   
   .. note:: This converter works with TensorFlow 1.x and numpy 1.19 or lower.



* For YOLO-v3:
  
  .. ref-code-block:: cpp
  
  	python3 convert_weights_pb.py --class_names coco.names --data_format NHWC --weights_file yolov3.weights

* For YOLOv3-tiny:
  
  .. ref-code-block:: cpp
  
  	python3 convert_weights_pb.py --class_names coco.names --data_format NHWC --weights_file yolov3-tiny.weights --tiny

At this step, you may receive a warning like ``WARNING:tensorflow:Entity <...> could not be transformed and will be executed as-is.``. To work around this issue, switch to gast 0.2.2 with the following command:

.. ref-code-block:: cpp

	pip3 install --user gast==0.2.2

If you have YOLOv3 weights trained for an input image with the size different from 416 (320, 608 or your own), please provide the ``--size`` key with the size of your image specified while running the converter. For example, run the following command for an image with size 608:

.. ref-code-block:: cpp

	python3 convert_weights_pb.py --class_names coco.names --data_format NHWC --weights_file yolov3_608.weights --size 608

Convert YOLOv3 TensorFlow Model to IR
-------------------------------------

To solve the problems explained in the `YOLOv3 architecture overview <#yolov3-overview>`__ section, use the ``yolo_v3.json`` or ``yolo_v3_tiny.json`` (depending on a model) configuration file with custom operations located in the ``<OPENVINO_INSTALL_DIR>/tools/model_optimizer/extensions/front/tf`` repository.

It consists of several attributes:



.. ref-code-block:: cpp

	[
	  {
	    "id": "TFYOLOV3",
	    "match_kind": "general",
	    "custom_attributes": {
	      "classes": 80,
	      "anchors": [10, 13, 16, 30, 33, 23, 30, 61, 62, 45, 59, 119, 116, 90, 156, 198, 373, 326],
	      "coords": 4,
	      "num": 9,
	      "masks":[[6, 7, 8], [3, 4, 5], [0, 1, 2]],
	      "entry_points": ["detector/yolo-v3/Reshape", "detector/yolo-v3/Reshape_4", "detector/yolo-v3/Reshape_8"]
	    }
	  }
	]

where:

* ``id`` and ``match_kind`` are parameters that you cannot change.

* ``custom_attributes`` is a parameter that stores all the YOLOv3 specific attributes:
  
  * ``classes``, ``coords``, ``num``, and ``masks`` are attributes that you should copy from the configuration file that was used for model training. If you used DarkNet officially shared weights, you can use ``yolov3.cfg`` or ``yolov3-tiny.cfg`` configuration file from `https://github.com/david8862/keras-YOLOv3-model-set/tree/master/cfg <https://github.com/david8862/keras-YOLOv3-model-set/tree/master/cfg>`__. Replace the default values in ``custom_attributes`` with the parameters that follow the ``[yolo]`` titles in the configuration file.
  
  * ``anchors`` is an optional parameter that is not used while inference of the model, but it used in a demo to parse ``Region`` layer output
  
  * ``entry_points`` is a node name list to cut off the model and append the Region layer with custom attributes specified above.

To generate an IR of the YOLOv3 TensorFlow model, run:



.. ref-code-block:: cpp

	 mo                                                   \
	--input_model /path/to/yolo_v3.pb                                  \
	--transformations_config front/tf/yolo_v3.json \
	--batch 1                                                          \
	--output_dir <OUTPUT_MODEL_DIR>

To generate an IR of the YOLOv3-tiny TensorFlow model, run:



.. ref-code-block:: cpp

	 mo                                                        \
	--input_model /path/to/yolo_v3_tiny.pb                                  \
	--transformations_config front/tf/yolo_v3_tiny.json \
	--batch 1                                                               \
	--output_dir <OUTPUT_MODEL_DIR>

where:

* ``--batch`` defines shape of model input. In the example, ``--batch`` is equal to 1, but you can also specify other integers larger than 1.

* ``--transformations_config`` adds missing ``Region`` layers to the model. In the IR, the ``Region`` layer has name ``RegionYolo``.

.. note:: The color channel order (RGB or BGR) of an input data should match the channel order of the model training dataset. If they are different, perform the ``RGB<->BGR`` conversion specifying the command-line parameter: ``--reverse_input_channels``. Otherwise, inference results may be incorrect. For more information about the parameter, refer to **When to Reverse Input Channels** section of :ref:`Converting a Model to Intermediate Representation (IR) <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`.

OpenVINO toolkit provides a demo that uses YOLOv3 model. For more information, refer to Object Detection C++ Demo.

Convert YOLOv1 and YOLOv2 Models to the IR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before converting Choose a YOLOv1 or YOLOv2 model version that best suits your task. Download model configuration file and corresponding weight file:

* From `DarkFlow repository <https://github.com/thtrieu/darkflow>`__ : configuration files are stored in the ``cfg`` directory, links to weight files are given in the ``README.md`` file. The files from this repository are adapted for conversion to TensorFlow using DarkFlow.

* From DarkNet website and repository: configuration files are stored in the ``cfg`` directory of the `repository <https://github.com/pjreddie/darknet>`__, links to weight files are given on the `YOLOv1 <https://pjreddie.com/darknet/yolov1/>`__ and `YOLOv2 <https://pjreddie.com/darknet/yolov2/>`__ websites.

To convert DarkNet YOLOv1 and YOLOv2 models to IR, follow the next steps:

#. `Install DarkFlow  <#install-darkflow>`__

#. `Convert DarkNet YOLOv1 or YOLOv2 model to TensorFlow <#yolov1-v2-to-tf>`__ using DarkFlow

#. `Convert TensorFlow YOLOv1 or YOLOv2 model to IR <#yolov1-v2-to-ir>`__

.. _install-darkflow:

Install DarkFlow\*
++++++++++++++++++

You need DarkFlow to convert YOLOv1 and YOLOv2 models to TensorFlow. To install DarkFlow:

#. Install DarkFlow `required dependencies <https://github.com/thtrieu/darkflow#dependencies>`__.

#. Clone DarkFlow git repository:
   
   
   
   .. ref-code-block:: cpp
   
   	git clone https://github.com/thtrieu/darkflow.git

#. Go to the root directory of the cloned repository:
   
   
   
   .. ref-code-block:: cpp
   
   	cd darkflow

#. Install DarkFlow using the instructions from the ``README.md`` file in the `DarkFlow repository <https://github.com/thtrieu/darkflow/blob/master/README.md#getting-started>`__.

.. _yolov1-v2-to-tf:

Convert DarkNet\* YOLOv1 or YOLOv2 Model to TensorFlow\*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

To convert YOLOv1 or YOLOv2 model to TensorFlow, go to the root directory of the cloned DarkFlow repository, place downloaded above \*.cfg and \*.weights files in the current directory and run the following command:



* For YOLOv1:
  
  .. ref-code-block:: cpp
  
  	python3 flow --model yolov1.cfg --load yolov1.weights --savepb

* For YOLOv2 with VOC dataset ``--labels`` argument should be specified and additional changes in the original exporting script are required. In the file `https://github.com/thtrieu/darkflow/blob/b187c65/darkflow/utils/loader.py#L121 <https://github.com/thtrieu/darkflow/blob/b187c65630f9aa1bb8b809c33ec67c8cc5d60124/darkflow/utils/loader.py#L121>`__ change line 121 from ``self.offset = 16`` to ``self.offset = 20``. Then run:
  
  .. ref-code-block:: cpp
  
  	python3 flow --model yolov2-voc.cfg --load yolov2-voc.weights --labels voc-labels.txt --savepb

VOC labels can be found on the following link `https://raw.githubusercontent.com/szaza/android-yolo-v2/master/assets/tiny-yolo-voc-labels.txt <https://raw.githubusercontent.com/szaza/android-yolo-v2/master/assets/tiny-yolo-voc-labels.txt>`__

General conversion command is:

.. ref-code-block:: cpp

	python3 flow --model <path_to_model>/<model_name>.cfg --load <path_to_model>/<model_name>.weights --labels <path_to_dataset_labels_file> --savepb

For YOLOv1 the argument ``--labels`` can be skipped. If the model was successfully converted, you can find the ``<model_name>.meta`` and ``<model_name>.pb`` files in ``built_graph`` subdirectory of the cloned DarkFlow repository.

File ``<model_name>.pb`` is a TensorFlow representation of the YOLO model.

.. _yolov1-v2-to-ir:

Convert TensorFlow YOLOv1 or YOLOv2 Model to the IR
+++++++++++++++++++++++++++++++++++++++++++++++++++

Converted TensorFlow YOLO model is missing ``Region`` layer and its parameters. Original YOLO ``Region`` layer parameters are stored in the configuration ``<path_to_model>/<model_name>.cfg`` file under the ``[region]`` title.

To recreate the original model structure, use the corresponding yolo ``.json`` configuration file with custom operations and ``Region`` layer parameters when converting the model to the IR. This file is located in the ``<OPENVINO_INSTALL_DIR>/tools/model_optimizer/extensions/front/tf`` directory.

If chosen model has specific values of this parameters, create another configuration file with custom operations and use it for conversion.

To generate the IR of the YOLOv1 model, provide TensorFlow YOLOv1 or YOLOv2 model to the Model Optimizer with the following parameters:



.. ref-code-block:: cpp

	 mo
	--input_model <path_to_model>/<model_name>.pb       \
	--batch 1                                       \
	--scale 255 \
	--transformations_config front/tf/<yolo_config>.json

where:

* ``--batch`` defines shape of model input. In the example, ``--batch`` is equal to 1, but you can also specify other integers larger than 1.

* ``--scale`` specifies scale factor that input values will be divided by. The model was trained with input values in the range ``[0,1]``. OpenVINO toolkit samples read input images as values in ``[0,255]`` range, so the scale 255 must be applied.

* ``--transformations_config`` adds missing ``Region`` layers to the model. In the IR, the ``Region`` layer has name ``RegionYolo``. For other applicable parameters, refer to :ref:`Convert Model from TensorFlow <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__tensor_flow>`.

.. note:: The color channel order (RGB or BGR) of an input data should match the channel order of the model training dataset. If they are different, perform the ``RGB<->BGR`` conversion specifying the command-line parameter: ``--reverse_input_channels``. Otherwise, inference results may be incorrect. For more information about the parameter, refer to **When to Reverse Input Channels** section of :ref:`Converting a Model to Intermediate Representation (IR) <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`.

