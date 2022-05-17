.. index:: pair: page; Attributes
.. _doxid-openvino_docs__o_v__u_g_lpt_attributes:


Attributes
==========

:target:`doxid-openvino_docs__o_v__u_g_lpt_attributes_1md_openvino_docs_ie_plugin_dg_plugin_transformation_pipeline_low_precision_transformations_lpt_attributes`





.. toctree::
   :maxdepth: 1
   :caption: Attributes
   :hidden:

   AvgPoolPrecisionPreserved <openvino_docs_OV_UG_lpt_AvgPoolPrecisionPreserved>
   IntervalsAlignment <openvino_docs_OV_UG_lpt_IntervalsAlignment>   
   PrecisionPreserved <openvino_docs_OV_UG_lpt_PrecisionPreserved>
   Precisions <openvino_docs_OV_UG_lpt_Precisions>
   QuantizationAlignment <openvino_docs_OV_UG_lpt_QuantizationAlignment>
   QuantizationGranularity <openvino_docs_OV_UG_lpt_QuantizationGranularity>

Introduction
~~~~~~~~~~~~

.. list-table::
    :header-rows: 1

    * - Name
      - Target
      - Required
      - Mutable
    * - :ref:`AvgPoolPrecisionPreserved <doxid-openvino_docs__o_v__u_g_lpt__avg_pool_precision_preserved>`
      - Precision
      - No
      - Yes
    * - :ref:`IntervalsAlignment <doxid-openvino_docs__o_v__u_g_lpt__intervals_alignment>`
      - Quantization interval
      - Yes
      - Yes
    * - :ref:`PrecisionPreserved <doxid-openvino_docs__o_v__u_g_lpt__precision_preserved>`
      - Precision
      - Yes
      - Yes
    * - :ref:`Precisions <doxid-openvino_docs__o_v__u_g_lpt__precisions>`
      - Precision
      - Yes
      - Yes
    * - :ref:`QuantizationAlignment <doxid-openvino_docs__o_v__u_g_lpt__quantization_alignment>`
      - Quantization granularity
      - Yes
      - Yes
    * - :ref:`QuantizationGranularity <doxid-openvino_docs__o_v__u_g_lpt__quantization_granularity>`
      - Quantization granularity
      - Yes
      - No

``Target`` attribute group defines attribute usage during model transformation for the best performance:

* ``Precision`` - the attribute defines the most optimal output port precision.

* ``Quantization interval`` - the attribute defines quantization interval.

* ``Quantization alignment`` - the attribute defines quantization granularity in runtime: per-channel or per-tensor quantization.

* ``Quantization granularity`` - the attribute is set by plugin to define quantization granularity: per-channel or per-tensor quantization.

``Required`` attribute group defines if attribute usage is required to get an optimal model during transformation:

* ``Yes`` - the attribute is used by all OpenVINO plugins for low-precision optimization.

* ``No`` - the attribute is used in a specific OpenVINO plugin.

``Mutable`` attribute group defines if transformation can update an existing attribute:

* ``Yes`` - the attribute can be updated by the next transformations in the pipeline. But attribute update order is still important.

* ``No`` - existing attribute can not be updated by the next transformation. Previous handled transformation has optimized a model according to the current value.

``FakeQuantize`` decomposition is a mandatory part of low precision transformations. Attributes used during decomposition are mandatory. Optional attributes are required only for certain operations.

Attributes usage by transformations:

.. list-table::
    :header-rows: 1

    * - Attribute name
      - Created by transformations
      - Used by transformations
    * - PrecisionPreserved
      - MarkupPrecisions, MarkupAvgPoolPrecisionPreserved
      - AlignQuantizationIntervals, AlignQuantizationParameters, FakeQuantizeDecompositionTransformation, MarkupAvgPoolPrecisionPreserved
    * - AvgPoolPrecisionPreserved
      - MarkupAvgPoolPrecisionPreserved
      - 
    * - Precisions
      - MarkupCanBeQuantized, MarkupPrecisions
      - FakeQuantizeDecompositionTransformation
    * - PerTensorQuantization
      - MarkupPerTensorQuantization
      - 
    * - IntervalsAlignment
      - AlignQuantizationIntervals
      - FakeQuantizeDecompositionTransformation
    * - QuantizationAlignment
      - AlignQuantizationParameters
      - FakeQuantizeDecompositionTransformation

**Note:** the same type of attribute instances can be created in different transformations. This approach is the result of the transformation single-responsibility principle. For example, ``Precision`` attribute instances are created in ``MarkupCanBeQuantized`` and ``MarkupPrecisions`` transformations, but the reasons for their creation are different.

