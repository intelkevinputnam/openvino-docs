.. index:: pair: page; Converting a PyTorch\* Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__py_torch:


Converting a PyTorch\* Model
============================

.. _typical-pytorch:

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__py_torch_1md_openvino_docs_mo_dg_prepare_model_convert_model_convert_model_from_pytorch`

Typical Steps to Convert PyTorch Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyTorch\* framework is supported through export to ONNX\* format. A summary of the steps for optimizing and deploying a model that was trained with the PyTorch\* framework:

#. `Export PyTorch model to ONNX\* <#export-to-onnx>`__.

#. :ref:`Convert an ONNX\\* model <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__o_n_n_x>` to produce an optimized :ref:`Intermediate Representation (IR) <doxid-openvino_docs__m_o__d_g__i_r_and_opsets>` of the model based on the trained network topology, weights, and biases values.

.. _export-to-onnx:

Export PyTorch\* Model to ONNX\* Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyTorch models are defined in a Python\* code, to export such models use ``torch.onnx.export()`` method. Usually code to evaluate or test the model is provided with the model code and can be used to initialize and export model. Only the basics will be covered here, the step to export to ONNX\* is crucial but it is covered by PyTorch\* framework. For more information, please refer to `Exporting PyTorch models to ONNX format <https://pytorch.org/docs/stable/onnx.html>`__.

To export a PyTorch\* model you need to obtain the model as an instance of ``torch.nn.Module`` class and call the ``export`` function.

.. ref-code-block:: cpp

	import torch
	
	# Instantiate your model. This is just a regular PyTorch model that will be exported in the following steps.
	model = SomeModel()
	# Evaluate the model to switch some operations from training mode to inference.
	model.eval()
	# Create dummy input for the model. It will be used to run the model inside export function.
	dummy_input = torch.randn(1, 3, 224, 224)
	# Call the export function
	torch.onnx.export(model, (dummy_input, ), 'model.onnx')

Known Issues
~~~~~~~~~~~~

* Not all PyTorch\* operations can be exported to ONNX\* opset 9 which is used by default, as of version 1.8.1. It is recommended to export models to opset 11 or higher when export to default opset 9 is not working. In that case, use ``opset_version`` option of the ``torch.onnx.export``. For more information about ONNX\* opset, refer to the `Operator Schemas <https://github.com/onnx/onnx/blob/master/docs/Operators.md>`__.

See Also
~~~~~~~~

:ref:`Model Conversion Tutorials <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tutorials>`

