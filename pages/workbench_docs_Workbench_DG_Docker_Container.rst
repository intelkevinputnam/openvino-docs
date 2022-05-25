.. index:: pair: page; Work with Docker Container
.. _doxid-workbench_docs__workbench__d_g__docker__container:


Work with Docker Container
==========================

:target:`doxid-workbench_docs__workbench__d_g__docker__container_1md_openvino_workbench_docs_workbench_dg_docker_container` When working with the application inside a Docker container, you might need to:

* `Pause and resume a Docker container <#pause>`__

* `Update the DL Workbench inside a Docker container <#upgrade>`__

* `Copy files from a Docker container <#copy>`__

* `Enter a Docker container <#enter>`__

Refer to the sections below to see instructions for each scenario.

.. note:: To learn about the commands, see :ref:`Advanced Configurations <doxid-workbench_docs__workbench__d_g__advanced__configurations>`.

.. note:: In the snippets below, replace ``workbench`` with the name of your container if you renamed it.

.. _pause:

Pause and Resume Docker Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To pause a container with the DL Workbench while keeping all your data in it, stop the container and then restart it later to the previous state with the commands below:

#. Stop the container:

.. ref-code-block:: cpp

	docker stop workbench

* When the container was run in *interactive* mode:
  
  **Ctrl + C**



#. Restart the container:

.. tab:: `docker run` *detached* mode command

   .. code-block:: 

      docker start workbench

.. tab:: `docker run` *interactive* mode command

   .. code-block:: 

      docker start -ai <container-name>

.. tab:: `openvino-workbench` command

   .. code-block:: 

      openvino-workbench --restart workbench

.. _upgrade:

Upgrade the DL Workbench Inside a Docker Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get the highest version of the application in your Docker container, pause the container, pull the latest version, and run the container with the same folder or volume that you mounted to your previous Docker container.

1. Stop Container
-----------------

.. ref-code-block:: cpp

	docker stop workbench

* When the container was run in *interactive* mode:
  
  **Ctrl + C**

2. Pull the Highest Version of the DL Workbench
-----------------------------------------------

.. tab:: `docker`  command

  .. code-block:: 

      docker start workbench

.. tab:: `openvino-workbench` command

  .. code-block:: 

      openvino-workbench --image openvino/workbench:2022.1

3. Start New Container
----------------------

Mount the same folder or volume that you mounted to your previous Docker container and run the new container. You can specify the name of the new container using the ``--container-name`` argument, for example, ``workbench_2022.1``.

.. tab:: `docker` command

  .. code-block:: 

        docker run -p 0.0.0.0:5665:5665 --name workbench_2022.1 -it openvino/workbench:2022.1 --assets-directory  ~/.workbench

.. tab:: `openvino-workbench` command

  .. code-block:: 

      openvino-workbench --image openvino/workbench:2022.1 --assets-directory ~/.workbench --container-name workbench_2022.1

For full instructions on running a container and description of the arguments in the command above, see the :ref:`Advanced Configurations <doxid-workbench_docs__workbench__d_g__advanced__configurations>` page.

Once the command executes, open the link `https://127.0.0.1:5665 <https://127.0.0.1:5665>`__ in your browser, and the DL Workbench **Start Page** appears:

.. image:: start_page_crop.png

.. _copy:

Copy Files from Docker Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To copy files from the container, you do not need to enter it. Use ``docker cp`` command, for example, this command copies the token to your Desktop:

.. ref-code-block:: cpp

	docker cp <container_name>:/home/workbench/.workbench/token.txt token.txt

Copy Server Logs
----------------

If you cannot copy the logs from the DL Workbench UI, use the following command:

.. ref-code-block:: cpp

	docker cp workbench:/home/workbench/.workbench/server.log server.log

.. _enter:

Enter Docker Container with DL Workbench
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: For this step, the container must be running.

1. Enter Container
------------------

If you want to inspect the container, run the following command:

.. ref-code-block:: cpp

	docker exec -it workbench /bin/bash

This command creates a new instance of a shell in the running Docker container and gives you access to a bash console as an OpenVINO user.

If you want to change the container configurations, use:

.. ref-code-block:: cpp

	docker exec -u root -it workbench /bin/bash

2. Inspect the Container
------------------------

The container directory displayed in the terminal is ``/opt/intel/openvino_2022/tools/workbench/``.

To see a list of files available inside the container, run ``ls``.

.. note:: The ``/opt/intel/openvino/tools/workbench/`` directory inside the container includes a service folder ``wb/data``. Make sure you do not apply any changes to it.

3. Inspect Entry Point
----------------------

Inspect entry point if you want to see the commands that run DL Workbench.

.. ref-code-block:: cpp

	cat docker/scripts/docker-entrypoint.sh

4. Exit Container
-----------------

To exit the container, run ``exit`` inside the container.

Clear All Files
~~~~~~~~~~~~~~~

The ``rm`` command clears all loaded models, datasets, experiments, and profiling data:

.. ref-code-block:: cpp

	docker rm workbench

See Also
~~~~~~~~

* :ref:`Advanced Configurations <doxid-workbench_docs__workbench__d_g__advanced__configurations>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

* :ref:`Deep Learning Workbench Security <doxid-openvino_docs_security_guide_workbench>`

