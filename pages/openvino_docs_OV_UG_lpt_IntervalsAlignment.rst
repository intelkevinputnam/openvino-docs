.. index:: pair: page; IntervalsAlignment attribute
.. _doxid-openvino_docs__o_v__u_g_lpt__intervals_alignment:


IntervalsAlignment attribute
============================

:target:`doxid-openvino_docs__o_v__u_g_lpt__intervals_alignment_1md_openvino_docs_ie_plugin_dg_plugin_transformation_pipeline_low_precision_transformations_attributes_intervals_alignment` :ref:`ngraph::IntervalsAlignmentAttribute <doxid-classngraph_1_1_intervals_alignment_attribute>` class represents the ``IntervalsAlignment`` attribute.

The attribute defines a subgraph with the same quantization intervals alignment. ``FakeQuantize`` operations are included. The attribute is used by quantization operations.

.. list-table::
    :header-rows: 1

    * - Property name
      - Values
    * - Required
      - Yes
    * - Defined
      - Operation
    * - Properties
      - combined interval, minimal interval, minimal levels, preferable precisions

