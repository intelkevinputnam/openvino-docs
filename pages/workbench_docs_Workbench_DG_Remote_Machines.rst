.. index:: pair: page; Manipulate Remote Machines
.. _doxid-workbench_docs__workbench__d_g__remote__machines:


Manipulate Remote Machines
==========================

:target:`doxid-workbench_docs__workbench__d_g__remote__machines_1md_openvino_workbench_docs_workbench_dg_remote_machines` Machines registered in the DL Workbench are added to the **Environment** table on the **Create Project** page. You can only select a machine that indicates **Available** state:

.. image:: available-001.png

**Configuring** and **Connecting** states mean that you need to wait for the machine to set up:

.. image:: configuring-env-001.png

.. image:: connecting-001.png

If the machine you want to use indicates **Configuration Failure** state, click **Review** :

.. image:: config-failure-001.png

Once you click **Review**, you get to the **Target Machines** page with the details of your machines:

.. image:: available-001.png

To remove a configuration, click the bin icon in the **Action** column. To edit the configuration, click the pencil icon in the **Action** column of the **Machines Table** and edit parameters on the **Edit Remote Target** page that will open. Refer to :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>` to fix an issue.

Click **Refresh** to update remote machine parameters. The **Configuration Status**, **Connection Status** tables and the **System Resources** field will get configured again:

.. image:: refresh-001.png

See Also
~~~~~~~~

* :ref:`Work with Remote Targets <doxid-workbench_docs__workbench__d_g__remote__profiling>`

* :ref:`Profile on a Remote Machine <doxid-workbench_docs__workbench__d_g__profile_on__remote__machine>`

* `Set Up Remote Target <workbench_docs_Workbench_DG_Setup_Remote_Target.html>`__

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

