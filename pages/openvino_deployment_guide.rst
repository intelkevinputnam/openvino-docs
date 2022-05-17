.. index:: pair: page; Deploy with OpenVINO
.. _doxid-openvino_deployment_guide:


Deploy with OpenVINO
====================

:target:`doxid-openvino_deployment_guide_1md_openvino_docs_ov_runtime_ug_deployment_deployment_intro`





.. toctree::
   :maxdepth: 1
   :hidden:

   openvino_docs_install_guides_deployment_manager_tool
   openvino_docs_deploy_local_distribution

Once the :ref:`OpenVINO application development <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>` has been finished, usually application developers need to deploy their applications to end users. There are several ways how to achieve that:

* Set a dependency on existing prebuilt packages (so called *centralized distribution*):
  
  * Using Debian / RPM packages, a recommended way for a family of Linux operation systems
  
  * Using pip package manager on PyPi, default approach for Python-based applications
  
  * Using Docker images. If the application should be deployed as a Docker image, developer can use a pre-built runtime OpenVINO Docker image as a base image in the Dockerfile for the application container image. You can find more info about available OpenVINO Docker images in the Install Guides for :ref:`Linux <doxid-openvino_docs_install_guides_installing_openvino_docker_linux>` and :ref:`Windows <doxid-openvino_docs_install_guides_installing_openvino_docker_windows>`. Also, if you need to customize OpenVINO Docker image, you can use `Docker CI Framework <https://github.com/openvinotoolkit/docker_ci>`__ to generate a Dockerfile and built it.

* Grab a necessary functionality of OpenVINO together with your application (so-called *local distribution*):
  
  * Using :ref:`OpenVINO Deployment manager <doxid-openvino_docs_install_guides_deployment_manager_tool>` providing a convinient way create a distribution package
  
  * Using advanced :ref:`Local distribution <doxid-openvino_docs_deploy_local_distribution>` approach
  
  * Using `static version of OpenVINO Runtime linked into the final app <https://github.com/openvinotoolkit/openvino/wiki/StaticLibraries>`__

The table below shows which distribution type can be used depending on target operation system:

.. raw:: html

    <div class="collapsible-section" data-title="Click to expand/collapse">

.. list-table::
    :header-rows: 1

    * - Distribution type
      - Operation systems
    * - Debian packages
      - Ubuntu 18.04 long-term support (LTS), 64-bit; Ubuntu 20.04 long-term support (LTS), 64-bit
    * - RMP packages
      - Red Hat Enterprise Linux 8, 64-bit
    * - Docker images
      - Ubuntu 18.04 long-term support (LTS), 64-bit; Ubuntu 20.04 long-term support (LTS), 64-bit; Red Hat Enterprise Linux 8, 64-bit; Windows Server Core base LTSC 2019, 64-bit; Windows 10, version 20H2, 64-bit
    * - PyPi (pip package manager)
      - See `https://pypi.org/project/openvino/ <https://pypi.org/project/openvino/>`__
    * - :ref:`OpenVINO Deployment Manager <doxid-openvino_docs_install_guides_deployment_manager_tool>`
      - All operation systems
    * - :ref:`Local distribution <doxid-openvino_docs_deploy_local_distribution>`
      - All operation systems
    * - `Build OpenVINO statically and link into the final app <https://github.com/openvinotoolkit/openvino/wiki/StaticLibraries>`__
      - All operation systems

.. raw:: html

    </div>

Depending on the distribution type, the granularity of OpenVINO packages may vary: PyPi distribution `OpenVINO has a single package 'openvino' <https://pypi.org/project/openvino/>`__ containing all the runtime libraries and plugins, while more configurable ways like :ref:`Local distribution <doxid-openvino_docs_deploy_local_distribution>` provide higher granularity, so it is important to now some details about the set of libraries which are part of OpenVINO Runtime package:

.. image:: deployment_simplified.png

* The main library ``openvino`` is used by C++ user's applications to link against with. The library provides all OpenVINO Runtime public API for both OpenVINO API 2.0 and Inference Engine, nGraph APIs. For C language applications ``openvino_c`` is additionally required for distribution.

* The *optional* plugin libraries like ``openvino_intel_cpu_plugin`` (matching ``openvino_.+_plugin`` pattern) are used to provide inference capabilities on specific devices or additional capabitilies like :ref:`Hetero execution <doxid-openvino_docs__o_v__u_g__hetero_execution>` or :ref:`Multi-Device execution <doxid-openvino_docs__o_v__u_g__running_on_multiple_devices>`.

* The *optional* plugin libraries like ``openvino_ir_frontnend`` (matching ``openvino_.+_frontend``) are used to provide capabilities to read models of different file formats like OpenVINO IR, ONNX or Paddle.

The *optional* means that if the application does not use the capability enabled by the plugin, the plugin's library or package with the plugin is not needed in the final distribution.

The information above covers granularity aspects of majority distribution types, more detailed information is only needed and provided in :ref:`Local Distribution <doxid-openvino_docs_deploy_local_distribution>`.

.. note:: Depending on target OpenVINO devices, you also have to use :ref:`Configurations for GPU <doxid-openvino_docs_install_guides_configurations_for_intel_gpu>`, :ref:`Configurations for GNA <doxid-openvino_docs_install_guides_configurations_for_intel_gna>`, :ref:`Configurations for NCS2 <doxid-openvino_docs_install_guides_configurations_for_ncs2>` or :ref:`Configurations for VPU <doxid-openvino_docs_install_guides_installing_openvino_ivad_vpu>` for proper configuration of deployed machines.

