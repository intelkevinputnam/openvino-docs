.. index:: pair: page; Configurations for Intel® Neural Compute Stick 2
.. _doxid-openvino_docs_install_guides_configurations_for_ncs2:


Configurations for Intel® Neural Compute Stick 2
=================================================

:target:`doxid-openvino_docs_install_guides_configurations_for_ncs2_1md_openvino_docs_install_guides_configurations-for-ncs2`





.. _ncs guide:

This page introduces additional configurations for Intel® Neural Compute Stick 2 with Intel® Distribution of OpenVINO™ toolkit on Linux, Raspbian OS and macOS.

Linux
~~~~~

Once you have your Intel® Distribution of OpenVINO™ toolkit installed, follow the steps to be able to work on NCS2:

#. Go to the install_dependencies directory:
   
   .. ref-code-block:: cpp
   
   	cd <INSTALL_DIR>/install_dependencies/

#. Run the ``install_NCS_udev_rules.sh`` script:
   
   .. ref-code-block:: cpp
   
   	./install_NCS_udev_rules.sh

#. You may need to reboot your machine for this to take effect.

You've completed all required configuration steps to perform inference on Intel® Neural Compute Stick 2. Proceed to the :ref:`Get Started Guide <doxid-get_started>` section to learn the basic OpenVINO™ toolkit workflow and run code samples and demo applications.

.. _ncs guide raspbianos:

Raspbian OS
~~~~~~~~~~~

#. Add the current Linux user to the ``users`` group:
   
   .. ref-code-block:: cpp
   
   	sudo usermod -a -G users "$(whoami)"
   
   Log out and log in for it to take effect.

#. If you didn't modify ``.bashrc`` to permanently set the environment variables, run ``setupvars.sh`` again after logging in:
   
   .. ref-code-block:: cpp
   
   	source /opt/intel/openvino_2022/setupvars.sh

#. To perform inference on the Intel® Neural Compute Stick 2, install the USB rules running the ``install_NCS_udev_rules.sh`` script:
   
   .. ref-code-block:: cpp
   
   	sh /opt/intel/openvino_2022/install_dependencies/install_NCS_udev_rules.sh

#. Plug in your Intel® Neural Compute Stick 2.

#. (Optional) If you want to compile and run the Image Classification sample to verify the OpenVINO™ toolkit installation follow the next steps.
   
   a. Navigate to a directory that you have write access to and create a samples build directory. This example uses a directory named ``build`` :
   
   .. ref-code-block:: cpp
   
   	mkdir build && cd build
   
   b. Build the Hello Classification Sample:
   
   .. ref-code-block:: cpp
   
   	cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-march=armv7-a" /opt/intel/openvino_2022/samples/cpp

.. ref-code-block:: cpp

	make -j2 hello_classification

c. Download the pre-trained squeezenet1.1 image classification model with the Model Downloader or copy it from the host machine:

.. ref-code-block:: cpp

	git clone --depth 1 https://github.com/openvinotoolkit/open_model_zoo
	cd open_model_zoo/tools/model_tools
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.in
	python3 downloader.py --name squeezenet1.1

d. Run the sample specifying the model, a path to the input image, and the VPU required to run with the Raspbian OS:

.. ref-code-block:: cpp

	./armv7l/Release/hello_classification <path_to_model>/squeezenet1.1.xml <path_to_image> MYRIAD

The application outputs to console window top 10 classification results.

.. _ncs guide macos:

macOS
~~~~~

These steps are required only if you want to perform inference on Intel® Neural Compute Stick 2 powered by the Intel® Movidius™ Myriad™ X VPU.

To perform inference on Intel® Neural Compute Stick 2, the ``libusb`` library is required. You can build it from the `source code <https://github.com/libusb/libusb>`__ or install using the macOS package manager you prefer: `Homebrew <https://brew.sh/>`__, `MacPorts <https://www.macports.org/>`__ or other.

For example, to install the ``libusb`` library using Homebrew, use the following command:

.. ref-code-block:: cpp

	brew install libusb

You've completed all required configuration steps to perform inference on your Intel® Neural Compute Stick 2. Proceed to the `Start Using the Toolkit <openvino_docs_install_guides_installing_openvino_macos.html#get-started>`__ section to learn the basic OpenVINO™ toolkit workflow and run code samples and demo applications.

