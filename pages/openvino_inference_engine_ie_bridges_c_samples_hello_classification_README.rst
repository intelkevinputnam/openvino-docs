.. index:: pair: page; Hello Classification C Sample
.. _doxid-openvino_inference_engine_ie_bridges_c_samples_hello_classification__r_e_a_d_m_e:


Hello Classification C Sample
=============================

:target:`doxid-openvino_inference_engine_ie_bridges_c_samples_hello_classification__r_e_a_d_m_e_1md_openvino_samples_c_hello_classification_readme` This sample demonstrates how to execute an inference of image classification networks like AlexNet and GoogLeNet using Synchronous Inference Request API and input auto-resize feature.

Hello Classification C sample application demonstrates how to use the following Inference Engine C API in applications:

.. list-table::
    :header-rows: 1

    * - Feature
      - API
      - Description
    * - Basic Infer Flow
      - `ie_core_create <https://docs.openvino.ai/latest/ie_c_api/group__Core.html#gaab73c7ee3704c742eaac457636259541>`__ , `ie_core_read_network <https://docs.openvino.ai/latest/ie_c_api/group__Core.html#gaa40803295255b3926a3d1b8924f26c29>`__ , `ie_core_load_network <https://docs.openvino.ai/latest/ie_c_api/group__Core.html#ga318d4b0214b8a3fd33f9e44170befcc5>`__ , `ie_exec_network_create_infer_request <https://docs.openvino.ai/latest/ie_c_api/group__ExecutableNetwork.html#gae72247391c1429a18c367594a4b7db9f>`__ , `ie_infer_request_set_blob <https://docs.openvino.ai/latest/ie_c_api/group__InferRequest.html#ga891c2d475501bba761148a0c3faca196>`__ , `ie_infer_request_get_blob <https://docs.openvino.ai/latest/ie_c_api/group__InferRequest.html#ga6cd04044ea95987260037bfe17ce1a2d>`__
      - Common API to do inference: configure input and output blobs, loading model, create infer request
    * - Synchronous Infer
      - `ie_infer_request_infer <https://docs.openvino.ai/latest/ie_c_api/group__InferRequest.html#gac6c6fcb67ccb4d0ec9ad1c63a5bee7b6>`__
      - Do synchronous inference
    * - Network Operations
      - `ie_network_get_input_name <https://docs.openvino.ai/latest/ie_c_api/group__Network.html#ga36b0c28dfab6db2bfcc2941fd57fbf6d>`__ , `ie_network_get_inputs_number <https://docs.openvino.ai/latest/ie_c_api/group__Network.html#ga6a3349bca66c4ba8b41a434061fccf52>`__ , `ie_network_get_outputs_number <https://docs.openvino.ai/latest/ie_c_api/group__Network.html#ga869b8c309797f1e09f73ddffd1b57509>`__ , `ie_network_set_input_precision <https://docs.openvino.ai/latest/ie_c_api/group__Network.html#gadd99b7cc98b3c33daa2095b8a29f66d7>`__ , `ie_network_get_output_name <https://docs.openvino.ai/latest/ie_c_api/group__Network.html#ga1feabc49576db24d9821a150b2b50a6c>`__ , `ie_network_get_output_precision <https://docs.openvino.ai/latest/ie_c_api/group__Network.html#gaeaa7f1fb8f56956fc492cd9207235984>`__
      - Managing of network
    * - Blob Operations
      - `ie_blob_make_memory_from_preallocated <https://docs.openvino.ai/latest/ie_c_api/group__Blob.html#ga7a874d46375e10fa1a7e8e3d7e1c9c9c>`__ , `ie_blob_get_dims <https://docs.openvino.ai/latest/ie_c_api/group__Blob.html#ga25d93efd7ec1052a8896ac61cc14c30a>`__ , `ie_blob_get_cbuffer <https://docs.openvino.ai/latest/ie_c_api/group__Blob.html#gaf6b4a110b4c5723dcbde135328b3620a>`__
      - Work with memory container for storing inputs, outputs of the network, weights and biases of the layers
    * - Input auto-resize
      - `ie_network_set_input_resize_algorithm <https://docs.openvino.ai/latest/ie_c_api/group__Network.html#ga46ab3b3a06359f2b77f58bdd6e8a5492>`__ , `ie_network_set_input_layout <https://docs.openvino.ai/latest/ie_c_api/group__Network.html#ga27ea9f92290e0b2cdedbe8a85feb4c01>`__
      - Set image of the original size as input for a network with other input size. Resize and layout conversions will be performed automatically by the corresponding plugin just before inference

.. list-table::
    :header-rows: 1

    * - Options
      - Values
    * - Validated Models
      - alexnet, googlenet-v1
    * - Model Format
      - Inference Engine Intermediate Representation (\*.xml + \*.bin), ONNX (\*.onnx)
    * - Validated images
      - The sample uses OpenCV\* to `read input image <https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56>`__ (\*.bmp, \*.png)
    * - Supported devices
      - :ref:`All <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`
    * - Other language realization
      - :ref:`C++ <doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e>` , :ref:`Python <doxid-openvino_inference_engine_ie_bridges_python_sample_hello_classification__r_e_a_d_m_e>`

How It Works
~~~~~~~~~~~~

Upon the start-up, the sample application reads command line parameters, loads specified network and an image to the Inference Engine plugin. Then, the sample creates an synchronous inference request object. When inference is done, the application outputs data to the standard output stream.

You can see the explicit description of each sample step at :ref:`Integration Steps <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>` section of "Integrate OpenVINO™ Runtime with Your Application" guide.

Building
~~~~~~~~

To build the sample, please use instructions available at :ref:`Build the Sample Applications <doxid-openvino_docs__o_v__u_g__samples__overview>` section in Inference Engine Samples guide.

Running
~~~~~~~

To run the sample, you need specify a model and image:

* you can use public or Intel's pre-trained models from the Open Model Zoo. The models can be downloaded using the Model Downloader.

* you can use images from the media files collection available at `https://storage.openvinotoolkit.org/data/test_data <https://storage.openvinotoolkit.org/data/test_data>`__.

**NOTES** :

* By default, OpenVINO™ Toolkit Samples and Demos expect input with BGR channels order. If you trained your model to work with RGB order, you need to manually rearrange the default channels order in the sample or demo application or reconvert your model using the Model Optimizer tool with ``--reverse_input_channels`` argument specified. For more information about the argument, refer to **When to Reverse Input Channels** section of :ref:`Embedding Preprocessing Computation <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`.

* Before running the sample with a trained model, make sure the model is converted to the Inference Engine format (\*.xml + \*.bin) using the :ref:`Model Optimizer tool <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`.

* The sample accepts models in ONNX format (\*.onnx) that do not require preprocessing.

Example
-------

#. Download a pre-trained model using Model Downloader:
   
   .. ref-code-block:: cpp
   
   	python <path_to_omz_tools>/downloader.py --name alexnet

#. If a model is not in the Inference Engine IR or ONNX format, it must be converted. You can do this using the model converter script:

.. ref-code-block:: cpp

	python <path_to_omz_tools>/converter.py --name alexnet

#. Perform inference of ``car.bmp`` using ``alexnet`` model on a ``GPU``, for example:

.. ref-code-block:: cpp

	<path_to_sample>/hello_classification_c <path_to_model>/alexnet.xml <path_to_image>/car.bmp GPU

Sample Output
~~~~~~~~~~~~~

The application outputs top-10 inference results.

.. ref-code-block:: cpp

	Top 10 results:
	
	Image /opt/intel/openvino/samples/scripts/car.png
	
	classid probability
	------- -----------
	656       0.666479
	654       0.112940
	581       0.068487
	874       0.033385
	436       0.026132
	817       0.016731
	675       0.010980
	511       0.010592
	569       0.008178
	717       0.006336
	
	This sample is an API example, for any performance measurements please use the dedicated benchmark_app tool

See Also
~~~~~~~~

* :ref:`Integrate OpenVINO™ into Your Application <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`

* :ref:`Using OpenVINO™ Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

* Model Downloader

* :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`

