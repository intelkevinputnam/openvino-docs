.. index:: pair: page; Converting a PaddlePaddle\* Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__paddle:


Converting a PaddlePaddle\* Model
=================================

.. _Convert_From_Paddle:

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__paddle_1md_openvino_docs_mo_dg_prepare_model_convert_model_convert_model_from_paddle`

Convert a PaddlePaddle Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To convert a PaddlePaddle model, use the ``mo`` script and specify the path to the input model ``.pdmodel`` file:

.. ref-code-block:: cpp

	mo --input_model <INPUT_MODEL>.pdmodel

Example of Converting a PaddlePaddle Model
------------------------------------------

Below is the example command to convert yolo v3 PaddlePaddle network to OpenVINO IR network with Model Optimizer.

.. ref-code-block:: cpp

	mo --input_model=yolov3.pdmodel --input=image,im_shape,scale_factor --input_shape=[1,3,608,608],[1,2],[1,2] --reverse_input_channels --output=save_infer_model/scale_0.tmp_1,save_infer_model/scale_1.tmp_1

Supported PaddlePaddle Layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to :ref:`Supported Framework Layers <doxid-openvino_docs__m_o__d_g_prepare_model__supported__frameworks__layers>` for the list of supported standard layers.

Frequently Asked Questions (FAQ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Model Optimizer is unable to run to completion due to issues like typographical errors, incorrectly used options, etc., it provides explanatory messages. They describe the potential cause of the problem and give a link to the :ref:`Model Optimizer FAQ <doxid-openvino_docs__m_o__d_g_prepare_model__model__optimizer__f_a_q>`, which provides instructions on how to resolve most issues. The FAQ also includes links to relevant sections in the Model Optimizer Developer Guide to help you understand what went wrong.

See Also
~~~~~~~~

:ref:`Model Conversion Tutorials <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tutorials>`

