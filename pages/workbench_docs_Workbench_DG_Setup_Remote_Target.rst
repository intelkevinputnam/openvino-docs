.. index:: pair: page; Set Up Remote Target
.. _doxid-workbench_docs__workbench__d_g__setup__remote__target:


Set Up Remote Target
====================

:target:`doxid-workbench_docs__workbench__d_g__setup__remote__target_1md_openvino_workbench_docs_workbench_dg_setup_remote_target` To allow profiling on a remote Linux\* system, follow the steps below:

#. Make sure your target machine meets the `requirements <#prerequisites>`__.

#. `Configure a paswordless SSH connection between  and  machines <#ssh>`__.

#. If you have GPU and MYRIAD devices on the *target* machine, `configure sudo privileges without a password <#sudo>`__ to enable the DL Workbench to set up devices automatically.

Then proceed to :ref:`register the remote target <doxid-workbench_docs__workbench__d_g__add__remote__target>` in the DL Workbench.

.. _prerequisites:

Target Prerequisites
~~~~~~~~~~~~~~~~~~~~

Your target system must meet the following requirements:

.. note:: The provided combination of dependencies versions is recommended. Other combinations are not validated.

.. list-table::
    :header-rows: 1

    * - Prerequisite
      - Requirement
    * - Operating system
      - Ubuntu\* 18.04
    * - Internet connection
      - Required
    * - Default Shell
      - Bash\* ``4.4.20(1)-release``
    * - Dependencies
      - OpenSSH\* ``1:7.6p1-4ubuntu0.3`` SSH\* ``1:7.6p1-4ubuntu0.3`` Python\* 3.6, 3.7, or 3.8 pip\* 18 python3-distutils\* ``3.6.9-1~18.04`` python3-apt\* ``1.6.5ubuntu0.3`` python3-dev\* ``3.6.7-1~18.04`` libgtk-3-0\* ``3.22.30-1ubuntu4`` GCC\* ``4:7.4.0-1ubuntu2.3`` ffmpeg\* ``7:3.4.8-0ubuntu0.2`` (required for remote calibration)

Run the commands below to install the dependencies:

.. ref-code-block:: cpp

	sudo apt-get update

.. note:: The command below installs the highest versions of the packages. To specify a package version, add ``=<version>`` after the name of a package.

.. ref-code-block:: cpp

	sudo apt-get install -y --no-install-recommends \
	openssh-server \
	ssh \
	python3 \
	python3-distutils \
	python3-apt \
	python3-dev \
	python3-pip \
	gcc \
	libgtk-3-0 \
	ffmpeg

.. ref-code-block:: cpp

	python3 -m pip install --upgrade pip

.. _ssh:

Set Up SSH Connection Using SSH-Keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perform all steps in this section on your *host* machine. Choose the option that works for you:

* `Configure SSH Connection from Linux or macOS\* to Linux <#linux>`__

* `Configure SSH Connection from Windows to Linux Using OpenSSH <#win-ssh>`__

.. _linux:

Configure SSH Connection from Linux or macOS\* to Linux
-------------------------------------------------------

.. note:: This option assumes your *host* machine has the ``openssh-server`` package installed. If not, run the following:

.. ref-code-block:: cpp

	sudo apt update
	sudo apt install openssh-server

**Step 1** : Generate an SSH key pair with the command below:

.. ref-code-block:: cpp

	ssh-keygen

Save keys to default files and **do not use a passphrase**.

**Step 2** : Copy the **public** key to the target machine using the command below. Replace ``USERNAME`` with your username on the *target* machine, and ``HOSTNAME`` with the hostname or IP of the *target* machine.

.. ref-code-block:: cpp

	ssh-copy-id USERNAME@HOSTNAME

.. note:: On macOS, install ``ssh-copy-id`` first. Use the command below:

.. ref-code-block:: cpp

	brew install ssh-copy-id

See `Ssh-copy-id on Mac <https://www.ssh.com/ssh/copy-id#ssh-copy-id-on-mac>`__ for other options.

**Step 3** : Verify that you can connect to your target machine without a password by running the command below. Replace ``USERNAME`` with your username on the *target* machine, and ``HOSTNAME`` with the hostname or IPv4 of the *target* machine.

.. ref-code-block:: cpp

	ssh USERNAME@HOSTNAME

The command should connect you to the target machine **without a password**.

If you have MYRIAD or GPU devices on your target, see `Configure Sudo Privileges without Password <#sudo>`__. If you do not have such devices or they are configured correctly, move on to :ref:`register a remote machine in the DL Workbench <doxid-workbench_docs__workbench__d_g__add__remote__target>`.

.. _win-ssh:

Configure SSH Connection from Windows to Linux Using OpenSSH
------------------------------------------------------------

.. note:: If you do not have OpenSSH on your *host* machine, follow the `OpenSSH installation guide <https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse>`__.

**Step 1** : In a Windows PowerShell\* terminal, generate an SSH key pair with the command below:

.. ref-code-block:: cpp

	ssh-keygen

Save the keys to default files and do not use a passphrase. The keys will be stored at ``C:\Users\<username>/.ssh/id_rsa``.

**Step 2** : Manually copy the **public** key to the *target* machine. Follow the steps below:



#. Open the contents of the public key:
   
   .. ref-code-block:: cpp
   
   	.ssh\id_rsa.pub

#. Copy the contents and transfer them to the *target* machine.

#. On the *target* machine, add the key as a new line in ``authorized_keys``. The ``authorized_keys`` file is typically found in the ``.ssh`` directory for the target user. For the root user, this would be in ``/root/.ssh``. For other users, it would be in the ``/home/<username>`` directory.

**Step 3** : Verify that you can connect to your target machine without a password by running the command below. Replace ``USERNAME`` with your username on the *target* machine, and ``HOSTNAME`` with the hostname or IP of the *target* machine.

.. ref-code-block:: cpp

	ssh USERNAME@HOSTNAME

The command should connect you to the target machine **without a password**.

If you have MYRIAD or GPU devices on your target, see `Configure Sudo Privileges without Password <#sudo>`__. If you do not have such devices or they are configured correctly, move on to :ref:`register a remote machine in the DL Workbench <doxid-workbench_docs__workbench__d_g__add__remote__target>`.

.. _sudo:

Configure Sudo Privileges without Password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DL Workbench tries to set up GPU and MYRIAD devices on the *target* machine automatically. For this, the DL Workbench needs sudo and root privileges for GPU devices and sudo privileges for MYRIAD devices. Skip this section if your devices are configured correctly or you do not have them on the target.

Follow the steps to configure sudo privileges without a password:

**Step 1** : Check sudo permissions using the following command:

.. ref-code-block:: cpp

	sudo ls -la /

If you are not asked for a sudo password during the execution of the command above, skip this section and proceed to :ref:`register the remote target <doxid-workbench_docs__workbench__d_g__add__remote__target>` in the DL Workbench.

**Step 2** : If you do not have sudo permissions, add the user to the ``sudo`` group. Replace ``USERNAME`` with the username of the user you want to grant sudo permissions to and run the command below:

.. ref-code-block:: cpp

	su
	usermod -a -G sudo USERNAME
	exit

**Step 3** : Open the ``/etc/sudoers.tmp`` file as root using the command below:

.. ref-code-block:: cpp

	sudo visudo

**Step 4** : At the end of the ``sudoers`` file, add the line provided below. Replace ``USERNAME`` with the username of the user you want to grant sudo permissions to.

.. ref-code-block:: cpp

	USERNAME ALL=(ALL) NOPASSWD: ALL

Follow the command-line instructions to exit and save the changes.

.. note:: Be careful when editing the ``sudoers`` file and apply only the required changes.

**Step 5** : Check sudo permissions using the following command:

.. ref-code-block:: cpp

	sudo ls -la /

The user ``USERNAME`` received sudo permissions if you are not asked for a sudo password during the execution of the command above.

If you do not have the rights to perform these steps, contact your system administrator or set up the devices manually by following the **Steps for Intel® Processor Graphics (GPU)** and **Steps for Intel® Movidius™ Neural Compute Stick and Intel® Neural Compute Stick 2** sections of :ref:`Install Intel® Distribution of OpenVINO™ toolkit for Linux <doxid-openvino_docs_install_guides_installing_openvino_linux>`.

See Also
~~~~~~~~

* :ref:`Register a Remote Machine in the DL Workbench <doxid-workbench_docs__workbench__d_g__add__remote__target>`

* :ref:`Work with Remote Targets <doxid-workbench_docs__workbench__d_g__remote__profiling>`

* :ref:`Manipulate Remote Machines <doxid-workbench_docs__workbench__d_g__remote__machines>`

* :ref:`Profile on a Remote Machine <doxid-workbench_docs__workbench__d_g__profile_on__remote__machine>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

