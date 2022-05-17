.. index:: pair: page; Compression of a Model to FP16
.. _doxid-openvino_docs__m_o__d_g__f_p16__compression:


Compression of a Model to FP16
==============================

:target:`doxid-openvino_docs__m_o__d_g__f_p16__compression_1md_openvino_docs_mo_dg_prepare_model_fp16_compression` Model Optimizer can convert all floating-point weights to ``FP16`` data type. The resulting IR is called compressed ``FP16`` model.

To compress the model, use the ``--data_type`` option:

.. ref-code-block:: cpp

	mo --input_model INPUT_MODEL --data_type FP16

.. note:: Using ``--data_type FP32`` will give no result and will not force ``FP32`` precision in the model. If the model was ``FP16`` it will have ``FP16`` precision in IR as well.

The resulting model will occupy about twice as less space in the file system, but it may have some accuracy drop, although for the majority of models accuracy degradation is negligible. For details on how plugins handle compressed ``FP16`` models refer to :ref:`Working with devices <doxid-openvino_docs__o_v__u_g__working_with_devices>` page.

.. note:: ``FP16`` compression is sometimes used as initial step for ``INT8`` quantization, please refer to :ref:`Post-training optimization <doxid-pot_introduction>` for more information about that.

