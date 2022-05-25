.. index:: pair: page; Cut Datasets
.. _doxid-workbench_docs__workbench__d_g__download_and__cut__datasets:


Cut Datasets
============

:target:`doxid-workbench_docs__workbench__d_g__download_and__cut__datasets_1md_openvino_workbench_docs_workbench_dg_download_and_cut_datasets` Original datasets are considerably big in size. If you want to save your time when loading original datasets into the DL Workbench, cut them as described in the following sections.

* `ImageNet <#imagenet>`__

* `Pascal Visual Object Classes (Pascal VOC) <#voc>`__

* `Common Objects in Context (COCO) <#coco>`__

To learn more about dataset types supported by the DL Workbench, their structure, and how to download them, refer to :ref:`Dataset Types <doxid-workbench_docs__workbench__d_g__dataset__types>`.

.. _imagenet:

ImageNet Dataset
~~~~~~~~~~~~~~~~

Cut ImageNet Dataset
--------------------

#. Save `the script to cut datatsets <https://raw.githubusercontent.com/aalborov/cut_dataset/38c6dd3948ce4084a52c66e2e83c63eb3fa883e9/cut_dataset.py>`__ to the following directory:
   
   * Linux\*, macOS\*: ``/home/<user>/Work``. Replace ``<user>`` with your username.
   
   * Windows\* : ``C:\Work``

#. Put the :ref:`downloaded dataset <doxid-workbench_docs__workbench__d_g__dataset__types>` in the same directory.

#. Follow instructions for your operating system.

.. note:: Replace ``<user>`` with your username. Run the following command in a terminal for Linux, macOS and in the Windows PowerShell\* for Windows.

.. tab:: Linux, macOS

  .. code-block:: 

    python /home/<user>/Work/cut_dataset.py \
      --source_archive_dir=/home/<user>/Work/imagenet.zip \
       --output_size=20 \
       --output_archive_dir=/home/<user>/Work/subsets \
      --dataset_type=imagenet \
      --first_image=10


.. tab:: Windows

  .. code-block:: 


    python C:\\Work\\cut_dataset.py `
       --source_archive_dir=C:\\Work\\imagenet.zip `
       --output_size=20 `
       --output_archive_dir=C:\\Work\\subsets `
      --dataset_type=imagenet `
      --first_image=10

This command runs the script with the following arguments:

.. list-table::
    :header-rows: 1

    * - Parameter
      - Explanation
    * - ``--source_archive_dir``
      - Full path to a downloaded archive
    * - ``--output_size=20``
      - Number of images to be left in a smaller dataset
    * - ``--output_archive_dir``
      - Full directory to the smaller dataset, excluding the name
    * - ``--dataset_type``
      - Type of the source dataset
    * - ``--first_image``
      - *Optional* . The index of the image to start cutting from. Specify if you want to split your dataset into training and validation subsets. The default value is 0.

.. _voc:

Pascal Visual Object Classes (VOC) Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cut Pascal VOC Dataset
----------------------

#. Save `the script to cut datatsets <https://raw.githubusercontent.com/aalborov/cut_dataset/38c6dd3948ce4084a52c66e2e83c63eb3fa883e9/cut_dataset.py>`__ to the following directory:
   
   * Linux\*, macOS\*: ``/home/<user>/Work``. Replace ``<user>`` with your username.
   
   * Windows\* : ``C:\Work``

#. Put the :ref:`downloaded dataset <doxid-workbench_docs__workbench__d_g__dataset__types>` in the same directory.

#. Follow instructions for your operating system.

.. note:: Replace ``<user>`` with your username. Run the following command in a terminal for Linux, macOS and in the Windows PowerShell\* for Windows.

.. tab:: Linux, macOS

  .. code-block:: 


   python /home/<user>/Work/cut_dataset.py \
       --source_archive_dir=/home/<user>/Work/voc.tar.gz \
       --output_size=20 \
       --output_archive_dir=/home/<user>/Work/subsets \
       --dataset_type=voc \
       --first_image=10


.. tab:: Windows

  .. code-block:: 

   python C:\\Work\\cut_dataset.py `
       --source_archive_dir=C:\\Work\\voc.tar.gz `
       --output_size=20 `
       --output_archive_dir=C:\\Work\\subsets `
       --dataset_type=voc `
       --first_image=10

This command runs the script with the following arguments:

.. list-table::
    :header-rows: 1

    * - Parameter
      - Explanation
    * - ``--source_archive_dir``
      - Full path to a downloaded archive
    * - ``--output_size=20``
      - Number of images to be left in a smaller dataset
    * - ``--output_archive_dir``
      - Full directory to the smaller dataset, excluding the name
    * - ``--dataset_type``
      - Type of the source dataset
    * - ``--first_image``
      - *Optional* . The index of the image to start cutting from. Specify if you want to split your dataset into training and validation subsets. The default value is 0.

.. _coco:

Common Objects in Context (COCO) Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cut COCO Dataset
----------------

#. Save `the script to cut datatsets <https://raw.githubusercontent.com/aalborov/cut_dataset/38c6dd3948ce4084a52c66e2e83c63eb3fa883e9/cut_dataset.py>`__ to the following directory:
   
   * Linux\*, macOS\*: ``/home/<user>/Work``. Replace ``<user>`` with your username. > **NOTE** : Replace ``<user>`` with your username.
   
   * Windows\* : ``C:\Work``

#. Put the :ref:`downloaded archives <doxid-workbench_docs__workbench__d_g__dataset__types>` in the same directory.

#. Follow instructions for your operating system.

.. note:: Replace ``<user>`` with your username. Run the following command in a terminal for Linux, macOS and in the Windows PowerShell\* for Windows.

.. tab:: Linux, macOS

  .. code-block:: 


   python /home/<user>/Work/cut_dataset.py \
       --source_images_archive_dir=/home/<user>/Work/coco_images.zip \
       --source_annotations_archive_dir=/home/<user>/Work/coco_annotations_.zip \
       --output_size=20 \
       --output_archive_dir=/home/<user>/Work/subsets \
       --dataset_type=coco \
       --first_image=10

.. tab:: Windows

  .. code-block:: 

   python C:\\Work\\cut_dataset.py `
       --source_images_archive_dir=C:\\Work\\coco_images.zip `
       --source_annotations_archive_dir=C:\\Work\\coco_annotations_.zip `
       --output_size=20 `
       --output_archive_dir=C:\\Work\\subsets `
       --dataset_type=coco `
       --first_image=10

This command runs the script with the following arguments:

.. list-table::
    :header-rows: 1

    * - Parameter
      - Explanation
    * - ``--source_images_archive_dir``
      - Full path to the downloaded archive with images, including the name
    * - ``--source_annotations_archive_dir``
      - Full path to the downloaded archive with annotations, including the name
    * - ``--output_size``
      - Number of images to be left in a smaller dataset
    * - ``--output_archive_dir``
      - Full directory to the smaller dataset excluding the name
    * - ``--dataset_type``
      - Type of the source dataset
    * - ``--first_image``
      - *Optional* . The number of the image to start cutting from. Specify if you want to split your dataset into training and validation subsets. The default value is 0.

See Also
~~~~~~~~

* :ref:`Dataset Types <doxid-workbench_docs__workbench__d_g__dataset__types>`

* :ref:`Import Datasets <doxid-workbench_docs__workbench__d_g__generate__datasets>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

