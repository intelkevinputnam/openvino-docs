.. index:: pair: page; Overview of Inference Engine Plugin Library
.. _doxid-openvino_docs_ie_plugin_dg_overview:


Overview of Inference Engine Plugin Library
===========================================

:target:`doxid-openvino_docs_ie_plugin_dg_overview_1md_openvino_docs_ie_plugin_dg_intro`





.. toctree::
   :maxdepth: 1
   :caption: Converting and Preparing Models
   :hidden:

   Implement Plugin Functionality <openvino_docs_ie_plugin_dg_plugin>
   Implement Executable Network Functionality <openvino_docs_ie_plugin_dg_executable_network>
   Implement Synchronous Inference Request <openvino_docs_ie_plugin_dg_infer_request>
   Implement Asynchronous Inference Request <openvino_docs_ie_plugin_dg_async_infer_request>
   openvino_docs_ie_plugin_dg_plugin_build
   openvino_docs_ie_plugin_dg_plugin_testing
   openvino_docs_ie_plugin_detailed_guides
   openvino_docs_ie_plugin_api_references

The plugin architecture of the Inference Engine allows to develop and plug independent inference solutions dedicated to different devices. Physically, a plugin is represented as a dynamic library exporting the single ``CreatePluginEngine`` function that allows to create a new plugin instance.

Inference Engine Plugin Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inference Engine plugin dynamic library consists of several main components:

#. :ref:`Plugin class <doxid-openvino_docs_ie_plugin_dg_plugin>` :
   
   * Provides information about devices of a specific type.
   
   * Can create an :ref:`executable network <doxid-openvino_docs_ie_plugin_dg_executable_network>` instance which represents a Neural Network backend specific graph structure for a particular device in opposite to the :ref:`InferenceEngine::ICNNNetwork <doxid-class_inference_engine_1_1_i_c_n_n_network>` interface which is backend-independent.
   
   * Can import an already compiled graph structure from an input stream to an :ref:`executable network <doxid-openvino_docs_ie_plugin_dg_executable_network>` object.

#. :ref:`Executable Network class <doxid-openvino_docs_ie_plugin_dg_executable_network>` :
   
   * Is an execution configuration compiled for a particular device and takes into account its capabilities.
   
   * Holds a reference to a particular device and a task executor for this device.
   
   * Can create several instances of :ref:`Inference Request <doxid-openvino_docs_ie_plugin_dg_infer_request>`.
   
   * Can export an internal backend specific graph structure to an output stream.

#. :ref:`Inference Request class <doxid-openvino_docs_ie_plugin_dg_infer_request>` :
   
   * Runs an inference pipeline serially.
   
   * Can extract performance counters for an inference pipeline execution profiling.

#. :ref:`Asynchronous Inference Request class <doxid-openvino_docs_ie_plugin_dg_async_infer_request>` :
   
   * Wraps the :ref:`Inference Request <doxid-openvino_docs_ie_plugin_dg_infer_request>` class and runs pipeline stages in parallel on several task executors based on a device-specific pipeline structure.

.. note:: This documentation is written based on the ``Template`` plugin, which demonstrates plugin



development details. Find the complete code of the ``Template``, which is fully compilable and up-to-date, at ``<dldt source dir>/docs/template_plugin``.

Detailed guides
~~~~~~~~~~~~~~~

* :ref:`Build <doxid-openvino_docs_ie_plugin_dg_plugin_build>` a plugin library using CMake\*

* Plugin and its components :ref:`testing <doxid-openvino_docs_ie_plugin_dg_plugin_testing>`

* :ref:`Quantized networks <doxid-openvino_docs_ie_plugin_dg_quantized_networks>`

* :ref:`Low precision transformations <doxid-openvino_docs__o_v__u_g_lpt>` guide

* :ref:`Writing OpenVINO™ transformations <doxid-openvino_docs_transformations>` guide

API References
~~~~~~~~~~~~~~

* :ref:`Inference Engine Plugin API <doxid-group__ie__dev__api>`

* :ref:`Inference Engine Transformation API <doxid-group__ie__transformation__api>`

