.. index:: pair: page; Hello Reshape SSD Python\* Sample
.. _doxid-openvino_inference_engine_ie_bridges_python_sample_hello_reshape_ssd__r_e_a_d_m_e:


Hello Reshape SSD Python\* Sample
=================================

:target:`doxid-openvino_inference_engine_ie_bridges_python_sample_hello_reshape_ssd__r_e_a_d_m_e_1md_openvino_samples_python_hello_reshape_ssd_readme` This sample demonstrates how to do synchronous inference of object detection models using :ref:`Shape Inference feature <doxid-openvino_docs__o_v__u_g__shape_inference>`.

Models with only 1 input and output are supported.

The following Python API is used in the application:

.. list-table::
    :header-rows: 1

    * - Feature
      - API
      - Description
    * - Model Operations
      - [openvino.runtime.Model.reshape], `openvino.runtime.Model.input <[openvino.runtime.Output.get_any_name]:>`__ , [openvino.runtime.Output.get_any_name], [openvino.runtime.PartialShape]
      - Managing of model

Basic OpenVINO™ Runtime API is covered by :ref:`Hello Classification Python\* Sample <doxid-openvino_inference_engine_ie_bridges_python_sample_hello_classification__r_e_a_d_m_e>`.

.. list-table::
    :header-rows: 1

    * - Options
      - Values
    * - Validated Models
      - mobilenet-ssd
    * - Validated Layout
      - NCHW
    * - Model Format
      - OpenVINO™ toolkit Intermediate Representation (.xml + .bin), ONNX (.onnx)
    * - Supported devices
      - :ref:`All <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`
    * - Other language realization
      - :ref:`C++ <doxid-openvino_inference_engine_samples_hello_reshape_ssd__r_e_a_d_m_e>`

How It Works
~~~~~~~~~~~~

At startup, the sample application reads command-line parameters, prepares input data, loads a specified model and image to the OpenVINO™ Runtime plugin, performs synchronous inference, and processes output data.

As a result, the program creates an output image, logging each step in a standard output stream.

You can see the explicit description of each sample step at :ref:`Integration Steps <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>` section of "Integrate OpenVINO™ Runtime with Your Application" guide.

Running
~~~~~~~

.. ref-code-block:: cpp

	python hello_reshape_ssd.py <path_to_model> <path_to_image> <device_name>

To run the sample, you need specify a model and image:

* you can use public or Intel's pre-trained models from the Open Model Zoo. The models can be downloaded using the Model Downloader.

* you can use images from the media files collection available at `https://storage.openvinotoolkit.org/data/test_data <https://storage.openvinotoolkit.org/data/test_data>`__.

**NOTES** :

* By default, OpenVINO™ Toolkit Samples and demos expect input with BGR channels order. If you trained your model to work with RGB order, you need to manually rearrange the default channels order in the sample or demo application or reconvert your model using the Model Optimizer tool with ``--reverse_input_channels`` argument specified. For more information about the argument, refer to **When to Reverse Input Channels** section of :ref:`Embedding Preprocessing Computation <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`.

* Before running the sample with a trained model, make sure the model is converted to the intermediate representation (IR) format (\*.xml + \*.bin) using the :ref:`Model Optimizer tool <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`.

* The sample accepts models in ONNX format (.onnx) that do not require preprocessing.

Example
-------

#. Install the ``openvino-dev`` Python package to use Open Model Zoo Tools:

.. ref-code-block:: cpp

	python -m pip install openvino-dev[caffe,onnx,tensorflow2,pytorch,mxnet]

#. Download a pre-trained model:
   
   .. ref-code-block:: cpp
   
   	omz_downloader --name ssdlite_mobilenet_v2

#. If a model is not in the IR or ONNX format, it must be converted. You can do this using the model converter:

.. ref-code-block:: cpp

	omz_converter --name ssdlite_mobilenet_v2

#. Perform inference of ``banana.jpg`` using ``ssdlite_mobilenet_v2`` model on a ``GPU``, for example:

.. ref-code-block:: cpp

	python hello_reshape_ssd.py ssdlite_mobilenet_v2.xml banana.jpg GPU

Sample Output
~~~~~~~~~~~~~

The sample application logs each step in a standard output stream and creates an output image, drawing bounding boxes for inference results with an over 50% confidence.

.. ref-code-block:: cpp

	[ INFO ] Creating OpenVINO Runtime Core
	[ INFO ] Reading the model: C:/test_data/models/ssdlite_mobilenet_v2.xml
	[ INFO ] Reshaping the model to the height and width of the input image
	[ INFO ] Loading the model to the plugin
	[ INFO ] Starting inference in synchronous mode
	[ INFO ] Found: class_id = 52, confidence = 0.98, coords = (21, 98), (276, 210)
	[ INFO ] Image out.bmp was created!
	[ INFO ] This sample is an API example, for any performance measurements please use the dedicated benchmark_app tool

See Also
~~~~~~~~

* :ref:`Integrate the OpenVINO™ Runtime with Your Application <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`

* :ref:`Using OpenVINO™ Toolkit Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

* Model Downloader

* :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`

