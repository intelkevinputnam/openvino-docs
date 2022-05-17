.. index:: pair: page; Post-training Optimization Tool Frequently Asked Questions
.. _doxid-pot_docs__frequently_asked_questions:


Post-training Optimization Tool Frequently Asked Questions
==========================================================

:target:`doxid-pot_docs__frequently_asked_questions_1md_openvino_tools_pot_docs_frequentlyaskedquestions` If your question is not covered below, use the `OpenVINO™ Community Forum page <https://community.intel.com/t5/Intel-Distribution-of-OpenVINO/bd-p/distribution-openvino-toolkit>`__, where you can participate freely.

* `Is the Post-training Optimization Tool opensourced? <#opensourced>`__

* `Can I quantize my model without a dataset? <#dataset>`__

* `Can a model in any framework be quantized by the POT? <#framework>`__

* `What is a tradeoff when you go to low precision? <#tradeoff>`__

* `I'd like to quantize a model and I've converted it to IR but I don't have the Accuracy Checker config. What can I do? <#noac>`__

* `I tried all recommendations from "Post-Training Optimization Best Practices" but either have a high accuracy drop or bad performance after quantization. What else can I do? <#nncf>`__

* `I get “RuntimeError: Cannot get memory” and “RuntimeError: Output data was not allocated” when I quantize my model by the POT. <#memory>`__

* `I have successfully quantized my model with a low accuracy drop and improved performance but the output video generated from the low precision model is much worse than from the full precision model. What could be the root cause? <#quality>`__

* `The quantization process of my model takes a lot of time. Can it be decreased somehow? <#longtime>`__

* `I get "Import Error:... No such file or directory". How can I avoid it? <#import>`__

* `When I execute POT CLI, I get "File "/workspace/venv/lib/python3.6/site-packages/nevergrad/optimization/base.py", line 35... SyntaxError: invalid syntax". What is wrong? <#python>`__

* `What does a message "ModuleNotFoundError: No module named 'some\_module\_name'" mean? <#nomodule>`__

* `Is there a way to collect an intermidiate IR when the AccuracyAware mechanism fails? <#dump>`__

.. _#outputs:

* :target:`doxid-pot_docs__frequently_asked_questions_1#outputs` What do the messages "Output name: <result_operation_name> not found" or "Output node with <result_operation_name> is not found in graph" mean?

.. _opensourced:

Is the Post-training Optimization Tool (POT) opensourced?
---------------------------------------------------------

Yes, POT is developed on GitHub as a part of `https://github.com/openvinotoolkit/openvino <https://github.com/openvinotoolkit/openvino>`__ under Apache-2.0 License.

.. _dataset:

Can I quantize my model without a dataset?
------------------------------------------

In general, you should have a dataset. The dataset should be annotated if you want to validate the accuracy. If your dataset is not annotated, you can use :ref:`Default Quantization <doxid-pot_default_quantization_usage>` to quantize the model or command-line interface with :ref:`Simplified mode <doxid-pot_docs_simplified_mode>`.

.. _framework:

Can a model in any framework be quantized by the POT?
-----------------------------------------------------

The POT accepts models in the OpenVINO Intermediate Representation (IR) format only. For that you need to convert your model to the IR format using :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`.

.. _noac:

I'd like to quantize a model and I've converted it to IR but I don't have the Accuracy Checker config. What can I do?
---------------------------------------------------------------------------------------------------------------------

#. Try quantization using Python\* API of the Post-training Optimization Tool. For more details see [Default Quantization](:ref:`Quantizing Model <doxid-pot_default_quantization_usage>`.

#. If you consider command-line usage only refer to Accuracy Checker documentation to create the Accuracy Checker configuration file, and try to find the configuration file for your model among the ones available in the Accuracy Checker examples.

#. An alternative way is to quantize the model in the `Simplified mode <#ref pot_docs_simplified_mode>`__ but you will not be able to measure the accuracy.

.. _tradeoff:

What is a tradeoff when you go to low precision?
------------------------------------------------

The tradeoff is between the accuracy drop and performance. When a model is in low precision, it is usually performed compared to the same model in full precision but the accuracy might be worse. You can find some benchmarking results in :ref:`INT8 vs FP32 Comparison on Select Networks and Platforms <doxid-openvino_docs_performance_int8_vs_fp32>`. The other benefit of having a model in low precision is its smaller size.

.. _nncf:

I tried all recommendations from "Post-Training Optimization Best Practices" but either have a high accuracy drop or bad performance after quantization. What else can I do?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First of all, you should validate the POT compression pipeline you are running, which can be done with the following steps:

#. Make sure the accuracy of the original uncompressed model has the value you expect. Run your POT pipeline with an empty compression config and evaluate the resulting model metric. Compare this uncompressed model accuracy metric value with your reference.

#. Run your compression pipeline with a single compression algorithm (:ref:`Default Quantization <doxid-pot_default_quantization_usage>` or :ref:`Accuracy-aware Quantization <doxid-pot_accuracyaware_usage>`) without any parameter values specified in the config (except for ``preset`` and ``stat_subset_size``). Make sure you get the desirable accuracy drop/performance gain in this case.

Finally, if you have done the steps above and the problem persists, you could try to compress your model using the `Neural Network Compression Framework (NNCF) <https://github.com/openvinotoolkit/nncf_pytorch>`__. Note that NNCF usage requires you to have a PyTorch or TensorFlow 2 based training pipeline of your model to perform Quantization-aware Training. See :ref:`Model Optimization Guide <doxid-openvino_docs_model_optimization_guide>` for more details.

.. _memory:

I get “RuntimeError: Cannot get memory” and “RuntimeError: Output data was not allocated” when I quantize my model by the POT.
--------------------------------------------------------------------------------------------------------------------------------------

These issues happen due to insufficient available amount of memory for statistics collection during the quantization process of a huge model or due to a very high resolution of input images in the quantization dataset. If you do not have a possibility to increase your RAM size, one of the following options can help:

* Set ``inplace_statistic`` parameters to "True". In that case the POT will change method collect statistics and use less memory. Note that such change might increase time required for quantization.

* Set ``eval_requests_number`` and ``stat_requests_number`` parameters to 1. In that case the POT will limit the number of infer requests by 1 and use less memory. Note that such change might increase time required for quantization.

* Set ``use_fast_bias`` parameter to ``false``. In that case the POT will switch from the FastBiasCorrection algorithm to the full BiasCorrection algorithm which is usually more accurate and takes more time but requires less memory. See :ref:`Post-Training Optimization Best Practices <doxid-pot_docs__best_practices>` for more details.

* Reshape your model to a lower resolution and resize the size of images in the dataset. Note that such change might impact the accuracy.

.. _quality:

I have successfully quantized my model with a low accuracy drop and improved performance but the output video generated from the low precision model is much worse than from the full precision model. What could be the root cause?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It can happen due to the following reasons:

* A wrong or not representative dataset was used during the quantization and accuracy validation. Please make sure that your data and labels are correct and they sufficiently reflect the use case.

* If the command-line interface was used for quantization, a wrong Accuracy Checker configuration file could lead to this problem. Refer to Accuracy Checker documentation for more information.

* If :ref:`Default Quantization <doxid-pot_default_quantization_usage>` was used for quantization you can also try :ref:`Accuracy-aware Quantization <doxid-pot_accuracyaware_usage>` method that allows controlling maximum accuracy deviation.

.. _longtime:

The quantization process of my model takes a lot of time. Can it be decreased somehow?
--------------------------------------------------------------------------------------

Quantization time depends on multiple factors such as the size of the model and the dataset. It also depends on the algorithm: the :ref:`Default Quantization <doxid-pot_default_quantization_usage>` algorithm takes less time than the [:ref:`Accuracy-aware Quantization <doxid-pot_accuracyaware_usage>` algorithm. The following configuration parameters also impact the quantization time duration (see details in :ref:`Post-Training Optimization Best Practices <doxid-pot_docs__best_practices>`):

* ``use_fast_bias`` : when set to ``false``, it increases the quantization time

* ``stat_subset_size`` : the higher the value of this parameter, the more time will be required for the quantization

* ``tune_hyperparams`` : if set to ``true`` when the AccuracyAwareQuantization algorithm is used, it increases the quantization time

* ``stat_requests_number`` : the lower number, the more time might be required for the quantization

* ``eval_requests_number`` : the lower number, the more time might be required for the quantization Note that higher values of ``stat_requests_number`` and ``eval_requests_number`` increase memory consumption by POT.

.. _python:

When I execute POT CLI, I get "File "/workspace/venv/lib/python3.6/site-packages/nevergrad/optimization/base.py", line 35... SyntaxError: invalid syntax". What is wrong?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This error is reported when you have a Python version older than 3.6 in your environment. Upgrade your Python version.

.. _nomodule:

What does a message "ModuleNotFoundError: No module named 'some\_module\_name'" mean?
-------------------------------------------------------------------------------------

It means that some required python module is not installed in your environment. To install it, run ``pip install some_module_name``.

.. _dump:

Is there a way to collect an intermidiate IR when the AccuracyAware mechanism fails?
------------------------------------------------------------------------------------

You can add ``"dump_intermediate_model": true`` to the POT configuration file and it will drop an intermidiate IR to ``accuracy_aware_intermediate`` folder.

.. _outputs:

What do the messages "Output name: <result_operation_name> not found" or "Output node with <result_operation_name> is not found in graph" mean?
-----------------------------------------------------------------------------------------------------------------------------------------------

Errors are caused by missing output nodes names in a graph when using the POT tool for model quantization. It might appear for some models only for IRs converted from ONNX models using new frontend (which is the default conversion path starting from 2022.1 release). To avoid such errors, use legacy MO frontend to convert a model to IR by passing the use_legacy_frontend option. Then, use the produced IR for quantization.

