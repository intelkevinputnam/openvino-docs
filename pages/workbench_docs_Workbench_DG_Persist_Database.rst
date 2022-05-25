.. index:: pair: page; Restore DL Workbench State
.. _doxid-workbench_docs__workbench__d_g__persist__database:


Restore DL Workbench State
==========================

:target:`doxid-workbench_docs__workbench__d_g__persist__database_1md_openvino_workbench_docs_workbench_dg_persist_database`

DL Workbench enables performing multiple experiments to analyze performance and accuracy data. To always have access to your data in the DL Workbench, use additional parameters when you :ref:`run the DL Workbench <doxid-workbench_docs__workbench__d_g__run__locally>` that enable DL Workbench state preservation.

.. note:: It is highly recommended to enable DL Workbench state preservation.

Why you need to preserve DL Workbench state:

* Your data might be lost due to accidental removal of a container or other infrastructural failures.

* You want to share your experimental data and DL Workbench artifacts with your team.

* You want to transfer DL Workbench data to another machine and continue your experiments there.

* You work with the DL Workbench of some version and want to update to a higher version, for example, from 2020.4 to 2021.1.

Ignore state preservation if:

* You do not plan to share data.

* You do not plan to update the DL Workbench in the future.

* You just want to get acquainted with the DL Workbench and understand its key offerings.

Even if you do not enable state preservation, your data is secured as long as there is a container on your machine. When you stop a container, you still have access to your data when you resume the container as described in the *Pause and Resume Docker Container* section of :ref:`Work with Docker Container <doxid-workbench_docs__workbench__d_g__docker__container>`. However, if you remove a container that you ran without enabling state preservation, all your data is lost with that removed container.

To restore the DL Workbench data:

#. Follow instructions for you operating system to enable state preservation:
   
   * `Preserve the DL Workbench state on Linux\* and macOS\*  <#preserve-linux-macos>`__
   
   * `Preserve the DL Workbench state on Windows\*  <#preserve-windows>`__

#. When you remove a container, all data is present in the mounted host folder. To continue working with the data in a new DL Workbench container, start the DL Workbench with the mounted folder or volume using ``--assets-directory`` or ``--volume``.

.. _preserve-linux-macos:

Preserve DL Workbench State on Linux and macOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable DL Workbench state preservation, mount a host directory to a Docker container. The example below shows how to mount a local folder while running a Docker container on Linux\* with a CPU enabled as a profiling target and in detached mode. To learn how to run the application on different targets, operating system, or in a different mode, see :ref:`Advanced Configurations <doxid-workbench_docs__workbench__d_g__advanced__configurations>` page.

#. To run DL Workbench with Python Starter on your OS, use the first command from :ref:`installation form <doxid-workbench_docs__workbench__d_g__run__locally>` :
   
   .. ref-code-block:: cpp
   
   	python3 -m pip install -U openvino-workbench

#. In the directory with the ``openvino-workbench`` script, create the ``/home/workbench/.workbench`` folder with read, write, and execute permissions:
   
   .. ref-code-block:: cpp
   
   	mkdir -m 777 /home/workbench/.workbench

#. Run the command below:
   
   
   
   .. ref-code-block:: cpp
   
   	openvino-workbench --image openvino/workbench:2022.1 --assets-directory ~/.workbench

All your data is placed in the mounted directory once you mount it and run the DL Workbench:

.. ref-code-block:: cpp

	|-- ~/.workbench
	  |-- token.txt
	  |-- datasets/
	  |-- models/
	  |-- postgresql_data_directory/
	  |-- tutorials/

.. _preserve-windows:

Preserve DL Workbench State on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Due to `problems of mounting a local folder to a Docker container on Windows <https://github.com/docker/for-win/issues/77>`__, the best way to preserve the state on Windows is to use Docker `volumes <https://docs.docker.com/storage/volumes/>`__ :

#. Get a Docker image as described in the **Install DL Workbench** section of :ref:`Install DL Workbench <doxid-workbench_docs__workbench__d_g__run__locally>`.

#. Create a Docker volume:
   
   
   
   .. ref-code-block:: cpp
   
   	docker volume create workbench_volume

#. Start the DL Workbench with the mounted volume:
   
   
   
   .. ref-code-block:: cpp
   
   	docker run -p 127.0.0.1:5665:5665 `
   	    --name workbench `
   	    --volume workbench_volume:/home/workbench/.workbench `
   	    -d openvino/workbench:latest

All your data is placed in the mounted volume once you mount it and run the DL Workbench:

.. ref-code-block:: cpp

	|-- token.txt
	|-- datasets/
	|-- models/
	|-- postgresql_data_directory/

Share Profiling Data
~~~~~~~~~~~~~~~~~~~~

DL Workbench ``--assets-directory`` contains sensitive data such as a token, models, and datasets. Share this data only in a trusted environment. DL Workbench supports a scenario when you share only system files with profiling data, and not models and datasets.

Choose instructions for your operating system:

* `Share profiling data on Linux and macOS <#share-linux-macos>`__

* `Share profiling data on Windows <#share-windows>`__

When you share only profiling data, the DL Workbench marks models, datasets, and projects as *Read-only*. *Read-only* means that it is not possible to run optimizations, profiling, or measurements on removed assets, while you can continue with importing new models and datasets.

Read-only model:

.. image:: read-only.png

.. _share-linux-macos:

Share Profiling Data on Linux and macOS
---------------------------------------

#. Remove models and datasets directories from the ``~/.workbench`` folder, so that it contains only the ``postgresql_data_directory/`` folder:
   
   
   
   .. ref-code-block:: cpp
   
   	~/.workbench
   	└───postgresql_data_directory/

#. Transfer the ``~/.workbench`` folder to another machine and import it with the following command:
   
   
   
   .. ref-code-block:: cpp
   
   	openvino-workbench --image openvino/workbench:2022.1 --assets-directory ~/.workbench

.. _share-windows:

Share Profiling Data on Windows
-------------------------------

#. Create an empty local folder.

#. Copy the DL Workbench data to the local folder:
   
   
   
   .. ref-code-block:: cpp
   
   	docker run --rm -v <full_path_to_local_folder>:/backup -v workbench_volume:/data busybox sh -c "cp -rp /data/\* /backup"

#. Remove models and datasets directories from the local folder, so that it contains only the ``postgresql_data_directory/`` folder:
   
   
   
   .. ref-code-block:: cpp
   
   	/local_folder
   	└───postgresql_data_directory/

#. Transfer the local folder to another machine and create a new volume:
   
   
   
   .. ref-code-block:: cpp
   
   	docker volume create workbench_volume

#. Copy the data from the local folder to the ``workbench_volume`` volume:
   
   
   
   .. ref-code-block:: cpp
   
   	docker run --rm -v <full_path_to_local_folder>:/backup -v workbench_volume:/data busybox sh -c "cp -rp /backup/\* /data && chown -R 5665:5665 /data && chmod -R 700 /data/postgresql_data_directory"

#. Start the DL Workbench with the mounted volume:
   
   
   
   .. ref-code-block:: cpp
   
   	docker run -p 127.0.0.1:5665:5665 `
   	    --name workbench `
   	    --volume workbench_volume:/home/workbench/.workbench `
   	    -it openvino/workbench:latest

Troubleshooting
~~~~~~~~~~~~~~~

When importing assets, DL Workbench validates their consistency. If any assets have different checksum to what the DL Workbench stores, these artifacts are considered as threatening security of the DL Workbench. Remove these assets and try to run the DL Workbench again.

DL Workbench fails to start if the provided assets cannot be imported due to aforementioned versioning policy. In that case, create new assets directory and mount it instead of the existing one.

