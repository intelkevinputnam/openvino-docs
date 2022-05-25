.. index:: pair: page; Compare Performance between Two Versions of a Model
.. _doxid-workbench_docs__workbench__d_g__compare__performance_between__two__versions_of__models:


Compare Performance between Two Versions of a Model
===================================================

:target:`doxid-workbench_docs__workbench__d_g__compare__performance_between__two__versions_of__models_1md_openvino_workbench_docs_workbench_dg_compare_performance_between_two_versions_of_models` You can compare performance between two versions of a model; for example, between an original FP32 model and an optimized INT8 model. Once the optimization is complete, click **Compare** above the **Projects** table:

.. image:: compare_projects.png

The **Setup to Compare Performance** page appears:

.. image:: compare_performances_mobilenet.png

Select project A and project B in the drop-down lists. By default, project B is a project with the best throughput.

.. raw:: html

    <iframe  allowfullscreen mozallowfullscreen msallowfullscreen oallowfullscreen webkitallowfullscreen  width="560" height="315" src="https://www.youtube.com/embed/eN0H3s8ITss" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You can select a certain inference experiment within a project by checking the corresponding row. As you select a version, the graphs with latency and throughput values for both versions appear. The graphs instantly adjust to your selection of versions by adding and removing corresponding points.

.. image:: compare_performances_3_4.png

Right under the **Inference Results** graph, find the graph legend:

* Line with a squared point stands for a separate configuration (a separate model version, different dataset or target)

* Line with a round point stands for inferences within one configuration

* **A**, **B** points stand for the selected inferences

* Sweet Spot is the configuration with the best throughput given the selected latency threshold

.. image:: compare_performances_legend-001.png

In the **Latency Threshold** box, specify the maximum latency value to find the optimal configuration with the best throughput. The point representing the sweet spot becomes a blue filled circle:

.. image:: compare_performances_threshold-001.png

If one of the two compared points happens to be a sweet spot, it turns blue while the letter is still indicated:

.. image:: compare_performances_threshold_002.png

Click **Compare** to proceed to the detailed analysis. The **Model Performance Summary** section appears. It contains three tabs:

* `Performance Summary <#performance-summary>`__

* `Inference Time <#inference-time>`__

* `Kernel-Level Performance <#kernel-level-performance>`__

.. _performance-summary:

Performance Summary
~~~~~~~~~~~~~~~~~~~

**Performance Summary** table contains the table with information on layer types of both projects, their execution time, and the number of layers of each type executed in a certain precision. Layer types are arranged from the most to the least time taken.

.. image:: compare_performances_performance_summary_001.png

The table visually demonstrates the ratio of time taken by each layer type. Uncheck boxes in the **Include to Distribution Chart** column to filter out certain layers. You can sort layers by any parameter by clicking the name of the corresponding column.

.. image:: compare_performances_performance_summary_002.png

.. _inference-time:

Inference Time
~~~~~~~~~~~~~~

**Inference Time** chart compares throughput and latency values. By default, the chart shows throughput values. Switch to **Latency** to see the difference in latency values.

.. image:: compare_performances_005.png

.. note:: The colors used in the **Inference Time** chart correspond to the colors of the points A and B.

.. _kernel-level-performance:

Kernel-Level Performance
~~~~~~~~~~~~~~~~~~~~~~~~

**Kernel-Level Performance** table shows all layers of both versions of a model. For details on reading the table, see the **Per-Layer Comparison** section of the :ref:`Visualize Model <doxid-workbench_docs__workbench__d_g__visualize__model>` page.

Find the **Model Performance Summary** at the bottom of the page.

The **Performance Summary** tab contains the table with information on layer types of both projects, their execution time, and the number of layers of each type executed in a certain precision.

.. image:: comparison_performance_summary.png

You can sort values in each column by clicking the column name. By default, layer types are arranged from the most to the least time taken. The table visually demonstrates the ratio of time taken by each layer type. Uncheck boxes in the **Include to Distribution Chart** column to filter out certain layers.

.. image:: comparison_performance_summary_filtered.png

The **Inference Time** tab compares throughput and latency values. By default, the chart shows throughput values. Switch to **Latency** to see the difference in latency values.

.. image:: comparison_inference_time.png

The **Kernel-Level Performance** tab

.. image:: layers_table_06.png

.. note:: Make sure you select points on both graphs.

Each row of a table represents a layer of executed graphs of different model versions. The table displays execution time and runtime precision. If a layer was executed in both versions, the table shows the difference between the execution time values of different model versions layers.

Click the layer name to see the details that appear on the right to the table. Switch between tabs to see parameters of layers that differ between the versions of the model:

.. image:: layers_table_07.png

In case a layer was not executed in one of the versions, the tool notifies you:

.. image:: layers_table_08.png

See Also
~~~~~~~~

* :ref:`Visualize Model <doxid-workbench_docs__workbench__d_g__visualize__model>`

* :ref:`Run Single Inference <doxid-workbench_docs__workbench__d_g__run__single__inference>`

* :ref:`View Inference Results <doxid-workbench_docs__workbench__d_g__view__inference__results>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

