.. index:: pair: page; Work with Remote Targets
.. _doxid-workbench_docs__workbench__d_g__remote__profiling:


Work with Remote Targets
========================

:target:`doxid-workbench_docs__workbench__d_g__remote__profiling_1md_openvino_workbench_docs_workbench_dg_remote_profiling`





.. toctree::
   :maxdepth: 1
   :hidden:

   workbench_docs_Workbench_DG_Profile_on_Remote_Machine
   workbench_docs_Workbench_DG_Setup_Remote_Target
   workbench_docs_Workbench_DG_Add_Remote_Target
   workbench_docs_Workbench_DG_Remote_Machines

DL Workbench can collect performance data not only on the machine on which you run it, but also on other machines in your local network. This helps when you cannot run the DL Workbench on a machine due to security or network issues or because it is impossible to install Docker. If this is the case, run the DL Workbench on another machine and collect performance data on a remote machine in your local network.

When connected to a remote machine, you can currently use a limited set of DL Workbench features:

.. list-table::
    :header-rows: 1

    * - Feature
      - Supported
    * - Single and group inference
      - Yes (HDDL plugin is not supported)
    * - INT8 calibration
      - Yes
    * - Accuracy measurements
      - No
    * - Performance comparison between models on local and remote machines
      - Yes
    * - Deployment package creation
      - No

Follow the steps below to profile your model on a remote target:

#. :ref:`Set up the target machine <doxid-workbench_docs__workbench__d_g__setup__remote__target>`

#. :ref:`Register the remote target in the DL Workbench <doxid-workbench_docs__workbench__d_g__add__remote__target>`

#. :ref:`Profile on the remote machine <doxid-workbench_docs__workbench__d_g__profile_on__remote__machine>`

.. note:: Working with machines in your local network is not available when you run the DL Workbench in the :ref:`Intel® DevCloud for the Edge <doxid-workbench_docs__workbench__d_g__start__d_l__workbench_in__dev_cloud>`.

See Also
~~~~~~~~

* :ref:`Manipulate Remote Machines <doxid-workbench_docs__workbench__d_g__remote__machines>`

* `Set Up Remote Target <workbench_docs_Workbench_DG_Setup_Remote_Target.html>`__

* :ref:`Profile on a Remote Machine <doxid-workbench_docs__workbench__d_g__profile_on__remote__machine>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

