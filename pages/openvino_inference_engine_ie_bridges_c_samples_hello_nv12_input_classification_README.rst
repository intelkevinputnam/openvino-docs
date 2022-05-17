.. index:: pair: page; Hello NV12 Input Classification C Sample
.. _doxid-openvino_inference_engine_ie_bridges_c_samples_hello_nv12_input_classification__r_e_a_d_m_e:


Hello NV12 Input Classification C Sample
========================================

:target:`doxid-openvino_inference_engine_ie_bridges_c_samples_hello_nv12_input_classification__r_e_a_d_m_e_1md_openvino_samples_c_hello_nv12_input_classification_readme` This sample demonstrates how to execute an inference of image classification networks like AlexNet with images in NV12 color format using Synchronous Inference Request API.

Hello NV12 Input Classification C Sample demonstrates how to use the NV12 automatic input pre-processing API of the Inference Engine in your applications:

.. list-table::
    :header-rows: 1

    * - Feature
      - API
      - Description
    * - Blob Operations
      - `ie_blob_make_memory_nv12 <https://docs.openvino.ai/latest/ie_c_api/group__Blob.html#ga0a2d97b0d40a53c01ead771f82ae7f4a>`__
      - Create a NV12 blob
    * - Input in N12 color format
      - `ie_network_set_color_format <https://docs.openvino.ai/latest/ie_c_api/group__Network.html#ga85f3251f1f7b08507c297e73baa58969>`__
      - Change the color format of the input data

Basic Inference Engine API is covered by :ref:`Hello Classification C sample <doxid-openvino_inference_engine_ie_bridges_c_samples_hello_classification__r_e_a_d_m_e>`.

.. list-table::
    :header-rows: 1

    * - Options
      - Values
    * - Validated Models
      - alexnet
    * - Model Format
      - Inference Engine Intermediate Representation (\*.xml + \*.bin), ONNX (\*.onnx)
    * - Validated images
      - An uncompressed image in the NV12 color format - \*.yuv
    * - Supported devices
      - :ref:`All <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`
    * - Other language realization
      - :ref:`C++ <doxid-openvino_inference_engine_samples_hello_nv12_input_classification__r_e_a_d_m_e>`

How It Works
~~~~~~~~~~~~

Upon the start-up, the sample application reads command-line parameters, loads specified network and an image in the NV12 color format to an Inference Engine plugin. Then, the sample creates an synchronous inference request object. When inference is done, the application outputs data to the standard output stream.

You can see the explicit description of each sample step at :ref:`Integration Steps <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>` section of "Integrate OpenVINO™ Runtime with Your Application" guide.

Building
~~~~~~~~

To build the sample, please use instructions available at :ref:`Build the Sample Applications <doxid-openvino_docs__o_v__u_g__samples__overview>` section in Inference Engine Samples guide.

Running
~~~~~~~

To run the sample, you need specify a model and image:

* you can use public or Intel's pre-trained models from the Open Model Zoo. The models can be downloaded using the Model Downloader.

* you can use images from the media files collection available at `https://storage.openvinotoolkit.org/data/test_data <https://storage.openvinotoolkit.org/data/test_data>`__.

The sample accepts an uncompressed image in the NV12 color format. To run the sample, you need to convert your BGR/RGB image to NV12. To do this, you can use one of the widely available tools such as FFmpeg\* or GStreamer\*. The following command shows how to convert an ordinary image into an uncompressed NV12 image using FFmpeg:

.. ref-code-block:: cpp

	ffmpeg -i cat.jpg -pix_fmt nv12 cat.yuv

**NOTES** :

* Because the sample reads raw image files, you should provide a correct image size along with the image path. The sample expects the logical size of the image, not the buffer size. For example, for 640x480 BGR/RGB image the corresponding NV12 logical image size is also 640x480, whereas the buffer size is 640x720.

* By default, this sample expects that network input has BGR channels order. If you trained your model to work with RGB order, you need to reconvert your model using the Model Optimizer tool with ``--reverse_input_channels`` argument specified. For more information about the argument, refer to **When to Reverse Input Channels** section of :ref:`Embedding Preprocessing Computation <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`.

* Before running the sample with a trained model, make sure the model is converted to the Inference Engine format (\*.xml + \*.bin) using the :ref:`Model Optimizer tool <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`.

* The sample accepts models in ONNX format (.onnx) that do not require preprocessing.

Example
-------

#. Download a pre-trained model using Model Downloader:
   
   .. ref-code-block:: cpp
   
   	python <path_to_omz_tools>/downloader.py --name alexnet

#. If a model is not in the Inference Engine IR or ONNX format, it must be converted. You can do this using the model converter script:

.. ref-code-block:: cpp

	python <path_to_omz_tools>/converter.py --name alexnet

#. Perform inference of NV12 image using ``alexnet`` model on a ``CPU``, for example:

.. ref-code-block:: cpp

	<path_to_sample>/hello_nv12_input_classification_c <path_to_model>/alexnet.xml <path_to_image>/cat.yuv 300x300 CPU

Sample Output
~~~~~~~~~~~~~

The application outputs top-10 inference results.

.. ref-code-block:: cpp

	Top 10 results:
	
	Image ./cat.yuv
	
	classid probability
	------- -----------
	435       0.091733
	876       0.081725
	999       0.069305
	587       0.043726
	666       0.038957
	419       0.032892
	285       0.030309
	700       0.029941
	696       0.021628
	855       0.020339
	
	This sample is an API example, for any performance measurements please use the dedicated benchmark_app tool

See Also
~~~~~~~~

* :ref:`Integrate the OpenVINO™ into Your Application <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`

* :ref:`Using OpenVINO™ Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

* Model Downloader

* :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`

