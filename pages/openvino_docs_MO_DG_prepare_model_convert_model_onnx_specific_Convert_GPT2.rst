.. index:: pair: page; Convert ONNX\* GPT-2 Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_onnx_specific__convert__g_p_t2:


Convert ONNX\* GPT-2 Model
==========================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_onnx_specific__convert__g_p_t2_1md_openvino_docs_mo_dg_prepare_model_convert_model_onnx_specific_convert_gpt2` `Public pre-trained GPT-2 model <https://github.com/onnx/models/tree/master/text/machine_comprehension/gpt-2>`__ is a large transformer-based language model with a simple objective: predict the next word, given all of the previous words within some text.

Download the Pre-Trained Base GPT-2 Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To download the model, click **Download** on `https://github.com/onnx/models/blob/master/text/machine_comprehension/gpt-2/model/gpt2-10.onnx <https://github.com/onnx/models/blob/master/text/machine_comprehension/gpt-2/model/gpt2-10.onnx>`__.

To download the model and sample test data, click **Download** on `https://github.com/onnx/models/blob/master/text/machine_comprehension/gpt-2/model/gpt2-10.tar.gz <https://github.com/onnx/models/blob/master/text/machine_comprehension/gpt-2/model/gpt2-10.tar.gz>`__.

Convert ONNX\* GPT-2 Model to IR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To generate the Intermediate Representation (IR) of the model GPT-2, run the Model Optimizer with the following parameters:

.. ref-code-block:: cpp

	mo --input_model gpt2-10.onnx --input_shape [X,Y,Z] --output_dir <OUTPUT_MODEL_DIR>

